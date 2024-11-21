import sys
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from database_description import MyWidget
from di import dia
import subprocess



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение на PyQt6")
        self.setGeometry(1000, 100, 500, 400)  # x, y, width, height
        self.setWindowTitle('plants')
        self.setWindowIcon(QIcon("pmg/plants_son.webp"))
        # Создаем виджет для переключения между окнами
        self.stacked_widget = QStackedWidget()
        # Создаем окна
        self.database_description = self.create_window1()
        # Добавляем окна в QStackedWidget
        self.stacked_widget.addWidget(self.database_description)
        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

    def create_window1(self):
        # Переключаемся
        subprocess.run(['python', 'database_description.py'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
