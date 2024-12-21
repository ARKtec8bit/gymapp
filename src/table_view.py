from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem
from src.data_storage import get_usernames, get_data


class TableView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.user_selector_layout = QHBoxLayout()
        self.user_label = QLabel("Select User:")
        self.user_combo = QComboBox()
        self.user_combo.addItems(get_usernames())
        self.user_combo.currentTextChanged.connect(self.update_table)

        self.user_selector_layout.addWidget(self.user_label)
        self.user_selector_layout.addWidget(self.user_combo)
        self.layout.addLayout(self.user_selector_layout)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)
        self.update_table()

    def update_table(self):
        selected_user = self.user_combo.currentText()
        data = get_data()
        user_data = [entry for entry in data if entry[2] == selected_user]

        self.table.setRowCount(len(user_data))
        self.table.setColumnCount(len(user_data[0]) - 1)
        self.table.setHorizontalHeaderLabels([
            "Date", "User", "Weight", "Height", "Chest", "Hips", "Waist", "Shoulder", "Left Bicep", "Right Bicep", "Left Forearm", "Right Forearm", "Left Leg", "Right Leg", "Left Calf", "Right Calf"
        ])

        for row_index, row_data in enumerate(user_data):
            for col_index, col_data in enumerate(row_data[1:]):
                self.table.setItem(row_index, col_index,
                                   QTableWidgetItem(str(col_data)))
