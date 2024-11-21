import io
import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QStackedWidget
from PyQt6.QtGui import QIcon
from di import dia
import subprocess

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>457</width>
    <height>429</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QTableWidget" name="tableWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>101</width>
     <height>431</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>400</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Выбран:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>400</y>
     <width>211</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>190</y>
     <width>76</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Настройки</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>140</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Описание</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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

        solution = (f'SELECT name FROM description')
        res = self.cur.execute(solution).fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        for row, films in enumerate(res):
            for line, name in enumerate(films):
                self.tableWidget.setItem(row, line, QTableWidgetItem(str(name)))
        # конектим tableWidget
        self.tableWidget.cellClicked.connect(self.perenos)
        # конектим pushButton
        self.pushButton.clicked.connect(self.perexod)
        # конектим pushButton_2
        self.pushButton_2.clicked.connect(self.dialog_box)

    def perenos(self, row):
        self.label_2.setText(str(row + 1))
        with open('txt/peredacha.txt', 'w', encoding="utf-8") as f:
            f.write(str(row + 1))

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