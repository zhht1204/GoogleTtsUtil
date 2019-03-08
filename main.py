import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from dialog import *
from google_ttf import save_voice_file

class MyDialog(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        # button event
        self.commitChangeButton.clicked.connect(self.change)

    def change(self):
    	_voiceText = self.voiceTextLine.text()
    	save_voice_file(_voiceText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myDlg = MyDialog()
    myDlg.show()
    sys.exit(app.exec_())
