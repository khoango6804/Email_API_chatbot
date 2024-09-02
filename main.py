import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic
import getRespone as GS

# Đường dẫn tới tệp lưu lịch sử cuộc trò chuyện
HISTORY_FILE_PATH = "chat_history.json"


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"D:\API\Viết mail\form.ui", self)
        self.setWindowTitle('9.5 Hỗ Trợ Viết Mail')

        # Kết nối các widget với các hàm tương ứng
        self.BG.clicked.connect(self.BG_function)
        self.TT.clicked.connect(self.TT_function)
        self.E2V.clicked.connect(self.Eng2Vie_function)
        self.V2E.clicked.connect(self.Vie2Eng_function)
        self.clear.clicked.connect(self.clear_content)  # Thêm kết nối cho nút "Xóa"

        self.history = []  # Khởi tạo thuộc tính cho lịch sử cuộc trò chuyện
        self.load_history()  # Tải lịch sử cuộc trò chuyện khi khởi động ứng dụng

    def load_history(self):
        """Tải lịch sử từ file khi khởi động ứng dụng."""
        if os.path.exists(HISTORY_FILE_PATH):
            with open(HISTORY_FILE_PATH, "r", encoding="utf-8") as history_file:
                self.history = json.load(history_file)
                for entry in self.history:
                    self.output.append(f"User: {entry['user']}")
                    self.output.append(f"Bot: {entry['bot']}\n")
        else:
            self.output.setPlainText("")  # Làm trống bộ text

    def save_history(self):
        """Lưu lịch sử vào file."""
        with open(HISTORY_FILE_PATH, "w", encoding="utf-8") as history_file:
            json.dump(self.history, history_file, ensure_ascii=False, indent=4)

    def handle_chat(self, inputText, mode):
        try:
            res = GS.getRes(inputText, mode)
            self.output.append(f"User: {inputText}")
            self.output.append(f"Bot: {res}\n")
            self.history.append({"user": inputText, "bot": res})
            self.save_history()  # Lưu lại sau mỗi lần chat mới
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def clear_content(self):
        """Xóa nội dung trong cả input và output."""
        self.input.clear()
        self.output.clear()

    def BG_function(self):
        inputText = self.input.toPlainText()
        self.handle_chat(inputText, "begin")

    def TT_function(self):
        inputText = self.input.toPlainText()
        self.handle_chat(inputText, "tomtat")

    def Eng2Vie_function(self):
        inputText = self.input.toPlainText()
        self.handle_chat(inputText, "E2V")

    def Vie2Eng_function(self):
        inputText = self.input.toPlainText()
        self.handle_chat(inputText, "V2E")


app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()
