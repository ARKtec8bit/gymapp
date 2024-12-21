from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QGroupBox, QSizePolicy

from src.data_storage import load_data, get_random_exercise


class WorkoutGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.exercises = load_data('data/exercise_list.json')

        self.generate_button = QPushButton("Generate Workout")
        self.generate_button.setStyleSheet(
            """
            QPushButton {
            background-color: #44475a;
            color: #50fa7b;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: #6272a4;
            font: bold 14px;
            min-width: 138px;
            padding: 6px;
            }
            QPushButton:pressed {
            background-color: #50fa7b;
            color: #44475a;
            border-style: inset;
            }
            """
        )
        self.generate_button.clicked.connect(self.generate_workout)
        self.layout.addWidget(self.generate_button)

        self.workout_display = QGridLayout()
        self.layout.addLayout(self.workout_display)

        self.setLayout(self.layout)

    def generate_workout(self):
        workout = get_random_exercise(self.exercises)
        # Clear previous workout
        while self.workout_display.count():
            child = self.workout_display.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Display new workout
        row = 0
        col = 0
        for category, groups in workout.items():
            group_box = QGroupBox(category)
            group_box.setStyleSheet("QGroupBox { font-weight: bold; }")
            group_layout = QVBoxLayout()

            if isinstance(groups, dict):
                for group, exercise in groups.items():
                    label = QLabel(f"{group}: {exercise}")
                    group_layout.addWidget(label)
            else:
                label = QLabel(groups)
                group_layout.addWidget(label)

            group_box.setLayout(group_layout)
            group_box.setSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.workout_display.addWidget(group_box, row, col)

            col += 1
            if col > 1:  # Adjust the number of columns as needed
                col = 0
                row += 1
