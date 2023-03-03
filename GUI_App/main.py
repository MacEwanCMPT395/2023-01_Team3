import sys

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLineEdit, QTableView, QMessageBox, QComboBox
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream, QDir, Qt, QStandardPaths

import pandas as pd

from Scheduler1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page1)

        ############ Buttons Clicked ############################
        self.ui.data_page_button.clicked.connect(self.showDataPage)
        self.ui.schedule_page_button.clicked.connect(self.showSchedulePage)
        self.ui.load_data_button.clicked.connect(self.load_data)
        self.ui.room_533_page_btn.clicked.connect(self.show533Page)
        self.ui.room_534_page_btn.clicked.connect(self.show534Page)
        self.ui.room_560_page_btn.clicked.connect(self.show560Page)
        self.ui.room_458_page_btn.clicked.connect(self.show458Page)
        self.ui.room_562_page_btn.clicked.connect(self.show562Page)
        self.ui.room_564_page_btn.clicked.connect(self.show564Page)
        self.ui.room_320_page_btn.clicked.connect(self.show320Page)
        self.ui.room_430_page_btn.clicked.connect(self.show533Page)
        self.ui.room_532_lab_page_btn.clicked.connect(self.show532LabPage)

        
        self.ui.save_data_btn.clicked.connect(self.save_data)
        

        ############################################################

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



    ############################## Button Functions ###################################

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
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter a CSV file path")
            msg.exec()


    @pyqtSlot()
    def showDataPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page1)

    @pyqtSlot()
    def showSchedulePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)
    
    @pyqtSlot()
    def show533Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page3)
    
    @pyqtSlot()
    def show534Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page4)
    
    @pyqtSlot()
    def show560Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page11)
    
    @pyqtSlot()
    def show458Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page5)
    
    @pyqtSlot()
    def show562Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page6)
    
    @pyqtSlot()
    def show564Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page7)
    
    @pyqtSlot()
    def show320Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page8)
    
    @pyqtSlot()
    def show430Page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page9)
    
    @pyqtSlot()
    def show532LabPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page10)
    
    @pyqtSlot()
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
    
    @pyqtSlot()
    def input_check(self):
    # list of all the Line Edits
        line_edits = [
            self.ui.p_comm_input_1,
            self.ui.b_comm_input_1,
            self.ui.pm_input_1,
            self.ui.ba_input_1,
            self.ui.glm_input_1,
            self.ui.fs_input_1,
            self.ui.dxd_input_1,
            self.ui.bookkeep_input,
            self.ui.p_comm_input_2,
            self.ui.b_comm_input_2,
            self.ui.pm_input_2,
            self.ui.ba_input_2,
            self.ui.glm_input_2,
            self.ui.fs_input_2,
            self.ui.dxd_input_2,
            self.ui.bookkeep_input_2,
            self.ui.p_comm_input_3,
            self.ui.b_comm_input_3,
            self.ui.pm_input_3,
            self.ui.ba_input_3,
            self.ui.glm_input_3,
            self.ui.fs_input_3,
            self.ui.dxd_input_3,
            self.ui.bookkeep_input_3
        ]

        # iterate through all Line Edits and check if they contain valid input
        for line_edit in line_edits:
            text = line_edit.text()
            if text != '':
                try:
                    num = int(text)
                    if num < 0:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Icon.Warning)
                        msg.setText("Please input only numbers 0 or higher in the text fields")
                        msg.exec()
                        return False
                except ValueError:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Warning)
                    msg.setText("Please input only numbers 0 or higher in the text fields")
                    msg.exec()
                    return False
        return True

    @pyqtSlot()
    def update_data(self):
        # update first term
        self.df.loc[0, '1st Term Students'] = int(self.ui.p_comm_input_1.text() or 0)
        self.df.loc[1, '1st Term Students'] = int(self.ui.b_comm_input_1.text() or 0)
        self.df.loc[2, '1st Term Students'] = int(self.ui.pm_input_1.text() or 0)
        self.df.loc[3, '1st Term Students'] = int(self.ui.ba_input_1.text() or 0)
        self.df.loc[4, '1st Term Students'] = int(self.ui.glm_input_1.text() or 0)
        self.df.loc[5, '1st Term Students'] = int(self.ui.fs_input_1.text() or 0)
        self.df.loc[6, '1st Term Students'] = int(self.ui.dxd_input_1.text() or 0)
        self.df.loc[7, '1st Term Students'] = int(self.ui.bookkeep_input.text() or 0)

        # update second term
        self.df.loc[0, '2nd Term Students'] = int(self.ui.p_comm_input_2.text() or 0)
        self.df.loc[1, '2nd Term Students'] = int(self.ui.b_comm_input_2.text() or 0)
        self.df.loc[2, '2nd Term Students'] = int(self.ui.pm_input_2.text() or 0)
        self.df.loc[3, '2nd Term Students'] = int(self.ui.ba_input_2.text() or 0)
        self.df.loc[4, '2nd Term Students'] = int(self.ui.glm_input_2.text() or 0)
        self.df.loc[5, '2nd Term Students'] = int(self.ui.fs_input_2.text() or 0)
        self.df.loc[6, '2nd Term Students'] = int(self.ui.dxd_input_2.text() or 0)
        self.df.loc[7, '2nd Term Students'] = int(self.ui.bookkeep_input_2.text() or 0)

        # update third term
        self.df.loc[0, '3rd Term Students'] = int(self.ui.p_comm_input_3.text() or 0)
        self.df.loc[1, '3rd Term Students'] = int(self.ui.b_comm_input_3.text() or 0)
        self.df.loc[2, '3rd Term Students'] = int(self.ui.pm_input_3.text() or 0)
        self.df.loc[3, '3rd Term Students'] = int(self.ui.ba_input_3.text() or 0)
        self.df.loc[4, '3rd Term Students'] = int(self.ui.glm_input_3.text() or 0)
        self.df.loc[5, '3rd Term Students'] = int(self.ui.fs_input_3.text() or 0)
        self.df.loc[6, '3rd Term Students'] = int(self.ui.dxd_input_3.text() or 0)
        self.df.loc[7, '3rd Term Students'] = int(self.ui.bookkeep_input_3.text() or 0)

        print(self.df)

    @pyqtSlot()
    def save_data(self):

        # Get the currently selected index of the semester_select_combobox
        selected_index = self.ui.semester_select_combobox.currentIndex()
        #Check if the selected index is 0
        if selected_index == 0:
            # Display a warning message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please Select a Semester!")
            msg.setWindowTitle("Warning")
            msg.exec()
        else:
            if self.input_check():
                self.update_data()
                # print(self.df[0])
            else:
                return

    

    
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
