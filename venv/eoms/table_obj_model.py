# -*- coding: utf-8 -*-
from PyQt5.QtGui import *


class TableModel(object):
    # 定义表格数据模型
    def __init__(self):
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])
        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model. setItem(row, column, item)

    def get_model(self):
        return self.model

    def set_model(self, row, column):
        self.model = QStandardItemModel(row, column)

    def set_header(self, header_list):
        self.model.setHorizontalHeaderLabels(header_list)

    def add_row(self, data_rows):
        for v in data_rows:
            row_list = v.strip().split("\t")
            items = []
            for row_value in row_list:
                items.append(QStandardItem(row_value))
            self.model.appendRow(items)

    def del_row(self, row_index):
        self.model.removeRow(row_index)

    def del_all_row(self):
        # print(self.model.rowCount())
        for row_index in range(self.model.rowCount()):
            self.model.removeRow(0)

    def reload_data(self, rows_list):
        for row_value in rows_list:
            self.model.appendRow(row_value)
