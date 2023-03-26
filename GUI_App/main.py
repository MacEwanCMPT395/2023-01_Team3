import datetime
import sys

from courseClass import *

from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLineEdit, QTableView, QMessageBox, \
    QComboBox, QSizePolicy, QHeaderView
from PyQt6.QtWidgets import QDialog, QLabel, QInputDialog
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream, QDir, Qt, QStandardPaths

import pandas as pd

from Scheduler1 import Ui_MainWindow
from courseClass import *

import random
import csv

import pathlib


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        # create the data frames
        self.df = pd.DataFrame  
        self.df_rooms = pd.DataFrame
        self.df_programs = pd.DataFrame
        self.df_students = self.create_programs()

        ########## Initialize Degree and Program ############
        self.degree = Degree()
        self.program = Program(150, '')
        self.degree.core_courses["PCOM"] = [] 
        self.degree.core_courses["BCOM"] = [] 
        self.program.program_courses["PM"] = []
        self.program.program_courses["BA"] = []
        self.program.program_courses["GLM"] = []
        self.program.program_courses["DXD"] = []
        self.program.program_courses["BK"] = []

        self.ui.stackedWidget.setCurrentWidget(self.ui.page12)

        ############ Buttons Clicked ############################
        self.ui.data_page_button.clicked.connect(self.showDataPage)
        self.ui.schedule_page_button.clicked.connect(self.showSchedulePage)
        self.ui.load_data_button.clicked.connect(self.load_student_data)
        self.ui.load_data_button_room.clicked.connect(self.load_room_data)
        self.ui.load_data_button_program.clicked.connect(lambda: read_csv(self.ui.file_name_input_program.text(), self.degree, self.program))
        self.ui.room_533_page_btn.clicked.connect(self.show533Page)
        self.ui.room_534_page_btn.clicked.connect(self.show534Page)
        self.ui.room_560_page_btn.clicked.connect(self.show560Page)
        self.ui.room_458_page_btn.clicked.connect(self.show458Page)
        self.ui.room_562_page_btn.clicked.connect(self.show562Page)
        self.ui.room_564_page_btn.clicked.connect(self.show564Page)
        self.ui.room_320_page_btn.clicked.connect(self.show320Page)
        self.ui.room_430_page_btn.clicked.connect(self.show533Page)
        self.ui.room_532_lab_page_btn.clicked.connect(self.show532LabPage)
        self.ui.rooms_page_btn.clicked.connect(self.showRoomsPage)

        ################## Data Page Buttons Clicked ################
        self.ui.save_data_btn.clicked.connect(self.save_data)

        ################## Rooms Page Buttons Clicked ###############

        # connect the remove button to the remove_classroom function
        self.ui.remove_room_btn.clicked.connect(self.remove_classroom)

        # connect the add button to the add_room function
        self.ui.add_room_btn.clicked.connect(self.add_room)

        ############################################################

        self.ui.file_name_input.mousePressEvent = self.browse_student_file
        self.ui.file_name_input_program.mousePressEvent = self.browse_program_file
        self.ui.file_name_input_room.mousePressEvent = self.browse_room_file

        # Create table view
        self.table_view = QTableView(self.ui.page2)
        self.table_view.setGeometry(100, 70, 700, 500)
        self.table_model = QStandardItemModel()
        self.table_view.setModel(self.table_model)

        # Set the size policy of the table view
        self.table_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Add a dropdown for selecting the term
        self.term_combo_box = QComboBox(self.ui.page2)
        self.term_combo_box.setGeometry(100, 40, 150, 30)
        self.term_combo_box.addItem("Term 1")
        self.term_combo_box.addItem("Term 2")
        self.term_combo_box.addItem("Term 3")
        # self.term_combo_box.currentIndexChanged.connect(self.refresh_table)

        # Add a dropdown for selecting the class
        self.week_combo_box = QComboBox(self.ui.page2)
        self.week_combo_box.setGeometry(300, 40, 150, 30)
        # self.week_combo_box.currentIndexChanged.connect(self.refresh_table)

        # Set schedule default as week 1
        self.week = 1

        self.ui.previous_btn.clicked.connect(self.decrement_week)
        self.ui.previous_btn.clicked.connect(self.refresh_table)
        self.ui.next_button.clicked.connect(self.increment_week)
        self.ui.next_button.clicked.connect(self.refresh_table)

        # TEst button for dispaying the tableview values
        self.display_btn = QPushButton("Display", self)
        self.display_btn.setGeometry(400, 580, 40, 20)
        self.display_btn.clicked.connect(self.refresh_table)

        self.table_fields()

        # Set the stretch factor for each column
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        # ----------------- list of lists of text field values------------------
        self.new_list = []

    def refresh_table(self):
        # Clear the current table view and repopulate it
        self.table_model.clear()
        print(self.term_combo_box.currentText())
        print(self.week_combo_box.currentText())
        self.table_fields()
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

    def table_fields(self):
        # Create table with rows from 8:00am to 10pm incrementing by 30 minutes
        rows = []
        row_labels = []
        current_time = pd.Timestamp("08:00:00")
        while current_time <= pd.Timestamp("22:00:00"):
            rows.append([str(current_time.time()), "", "", "", ""])
            row_labels.append(current_time.strftime("%I:%M %p"))
            current_time += pd.Timedelta(minutes=30)

        # Create table with columns from Monday to Thursday
        columns = ["Monday", "Tuesday", "Wednesday", "Thursday"]

        # Set the table cols and rows
        self.table_model.clear()
        self.table_model.setHorizontalHeaderLabels(columns)
        self.table_model.setVerticalHeaderLabels(row_labels)

        # Keep track of colors and testing dictionary
        course_color = {}
        classes = {
            "Term 1": {
                "Week 1": {
                    "11-534": {
                        "monday": [
                            {"course": "Math 534A", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "Science 534A", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "English 534A", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ],
                        "tuesday": [
                            {"course": "History 534A", "start_time": "09:00 AM", "end_time": "10:30 AM"},
                            {"course": "Math 534A", "start_time": "01:00 PM", "end_time": "02:30 PM"},
                            {"course": "Science 534A", "start_time": "03:00 PM", "end_time": "04:30 PM"}
                        ],
                        "wednesday": [
                            {"course": "English 534A", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "History 534A", "start_time": "11:00 AM", "end_time": "12:30 PM"}
                        ],
                        "thursday": [
                            {"course": "Math 534A", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "Science 534A", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ]
                    },
                    "11-560": {
                        "monday": [
                            {"course": "Math 560A", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "Science 560A", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "English 560A", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ],
                        "tuesday": [
                            {"course": "History 560A", "start_time": "09:00 AM", "end_time": "10:30 AM"},
                            {"course": "Math 560A", "start_time": "01:00 PM", "end_time": "02:30 PM"},
                            {"course": "Science 560A", "start_time": "03:00 PM", "end_time": "04:30 PM"}
                        ],
                        "wednesday": [
                            {"course": "English 560A", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "History 560A", "start_time": "11:00 AM", "end_time": "12:30 PM"}
                        ],
                        "thursday": [
                            {"course": "Math 560A", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "Science 560A", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ]
                    }
                },
                "Week 2": {
                    "11-534": {
                        "monday": [
                            {"course": "Math 534B", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "Science 534B", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "English 534B", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ],
                        "tuesday": [
                            {"course": "History 534B", "start_time": "09:00 AM", "end_time": "10:30 AM"},
                            {"course": "Math 534B", "start_time": "01:00 PM", "end_time": "02:30 PM"},
                            {"course": "Science 534B", "start_time": "03:00 PM", "end_time": "04:30 PM"}
                        ],
                        "wednesday": [
                            {"course": "English 534B", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "History 534B", "start_time": "11:00 AM", "end_time": "12:30 PM"}
                        ],
                        "thursday": [
                            {"course": "Math 534B", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "Science 534B", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ]
                    },
                    "11-560": {
                        "monday": [
                            {"course": "Math 560A", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "Science 560A", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "English 560A", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ],
                        "tuesday": [
                            {"course": "History 560A", "start_time": "09:00 AM", "end_time": "10:30 AM"},
                            {"course": "Math 560A", "start_time": "01:00 PM", "end_time": "02:30 PM"},
                            {"course": "Science 560A", "start_time": "03:00 PM", "end_time": "04:30 PM"}
                        ],
                        "wednesday": [
                            {"course": "English 560A", "start_time": "08:00 AM", "end_time": "09:30 AM"},
                            {"course": "History 560A", "start_time": "11:00 AM", "end_time": "12:30 PM"}
                        ],
                        "thursday": [
                            {"course": "Math 560A", "start_time": "10:00 AM", "end_time": "11:30 AM"},
                            {"course": "Science 560A", "start_time": "02:00 PM", "end_time": "03:30 PM"}
                        ]
                    }
                }
            }
        }

        # Iterate through each row and column of the table model and set dummy text
        for row in range(len(rows)):
            for col in range(len(columns)):
                # Check if this cell is within the start and end time of any course in week 1 on this day
                course_in_cell = None
                if self.term_combo_box.currentText() != '' and self.week_combo_box.currentText() != '':
                    for course_data in classes[self.term_combo_box.currentText()][self.ui.label_9.text()][
                        self.week_combo_box.currentText()][
                        columns[col].lower()]:
                        start_time = datetime.datetime.strptime(course_data["start_time"], '%I:%M %p').time()
                        end_time = datetime.datetime.strptime(course_data["end_time"], '%I:%M %p').time()
                        if datetime.datetime.strptime(rows[row][0], '%H:%M:%S').time() >= start_time and \
                                datetime.datetime.strptime(rows[row][0], '%H:%M:%S').time() < end_time:
                            course_in_cell = course_data["course"]
                            break
                    if course_in_cell:
                        # Set the text and alignment for the cell
                        item = QStandardItem(course_in_cell)
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        # Set the background color for the cell
                        if course_in_cell in course_color:
                            item.setBackground(QColor(course_color[course_in_cell]))
                        else:
                            color = QColor.fromHsl(random.randint(0, 255), 255, 191)
                            course_color[course_in_cell] = color.name()
                            item.setBackground(color)
                        # Set the item in the table model
                        self.table_model.setItem(row, col, item)
                    else:
                        # Set the text and alignment for the cell
                        item = QStandardItem("")
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        # Set the item in the table model
                        self.table_model.setItem(row, col, item)

    def increment_week(self):
        if self.week < 13:
            self.week += 1
            self.ui.label_9.setText(f"Week {self.week}")

    def decrement_week(self):
        if self.week > 1:
            self.week -= 1
            self.ui.label_9.setText(f"Week {self.week}")

    @pyqtSlot()
    def browse_student_file(self, line_edit):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select file", "",
                                                   "CSV files (*.csv);;Excel files (*.xls *.xlsx)")
        if file_name:
            self.ui.file_name_input.setText(file_name)
    
    @pyqtSlot()
    def browse_room_file(self, line_edit):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select file", "",
                                                   "CSV files (*.csv);;Excel files (*.xls *.xlsx)")
        if file_name:
            self.ui.file_name_input_room.setText(file_name)
    @pyqtSlot()
    def browse_program_file(self, line_edit):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select file", "",
                                                   "CSV files (*.csv);;Excel files (*.xls *.xlsx)")
        if file_name:
            self.ui.file_name_input_program.setText(file_name)

    ############################## Button Functions ###################################

    @pyqtSlot()
    def load_student_data(self):

        file_name = self.ui.file_name_input.text()

        if file_name:
            if file_name.endswith('StudentsInfo.csv'):
                self.update_enrollment(file_name)
            elif file_name.endswith('StudentsInfo.xls') or file_name.endswith('StudentsInfo.xlsx'):
                self.update_enrollment(file_name)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Please enter the correct CSV file path")
                msg.exec()
                return

            print(self.df_students)  # print the loaded dataframe
            self.updateProgramsFields()
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter a CSV file path")
            msg.exec()

        # [Classroom("11-532", 30, 1),
        #  Classroom("11-533", 36, 0),
        #  Classroom("11-534", 36, 0),
        #  Classroom("11-560", 24, 0),
        #  Classroom("11-562", 24, 0),
        #  Classroom("11-564", 24, 0),
        #  Classroom("11-458", 40, 0),
        #  Classroom("11-430", 30, 0),
        #  Classroom("11-320", 30, 0)]

        # self.edit_room_text(self.ui.text_533, self.classroom_schedule(0))
        # self.edit_room_text(self.ui.text_534, self.classroom_schedule(1))
        # self.edit_room_text(self.ui.text_560, self.classroom_schedule(2))
        # self.edit_room_text(self.ui.text_562, self.classroom_schedule(3))
        # self.edit_room_text(self.ui.text_564, self.classroom_schedule(4))
        # self.edit_room_text(self.ui.text_458, self.classroom_schedule(5))
        # self.edit_room_text(self.ui.text_430, self.classroom_schedule(6))
        # self.edit_room_text(self.ui.text_320, self.classroom_schedule(7))
    
    @pyqtSlot()
    def load_room_data(self):

        file_name = self.ui.file_name_input_room.text()

        if file_name:
            if file_name.endswith('RoomInfo.csv'):
                self.df_rooms = pd.read_csv(file_name)
            elif file_name.endswith('RoomInfo.xls') or file_name.endswith('RoomInfo.xlsx'):
                self.df_rooms = pd.read_excel(file_name)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Please enter the correct CSV file path")
                msg.exec()
                return

            print(self.df_rooms)  # print the loaded dataframe
            self.update_rooms()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter the correct CSV file path")
            msg.exec()

    ####################### Menu BUttons #################################
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
    def showRoomsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page12)

    @pyqtSlot()
    def updateProgramsFields(self):
        # update QLineEdits for first term
        self.ui.p_comm_input_1.setText(str(self.df_students.loc['PCOM', '1st Term Students']))
        self.ui.b_comm_input_1.setText(str(self.df_students.loc['BCOM', '1st Term Students']))
        self.ui.pm_input_1.setText(str(self.df_students.loc['PM', '1st Term Students']))
        self.ui.ba_input_1.setText(str(self.df_students.loc['BA', '1st Term Students']))
        self.ui.glm_input_1.setText(str(self.df_students.loc['GLM', '1st Term Students']))
        self.ui.fs_input_1.setText(str(self.df_students.loc['FS', '1st Term Students']))
        self.ui.dxd_input_1.setText(str(self.df_students.loc['DXD', '1st Term Students']))
        self.ui.bookkeep_input.setText(str(self.df_students.loc['BOOK', '1st Term Students']))

        # update QLineEdits for second term
        self.ui.p_comm_input_2.setText(str(self.df_students.loc['PCOM', '2nd Term Students']))
        self.ui.b_comm_input_2.setText(str(self.df_students.loc['BCOM', '2nd Term Students']))
        self.ui.pm_input_2.setText(str(self.df_students.loc['PM', '2nd Term Students']))
        self.ui.ba_input_2.setText(str(self.df_students.loc['BA', '2nd Term Students']))
        self.ui.glm_input_2.setText(str(self.df_students.loc['GLM', '2nd Term Students']))
        self.ui.fs_input_2.setText(str(self.df_students.loc['FS', '2nd Term Students']))
        self.ui.dxd_input_2.setText(str(self.df_students.loc['DXD', '2nd Term Students']))
        self.ui.bookkeep_input_2.setText(str(self.df_students.loc['BOOK', '2nd Term Students']))

        # update QLineEdits for third term
        self.ui.p_comm_input_3.setText(str(self.df_students.loc['PCOM', '3rd Term Students']))
        self.ui.b_comm_input_3.setText(str(self.df_students.loc['BCOM', '3rd Term Students']))
        self.ui.pm_input_3.setText(str(self.df_students.loc['PM', '3rd Term Students']))
        self.ui.ba_input_3.setText(str(self.df_students.loc['BA', '3rd Term Students']))
        self.ui.glm_input_3.setText(str(self.df_students.loc['GLM', '3rd Term Students']))
        self.ui.fs_input_3.setText(str(self.df_students.loc['FS', '3rd Term Students']))
        self.ui.dxd_input_3.setText(str(self.df_students.loc['DXD', '3rd Term Students']))
        self.ui.bookkeep_input_3.setText(str(self.df_students.loc['BOOK', '3rd Term Students']))

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
        self.df_students.loc['PCOM', '1st Term Students'] = int(self.ui.p_comm_input_1.text() or 0)
        self.df_students.loc['BCOM', '1st Term Students'] = int(self.ui.b_comm_input_1.text() or 0)
        self.df_students.loc['PM', '1st Term Students'] = int(self.ui.pm_input_1.text() or 0)
        self.df_students.loc['BA', '1st Term Students'] = int(self.ui.ba_input_1.text() or 0)
        self.df_students.loc['GLM', '1st Term Students'] = int(self.ui.glm_input_1.text() or 0)
        self.df_students.loc['FS', '1st Term Students'] = int(self.ui.fs_input_1.text() or 0)
        self.df_students.loc['DXD', '1st Term Students'] = int(self.ui.dxd_input_1.text() or 0)
        self.df_students.loc['BOOK', '1st Term Students'] = int(self.ui.bookkeep_input.text() or 0)

        # update second term
        self.df_students.loc['PCOM', '2nd Term Students'] = int(self.ui.p_comm_input_2.text() or 0)
        self.df_students.loc['BCOM', '2nd Term Students'] = int(self.ui.b_comm_input_2.text() or 0)
        self.df_students.loc['PM', '2nd Term Students'] = int(self.ui.pm_input_2.text() or 0)
        self.df_students.loc['BA', '2nd Term Students'] = int(self.ui.ba_input_2.text() or 0)
        self.df_students.loc['GLM', '2nd Term Students'] = int(self.ui.glm_input_2.text() or 0)
        self.df_students.loc['FS', '2nd Term Students'] = int(self.ui.fs_input_2.text() or 0)
        self.df_students.loc['DXD', '2nd Term Students'] = int(self.ui.dxd_input_2.text() or 0)
        self.df_students.loc['BOOK', '2nd Term Students'] = int(self.ui.bookkeep_input_2.text() or 0)

        # update third term
        self.df_students.loc['PCOM', '3rd Term Students'] = int(self.ui.p_comm_input_3.text() or 0)
        self.df_students.loc['BCOM', '3rd Term Students'] = int(self.ui.b_comm_input_3.text() or 0)
        self.df_students.loc['PM', '3rd Term Students'] = int(self.ui.pm_input_3.text() or 0)
        self.df_students.loc['BA', '3rd Term Students'] = int(self.ui.ba_input_3.text() or 0)
        self.df_students.loc['GLM', '3rd Term Students'] = int(self.ui.glm_input_3.text() or 0)
        self.df_students.loc['FS', '3rd Term Students'] = int(self.ui.fs_input_3.text() or 0)
        self.df_students.loc['DXD', '3rd Term Students'] = int(self.ui.dxd_input_3.text() or 0)
        self.df_students.loc['BOOK', '3rd Term Students'] = int(self.ui.bookkeep_input_3.text() or 0)

        print(self.df_students)

    @pyqtSlot()
    def save_data(self):

        # Get the currently selected index of the semester_select_combobox
        selected_index = self.ui.semester_select_combobox.currentIndex()
        # Check if the selected index is 0
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

    @pyqtSlot()
    def save_input(self):
        # Testing of data saving
        # Need variable/textinput for max students
        # Clear any data from old list
        self.new_list.clear()
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

        # iterate through all Line Edits
        for i in range(0, len(line_edits), 8):
            temp_list = [line_edits[i + j].text() for j in range(8)]
            self.new_list.append(temp_list)
        print(self.new_list)
        # program = Program()
        # return self.new_list
    

    ######################### Student Enrollment Update ###################################

    def update_enrollment(self, file_name):
        # Open the CSV file and read it row by row
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # skip the header row
            for row in csvreader:
                degree = row[2]
                program = row[3]
                term = row[4]

                # Check if the program exists in the dataframe
                if program in self.df_students.index:
                    # Update the enrollment numbers for the appropriate term
                    if term == '1':
                        self.df_students.loc[degree, '1st Term Students'] += 1
                        self.df_students.loc[program, '1st Term Students'] += 1
                    elif term == '2':
                        self.df_students.loc[degree, '2nd Term Students'] += 1
                        self.df_students.loc[program, '2nd Term Students'] += 1
                    elif term == '3':
                        self.df_students.loc[degree, '3rd Term Students'] += 1
                        self.df_students.loc[program, '3rd Term Students'] += 1


    ######################### Rooms updates ###############################################
    @pyqtSlot()
    def update_rooms(self):
        self.ui.rooms_combobox.clear()
        self.week_combo_box.clear()
        classrooms = self.df_rooms.loc[1:, 'Classroom #'].dropna().tolist()
        self.ui.rooms_combobox.addItems(classrooms)
        self.week_combo_box.addItems(classrooms)

    @pyqtSlot()
    def remove_classroom(self):
        # get the currently selected classroom number
        selected_classroom = self.ui.rooms_combobox.currentText()

        # remove the row(s) corresponding to the selected classroom number from the dataframe
        self.df_rooms.drop(self.df_rooms[self.df_rooms['Classroom #'] == selected_classroom].index, inplace=True)

        # update the combobox to reflect the removed classroom number
        self.update_rooms()
        print(self.df_rooms)

    @pyqtSlot()
    def add_room(self):

        # display model to get input from user
        room, ok_pressed = QInputDialog.getText(self, "Add Room", "Room Number:")
        if ok_pressed:
            # Check if room number already exists in the dataframe
            if room in self.df_rooms['Classroom #'].values:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText(f"Room number '{room}' already exists!")
                msg.exec()
            else:
                capacity, ok_pressed = QInputDialog.getInt(self, "Add Room", "Capacity:")
                if ok_pressed and capacity > 0:
                    # create a new dataframe with the new room information
                    new_room = pd.DataFrame({'Classroom #': [room], 'Normal Capacity': [capacity]})

                    # concatenate the new dataframe with the existing dataframe
                    self.df_rooms = pd.concat([self.df_rooms, new_room], ignore_index=True)

                    # update the combobox to reflect the added room
                    self.update_rooms()
                    print(self.df_rooms)
    
    #######################Dataframe initialization function ################################
    def create_programs(self):
        # Define the programs to include in the new dataframe
        programs = ['PCOM',
                    'BCOM',
                    'PM',
                    'BA',
                    'GLM',
                    'FS',
                    'DXD',
                    'BOOK']

        # Create a new dataframe with the programs as the index and 0 as the initial values
        new_df = pd.DataFrame(index=programs, columns=['1st Term Students', '2nd Term Students', '3rd Term Students']).fillna(0)

        # Return new df
        return new_df

    ################################ Populating the Classroom Tables ##################
    '''
    def classroom_schedule(self, index):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0),
                   Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0),
                   Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                   Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                   Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0)]
        classrooms = [Classroom("11-532", 30, 1),
                      Classroom("11-533", 36, 0),
                      Classroom("11-534", 36, 0),
                      Classroom("11-560", 24, 0),
                      Classroom("11-562", 24, 0),
                      Classroom("11-564", 24, 0),
                      Classroom("11-458", 40, 0),
                      Classroom("11-430", 30, 0),
                      Classroom("11-320", 30, 0)]
        term = [Term("Term 1", 1),
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, degree, program, courses, classrooms, term)

        schedule.term_schedule(classrooms, term)
        schedule.display_classroom(term[0], classrooms[index])
        return schedule.return_classroom(term[0], classrooms[index])
    '''
    #sched = classroom_schedule(1, 1)
    #print("Type: ", type(sched))
    #print("the shchedule:", classroom_schedule(1, 1))

    def edit_room_text(self, room_textbox, text):
        # Get the current text in the text edit
        current_text = room_textbox.toPlainText()
        # Append the new text to the current text
        new_text = current_text + text
        # Set the new text in the text edit
        room_textbox.setPlainText(new_text)

    #############################################################################################


"""======================================================================================"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # style sheet load
    filename = str(pathlib.Path(__file__).parent.resolve())+"\\"
    with open(filename+"style.qss", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
