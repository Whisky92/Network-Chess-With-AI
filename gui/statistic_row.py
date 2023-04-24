from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.uic import loadUi
import sys


class StatisticRow(QDialog):
    """
    A class to represent a row in the statistics table
    """

    def __init__(self, p1_name, p2_name, result):
        QDialog.__init__(self)

        loadUi("resource_ui_files/statistic_row.ui", self)

        self.label.setText(p1_name)
        self.label_2.setText(p2_name)
        self.label_3.setText(result)



