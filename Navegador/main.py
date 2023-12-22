from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class Browser():

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle('Navegador Browser.py')
        self.window.maximumSize()

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton('Go')
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton('<')
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton('>')
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        #clique no botão ir
        self.go_btn.clicked.connect(lambda: self.navigation(self.url_bar.toPlainText()))
        #clique no botão voltar
        self.back_btn.clicked.connect(self.browser.back)
        #clique no botão avançar
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        #URL padrão quando abre o navegador
        self.browser.setUrl(QUrl('http://google.com'))

        #Mostrando o layout
        self.window.setLayout(self.layout)
        self.window.show()

        #função para adicionar http no começo da URL
    def navigation(self, url):
        if not url.startswith('http'):
            url = 'http://'+ url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = Browser()
app.exec_()
