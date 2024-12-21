import json

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QLineEdit, QComboBox


class BoxingTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boxing Round Timer")
        # self.showMaximized()
        self.setMinimumSize(800, 600)
        # self.setStyleSheet("*{font-family:OptimusPrinceps ;}")

        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(
            """
            QWidget{
            background-color: #282a36;
            }
            """)
        self.setCentralWidget(self.central_widget)

        main_layout = QHBoxLayout()

        self.central_widget.setLayout(main_layout)

        # Left layout for controls
        self.controls_layout = QVBoxLayout()
        self.controls_layout.setContentsMargins(0, 0, 0, 0)

        self.workout_label = QLabel("Select Workout:")
        self.workout_label.setAlignment(Qt.AlignCenter)
        self.workout_label.setStyleSheet(
            """ 
            QLabel{
            font: bold 14px;
            color: #f8f8f2;
            margin: 1 0 1 0;
            padding: 0
            }
            """)
        self.workout_label.setMaximumWidth(150)
        self.workout_selector = QComboBox()
        self.workout_selector.setMaximumWidth(150)
        self.workout_selector.setStyleSheet(
            """
            QComboBox{
            font: bold 14px;
            color:#f8f8f2; 
            background-color: #44475a;
            margin: 1 0 1 0;
            padding: 0; 
            }
            """)

        self.controls_layout.addWidget(self.workout_label)
        self.controls_layout.addWidget(self.workout_selector)

        self.round_number_label = QLabel("Round Number:")
        self.round_number_label.setMaximumWidth(150)
        self.round_number_label.setAlignment(Qt.AlignCenter)
        self.round_number_label.setStyleSheet(
            """ 
            QLabel{
            font: bold 13px;
            color: #f8f8f2;
            margin: 1 0 1 0;
            padding: 0;
            }
            """
        )
        self.round_number_input = QLineEdit()
        self.round_number_input.setMaximumWidth(150)
        self.round_number_input.setAlignment(Qt.AlignCenter)
        self.round_number_input.setStyleSheet(
            """
            QLineEdit{
            color: #f8f8f2;
            background-color: #44475a;
            margin: 1 0 1 0;
            padding: 0;
            }
            """
        )
        self.controls_layout.addWidget(self.round_number_label)
        self.controls_layout.addWidget(self.round_number_input)

        self.round_length_label = QLabel("Round Length (seconds):")
        self.round_length_label.setAlignment(Qt.AlignCenter)
        self.round_length_label.setMaximumWidth(150)
        self.round_length_label.setStyleSheet(
            """ 
            QLabel{
            font: bold 13px;
            color: #f8f8f2;
            margin: 1 0 1 0;
            padding: 0;
            }
            """)
        self.round_length_input = QLineEdit()
        self.round_length_input.setAlignment(Qt.AlignCenter)
        self.round_length_input.setMaximumWidth(150)
        self.round_length_input.setStyleSheet(
            """
            QLineEdit{
            margin: 1 0 1 0;
            padding: 0;
            color: #f8f8f2;
            background-color: #44475a;
            }
            """
        )
        self.controls_layout.addWidget(self.round_length_label)
        self.controls_layout.addWidget(self.round_length_input)

        self.rest_time_label = QLabel("Rest Time (seconds):")
        self.rest_time_label.setAlignment(Qt.AlignCenter)
        self.rest_time_label.setMaximumWidth(150)
        self.rest_time_label.setStyleSheet(
            """ 
            QLabel{
            font: bold 13px;
            color: #f8f8f2;
            padding: 1 0 1 0;
            margin: 0;
            }
            """)
        self.rest_time_input = QLineEdit()
        self.rest_time_input.setAlignment(Qt.AlignCenter)
        self.rest_time_input.setMaximumWidth(150)
        self.rest_time_input.setStyleSheet(
            """
            QLineEdit{
            color: #f8f8f2;
            background-color: #44475a;
            padding: 1 0 1 0;
            margin: 0;
            }
            """
        )
        self.controls_layout.addWidget(self.rest_time_label)
        self.controls_layout.addWidget(self.rest_time_input)

        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet(
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

        self.pause_button = QPushButton("Pause")
        self.pause_button.setStyleSheet(
            """
            QPushButton{
            background-color: #44475a; 
            color: #ff5555;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: #6272a4;
            font: bold 14px;
            min-width: 138px;
            padding: 6px;
            }
            QPushButton:pressed{
            background-color: #ff5555;
            color:#44475a; 
            border-style: inset;
            }
            """
        )
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet(
            """
            QPushButton{
            background-color: #44475a; 
            color: #8be9fd ;
            border-style: outset;
            border-width: 2px;
            border-color: #6272a4;
            border-radius: 10px; 
            font: bold 14px;
            min-width: 138px;
            }
            QPushButton:pressed{
            background-color: #8be9fd;
            color: #44475a; 
            border-style: inset;}
            """
        )
        self.controls_layout.addWidget(self.start_button)
        self.controls_layout.addWidget(self.pause_button)
        self.controls_layout.addWidget(self.reset_button)

        main_layout.addLayout(self.controls_layout)

        # Right layout for display
        self.display_layout = QVBoxLayout()

        self.timer_display = QLabel("Time Remaining:\n00:00")
        self.timer_display.setStyleSheet("font-size: 60px; color: #50fa7b;")
        self.timer_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_layout.addWidget(self.timer_display)

        self.round_info_display = QLabel("Rounds Remaining:\n1")
        self.round_info_display.setStyleSheet(
            "font-size: 30px; color: #bd93f9")
        self.round_info_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_layout.addWidget(self.round_info_display)

        self.exercise_display = QLabel("Exercise:\n--")
        self.exercise_display.setStyleSheet("font-size: 40px; color:#ffb86c ")
        self.exercise_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_layout.addWidget(self.exercise_display)

        main_layout.addLayout(self.display_layout)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Timer state
        self.time_remaining = 0
        self.round_number = 1
        self.in_rest = False
        self.is_paused = False
        self.current_exercise_index = 0

        # Load workouts
        self.workouts = []
        self.load_workouts()

        # Connect buttons to functions
        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        self.workout_selector.currentTextChanged.connect(
            self.load_selected_workout)

        # Populate workout selector
        self.populate_workout_selector()

    def start_timer(self):
        self.time_remaining = int(self.round_length_input.text())
        self.round_number = int(self.round_number_input.text())
        self.in_rest = False
        self.is_paused = False
        self.current_exercise_index = 0
        self.update_display()
        self.timer.start(1000)
        self.play_sound("round_start")

    def pause_timer(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.timer.stop()
        else:
            self.timer.start(1000)

    def reset_timer(self):
        self.timer.stop()
        self.time_remaining = 0
        self.update_display()

    def update_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.update_display()
        else:
            if not self.in_rest:
                self.in_rest = True
                self.time_remaining = int(self.rest_time_input.text())
                self.play_sound("rest_start")
            else:
                self.in_rest = False
                self.current_exercise_index += 1
                if self.current_exercise_index < len(self.workouts[self.current_workout_index]["exercises"]):
                    self.time_remaining = int(
                        self.workouts[self.current_workout_index]["exercises"][self.current_exercise_index][
                            "round_time"])
                    self.round_number -= 1
                    self.play_sound("round_start")
                else:
                    self.timer.stop()

    def update_display(self):
        minutes, seconds = divmod(self.time_remaining, 60)
        self.timer_display.setText(
            f"Time Remaining:\n{minutes:02d}:{seconds:02d}")
        self.round_info_display.setText(
            f"Rounds Remaining:\n{self.round_number}")
        if self.current_exercise_index < len(self.workouts[self.current_workout_index]["exercises"]):
            current_exercise = self.workouts[self.current_workout_index]["exercises"][self.current_exercise_index][
                "exercise"]
        else:
            current_exercise = "--"
        self.exercise_display.setText(
            "Resting" if self.in_rest else f"Exercise:\n{current_exercise}")

    def play_sound(self, sound_type):
        # if sound_type == "round_start":
        #     playsound("round_start.mp3")
        # elif sound_type == "rest_start":
        #     playsound("rest_start.mp3")
        # elif sound_type == "round_end":
        #     playsound("round_end.mp3")
        pass

    def load_workouts(self, filename="data/timer_workouts.json"):
        try:
            with open(filename, "r") as file:
                self.workouts = json.load(file)
        except FileNotFoundError:
            self.workouts = []

    def populate_workout_selector(self):
        self.workout_selector.clear()
        for workout in self.workouts:
            self.workout_selector.addItem(workout["name"])

    def load_selected_workout(self):
        selected_workout = self.workout_selector.currentText()
        self.current_workout_index = -1
        for index, workout in enumerate(self.workouts):
            if workout["name"] == selected_workout:
                self.current_workout_index = index
                self.round_number_input.setText(str(len(workout["exercises"])))
                self.round_length_input.setText(
                    str(workout["exercises"][0]["round_time"]))
                self.rest_time_input.setText(
                    str(workout["exercises"][0]["rest_time"]))
                break

# if __name__ == "__main__":
#     with keep.presenting():
#         app = QApplication(sys.argv)
#         window = BoxingTimer()
#         window.show()
#         sys.exit(app.exec())
