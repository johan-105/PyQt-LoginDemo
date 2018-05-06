# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './loginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        self.login_dialog = login_dialog
        self.login_dialog.setObjectName("login_dialog")
        self.login_dialog.resize(300, 213)
        self.login_dialog.setFixedSize(login_dialog.size())

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_dialog.sizePolicy().hasHeightForWidth())
        self.login_dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.login_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.user_line_edit = QtWidgets.QLineEdit(self.login_dialog)
        self.user_line_edit.setObjectName("user_line_edit")
        self.verticalLayout.addWidget(self.user_line_edit)
        self.pw_line_edit = QtWidgets.QLineEdit(self.login_dialog)
        self.pw_line_edit.setObjectName("pw_line_edit")
        self.verticalLayout.addWidget(self.pw_line_edit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.login_button = QtWidgets.QPushButton(self.login_dialog)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.forget_button = QtWidgets.QPushButton(self.login_dialog)
        self.forget_button.setObjectName("forget_button")
        self.horizontalLayout.addWidget(self.forget_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(self.login_dialog)
        QtCore.QMetaObject.connectSlotsByName(self.login_dialog)

        self.login_button.clicked.connect(self.login)

        self.forget_button.clicked.connect(self.forget_password)

    def login(self):
        if self.user_line_edit.text() == 'admin' and self.pw_line_edit.text() == '666':
            self.login_dialog.accept()
        else:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'invalid login', parent=self.login_dialog)
            msg_box.exec_()

    def forget_password(self):
        content = 'Please contact the administrator: fuck@shit.edu.cn'
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Forget Password', content, parent=self.login_dialog)
        msg_box.exec_()

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "Login"))
        self.user_line_edit.setPlaceholderText(_translate("login_dialog", "Username"))
        self.pw_line_edit.setPlaceholderText(_translate("login_dialog", "Password"))
        self.login_button.setText(_translate("login_dialog", "Login"))
        self.forget_button.setText(_translate("login_dialog", "Forget Password"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    sys.exit(app.exec_())
