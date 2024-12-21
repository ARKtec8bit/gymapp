from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from src.workout_generator import WorkoutGenerator
from src.dracula_theme import apply_dracula_theme


class WorkoutGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Workout App")
        self.setGeometry(100, 100, 800, 600)
        apply_dracula_theme(self)
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()

        self.workout_generator = WorkoutGenerator()
        self.main_layout.addWidget(self.workout_generator)

        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
