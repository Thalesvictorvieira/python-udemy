import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout,QWidget, QMainWindow

app = QApplication(sys.argv)
windon = QMainWindow()
central = QWidget()
windon.setCentralWidget(central)
windon.setWindowTitle('Minha janela bonitinha')

botao = QPushButton('Botão 1')
botao.setStyleSheet('font-size: 40px; color:red;')

botão2 = QPushButton('Botão 2')
botão2.setStyleSheet('font-size: 40px; color:blue;')

botão3 = QPushButton('Botão 3')
botão3.setStyleSheet('font-size: 40px; color:brow;')


layou = QVBoxLayout()
central.setLayout(layou)
layou.addWidget(botao,)
layou.addWidget(botão2,)
layou.addWidget(botão3,)
def slot_exemple():
    print(123)

#status bar
status_bar = windon.statusBar()
status_bar.showMessage("Ola calvo")
status_bar.connect
# Menu bar
Menu = windon.menuBar()
Primeiro_menu = Menu.addMenu("Primeiro menu")
Primeira_acao = Primeiro_menu.addAction("Primeira ação")
Primeira_acao.triggered.connect(slot_exemple)



central.show()
windon.show()

app.exec()
