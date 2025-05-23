import sys

from PySide6.QtWidgets import QApplication,QPushButton,QWidget,QGridLayout

app = QApplication(sys.argv)

botao1 = QPushButton("Texto do Botão")
botao1.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Texto do Botão 2")
botao2.setStyleSheet("font-size: 40px;")

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1,1,1,1,1)
layout.addWidget(botao2,1,2,1,1)


central_widget.show()
app.exec()