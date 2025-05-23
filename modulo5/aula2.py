import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout,QWidget, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central = QWidget()
window.setCentralWidget(central)
window.setWindowTitle('Minha janela bonitinha')

botao = QPushButton('Botão 1')
botao.setStyleSheet('font-size: 40px; color:red;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px; color:blue;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px; color:brow;')


layou = QVBoxLayout()
central.setLayout(layou)
layou.addWidget(botao,)
layou.addWidget(botao2,)
layou.addWidget(botao3, )
def slot_exemple():
    print(123)

#status bar
status_bar = window.statusBar()
status_bar.showMessage("Ola calvo")
status_bar.connect
# Menu bar
Menu = window.menuBar()
Primeiro_menu = Menu.addMenu("Primeiro menu")
Primeira_acao = Primeiro_menu.addAction("Primeira ação")
Primeira_acao.triggered.connect(slot_exemple)



central.show()
window.show()

app.exec()
