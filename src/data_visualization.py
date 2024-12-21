from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from src.data_storage import get_data, get_usernames


class DataVisualization(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.user_selector_layout = QVBoxLayout()
        self.user_label = QLabel("Select User:")
        self.user_combo = QComboBox()
        self.user_combo.addItems(get_usernames())
        self.user_combo.currentTextChanged.connect(self.plot_data)

        self.user_selector_layout.addWidget(self.user_label)
        self.user_selector_layout.addWidget(self.user_combo)
        self.layout.addLayout(self.user_selector_layout)

        self.title_label = QLabel("Biometric Data Visualization")
        self.layout.addWidget(self.title_label)

        self.figure = plt.figure(facecolor='#282a36')
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)
        self.plot_data()

    def plot_data(self):
        selected_user = self.user_combo.currentText()
        data = [entry for entry in get_data() if entry[2] == selected_user]

        if not data:
            return

        dates = [entry[1] for entry in data]
        weights = [entry[3] for entry in data]
        heights = [entry[4] for entry in data]
        chests = [entry[5] for entry in data]
        hips = [entry[6] for entry in data]
        waists = [entry[7] for entry in data]
        shoulders = [entry[8] for entry in data]
        left_biceps = [entry[9] for entry in data]
        right_biceps = [entry[10] for entry in data]
        left_forearms = [entry[11] for entry in data]
        right_forearms = [entry[12] for entry in data]
        left_legs = [entry[13] for entry in data]
        right_legs = [entry[14] for entry in data]
        left_calves = [entry[15] for entry in data]
        right_calves = [entry[16] for entry in data]

        self.figure.clear()
        ax = self.figure.add_subplot(111, facecolor='#282a36')
        ax.spines['bottom'].set_color('#f8f8f2')
        ax.spines['top'].set_color('#f8f8f2')
        ax.spines['left'].set_color('#f8f8f2')
        ax.spines['right'].set_color('#f8f8f2')
        ax.tick_params(axis='x', colors='#f8f8f2')
        ax.tick_params(axis='y', colors='#f8f8f2')

        ax.plot(dates, weights, label="Weight", color='#bd93f9')
        ax.plot(dates, heights, label="Height", color='#ff79c6')
        ax.plot(dates, chests, label="Chest", color='#50fa7b')
        ax.plot(dates, hips, label="Hips", color='#8be9fd')
        ax.plot(dates, waists, label="Waist", color='#ffb86c')
        ax.plot(dates, shoulders, label="Shoulder", color='#ff5555')
        ax.plot(dates, left_biceps, label="Left Bicep", color='#f1fa8c')
        ax.plot(dates, right_biceps, label="Right Bicep", color='#6272a4')
        ax.plot(dates, left_forearms, label="Left Forearm", color='#bd93f9')
        ax.plot(dates, right_forearms, label="Right Forearm", color='#ff79c6')
        ax.plot(dates, left_legs, label="Left Leg", color='#50fa7b')
        ax.plot(dates, right_legs, label="Right Leg", color='#8be9fd')
        ax.plot(dates, left_calves, label="Left Calf", color='#ffb86c')
        ax.plot(dates, right_calves, label="Right Calf", color='#ff5555')
        ax.legend(loc="best", facecolor='#282a36',
                  edgecolor='#6272a4', labelcolor='#f1fa8c')

        self.canvas.draw()
