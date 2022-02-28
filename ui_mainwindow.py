# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 512)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 530, 91))
        self.lineEditCarrera = QLineEdit(self.groupBox)
        self.lineEditCarrera.setObjectName(u"lineEditCarrera")
        self.lineEditCarrera.setGeometry(QRect(410, 20, 100, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 50, 50, 20))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 20, 47, 20))
        self.lineEditCodigo = QLineEdit(self.groupBox)
        self.lineEditCodigo.setObjectName(u"lineEditCodigo")
        self.lineEditCodigo.setGeometry(QRect(240, 20, 100, 20))
        self.lineEditApellido = QLineEdit(self.groupBox)
        self.lineEditApellido.setObjectName(u"lineEditApellido")
        self.lineEditApellido.setGeometry(QRect(70, 50, 100, 20))
        self.lineEditTelefono = QLineEdit(self.groupBox)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")
        self.lineEditTelefono.setGeometry(QRect(240, 50, 100, 20))
        self.lineEditNombre = QLineEdit(self.groupBox)
        self.lineEditNombre.setObjectName(u"lineEditNombre")
        self.lineEditNombre.setGeometry(QRect(70, 20, 100, 20))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 20, 40, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 47, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 47, 20))
        self.pushButtonAgregar = QPushButton(self.groupBox)
        self.pushButtonAgregar.setObjectName(u"pushButtonAgregar")
        self.pushButtonAgregar.setGeometry(QRect(420, 50, 75, 23))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(180, 110, 181, 111))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 47, 20))
        self.lineEditCodigoEliminar = QLineEdit(self.groupBox_2)
        self.lineEditCodigoEliminar.setObjectName(u"lineEditCodigoEliminar")
        self.lineEditCodigoEliminar.setGeometry(QRect(60, 30, 100, 20))
        self.pushButtonEliminar = QPushButton(self.groupBox_2)
        self.pushButtonEliminar.setObjectName(u"pushButtonEliminar")
        self.pushButtonEliminar.setGeometry(QRect(50, 70, 75, 23))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 230, 530, 260))
        self.tableWidgetContactos = QTableWidget(self.groupBox_3)
        self.tableWidgetContactos.setObjectName(u"tableWidgetContactos")
        self.tableWidgetContactos.setGeometry(QRect(10, 20, 510, 230))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"A\u00f1adir contacto", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Carrera:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.pushButtonAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Eliminar contacto", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.pushButtonEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Contactos", None))
    # retranslateUi

