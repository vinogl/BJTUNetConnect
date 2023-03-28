from message_window import Ui_MessageWindow
from connect import connect, message_path
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import os


class Message(QMainWindow, Ui_MessageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.save_btn.clicked.connect(self.save_message)
        self.clear_btn.clicked.connect(self.clear_message)
        self.connect_btn.clicked.connect(self.connect)

        # 若存在保存的登录信息，自动填充到ui
        if os.path.exists(message_path):
            with open(message_path, 'r') as f_r:
                lines = f_r.readlines()
                self.user.setText(lines[0].strip())
                self.password.setText(lines[1].strip())

    def connect(self):
        """connect方法发送post请求连接校园网"""
        user = self.user.text()
        password = self.password.text()
        connect_info = connect(user=user, password=password)
        if connect_info == '认证成功页':
            QMessageBox.about(self, 'info', '%s\n\n连接成功！' % connect_info)
        else:
            QMessageBox.about(self, 'info', '%s\n\n连接失败！' % connect_info)

    def save_message(self):
        """将ui的信息保存至指定文件(message_path)"""
        user = str(self.user.text())
        password = str(self.password.text())
        with open(message_path, 'w') as f_w:
            f_w.write(user + '\n' + password)

    def clear_message(self):
        """清空ui的内容"""
        if os.path.exists(message_path):
            os.remove(message_path)
        self.user.clear()
        self.password.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Message()
    window.show()
    sys.exit(app.exec_())
