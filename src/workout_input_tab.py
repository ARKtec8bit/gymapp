from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton, QScrollArea, QComboBox, \
    QGridLayout

from src.data_storage import load_data


class WorkoutInputTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Load workout data
        self.workouts = load_data('data/workouts.json')

        # Create dropdown menus
        self.workout_name_combo = QComboBox()
        self.week_combo = QComboBox()
        self.day_combo = QComboBox()

        # Populate workout names
        self.workout_name_combo.addItems(self.workouts.keys())
        self.workout_name_combo.currentTextChanged.connect(self.update_weeks)

        # Connect signals
        self.week_combo.currentTextChanged.connect(self.update_days)
        self.day_combo.currentTextChanged.connect(self.display_workout_details)

        # Create form layout for the dropdown menus
        form_layout = QFormLayout()
        form_layout.addRow("Select Workout Name:", self.workout_name_combo)
        form_layout.addRow("Select Week:", self.week_combo)
        form_layout.addRow("Select Day:", self.day_combo)

        self.layout.addLayout(form_layout)

        # Create a scroll area for the workout details
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()

        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

        self.layout.addWidget(self.scroll_area)

        # Save button
        self.save_button = QPushButton("Save Workout Details")
        self.save_button.clicked.connect(self.save_workout_details)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

        self.update_weeks()

    def update_weeks(self):
        self.week_combo.clear()
        workout_name = self.workout_name_combo.currentText()
        if workout_name:
            self.week_combo.addItems(self.workouts[workout_name].keys())
            self.update_days()

    def update_days(self):
        self.day_combo.clear()
        workout_name = self.workout_name_combo.currentText()
        week = self.week_combo.currentText()
        if workout_name and week:
            self.day_combo.addItems(self.workouts[workout_name][week].keys())
            self.display_workout_details()

    def display_workout_details(self):
        self.clear_workout_details()
        workout_name = self.workout_name_combo.currentText()
        week = self.week_combo.currentText()
        day = self.day_combo.currentText()
        if workout_name and week and day:
            workout = self.workouts[workout_name][week][day]

            if "Weights" in workout:
                self.add_weights_section(workout["Weights"])
            if "Conditioning" in workout:
                self.add_workout_section("Conditioning", workout["Conditioning"], [
                    "exercise", "duration", "reps"])
            if "Cardio" in workout:
                self.add_cardio_section(workout["Cardio"])
            if "Technical" in workout:
                self.add_technical_section(workout["Technical"])

    def clear_workout_details(self):
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def add_weights_section(self, exercises):
        section_label = QLabel("Weights:")
        self.scroll_layout.addWidget(section_label)

        for exercise in exercises:
            grid_layout = QGridLayout()

            exercise_label = QLabel(exercise["exercise"])
            grid_layout.addWidget(exercise_label, 0, 0, 1, 5)

            for set_num in range(exercise["sets"]):
                reps_input = QLineEdit()
                reps_input.setFixedWidth(80)  # Set width to fit 8 characters
                reps_input.setObjectName(
                    f"reps_input_{exercise['exercise']}_{set_num + 1}")

                weight_input = QLineEdit()
                weight_input.setFixedWidth(80)  # Set width to fit 8 characters
                weight_input.setObjectName(
                    f"weight_input_{exercise['exercise']}_{set_num + 1}")

                grid_layout.addWidget(
                    QLabel(f"Set {set_num + 1} Reps:"), set_num + 1, 1)
                grid_layout.addWidget(reps_input, set_num + 1, 2)
                grid_layout.addWidget(QLabel("Weight:"), set_num + 1, 3)
                grid_layout.addWidget(weight_input, set_num + 1, 4)

            self.scroll_layout.addLayout(grid_layout)

    def add_workout_section(self, section_name, exercises, fields=["exercise", "sets", "reps", "weight"]):
        section_label = QLabel(f"{section_name}:")
        self.scroll_layout.addWidget(section_label)
        for exercise in exercises:
            form_layout = QFormLayout()
            for field in fields:
                input_field = QLineEdit(str(exercise.get(field, "")))
                input_field.setObjectName(
                    f"{field}_input_{exercise.get('exercise', '')}")
                form_layout.addRow(f"{field.capitalize()}:", input_field)
            self.scroll_layout.addLayout(form_layout)

    def add_cardio_section(self, cardio):
        section_label = QLabel("Cardio:")
        self.scroll_layout.addWidget(section_label)
        form_layout = QFormLayout()
        for field in ["exercise", "distance", "duration", "hr_avg", "hr_max"]:
            input_field = QLineEdit(str(cardio.get(field, "")))
            input_field.setObjectName(f"{field}_input")
            form_layout.addRow(f"{field.capitalize()}:", input_field)
        self.scroll_layout.addLayout(form_layout)

    def add_technical_section(self, technical):
        section_label = QLabel("Technical:")
        self.scroll_layout.addWidget(section_label)
        form_layout = QFormLayout()
        for field in ["Kata", "Kihon", "Renraku", "Other"]:
            input_field = QLineEdit(technical.get(field, ""))
            input_field.setObjectName(f"{field}_input")
            form_layout.addRow(f"{field}:", input_field)
        self.scroll_layout.addLayout(form_layout)

    def save_workout_details(self):
        # Implement save functionality to store workout details
        pass
