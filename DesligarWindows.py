from tkinter import messagebox
from PyQt5 import uic, QtWidgets, QtGui
import os

def desligar():
    try:
        tempo = int(tela_desligar.tempo.text())
        convert = tempo * 60
        cmd = "shutdown -s -t %s"
        comando = (cmd % convert)
        os.system(comando)
    except ValueError:
        messagebox.showerror(title = "Erro", message = "Insira apenas números inteiros")
        tempo = tela_desligar.tempo.setText("")
def cancelar():
    os.system("shutdown -a")

def sair():
    app.exit()





app = QtWidgets.QApplication([])

# Carregando tela
tela_desligar = uic.loadUi("tela_desligar.ui")


# Executando as funções de clicker
tela_desligar.desligar.clicked.connect(desligar)
tela_desligar.cancelar.clicked.connect(cancelar)
tela_desligar.sair.clicked.connect(sair)


tela_desligar.setWindowIcon(QtGui.QIcon('logo.png'))
tela_desligar.show()
app.exec()
