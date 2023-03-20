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


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.df = pd.DataFrame  # initialize the variable

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
        self.ui.rooms_page_btn.clicked.connect(self.showRoomsPage)

        ################## Data Page Buttons Clicked ################
        self.ui.save_data_btn.clicked.connect(self.save_data)

        ################## Rooms Page Buttons Clicked ###############

        # connect the remove button to the remove_classroom function
        self.ui.remove_room_btn.clicked.connect(self.remove_classroom)

        # connect the add button to the add_room function
        self.ui.add_room_btn.clicked.connect(self.add_room)

        ############################################################

        self.ui.file_name_input.mousePressEvent = self.browse_file

        # Create table view
        self.table_view = QTableView(self.ui.page2)
        self.table_view.setGeometry(100, 70, 700, 500)
        self.table_model = QStandardItemModel()
        self.table_view.setModel(self.table_model)

        # Set the size policy of the table view
        self.table_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Add a dropdown for selecting the week
        self.week_combo_box = QComboBox(self.ui.page2)
        self.week_combo_box.setGeometry(100, 40, 100, 30)

        # Classrooms for dropdown
        room = ["Class 11-533", "Class 11-534", "Class 11-560", "Class 11-562", "Class 11-564", "Class 11-458", "Class 11-430",
                "Class 11-320", "Class 11-532"]

        # Add options to the dropdown for each week
        for i in range(len(room)):
            self.week_combo_box.addItem(f"{room[i]}")


        # Set schedule default as week 1
        self.week = 1

        # Add buttons for changing week
        self.week_label = QLabel("Week 1", self)
        self.week_label.setGeometry(400, 580, 100, 20)
        self.week_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.left_button = QPushButton("<", self)
        self.left_button.setGeometry(350, 580, 40, 20)
        self.left_button.clicked.connect(self.decrement_week)
        self.left_button.clicked.connect(self.refresh_table)

        self.right_button = QPushButton(">", self)
        self.right_button.setGeometry(500, 580, 40, 20)
        self.right_button.clicked.connect(self.increment_week)
        self.right_button.clicked.connect(self.refresh_table)


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
        classroom_11_533 = {
            "Week 1": {
                "Course 1": {"start_time": "08:00", "end_time": "09:30", "days": ["Mon", "Wed"]},
                "Course 2": {"start_time": "10:00", "end_time": "11:30", "days": ["Tue", "Thu"]},
                "Course 3": {"start_time": "12:00", "end_time": "13:30", "days": ["Mon", "Wed"]},
                "Course 4": {"start_time": "14:00", "end_time": "15:30", "days": ["Tue", "Thu"]},
                "Course 5": {"start_time": "16:00", "end_time": "17:30", "days": ["Mon", "Wed"]},
                "Course 6": {"start_time": "18:00", "end_time": "19:30", "days": ["Tue", "Thu"]},
            },
            "Week 2": {
                "Course a": {"start_time": "08:30", "end_time": "10:00", "days": ["Mon", "Wed"]},
                "Course b": {"start_time": "11:00", "end_time": "12:30", "days": ["Tue", "Thu"]},
                "Course c": {"start_time": "13:00", "end_time": "14:30", "days": ["Mon", "Wed"]},
                "Course d": {"start_time": "15:00", "end_time": "16:30", "days": ["Tue", "Thu"]},
                "Course e": {"start_time": "17:00", "end_time": "18:30", "days": ["Mon", "Wed"]},
                "Course f": {"start_time": "19:00", "end_time": "20:30", "days": ["Tue", "Thu"]},
            }
        }
        # Iterate through each row and column of the table model and set dummy text
        for row in range(len(rows)):
            for col in range(len(columns)):
                # Check if this cell is within the start and end time of any course in classroom_11_533 on this day
                course_in_cell = None
                for course_name, course_data in classroom_11_533[self.week_label.text()].items():
                    start_time = datetime.datetime.strptime(course_data["start_time"], '%H:%M').time()
                    end_time = datetime.datetime.strptime(course_data["end_time"], '%H:%M').time()
                    if columns[col].startswith(course_data["days"][0]) and \
                            datetime.datetime.strptime(rows[row][0], '%H:%M:%S').time() >= start_time and \
                            datetime.datetime.strptime(rows[row][0], '%H:%M:%S').time() < end_time:
                        course_in_cell = course_name
                        break
                for course_name, course_data in classroom_11_533[self.week_label.text()].items():
                    start_time = datetime.datetime.strptime(course_data["start_time"], '%H:%M').time()
                    end_time = datetime.datetime.strptime(course_data["end_time"], '%H:%M').time()
                    if columns[col].startswith(course_data["days"][1]) and \
                            datetime.datetime.strptime(rows[row][0], '%H:%M:%S').time() >= start_time and \
                            datetime.datetime.strptime(rows[row][0], '%H:%M:%S').time() < end_time:
                        course_in_cell = course_name
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
            self.week_label.setText(f"Week {self.week}")

    def decrement_week(self):
        if self.week > 1:
            self.week -= 1
            self.week_label.setText(f"Week {self.week}")

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
            self.update_rooms()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please enter a CSV file path")
            msg.exec()

        [Classroom("11-532", 30, 1),
         Classroom("11-533", 36, 0),
         Classroom("11-534", 36, 0),
         Classroom("11-560", 24, 0),
         Classroom("11-562", 24, 0),
         Classroom("11-564", 24, 0),
         Classroom("11-458", 40, 0),
         Classroom("11-430", 30, 0),
         Classroom("11-320", 30, 0)]

        self.edit_room_text(self.ui.text_533, self.classroom_schedule(0))
        self.edit_room_text(self.ui.text_534, self.classroom_schedule(1))
        self.edit_room_text(self.ui.text_560, self.classroom_schedule(2))
        self.edit_room_text(self.ui.text_562, self.classroom_schedule(3))
        self.edit_room_text(self.ui.text_564, self.classroom_schedule(4))
        self.edit_room_text(self.ui.text_458, self.classroom_schedule(5))
        self.edit_room_text(self.ui.text_430, self.classroom_schedule(6))
        self.edit_room_text(self.ui.text_320, self.classroom_schedule(7))

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

    ######################### Rooms updates ###############################################
    @pyqtSlot()
    def update_rooms(self):
        self.ui.rooms_combobox.clear()
        classrooms = self.df.loc[9:, 'Programs'].dropna().tolist()
        self.ui.rooms_combobox.addItems(classrooms)

    @pyqtSlot()
    def remove_classroom(self):
        # get the currently selected classroom number
        selected_classroom = self.ui.rooms_combobox.currentText()

        # remove the row(s) corresponding to the selected classroom number from the dataframe
        self.df.drop(self.df[self.df['Programs'] == selected_classroom].index, inplace=True)

        # update the combobox to reflect the removed classroom number
        self.update_rooms()
        print(self.df)

    @pyqtSlot()
    def add_room(self):

        # display model to get input from user
        room, ok_pressed = QInputDialog.getText(self, "Add Room", "Room Number:")
        if ok_pressed:
            # Check if room number already exists in the dataframe
            if room in self.df['Programs'].values:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText(f"Room number '{room}' already exists!")
                msg.exec()
            else:
                capacity, ok_pressed = QInputDialog.getInt(self, "Add Room", "Capacity:")
                if ok_pressed and capacity > 0:
                    # create a new dataframe with the new room information
                    new_room = pd.DataFrame({'Programs': [room], '1st Term Students': [capacity]})

                    # concatenate the new dataframe with the existing dataframe
                    self.df = pd.concat([self.df, new_room], ignore_index=True)

                    # update the combobox to reflect the added room
                    self.update_rooms()
                    print(self.df)

    ################################ Populating the Classroom Tables ##################
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

    sched = classroom_schedule(1, 1)
    print("Type: ", type(sched))
    print("the shchedule:", classroom_schedule(1, 1))

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
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
