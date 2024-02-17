import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicializamos la conexión Bluetooth
        self.bluetooth = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        # Configuramos la ventana principal
        self.setWindowTitle("Conexión Bluetooth")
        self.setGeometry(100, 100, 280, 170)

        # Creamos los widgets
        self.label_estado = QLabel("Estado:", self)
        self.label_estado.move(10, 10)

        self.label_dispositivos = QLabel("Dispositivos:", self)
        self.label_dispositivos.move(10, 40)

        self.combo_dispositivos = QComboBox(self)
        self.combo_dispositivos.move(10, 60)

        self.boton_conectar = QPushButton("Conectar", self)
        self.boton_conectar.move(10, 100)
        self.boton_conectar.clicked.connect(self.conectar)

        self.boton_desconectar = QPushButton("Desconectar", self)
        self.boton_desconectar.move(130, 100)
        self.boton_desconectar.clicked.connect(self.desconectar)

        # Actualizamos el estado de la conexión
        self.actualizar_estado()

        # Obtenemos la lista de dispositivos Bluetooth
        self.dispositivos_emparejados = bluetooth.discover_devices()

        # Poblamos el combo de dispositivos
        for dispositivo in self.dispositivos_emparejados:
            self.combo_dispositivos.addItem(dispositivo[1])

    def conectar(self):
        # Obtenemos la dirección MAC del dispositivo seleccionado
        direccion_mac = self.combo_dispositivos.currentText()

        # Intentamos conectar al dispositivo
        try:
            self.bluetooth.connect((direccion_mac, 1))
            self.actualizar_estado("Conectado")
        except Exception as e:
            print(f"Error al conectar: {e}")

    def desconectar(self):
        # Cerramos la conexión Bluetooth
        self.bluetooth.close()
        self.actualizar_estado("Desconectado")

    def actualizar_estado(self, estado="Desconectado"):
        # Actualizamos el estado de la conexión
        self.label_estado.setText(f"Estado: {estado}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
