import sys

from PySide6.QtWidgets import QApplication,QPushButton

app = QApplication(sys.argv)

botao1 = QPushButton("Texto do Botão")
botao1.show()

botao2 = QPushButton("Texto do Botão 2")
botao2.show()

app.exec()
