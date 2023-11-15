from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from pandas import DataFrame


class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self._data: DataFrame = None

    def set_data(self, data):
        self._data = data
        self.setColumnCount(self._data.columns.size)
        self.setHorizontalHeaderLabels(self._data.columns.values)
        self._update_table()

    def _update_table(self):
        for row_index, row_data in self._data.iterrows():
            self.insertRow(row_index)
            for column_num, (column_name, value) in enumerate(row_data.items()):
                self.setItem(
                    int(row_index),
                    int(column_num),
                    QTableWidgetItem(str(value))
                )

