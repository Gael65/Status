from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from agenda import Entrada, Agenda
import pickle, time, threading
 
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #crear objeto agenda
        self.__agenda = Agenda()

        #recuperar informacion de las inputs
        try:
            #abrir archivo de informacion de respaldo si existe
            with open("input_data", "rb") as entrada:
                contacto = pickle.load(entrada)
            entrada.close()

            #cargar datos
            self.ui.lineEditNombre.setText(contacto.getNombre())
            self.ui.lineEditApellido.setText(contacto.getApellido())
            self.ui.lineEditCodigo.setText(contacto.getCodigo())
            self.ui.lineEditTelefono.setText(contacto.getTelefono())
            self.ui.lineEditCarrera.setText(contacto.getCarrera())
        except:
            pass

        #eventos
        self.ui.pushButtonAgregar.clicked.connect(self.capturarContacto)
        self.ui.pushButtonEliminar.clicked.connect(self.eliminarContacto)

        #inicializar la tabla
        tableHeaders = ["Nombre", "Apellido", "Codigo", "Telefono", "Carrera"]
        self.ui.tableWidgetContactos.setColumnCount(5)
        self.ui.tableWidgetContactos.setHorizontalHeaderLabels(tableHeaders)
        self.ui.tableWidgetContactos.verticalHeader().hide()

        #mostrar tabla al inicializar la interfaz
        self.mostrarContactos()

        #comenzar el respaldo
        threading.Thread(target=self.respaldarInformacion, daemon=True).start()
    
    #respaldar informacion periodicamente
    def respaldarInformacion(self):
        while True:
            nombre = self.ui.lineEditNombre.text()
            apellido = self.ui.lineEditApellido.text()
            codigo = self.ui.lineEditCodigo.text()
            telefono = self.ui.lineEditTelefono.text()
            carrera = self.ui.lineEditCarrera.text()

            contacto = Entrada(nombre, apellido, codigo, telefono, carrera)

            with open("input_data", "wb") as entrada:
                pickle.dump(contacto, entrada)
            entrada.close()

            time.sleep(2.5)

    #mostrar tabla cada vez que se modifica la agenda
    def mostrarContactos(self):
        self.ui.tableWidgetContactos.setRowCount(len(self.__agenda.getContactos()))
        row = 0
        
        for contacto in self.__agenda.getContactos():
            nombre = QTableWidgetItem(contacto.getNombre())
            apellido = QTableWidgetItem(contacto.getApellido())
            codigo = QTableWidgetItem(contacto.getCodigo())
            telefono = QTableWidgetItem(contacto.getTelefono())
            carrera = QTableWidgetItem(contacto.getCarrera())

            self.ui.tableWidgetContactos.setItem(row, 0, nombre)
            self.ui.tableWidgetContactos.setItem(row, 1, apellido)
            self.ui.tableWidgetContactos.setItem(row, 2, codigo)
            self.ui.tableWidgetContactos.setItem(row, 3, telefono)
            self.ui.tableWidgetContactos.setItem(row, 4, carrera)

            row += 1

    @Slot()
    def capturarContacto(self):
        if self.ui.lineEditNombre.text() == "" or self.ui.lineEditApellido.text() == "" or self.ui.lineEditCodigo.text() == ""or self.ui.lineEditTelefono.text() == "" or self.ui.lineEditCarrera.text() == "":
            QMessageBox.critical(
                self,
                "Error",
                "Campos incompletos"
            )
        else:
            nombre = self.ui.lineEditNombre.text()
            apellido = self.ui.lineEditApellido.text()
            codigo = self.ui.lineEditCodigo.text()
            telefono = self.ui.lineEditTelefono.text()
            carrera = self.ui.lineEditCarrera.text()

            self.__agenda.agregarEntrada(nombre, apellido, codigo, telefono, carrera)
            self.mostrarContactos()

    @Slot()
    def eliminarContacto(self):
        if self.ui.lineEditCodigoEliminar.text() == "":
            QMessageBox.critical(
                self,
                "Error",
                "Campos incompletos"
            )
        else:
            codigo = self.ui.lineEditCodigoEliminar.text()

            if self.__agenda.eliminarEntrada(codigo):
                self.mostrarContactos()
            else:
                QMessageBox.critical(
                self,
                "Error",
                "El codigo no existe"
            )
    