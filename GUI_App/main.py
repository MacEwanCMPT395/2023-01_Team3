import sys

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLineEdit, QTableView
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream, QDir, Qt, QStandardPaths

import pandas as pd

from Scheduler1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page1)

        self.ui.data_page_button.clicked.connect(self.showDataPage)
        self.ui.schedule_page_button.clicked.connect(self.showSchedulePage)

        self.ui.load_data_button.clicked.connect(self.load_data)

        self.df = None  # initialize the variable

        self.ui.file_name_input.mousePressEvent = self.browse_file

        # Create table view
        self.table_view = QTableView(self.ui.page2)
        self.table_view.setGeometry(10, 10, 700, 500)
        self.table_model = QStandardItemModel()
        self.table_view.setModel(self.table_model)

        self.table_fields()

    def table_fields(self):
        # create table with rows from 8:00am to 10pm incrementing by 30 minutes
        rows = []
        row_labels = []
        current_time = pd.Timestamp("08:00:00")
        while current_time <= pd.Timestamp("22:00:00"):
            rows.append([str(current_time.time()), "", "", "", ""])
            row_labels.append(current_time.strftime("%I:%M %p"))
            current_time += pd.Timedelta(minutes=30)

        # create table with columns from Monday to Thursday
        columns = ["Monday", "Tuesday", "Wednesday", "Thursday"]

        # set the table cols and rows
        self.table_model.clear()
        self.table_model.setHorizontalHeaderLabels(columns)
        self.table_model.setVerticalHeaderLabels(row_labels)

        ## testing of setting data
        for i, row in enumerate(rows):
            for j, col in enumerate(columns):
                item = QStandardItem(row[j])
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table_model.setItem(i, j, item)

    @pyqtSlot()
    def browse_file(self, event):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select file", "",
                                                   "CSV files (*.csv);;Excel files (*.xls *.xlsx)")
        if file_name:
            self.ui.file_name_input.setText(file_name)

    @pyqtSlot()
    def load_data(self):
        file_name = self.ui.file_name_input.text()

        if file_name:
            if file_name.endswith('.csv'):
                self.df = pd.read_csv(file_name)
            elif file_name.endswith('.xls') or file_name.endswith('.xlsx'):
                self.df = pd.read_excel(file_name)

            print(self.df)  # print the loaded dataframe
            self.updateProgramsFields()

    @pyqtSlot()
    def showDataPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page1)

    @pyqtSlot()
    def showSchedulePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)

    def updateProgramsFields(self):
        # update QLineEdits for first term
        self.ui.p_comm_input_1.setText(str(self.df.loc[0, '1st Term Students']))
        self.ui.b_comm_input_1.setText(str(self.df.loc[1, '1st Term Students']))
        self.ui.pm_input_1.setText(str(self.df.loc[2, '1st Term Students']))
        self.ui.ba_input_1.setText(str(self.df.loc[3, '1st Term Students']))
        self.ui.glm_input_1.setText(str(self.df.loc[4, '1st Term Students']))
        self.ui.fs_input_1.setText(str(self.df.loc[5, '1st Term Students']))
        self.ui.dxd_input_1.setText(str(self.df.loc[6, '1st Term Students']))
        self.ui.bookkeep_input.setText(str(self.df.loc[7, '1st Term Students']))

        # update QLineEdits for second term
        self.ui.p_comm_input_2.setText(str(self.df.loc[0, '2nd Term Students']))
        self.ui.b_comm_input_2.setText(str(self.df.loc[1, '2nd Term Students']))
        self.ui.pm_input_2.setText(str(self.df.loc[2, '2nd Term Students']))
        self.ui.ba_input_2.setText(str(self.df.loc[3, '2nd Term Students']))
        self.ui.glm_input_2.setText(str(self.df.loc[4, '2nd Term Students']))
        self.ui.fs_input_2.setText(str(self.df.loc[5, '2nd Term Students']))
        self.ui.dxd_input_2.setText(str(self.df.loc[6, '2nd Term Students']))
        self.ui.bookkeep_input_2.setText(str(self.df.loc[7, '2nd Term Students']))

        # update QLineEdits for third term
        self.ui.p_comm_input_3.setText(str(self.df.loc[0, '3rd Term Students']))
        self.ui.b_comm_input_3.setText(str(self.df.loc[1, '3rd Term Students']))
        self.ui.pm_input_3.setText(str(self.df.loc[2, '3rd Term Students']))
        self.ui.ba_input_3.setText(str(self.df.loc[3, '3rd Term Students']))
        self.ui.glm_input_3.setText(str(self.df.loc[4, '3rd Term Students']))
        self.ui.fs_input_3.setText(str(self.df.loc[5, '3rd Term Students']))
        self.ui.dxd_input_3.setText(str(self.df.loc[6, '3rd Term Students']))
        self.ui.bookkeep_input_3.setText(str(self.df.loc[7, '3rd Term Students']))


"""======================================================================================"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # style sheet load
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
