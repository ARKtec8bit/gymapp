import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, QLabel, QComboBox, QScrollArea, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from src.data_storage import load_data
from src.dracula_theme import apply_dracula_theme
from src.workout_input_tab import WorkoutInputTab
from src.timer_tab import BoxingTimer
from src.random_full_body import WorkoutGeneratorApp
from src.biometric_tab import BiometricTab


class WorkoutApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loser Barbell Workout App")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("data/lbb.png"))
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()  # Use vertical layout

        # Create tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_workout_selection_tab(),
                         "Workout Selection")
        self.tabs.addTab(WorkoutInputTab(),
                         "Input Workout Details")
        self.tabs.addTab(BoxingTimer(),
                         "Boxing Timer")
        self.tabs.addTab(WorkoutGeneratorApp(),
                         "Random Full Body Workout")
        self.tabs.addTab(BiometricTab(), "Biometric Data")

        # Add tabs to the main layout
        self.main_layout.addWidget(self.tabs)
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        apply_dracula_theme(self)

    def create_workout_selection_tab(self):
        # Create the workout selection tab
        workout_selection_tab = QWidget()
        layout = QVBoxLayout()

        # Load workout data
        self.workouts = load_data('data/workouts.json')

        # Create a vertical layout for the controls on the left
        control_layout = QVBoxLayout()

        # Create dropdown menus
        self.workout_name_combo = QComboBox()
        self.week_combo = QComboBox()
        self.day_combo = QComboBox()

        # Populate workout names
        self.workout_name_combo.addItems(self.workouts.keys())
        self.workout_name_combo.currentTextChanged.connect(self.update_weeks)

        # Connect signals
        self.week_combo.currentTextChanged.connect(self.update_days)
        self.day_combo.currentTextChanged.connect(self.display_exercises)

        # Add controls to the layout
        control_layout.addWidget(QLabel("Select Workout Name:"))
        control_layout.addWidget(self.workout_name_combo)
        control_layout.addWidget(QLabel("Select Week:"))
        control_layout.addWidget(self.week_combo)
        control_layout.addWidget(QLabel("Select Day:"))
        control_layout.addWidget(self.day_combo)

        # Add a spacer item to push the image to the bottom
        control_layout.addSpacerItem(QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Add an image to the bottom
        self.image_label = QLabel()
        # Replace with the path to your image
        pixmap = QPixmap('data/lbb.png')
        resized_pixmap = pixmap.scaled(200, 200, mode=Qt.SmoothTransformation)

        self.image_label.setPixmap(resized_pixmap)
        # Scale the image to fit the QLabel
        self.image_label.setScaledContents(True)
        control_layout.addWidget(self.image_label)

        # Create a scroll area for the output on the right
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()

        # Create a label to display the selected workout details
        self.exercises_label = QLabel("Select a workout to see details")
        self.exercises_label.setWordWrap(True)
        scroll_layout.addWidget(self.exercises_label)
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)

        # Create a horizontal layout to hold the control layout and scroll area
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addLayout(control_layout)
        horizontal_layout.addWidget(scroll_area)

        # Add the horizontal layout to the tab layout
        layout.addLayout(horizontal_layout)
        workout_selection_tab.setLayout(layout)

        return workout_selection_tab

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
            self.display_exercises()

    def display_exercises(self):
        workout_name = self.workout_name_combo.currentText()
        week = self.week_combo.currentText()
        day = self.day_combo.currentText()
        if workout_name and week and day:
            workout = self.workouts[workout_name][week][day]

            exercises_text = f"{day} Workouts:\n\n"
            if "Weights" in workout:
                exercises_text += "Weights:\n"
                for exercise in workout["Weights"]:
                    exercises_text += f"  Exercise: {exercise['exercise']}, Sets: {
                        exercise['sets']}, Reps: {exercise['reps']}\n"
                exercises_text += "\n"

            if "Conditioning" in workout:
                exercises_text += "Conditioning:\n"
                for exercise in workout["Conditioning"]:
                    exercises_text += f"  Exercise: {exercise['exercise']}, Duration: {
                        exercise['duration']}, Reps: {exercise['reps']}\n"
                exercises_text += "\n"

            if "Cardio" in workout:
                cardio = workout["Cardio"]
                exercises_text += "Cardio:\n"
                exercises_text += f"  Exercise: {cardio['exercise']}, Distance: {cardio['distance']}, Duration: {
                    cardio['duration']}, HR Avg: {cardio['hr_avg']}, HR Max: {cardio['hr_max']}\n"
                exercises_text += "\n"

            if "Technical" in workout:
                technical = workout["Technical"]
                exercises_text += "Technical:\n"
                exercises_text += f"  Kata: {technical['Kata']}\n"
                exercises_text += f"  Kihon: {technical['Kihon']}\n"
                exercises_text += f"  Renraku: {technical['Renraku']}\n"
                exercises_text += f"  Other: {technical['Other']}\n"
                exercises_text += "\n"

            self.exercises_label.setText(exercises_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorkoutApp()
    window.show()
    sys.exit(app.exec())
