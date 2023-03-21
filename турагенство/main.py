import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        print("Successfully logget in with email:", email, "and password:", password)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow=Login()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(480)
    widget.setFixedHeight(620)
    widget.show()
    sys.exit(app.exec_())



