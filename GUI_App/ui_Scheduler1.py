# Form implementation generated from reading ui file 'd:\MacEwan\CMPT 395\Project\2023-01_Team3_VLAD\GUI_App\Scheduler1.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 688)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icons2/menu-4-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.menu_widget = QtWidgets.QWidget(parent=self.widget)
        self.menu_widget.setGeometry(QtCore.QRect(-10, -10, 201, 691))
        self.menu_widget.setObjectName("menu_widget")
        self.title_label = QtWidgets.QLabel(parent=self.menu_widget)
        self.title_label.setGeometry(QtCore.QRect(50, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.exit_button = QtWidgets.QPushButton(parent=self.menu_widget)
        self.exit_button.setGeometry(QtCore.QRect(20, 630, 141, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icons2/account-logout-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_button.setIcon(icon1)
        self.exit_button.setCheckable(True)
        self.exit_button.setAutoExclusive(True)
        self.exit_button.setObjectName("exit_button")
        self.layoutWidget = QtWidgets.QWidget(parent=self.menu_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 100, 161, 402))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.data_page_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.data_page_button.setFont(font)
        self.data_page_button.setCheckable(True)
        self.data_page_button.setAutoExclusive(True)
        self.data_page_button.setObjectName("data_page_button")
        self.verticalLayout_2.addWidget(self.data_page_button)
        self.room_533_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_533_page_btn.setFont(font)
        self.room_533_page_btn.setObjectName("room_533_page_btn")
        self.verticalLayout_2.addWidget(self.room_533_page_btn)
        self.room_534_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_534_page_btn.setFont(font)
        self.room_534_page_btn.setObjectName("room_534_page_btn")
        self.verticalLayout_2.addWidget(self.room_534_page_btn)
        self.room_560_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_560_page_btn.setFont(font)
        self.room_560_page_btn.setObjectName("room_560_page_btn")
        self.verticalLayout_2.addWidget(self.room_560_page_btn)
        self.room_458_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_458_page_btn.setFont(font)
        self.room_458_page_btn.setObjectName("room_458_page_btn")
        self.verticalLayout_2.addWidget(self.room_458_page_btn)
        self.room_562_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_562_page_btn.setFont(font)
        self.room_562_page_btn.setObjectName("room_562_page_btn")
        self.verticalLayout_2.addWidget(self.room_562_page_btn)
        self.room_564_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_564_page_btn.setFont(font)
        self.room_564_page_btn.setObjectName("room_564_page_btn")
        self.verticalLayout_2.addWidget(self.room_564_page_btn)
        self.room_320_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_320_page_btn.setFont(font)
        self.room_320_page_btn.setObjectName("room_320_page_btn")
        self.verticalLayout_2.addWidget(self.room_320_page_btn)
        self.room_430_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_430_page_btn.setFont(font)
        self.room_430_page_btn.setObjectName("room_430_page_btn")
        self.verticalLayout_2.addWidget(self.room_430_page_btn)
        self.room_532_lab_page_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.room_532_lab_page_btn.setFont(font)
        self.room_532_lab_page_btn.setObjectName("room_532_lab_page_btn")
        self.verticalLayout_2.addWidget(self.room_532_lab_page_btn)
        self.schedule_page_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.schedule_page_button.setFont(font)
        self.schedule_page_button.setCheckable(True)
        self.schedule_page_button.setAutoExclusive(True)
        self.schedule_page_button.setObjectName("schedule_page_button")
        self.verticalLayout_2.addWidget(self.schedule_page_button)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setGeometry(QtCore.QRect(210, 0, 841, 681))
        self.widget_4.setObjectName("widget_4")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_4)
        self.stackedWidget.setGeometry(QtCore.QRect(-20, 0, 861, 681))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label = QtWidgets.QLabel(parent=self.page1)
        self.label.setGeometry(QtCore.QRect(200, 180, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=self.page1)
        self.label_4.setGeometry(QtCore.QRect(120, 360, 329, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.page1)
        self.label_5.setGeometry(QtCore.QRect(100, 240, 352, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.page1)
        self.label_6.setGeometry(QtCore.QRect(127, 270, 322, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.page1)
        self.label_7.setGeometry(QtCore.QRect(200, 410, 233, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.page1)
        self.label_8.setGeometry(QtCore.QRect(220, 440, 215, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.page1)
        self.label_10.setGeometry(QtCore.QRect(60, 480, 402, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.page1)
        self.label_11.setGeometry(QtCore.QRect(186, 510, 254, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.page1)
        self.label_12.setGeometry(QtCore.QRect(70, 540, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.page1)
        self.label_13.setGeometry(QtCore.QRect(210, 570, 222, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.save_data_btn = QtWidgets.QPushButton(parent=self.page1)
        self.save_data_btn.setGeometry(QtCore.QRect(380, 630, 93, 28))
        self.save_data_btn.setObjectName("save_data_btn")
        self.pm_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.pm_input_1.setGeometry(QtCore.QRect(433, 412, 91, 22))
        self.pm_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pm_input_1.setObjectName("pm_input_1")
        self.ba_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.ba_input_1.setGeometry(QtCore.QRect(433, 444, 91, 22))
        self.ba_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ba_input_1.setObjectName("ba_input_1")
        self.p_comm_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.p_comm_input_1.setGeometry(QtCore.QRect(430, 238, 91, 22))
        self.p_comm_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p_comm_input_1.setObjectName("p_comm_input_1")
        self.glm_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.glm_input_1.setGeometry(QtCore.QRect(433, 476, 91, 22))
        self.glm_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.glm_input_1.setObjectName("glm_input_1")
        self.fs_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.fs_input_1.setGeometry(QtCore.QRect(433, 508, 91, 22))
        self.fs_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fs_input_1.setObjectName("fs_input_1")
        self.dxd_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.dxd_input_1.setGeometry(QtCore.QRect(433, 540, 91, 22))
        self.dxd_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dxd_input_1.setObjectName("dxd_input_1")
        self.bookkeep_input = QtWidgets.QLineEdit(parent=self.page1)
        self.bookkeep_input.setGeometry(QtCore.QRect(433, 572, 91, 22))
        self.bookkeep_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bookkeep_input.setObjectName("bookkeep_input")
        self.file_name_input = QtWidgets.QLineEdit(parent=self.page1)
        self.file_name_input.setGeometry(QtCore.QRect(140, 40, 311, 31))
        self.file_name_input.setObjectName("file_name_input")
        self.load_data_button = QtWidgets.QPushButton(parent=self.page1)
        self.load_data_button.setGeometry(QtCore.QRect(500, 40, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.load_data_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Icons2/download-2-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.load_data_button.setIcon(icon2)
        self.load_data_button.setIconSize(QtCore.QSize(25, 25))
        self.load_data_button.setCheckable(True)
        self.load_data_button.setAutoExclusive(True)
        self.load_data_button.setObjectName("load_data_button")
        self.bookkeep_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.bookkeep_input_2.setGeometry(QtCore.QRect(560, 570, 91, 22))
        self.bookkeep_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bookkeep_input_2.setObjectName("bookkeep_input_2")
        self.pm_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.pm_input_2.setGeometry(QtCore.QRect(560, 410, 91, 22))
        self.pm_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pm_input_2.setObjectName("pm_input_2")
        self.p_comm_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.p_comm_input_2.setGeometry(QtCore.QRect(557, 236, 91, 22))
        self.p_comm_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p_comm_input_2.setObjectName("p_comm_input_2")
        self.ba_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.ba_input_2.setGeometry(QtCore.QRect(560, 442, 91, 22))
        self.ba_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ba_input_2.setObjectName("ba_input_2")
        self.b_comm_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.b_comm_input_2.setGeometry(QtCore.QRect(557, 268, 91, 22))
        self.b_comm_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.b_comm_input_2.setObjectName("b_comm_input_2")
        self.glm_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.glm_input_2.setGeometry(QtCore.QRect(560, 474, 91, 22))
        self.glm_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.glm_input_2.setObjectName("glm_input_2")
        self.dxd_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.dxd_input_2.setGeometry(QtCore.QRect(560, 538, 91, 22))
        self.dxd_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dxd_input_2.setObjectName("dxd_input_2")
        self.fs_input_2 = QtWidgets.QLineEdit(parent=self.page1)
        self.fs_input_2.setGeometry(QtCore.QRect(560, 506, 91, 22))
        self.fs_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fs_input_2.setObjectName("fs_input_2")
        self.bookkeep_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.bookkeep_input_3.setGeometry(QtCore.QRect(680, 570, 91, 22))
        self.bookkeep_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bookkeep_input_3.setObjectName("bookkeep_input_3")
        self.fs_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.fs_input_3.setGeometry(QtCore.QRect(680, 506, 91, 22))
        self.fs_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fs_input_3.setObjectName("fs_input_3")
        self.dxd_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.dxd_input_3.setGeometry(QtCore.QRect(680, 538, 91, 22))
        self.dxd_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dxd_input_3.setObjectName("dxd_input_3")
        self.p_comm_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.p_comm_input_3.setGeometry(QtCore.QRect(677, 236, 91, 22))
        self.p_comm_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p_comm_input_3.setObjectName("p_comm_input_3")
        self.b_comm_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.b_comm_input_3.setGeometry(QtCore.QRect(677, 268, 91, 22))
        self.b_comm_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.b_comm_input_3.setObjectName("b_comm_input_3")
        self.pm_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.pm_input_3.setGeometry(QtCore.QRect(680, 410, 91, 22))
        self.pm_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pm_input_3.setObjectName("pm_input_3")
        self.glm_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.glm_input_3.setGeometry(QtCore.QRect(680, 474, 91, 22))
        self.glm_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.glm_input_3.setObjectName("glm_input_3")
        self.ba_input_3 = QtWidgets.QLineEdit(parent=self.page1)
        self.ba_input_3.setGeometry(QtCore.QRect(680, 442, 91, 22))
        self.ba_input_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ba_input_3.setObjectName("ba_input_3")
        self.label_3 = QtWidgets.QLabel(parent=self.page1)
        self.label_3.setGeometry(QtCore.QRect(440, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_14 = QtWidgets.QLabel(parent=self.page1)
        self.label_14.setGeometry(QtCore.QRect(560, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.page1)
        self.label_15.setGeometry(QtCore.QRect(680, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.b_comm_input_1 = QtWidgets.QLineEdit(parent=self.page1)
        self.b_comm_input_1.setGeometry(QtCore.QRect(430, 270, 91, 22))
        self.b_comm_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.b_comm_input_1.setObjectName("b_comm_input_1")
        self.label_16 = QtWidgets.QLabel(parent=self.page1)
        self.label_16.setGeometry(QtCore.QRect(290, 110, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.semester_select_combobox = QtWidgets.QComboBox(parent=self.page1)
        self.semester_select_combobox.setGeometry(QtCore.QRect(500, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.semester_select_combobox.setFont(font)
        self.semester_select_combobox.setObjectName("semester_select_combobox")
        self.semester_select_combobox.addItem("")
        self.semester_select_combobox.addItem("")
        self.semester_select_combobox.addItem("")
        self.semester_select_combobox.addItem("")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.label_9 = QtWidgets.QLabel(parent=self.page2)
        self.label_9.setGeometry(QtCore.QRect(290, 110, 261, 291))
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label_17 = QtWidgets.QLabel(parent=self.page3)
        self.label_17.setGeometry(QtCore.QRect(400, 20, 101, 16))
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.label_18 = QtWidgets.QLabel(parent=self.page4)
        self.label_18.setGeometry(QtCore.QRect(410, 10, 101, 16))
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page4)
        self.page11 = QtWidgets.QWidget()
        self.page11.setObjectName("page11")
        self.label_24 = QtWidgets.QLabel(parent=self.page11)
        self.label_24.setGeometry(QtCore.QRect(410, 10, 101, 16))
        self.label_24.setObjectName("label_24")
        self.stackedWidget.addWidget(self.page11)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.label_19 = QtWidgets.QLabel(parent=self.page5)
        self.label_19.setGeometry(QtCore.QRect(390, 20, 101, 16))
        self.label_19.setObjectName("label_19")
        self.stackedWidget.addWidget(self.page5)
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.label_20 = QtWidgets.QLabel(parent=self.page6)
        self.label_20.setGeometry(QtCore.QRect(390, 10, 101, 16))
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.page6)
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName("page7")
        self.label_21 = QtWidgets.QLabel(parent=self.page7)
        self.label_21.setGeometry(QtCore.QRect(390, 10, 101, 16))
        self.label_21.setObjectName("label_21")
        self.stackedWidget.addWidget(self.page7)
        self.page8 = QtWidgets.QWidget()
        self.page8.setObjectName("page8")
        self.label_22 = QtWidgets.QLabel(parent=self.page8)
        self.label_22.setGeometry(QtCore.QRect(400, 10, 101, 16))
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.page8)
        self.page9 = QtWidgets.QWidget()
        self.page9.setObjectName("page9")
        self.label_25 = QtWidgets.QLabel(parent=self.page9)
        self.label_25.setGeometry(QtCore.QRect(410, 10, 101, 16))
        self.label_25.setObjectName("label_25")
        self.stackedWidget.addWidget(self.page9)
        self.page10 = QtWidgets.QWidget()
        self.page10.setObjectName("page10")
        self.label_23 = QtWidgets.QLabel(parent=self.page10)
        self.label_23.setGeometry(QtCore.QRect(390, 10, 131, 16))
        self.label_23.setObjectName("label_23")
        self.stackedWidget.addWidget(self.page10)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.exit_button.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduling App"))
        self.title_label.setText(_translate("MainWindow", "Scheduler"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.data_page_button.setText(_translate("MainWindow", "Data Input"))
        self.room_533_page_btn.setText(_translate("MainWindow", "Room 533"))
        self.room_534_page_btn.setText(_translate("MainWindow", "Room 534"))
        self.room_560_page_btn.setText(_translate("MainWindow", "Room 560"))
        self.room_458_page_btn.setText(_translate("MainWindow", "Room 458"))
        self.room_562_page_btn.setText(_translate("MainWindow", "Room 562"))
        self.room_564_page_btn.setText(_translate("MainWindow", "Room 564"))
        self.room_320_page_btn.setText(_translate("MainWindow", "Room 320"))
        self.room_430_page_btn.setText(_translate("MainWindow", "Room 430"))
        self.room_532_lab_page_btn.setText(_translate("MainWindow", "Room 532 Lab"))
        self.schedule_page_button.setText(_translate("MainWindow", "Schedule"))
        self.label.setText(_translate("MainWindow", "Core Programs"))
        self.label_4.setText(_translate("MainWindow", "Specialized Specific Programs"))
        self.label_5.setText(_translate("MainWindow", "Professional Communication (P-COMM):"))
        self.label_6.setText(_translate("MainWindow", "Business Communication (B-COMM):"))
        self.label_7.setText(_translate("MainWindow", "Project Management (PM):"))
        self.label_8.setText(_translate("MainWindow", "Business Analysis (BA): "))
        self.label_10.setText(_translate("MainWindow", "Supply Chain Management & Logistics (GLM):"))
        self.label_11.setText(_translate("MainWindow", "Full Stack Development (FS):"))
        self.label_12.setText(_translate("MainWindow", "Digital Experience Design Foundation (DXD):"))
        self.label_13.setText(_translate("MainWindow", "BookKeeping Certificate:"))
        self.save_data_btn.setText(_translate("MainWindow", "SAVE DATA"))
        self.pm_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.ba_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.p_comm_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.glm_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.fs_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.dxd_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.bookkeep_input.setPlaceholderText(_translate("MainWindow", "0"))
        self.file_name_input.setPlaceholderText(_translate("MainWindow", "Select File..."))
        self.load_data_button.setText(_translate("MainWindow", "Load Data"))
        self.bookkeep_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.pm_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.p_comm_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.ba_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.b_comm_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.glm_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.dxd_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.fs_input_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.bookkeep_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.fs_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.dxd_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.p_comm_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.b_comm_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.pm_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.glm_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.ba_input_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "1st Term"))
        self.label_14.setText(_translate("MainWindow", "2nd Term"))
        self.label_15.setText(_translate("MainWindow", "3rd Term"))
        self.b_comm_input_1.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Choose Semester:"))
        self.semester_select_combobox.setItemText(0, _translate("MainWindow", "(make selection)"))
        self.semester_select_combobox.setItemText(1, _translate("MainWindow", "Fall"))
        self.semester_select_combobox.setItemText(2, _translate("MainWindow", "Winter"))
        self.semester_select_combobox.setItemText(3, _translate("MainWindow", "Spring/Summer"))
        self.label_9.setText(_translate("MainWindow", "Table grid view, calendar possibly?"))
        self.label_17.setText(_translate("MainWindow", "page room 533"))
        self.label_18.setText(_translate("MainWindow", "page room 534"))
        self.label_24.setText(_translate("MainWindow", "page room 560"))
        self.label_19.setText(_translate("MainWindow", "page room 458"))
        self.label_20.setText(_translate("MainWindow", "page room 562"))
        self.label_21.setText(_translate("MainWindow", "page room 564"))
        self.label_22.setText(_translate("MainWindow", "page room 320"))
        self.label_25.setText(_translate("MainWindow", "page room 430"))
        self.label_23.setText(_translate("MainWindow", "page room 532 Lab"))