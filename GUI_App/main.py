import datetime

import sys

from courseClass import *

from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLineEdit, QTableView, QMessageBox, \
    QComboBox, QSizePolicy, QHeaderView
from PyQt6.QtWidgets import QDialog, QLabel, QInputDialog
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream, QDir, Qt, QStandardPaths, QDate

import pandas as pd

from Scheduler1 import Ui_MainWindow
import schedule2 as sc

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

        self.schedule = sc.Schedule([],[])
        self.schedule_out = {}

        self.ui.stackedWidget.setCurrentWidget(self.ui.page9)

        ############ Buttons Clicked ############################
        self.ui.data_page_button.clicked.connect(self.showDataPage)
        self.ui.schedule_page_button.clicked.connect(self.showSchedulePage)
        self.ui.load_data_button_students.clicked.connect(self.load_student_data)
        self.ui.load_data_button_room.clicked.connect(self.load_room_data)
        self.ui.load_data_button_program.clicked.connect(self.load_program_data)
        # self.ui.calendar.clicked.connect(self.print_selected_date)
        self.ui.room_533_page_btn.clicked.connect(self.show533Page)
        self.ui.room_534_page_btn.clicked.connect(self.show534Page)
        self.ui.instructions_page_btn.clicked.connect(self.showInstructionsPage)
        

        ###################### Calendar  ####################################

        self.ui.calendar.clicked.connect(self.on_calendar_clicked)
        self.selected_date = self.ui.calendar.selectedDate()
        self.date_time = datetime.datetime(self.selected_date.year(), self.selected_date.month(), self.selected_date.day())

        self.ui.rooms_page_btn.clicked.connect(self.showRoomsPage)

        ################## Data Page Buttons Clicked ################
        # self.ui.save_data_btn.clicked.connect(self.save_data)
        self.ui.generate_schedule_btn.clicked.connect(self.generate_schedule)

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
        # self.display_btn = QPushButton("Display", self)
        # self.display_btn.setGeometry(400, 580, 40, 20)
        self.ui.display_btn.clicked.connect(self.refresh_table)

        self.table_fields()

        # Set the stretch factor for each column
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        # ----------------- list of lists of text field values------------------
        self.new_list = []
    
    ####################### Calendar function ###################################

    @pyqtSlot(QDate)
    def on_calendar_clicked(self, date: QDate):
        # Update the selected date label with the selected date
        self.ui.selected_date_label.setText(f"Date selected: {date.toString()}")
        self.selected_date = date
        print(self.selected_date)
        self.date_time = datetime.datetime(self.selected_date.year(), self.selected_date.month(), self.selected_date.day())
        print(self.date_time)

    def refresh_table(self):
        # Clear the current table view and repopulate it
        self.table_model.clear()
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

    def populate_table(self,class_dict):
        '''
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
        '''

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
        
        course_color = {}

        # Iterate through each row and column of the table model and set dummy text
        for row in range(len(rows)):
            for col in range(len(columns)):
                # Check if this cell is within the start and end time of any course in week 1 on this day
                course_in_cell = None
                if self.week_combo_box.currentText() != '':
                    for course_data in class_dict[self.ui.label_9.text()][
                        self.week_combo_box.currentText()][
                        columns[col]]:
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

    def print_selected_date(self):
        selected_date = self.ui.calendar.selectedDate()
        date_time = datetime.datetime(selected_date.year(), selected_date.month(), selected_date.day())
        print("Type:", type(selected_date))
        print("Selected date:", selected_date.toString("yyyy-MM-dd"))
        print("Type of selected_date:", type(date_time))

    # ------------------------------------- #
    # ------------- LOAD CLASSROOMS ------- #
    # ------------------------------------- #
    @pyqtSlot()
    def load_room_data(self):

        file_name = self.ui.file_name_input_room.text()

        if file_name:
            if file_name.endswith('RoomInfo.csv'):
                self.df_rooms = pd.read_csv(file_name)
                self.ui.load_data_button_room.setText("Load Room Data ✔")
                self.ui.load_data_button_room.setStyleSheet("background-color: green")

            elif file_name.endswith('RoomInfo.xls') or file_name.endswith('RoomInfo.xlsx'):
                self.df_rooms = pd.read_excel(file_name)

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Please enter the correct CSV file path - RoomInfo.csv")
                msg.exec()
                return

            print(self.df_rooms)  # print the loaded dataframe
            self.update_rooms()
            
            self.schedule.update_classrooms(self.df_rooms.values.tolist())

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter the correct CSV file path")
            msg.exec()

    # --------------------------------------------- #
    # ------------- LOAD PROGRAM DATA ------------- #
    # --------------------------------------------- #
    @pyqtSlot()
    def load_program_data(self):

        file_name = self.ui.file_name_input_program.text()

        if file_name:
            if file_name.endswith('Programs.csv'):
                self.df_programs = pd.read_csv(file_name)
                self.ui.load_data_button_program.setText("Load Program Data ✔")
                self.ui.load_data_button_program.setStyleSheet("background-color: green")

            elif file_name.endswith('programs.xls') or file_name.endswith('programs.xlsx'):
                self.df_programs = pd.read_excel(file_name)

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Please enter the correct CSV file path - Programs.csv")
                msg.exec()
                return

            self.schedule.update_programs(self.df_programs.values.tolist())

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter a CSV file path")
            msg.exec()

    # --------------------------------------- #
    # ------------- LOAD STUDENT DATA ------- #
    # --------------------------------------- #
    @pyqtSlot()
    def load_student_data(self):

        file_name = self.ui.file_name_input.text()

        if file_name:
            if file_name.endswith('StudentsInfo.csv'):
                self.update_enrollment(file_name)
                self.ui.load_data_button_students.setText("Load Student Data ✔")
                self.ui.load_data_button_students.setStyleSheet("background-color: green")
            elif file_name.endswith('StudentsInfo.xls') or file_name.endswith('StudentsInfo.xlsx'):
                self.update_enrollment(file_name)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Please enter the correct CSV file path - StudentsInfo.csv")
                msg.exec()
                return

            print(self.df_students)  # print the loaded dataframe
            self.updateProgramsFields()
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter a CSV file path")
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
    def showInstructionsPage(self):
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
        self.ui.bookkeep_input.setText(str(self.df_students.loc['BK', '1st Term Students']))

        # update QLineEdits for second term
        self.ui.p_comm_input_2.setText(str(self.df_students.loc['PCOM', '2nd Term Students']))
        self.ui.b_comm_input_2.setText(str(self.df_students.loc['BCOM', '2nd Term Students']))
        self.ui.pm_input_2.setText(str(self.df_students.loc['PM', '2nd Term Students']))
        self.ui.ba_input_2.setText(str(self.df_students.loc['BA', '2nd Term Students']))
        self.ui.glm_input_2.setText(str(self.df_students.loc['GLM', '2nd Term Students']))
        self.ui.fs_input_2.setText(str(self.df_students.loc['FS', '2nd Term Students']))
        self.ui.dxd_input_2.setText(str(self.df_students.loc['DXD', '2nd Term Students']))
        self.ui.bookkeep_input_2.setText(str(self.df_students.loc['BK', '2nd Term Students']))

        # update QLineEdits for third term
        self.ui.p_comm_input_3.setText(str(self.df_students.loc['PCOM', '3rd Term Students']))
        self.ui.b_comm_input_3.setText(str(self.df_students.loc['BCOM', '3rd Term Students']))
        self.ui.pm_input_3.setText(str(self.df_students.loc['PM', '3rd Term Students']))
        self.ui.ba_input_3.setText(str(self.df_students.loc['BA', '3rd Term Students']))
        self.ui.glm_input_3.setText(str(self.df_students.loc['GLM', '3rd Term Students']))
        self.ui.fs_input_3.setText(str(self.df_students.loc['FS', '3rd Term Students']))
        self.ui.dxd_input_3.setText(str(self.df_students.loc['DXD', '3rd Term Students']))
        self.ui.bookkeep_input_3.setText(str(self.df_students.loc['BK', '3rd Term Students']))

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
        self.df_students.loc['BK', '1st Term Students'] = int(self.ui.bookkeep_input.text() or 0)

        # update second term
        self.df_students.loc['PCOM', '2nd Term Students'] = int(self.ui.p_comm_input_2.text() or 0)
        self.df_students.loc['BCOM', '2nd Term Students'] = int(self.ui.b_comm_input_2.text() or 0)
        self.df_students.loc['PM', '2nd Term Students'] = int(self.ui.pm_input_2.text() or 0)
        self.df_students.loc['BA', '2nd Term Students'] = int(self.ui.ba_input_2.text() or 0)
        self.df_students.loc['GLM', '2nd Term Students'] = int(self.ui.glm_input_2.text() or 0)
        self.df_students.loc['FS', '2nd Term Students'] = int(self.ui.fs_input_2.text() or 0)
        self.df_students.loc['DXD', '2nd Term Students'] = int(self.ui.dxd_input_2.text() or 0)
        self.df_students.loc['BK', '2nd Term Students'] = int(self.ui.bookkeep_input_2.text() or 0)

        # update third term
        self.df_students.loc['PCOM', '3rd Term Students'] = int(self.ui.p_comm_input_3.text() or 0)
        self.df_students.loc['BCOM', '3rd Term Students'] = int(self.ui.b_comm_input_3.text() or 0)
        self.df_students.loc['PM', '3rd Term Students'] = int(self.ui.pm_input_3.text() or 0)
        self.df_students.loc['BA', '3rd Term Students'] = int(self.ui.ba_input_3.text() or 0)
        self.df_students.loc['GLM', '3rd Term Students'] = int(self.ui.glm_input_3.text() or 0)
        self.df_students.loc['FS', '3rd Term Students'] = int(self.ui.fs_input_3.text() or 0)
        self.df_students.loc['DXD', '3rd Term Students'] = int(self.ui.dxd_input_3.text() or 0)
        self.df_students.loc['BK', '3rd Term Students'] = int(self.ui.bookkeep_input_3.text() or 0)

        output_dict = self.df_students.to_dict(orient='index')
        output_dict = {key: list(values.values()) for key, values in output_dict.items()}

        self.schedule.update_program_populations(output_dict)
        
        print(self.df_students)

    @pyqtSlot()
    def save_data(self):

        if self.input_check():
            self.update_data()
                # print(self.df[0])
        else:
            return
    
    ######################## Generate Schedule ###########################
    @pyqtSlot()
    def generate_schedule(self):
        

        if self.date_time.date() <= datetime.datetime.now().date() :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("You did not select a valid Semester Start Date")
            msg.exec()
            return
        else:
            self.save_data()

                    # ADD START DATE!!!!!! :)))))))
            self.schedule.update_start_date(self.date_time)

            self.schedule.schedule_all()
            self.schedule_out = self.schedule.generate_out()

            # POO POO LINE 640
            self.populate_table(self.schedule_out)
            

            #sc.pretty_print_nested_dict(self.schedule_out)

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
        
        output_dict = self.df_students.to_dict(orient='index')
        output_dict = {key: list(values.values()) for key, values in output_dict.items()}

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
                    'BK']

        # Create a new dataframe with the programs as the index and 0 as the initial values
        new_df = pd.DataFrame(index=programs, columns=['1st Term Students', '2nd Term Students', '3rd Term Students']).fillna(0)

        # Return new df
        return new_df



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