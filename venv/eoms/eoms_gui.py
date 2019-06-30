# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication

from eoms_frame import EomsFrame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    eoms_main = EomsFrame()
    sys.exit(app.exec_())
