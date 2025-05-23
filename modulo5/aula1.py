b import sys
from PySide6.QtWidgets import QApplication, QPushButton
app = QApplication(sys.argv)
botao = QPushButton('texto Botão')
botao.setStyleSheet('font-size: 40px; color:red;')
botao.show()
app.exec()
