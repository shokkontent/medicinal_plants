import io
import sys
import sqlite3

# Импортируем uic
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QPixmap

import subprocess


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>585</width>
    <height>303</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="photo">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>30</y>
     <width>141</width>
     <height>181</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="name">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>210</y>
     <width>81</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="Description_name">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>20</y>
     <width>91</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Описание</string>
   </property>
  </widget>
  <widget class="QLabel" name="Description">
   <property name="geometry">
    <rect>
     <x>246</x>
     <y>42</y>
     <width>261</width>
     <height>181</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>250</y>
     <width>81</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>От чего лечит:</string>
   </property>
  </widget>
  <widget class="QLabel" name="treatment">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>245</y>
     <width>311</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_exex">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>10</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Назад</string>
   </property>
   <property name="icon">
    <iconset>
     <normaloff>../../Downloads/ikonka.png</normaloff>../../Downloads/ikonka.png</iconset>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''


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
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.pushButton_exex.clicked.connect(self.my_exit)


        self.con = sqlite3.connect('db/lk.db')

        # Меняет изображение кнопки
        self.pushButton_exex.setStyleSheet("border-image : url(pmg/plants_son.webp);")
        size_button = int((min(self.width(), self.height()) // 10) / 1.54)
        self.pushButton_exex.setFixedSize(size_button + 25, size_button)

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
