import sys

from PySide6.QtWidgets import QApplication,QPushButton,QWidget,QGridLayout,QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()

botao1 = QPushButton("Texto do Botão")
botao1.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Texto do Botão 2")
botao2.setStyleSheet("font-size: 40px;")

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

layout.addWidget(botao1,1,1,1,1)
layout.addWidget(botao2,1,2,1,1)

#statusbar
status_bar = window.statusBar()
status_bar.showMessage("Texto da Status Bar")

#menu bar
menu = window.menuBar()
menu.addMenu("qualquer coisa")

primeiro_menu = menu.addMenu("primeiro menu")
primeiro_menu.addAction("primeira ação")


primeira_acao = primeiro_menu.addAction("primeira ação")
primeira_acao.triggered.connect(lambda: print("Ação 1 do menu 1 foi acionada"))

segunda_acao = primeiro_menu.addAction("segunda ação")
segunda_acao.setCheckable(True)
# segunda_acao.triggered.connect()


window.show()
app.exec()