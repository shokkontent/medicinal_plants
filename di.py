import io
import sys
import sqlite3

# Импортируем uic
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QPixmap

import subprocess

class dia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('db/lk.db')
        self.setWindowTitle('Description')
        self.setGeometry(1000, 100, 350, 400)
        self.setWindowTitle('Description')

        # Меняем фон
        self.setStyleSheet("""
                               QMainWindow { background-image:url(pmg/kosmos.jfif); 
                               background-repeat: no-repeat; background-position: center; }""")


        with open('txt/peredacha.txt', 'rt', encoding="utf-8") as f:
            read_data = f.read()

        # Создание курсора
        self.cur = self.con.cursor()
        # Загружаем дизайн
        uic.loadUi("QT/description.ui", self)

        self.pushButton.clicked.connect(self.my_exit)


        self.con = sqlite3.connect('db/lk.db')

        # Меняет изображение кнопки
        self.pushButton.setStyleSheet("border-image : url(pmg/plants_son.webp);")
        size_button = int((min(self.width(), self.height()) // 10) / 1.54)
        self.pushButton.setFixedSize(size_button + 25, size_button)

        # Создание курсора
        self.cur = self.con.cursor()
        solution_lk = (f'SELECT pfoto_lk FROM pfoto WHERE id = {int(read_data)}')
        res_lk = self.cur.execute(solution_lk).fetchall()
        a = ''
        name_plants = res_lk[0]
        for i in name_plants:
            a += i
        pfoto = QPixmap(a)
        pfoto = pfoto.scaledToWidth(200)
        self.photo.setPixmap(pfoto)
        # self.photo.resizeEvent(True)
        solution = (f'SELECT * FROM description WHERE id = {int(read_data)}')
        res = self.cur.execute(solution).fetchall()
        self.Description.setWordWrap(True)
        self.treatment.setWordWrap(True)
        for i in res:
            self.Description.setText(i[2])
            self.name.setText(i[1])
            self.treatment.setText(i[3])
        # меняем цвет текста
        self.treatment.setStyleSheet("QLabel { color : white; }")
        self.label.setStyleSheet("QLabel { color : white; }")
        self.Description.setStyleSheet("QLabel { color : white; }")
        self.Description_name.setStyleSheet("QLabel { color : white; }")
        self.name.setStyleSheet("QLabel { color : white; }")



    def my_exit(self):
        sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dia()
    ex.show()
    sys.exit(app.exec())
