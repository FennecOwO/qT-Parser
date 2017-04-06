import sys
import os
from PyQt5 import QtWidgets

rootDir = os.path.dirname(__file__)

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,40,1366,786)
        self.setWindowTitle("spadl")

        openLog = QtWidgets.QAction("&Open log", self)
        openLog.setShortcut("ctrl+O")
        openLog.triggered.connect(self.open_log)

        quitAction = QtWidgets.QAction("&Quit", self)
        quitAction.setShortcut("ctrl+Q")
        quitAction.triggered.connect(self.close_application)

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openLog)
        fileMenu.addAction(quitAction)

        self.show()

    def open_log(self):
        logName = QtWidgets.QFileDialog.getOpenFileName(self, "Open", rootDir + '\\logs')
        print(logName)
        log = open(logName[0], 'r', encoding='Latin-1')
    
        self.browser()
        
        with log:
            self.textBrowser.setText(log.read())
        
        log.close

    def browser(self):
        self.textBrowser = QtWidgets.QTextBrowser()
        self.setCentralWidget(self.textBrowser)
    
    def close_application(self):
        sys.exit()

def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())

run()
