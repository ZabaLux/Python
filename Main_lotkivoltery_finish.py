import sys
import numpy as np
import os
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMessageBox
import sqlite3

conn = sqlite3.connect('server.db')
c = conn.cursor()



class Ui_mainWindow(object):

    nameInteraction = ""
    startprey = 0
    startpredators = 0
    growthprey = 0
    deathpredator = 0
    predationrate = 0
    conversion = 0
    dt = 0
    time = 0



    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(712, 399)
        mainWindow.setMaximumSize(QtCore.QSize(712, 399))
        mainWindow.setMouseTracking(True)
        mainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        mainWindow.setToolTipDuration(0)

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Parameters_label = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.Parameters_label.setFont(font)
        self.Parameters_label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Parameters_label.setObjectName("Parameters_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole,
        self.Parameters_label)

        self.name_interaction_label = QtWidgets.QLabel(self.centralwidget)
        self.name_interaction_label.setObjectName("name_interaction_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.name_interaction_label)
        
        self.name_interaction_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_interaction_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.name_interaction_edit.setObjectName("name_interaction_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.name_interaction_edit)

        self.startprey_label = QtWidgets.QLabel(self.centralwidget)
        self.startprey_label.setObjectName("startprey_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.startprey_label)

        self.startprey_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.startprey_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.startprey_edit.setObjectName("startprey_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.startprey_edit)
        

        self.startpredators_label = QtWidgets.QLabel(self.centralwidget)
        self.startpredators_label.setObjectName("startpredators_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.startpredators_label)

        self.startpredators_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.startpredators_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.startpredators_edit.setObjectName("startpredators_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.startpredators_edit)
        

        self.deathpredator_label = QtWidgets.QLabel(self.centralwidget)
        self.deathpredator_label.setObjectName("deathpredator_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                  self.deathpredator_label)

        self.deathpredator_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.deathpredator_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.deathpredator_edit.setObjectName("deathpredator_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                  self.deathpredator_edit)

        self.growthprey_label = QtWidgets.QLabel(self.centralwidget)
        self.growthprey_label.setObjectName("growthprey_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole,
                                  self.growthprey_label)

        self.growthprey_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.growthprey_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.growthprey_edit.setObjectName("growthprey_edit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole,
                                  self.growthprey_edit)

        self.predationrate_label = QtWidgets.QLabel(self.centralwidget)
        self.predationrate_label.setObjectName("predationrate_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole,
                                  self.predationrate_label)

        self.predationrate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.predationrate_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.predationrate_edit.setObjectName("predationrate_edit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole,
                                  self.predationrate_edit)

        self.conversion_label = QtWidgets.QLabel(self.centralwidget)
        self.conversion_label.setObjectName("conversion_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole,
                                  self.conversion_label)

        self.conversion_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.conversion_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.conversion_edit.setObjectName("conversion_edit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole,
                                  self.conversion_edit)

        self.dt_label = QtWidgets.QLabel(self.centralwidget)
        self.dt_label.setObjectName("dt_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole,
                                  self.dt_label)

        self.dt_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.dt_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.dt_edit.setObjectName("dt_edit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole,
                                  self.dt_edit)

        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setObjectName("time_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole,
                                  self.time_label)

        self.time_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.time_edit.setMinimumSize(QtCore.QSize(143, 25))
        self.time_edit.setObjectName("time_edit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole,
                                  self.time_edit)

        #Robie wszystkie qlineEdit(oprocz Name Interaction) akceptowane tylko jako liczba całkowita
        self.onlyInt = QtGui.QDoubleValidator()
        self.startprey_edit.setValidator(self.onlyInt)
        self.deathpredator_edit.setValidator(self.onlyInt)
        self.growthprey_edit.setValidator(self.onlyInt)
        self.predationrate_edit.setValidator(self.onlyInt)
        self.conversion_edit.setValidator(self.onlyInt)
        self.dt_edit.setValidator(self.onlyInt)
        self.time_edit.setValidator(self.onlyInt)


        self.MakePlot_button = QtWidgets.QPushButton(self.centralwidget)
        self.MakePlot_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MakePlot_button.setObjectName("MakePlot_button")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole,
                                  self.MakePlot_button)
        self.MakePlot_button.clicked.connect(self.makeplot)

        self.AddtoDatebase_button = QtWidgets.QPushButton(self.centralwidget)
        self.AddtoDatebase_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddtoDatebase_button.clicked.connect(self.load_data)
        self.AddtoDatebase_button.setObjectName("AddtoDatebase_button")
        
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole,
                                  self.AddtoDatebase_button)
        

        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 2, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Box_name_label = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.Box_name_label.setFont(font)
        self.Box_name_label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Box_name_label.setObjectName("Box_name_label")
        self.gridLayout.addWidget(self.Box_name_label, 0, 0, 1, 1)

        self.Confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Confirm_button.setObjectName("Confirm_button")
        self.Confirm_button.clicked.connect(self.paste_values_box)
        self.gridLayout.addWidget(self.Confirm_button, 2, 0, 1, 1)

        self.Box_Interactions = QtWidgets.QComboBox(self.centralwidget)
        self.Box_Interactions.setMaximumSize(QtCore.QSize(294, 25))
        self.Box_Interactions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Box_Interactions.setMouseTracking(False)
        self.Box_Interactions.setToolTipDuration(-2)
        self.Box_Interactions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box_Interactions.setAutoFillBackground(False)
        
        self.Box_Interactions.addItems(self.take_data_head())
        self.gridLayout.addWidget(self.Box_Interactions, 1, 0, 1, 1)


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 22))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen_h = QtWidgets.QAction(mainWindow)
        self.actionOpen_h.setObjectName("actionOpen_h")
        self.actionOpen_a = QtWidgets.QAction(mainWindow)
        self.actionOpen_h.setObjectName("actionOpen_a")
        self.menuHelp.addAction(self.actionOpen_h)
        self.menuAbout.addAction(self.actionOpen_a)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.actionOpen_h.triggered.connect(self.open_h)
        self.actionOpen_a.triggered.connect(self.open_a)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Predator-prey interaction modelling"))
        self.Parameters_label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Parameters</p></body></html>"))
        self.name_interaction_label.setText(_translate("mainWindow", "Name Inetaction"))
        self.startprey_label.setText(_translate("mainWindow", "Start Prey"))
        self.startpredators_label.setText(_translate("mainWindow", "Start Predators"))
        self.deathpredator_label.setText(_translate("mainWindow", "Death Predator"))
        self.growthprey_label.setText(_translate("mainWindow", "Growth Prey"))
        self.predationrate_label.setText(_translate("mainWindow", "Predation Rate"))
        self.conversion_label.setText(_translate("mainWindow", "Conversion"))
        self.dt_label.setText(_translate("mainWindow", "DT"))
        self.time_label.setText(_translate("mainWindow", "Time"))
        self.MakePlot_button.setText(_translate("mainWindow", "Make plot"))
        self.AddtoDatebase_button.setText(_translate("mainWindow", "Add to database"))
        self.Box_name_label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Ready-made interactions</p></body></html>"))
        self.Confirm_button.setText(_translate("mainWindow", "Confirm"))

        self.menuAbout.setTitle(_translate("mainWindow", "About"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.actionOpen_h.setText(_translate("mainWindow", "Open"))
        self.actionOpen_a.setText(_translate("mainWindow", "Open"))


    def value_edit(self):
        self.nameInteraction = self.name_interaction_edit.text()
        self.startprey = int(self.startprey_edit.text())
        self.startpredators = int(self.startpredators_edit.text())
        self.growthprey = float(self.growthprey_edit.text().replace(",","."))
        self.deathpredator = float(self.deathpredator_edit.text().replace(",","."))
        self.predationrate = float(self.predationrate_edit.text().replace(",","."))
        self.conversion = float(self.conversion_edit.text().replace(",","."))
        self.dt = float(self.dt_edit.text().replace(",","."))
        self.time = int(self.time_edit.text().replace(",","."))


    def open_h(self):
        os.system('xdg-open help.pdf')

    def open_a(self):
        os.system('xdg-open about.pdf')



    # model
    def model(self,x,y):
        prey = (float(self.growthprey) -float( self.predationrate) * y * 1.0 ) * x * 1.0
        predators = (self.conversion*x - self.deathpredator)*y
        return(prey, predators)


    #dynamics
    def add(self,x,y):
        x1, y1 = self.model(x, y)
        x2, y2 = self.model(x + x1*self.dt/2, y + y1*self.dt/2)
        x3, y3 = self.model(x + x2*self.dt/2, y + y2*self.dt/2)
        x4, y4 = self.model(x + x3*self.dt, y + y3*self.dt)
        xnew = x + (x1 + 2*x2 + 2*x3 + x4)*self.dt/6
        ynew = y + (y1 + 2*y2 + 2*y3 + y4)*self.dt/6
        return xnew, ynew


    def makeplot(self):
        self.value_edit()
        x, y = self.make_xy()
        #time
        t = np.arange(self.time)*self.dt

        plt.plot(t, x, label='Prey', linewidth=1)
        plt.plot(t, y, label='Predator', linewidth=1)
        plt.legend(loc = 'upper right')
        plt.xlabel('Time')
        plt.show()


    def make_xy(self):
        x = np.zeros(self.time)
        y = np.zeros(self.time)
        x[0] = self.startprey
        y[0] = self.startpredators
        for k in range(self.time - 1):
            x[k+1], y[k+1] = self.add(x[k], y[k])
        return(x, y)


    def paste_values_box(self):
        value_from_list = self.Box_Interactions.currentText()
        

###########################################################################################################################
    def create_table(self):
            c.execute("""CREATE TABLE IF NOT EXISTS `COEFFICIENTS` (
            `Interactions` varchar(255) NOT NULL,
            `growthprey` decimal(18,5) DEFAULT NULL,
            `Death_rate_praedator` decimal(18,5) DEFAULT NULL,
            `Predation_rate` decimal(18,5) DEFAULT NULL,
            `Conversion_rate_of_preys_into_predators` decimal(18,5) DEFAULT NULL,
            PRIMARY KEY (`Interactions`)
            )""")

    def data_entry(self):
        c.execute("""INSERT INTO `COEFFICIENTS` VALUES ('Eagles-Seagulls',0.23270,0.18090,0.02417,0.00188),
                                                        ('Ladybug-Aphid',0.30000,0.10000,0.90000,0.00500),
                                                        ('Lion - Wildebeest',0.40500,1.50000,0.81000,0.12500),
                                                        ('Lion - Zebra',0.34000,1.50000,0.75000,0.12500),
                                                        ('Seal-Herring',0.40000,0.10000,0.01000,0.00200),
                                                        ('Seal-Steelhead trout',0.70000,0.10000,0.01000,0.00100),
                                                        ('Spider - Fly',0.10000,0.50000,0.00100,0.00100),
                                                        ('Wolf - Elk',0.05000,0.23000,0.19000,0.07000);""")
        conn.commit()
        c.close()
        conn.close()

    def load_data(self):
        self.value_edit()
        print(self.startpredators)
        self.Box_Interactions.addItem(self.nameInteraction)
        c.execute("""INSERT INTO `COEFFICIENTS`(`Interactions`, `growthprey`, `Death_rate_praedator`, `Predation_rate`, 
                                                `Conversion_rate_of_preys_into_predators`)
                            VALUES('%s', '%f','%f','%f','%f')""" % (self.nameInteraction, self.growthprey, self.deathpredator,
                                                                    self.predationrate, self.conversion))
        conn.commit()

    # def read_data(self):
    #     c.execute(""" SELECT * FROM `COEFFICIENTS`""")
    #     for row 


    def take_data_head(self):
        interaction_list = []
        c.execute("SELECT * FROM COEFFICIENTS")
        takeAll = c.fetchall()
        for i in takeAll:
            k = i[0]
            interaction_list.append(k)
        return(interaction_list)

    def paste_values_box(self):
        c.execute("SELECT * FROM COEFFICIENTS")
        takeAll = c.fetchall()
        value_from_list = self.Box_Interactions.currentText()
        for i in takeAll:
            if i[0] == value_from_list:
                self.name_interaction_edit.setText(i[0])
                self.growthprey_edit.setText(str(i[1]))
                self.deathpredator_edit.setText(str(i[2]))
                self.predationrate_edit.setText(str(i[3]))
                self.conversion_edit.setText(str(i[4]))
################################################################################################################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui =  Ui_mainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
