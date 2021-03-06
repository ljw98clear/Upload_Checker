import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton

driverpath = './chromedriver'
sleeptime = 0.2

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'https://manatoki92.net/comic/122227?stx=%EC%9B%90%ED%94%BC%EC%8A%A4'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
                
        site = QComboBox(self)
        site.addItem("마나토끼")
        site.addItem("Pear")
        site.addItem("Lemon")

        site.move(40, 50)

        title = QComboBox(self)
        title.addItem("원피스")
        title.addItem("진격의거인")
        title.addItem("Lemon")

        title.move(180, 50)

        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)

        #site.activated[str].connect(self.onChanged)      

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())