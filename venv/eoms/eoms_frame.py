from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox, QWidget
from PyQt5.QtCore import *
from eoms_model import Ui_MainWindow
from table_obj_model import TableModel
from get_zaitu_time import GetZaiTuTime
import xlwt     # excel 包
import json
import os
import time


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

    def msg(self):
        QMessageBox.about(self, "消息", "导出EXCEL文件成功")


class EomsFrame(Ui_MainWindow):
    # EOMS 窗体类，加载投诉工单数据

    def __init__(self):
        super().__init__()
        self.data_rows = []
        self.json_data = {}
        self.cwd_path = os.getcwd()
        self.load_data = TableModel()
        self.list_model = QStringListModel()
        self.config_filename = self.cwd_path + "\config.json"
        self.data_filename = self.cwd_path + "\zaitu_info.txt"
        print(self.config_filename)
        print(self.data_filename)
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.time_lineEdit.setText("120")
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.get_config()  # 获得配置信息
        self.load_treeview()  # 加载表数据
        self.find_pushButton.clicked.connect(self.get_data_time)
        self.clear_pushButton.clicked.connect(self.load_data.del_all_row)
        self.Button_addfield.clicked.connect(self.add_field_name)
        self.Button_delfield.clicked.connect(self.del_field_name)
        self.setpushButton.clicked.connect(self.save_config)
        self.outExcelpushButton.clicked.connect(self.output_excel)
        self.MainWindow.show()

    def output_excel(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet 1')
        sheet.write(0, 1, "test")  # 第n行第i列写入内容
        filename = 'out_{}.xls'.format(str(time.time()))
        wbk.save(filename)
        MyWindow().msg()
        print("write excel success!")


    def get_config(self):
        with open(self.config_filename, encoding="utf-8") as f_obj:
            self.json_data = json.load(f_obj)
        print(str(self.json_data['start_time']))
        start_time = QDateTime.fromString(self.json_data['start_time'], "yyyy/MM/dd hh:mm")
        self.start_dateTimeEdit.setDateTime(start_time)
        end_time = QDateTime.fromString(self.json_data['end_time'], "yyyy/MM/dd hh:mm")
        self.end_dateTimeEdit.setDateTime(end_time)
        self.lineEdit_update.setText(self.json_data["update_time"])
        self.lineEdit_runfile.setText(self.json_data["py_file"])
        self.lineEdit_datasource.setText(self.json_data["filename"])
        self.list_model.setStringList(self.json_data["field_list"])
        self.listView_field.setModel(self.list_model)


    def load_treeview(self):
        # 根据配置文件获得数据字段列表信息
        zaitu_header_list = self.json_data["field_list"]
        self.load_data.set_model(0, len(zaitu_header_list))
        self.load_data.set_header(zaitu_header_list)
        self.tableView.setModel(self.load_data.model)
        with open(self.data_filename, encoding="utf-8") as myfile:
            self.data_rows = myfile.readlines()
            self.load_data.add_row(self.data_rows)

    def get_data_time(self):
        gztt = GetZaiTuTime(self.data_rows)
        new_data = gztt.get_data(self.time_lineEdit.text())
        self.load_data.del_all_row()
        self.load_data.add_row(new_data)

    def add_field_name(self):
        field_name = self.lineEdit_fieldname.text().strip()
        if field_name != "":
            self.list_model.insertRow(self.list_model.rowCount())
            index = self.list_model.index(self.list_model.rowCount()-1, 0)
            self.list_model.setData(index, field_name, Qt.DisplayRole)
            self.listView_field.setCurrentIndex(index)

    def del_field_name(self):
        index = self.listView_field.currentIndex()
        self.list_model.removeRow(index.row())

    def save_config(self):
        self.json_data['start_time'] = self.start_dateTimeEdit.text()
        self.json_data['end_time'] = self.end_dateTimeEdit.text()
        self.json_data['update_time'] = self.lineEdit_update.text()
        self.json_data['py_file'] = self.lineEdit_runfile.text()
        self.json_data['filename'] = self.lineEdit_datasource.text()
        self.json_data['field_list'] = self.list_model.stringList()
        print(self.json_data)
        with open(self.config_filename, "w", encoding="utf-8") as f_obj:
            # ensure_ascii=False 中文正常输出，否则转换为UTF-8， indent=4 缩进数量
            json.dump(self.json_data, f_obj, ensure_ascii=False, indent=4)
            print("write config.json success!")







