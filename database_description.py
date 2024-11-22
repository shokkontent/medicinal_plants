import io
import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QStackedWidget
from PyQt6.QtGui import QIcon
from di import dia
import subprocess

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем дизайн
        uic.loadUi("QT/main_window.ui", self)
        # Меняем иконку
        self.setWindowIcon(QIcon("pmg/plants_son.webp"))
        # Меняем фон
        self.setStyleSheet("""
                       QMainWindow { background-image:url(pmg/kosmos.jfif); 
                       background-repeat: no-repeat; background-position: center; }""")
        # потключаемся в бд
        self.con = sqlite3.connect('db/lk.db')

        # Создание курсора
        self.cur = self.con.cursor()
        # меняем цвет текста
        self.label_2.setStyleSheet("QLabel { color : white; }")
        self.label.setStyleSheet("QLabel { color : white; }")
        # отмечаем какой выбор у tableWidget
        with open('txt/peredacha.txt', 'rt', encoding="utf-8") as f:
            read_data = f.read()
            self.label_2.setText(str(int(read_data) + 1))

        # Меняет изображение кнопку описания
        self.pushButton.setStyleSheet("border-image : url(pmg/plants_son.webp);")
        size_button = int((min(self.width(), self.height()) // 10) / 1.54)
        self.pushButton.setFixedSize(size_button + 25, size_button)

        # Меняет изображение кнопку настроек
        self.pushButton_2.setStyleSheet("border-image : url(pmg/plants2.jpg);")
        size_button = int((min(self.width(), self.height()) // 10) / 1.54)
        self.pushButton_2.setFixedSize(size_button + 25, size_button)

        # Меняет изображение кнопку удаления
        self.pushButton_3.setStyleSheet("border-image : url(pmg/plants2.jpg);")
        size_button = int((min(self.width(), self.height()) // 10) / 1.54)
        self.pushButton_3.setFixedSize(size_button + 25, size_button)
        # заполняет tableWidget
        solution = (f'SELECT name FROM description')
        res = self.cur.execute(solution).fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        for row, films in enumerate(res):
            for line, name in enumerate(films):
                self.tableWidget.setItem(row, line, QTableWidgetItem(str(name)))
        number = row
        # конектим tableWidget
        self.tableWidget.cellClicked.connect(self.perenos)

        # конектим pushButton
        self.pushButton.clicked.connect(self.perexod)
        # конектим pushButton_2
        self.pushButton_2.clicked.connect(self.dialog_box)
        # конектим pushButton_3
        self.pushButton_3.clicked.connect(self.delet)

    def perenos(self, row):
        self.label_2.setText(str(row + 1))
        with open('txt/peredacha.txt', 'w', encoding="utf-8") as f:
            f.write(str(row + 1))

    def delet(self, row):
        self.con = sqlite3.connect('db/lk.db')

        self.cur = self.con.cursor()
        sol = (f'DELETE FROM Description WHERE id = {row}')
        self.cur.execute(sol)
        self.con.commit()


    def dialog_box(self):
        subprocess.run(['python', 'dialog_box.py'])

    def perexod(self):
        ex.hide()
        subprocess.run(['python', 'di.py'])
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
