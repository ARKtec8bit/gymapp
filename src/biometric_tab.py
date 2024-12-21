from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QWidget
from src.data_storage import create_table
from src.biometric_input import BiometricInput
from src.data_visualization import DataVisualization
from src.table_view import TableView


class BiometricTab(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the database table if it doesn't exist
        create_table()

        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.addTab(BiometricInput(), "Biometric Input")
        self.tabs.addTab(DataVisualization(), "Data Visualization")
        self.tabs.addTab(TableView(), "Table View")

        self.main_layout.addWidget(self.tabs)
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
