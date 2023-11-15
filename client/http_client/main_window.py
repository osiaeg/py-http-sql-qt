from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QFrame, QTableWidget, QTableWidgetItem
import pandas as pd

from .table_widget import TableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window")

        data = pd.DataFrame([
            [None, 'Гончаров Егор Михайлович', 2000, 5, 'O4250'],
            [1, 9, 2, 3, 5],
            [1, 9, 2, 3, 5],
            [1, 9, 2, 3, 5],
            [1, 9, 2, 3, 5],
            [1, 9, 2, 3, 5],
        ], columns=['Фото', 'ФИО', 'Год', 'Номер курса', 'Нормер группы'])

        self.frame = QFrame()

        self.table = TableWidget(self)
        self.table.set_data(data)

        self.add_btn = QPushButton("Add new student")
        self.delete_btn = QPushButton("Delete selected student")
        self.delete_btn.clicked.connect(self.delete)

        frame_layout = QVBoxLayout()

        frame_layout.addWidget(self.table)
        frame_layout.addWidget(self.add_btn)
        frame_layout.addWidget(self.delete_btn)

        self.frame.setLayout(frame_layout)

        self.setCentralWidget(self.frame)

    def delete(self):
        print(self.table.currentRow())

