def apply_dracula_theme(app):
    app.setStyleSheet("""
        QMainWindow {
            background-color: #282a36;
            color: #f8f8f2;
        }
        QLabel, QPushButton, QComboBox, QLineEdit {
            font-size: 14px;
            color: #f8f8f2;
            background-color: #44475a;
            border: 1px solid #6272a4;
            border-radius: 4px;
            padding: 4px;
        }
        QComboBox, QLineEdit {
            padding: 4px;
            margin: 4px 0;
        }
        QPushButton {
            padding: 6px 12px;
        }
        QTabWidget::pane {
            border: 1px solid #6272a4;
            border-radius: 4px;
            margin: 0;
            padding: 0;
        }
        QTabBar::tab {
            background: #44475a;
            border: 1px solid #6272a4;
            border-bottom-color: #282a36;
            padding: 6px;
        }
        QTabBar::tab:selected {
            background: #6272a4;
            color: #f8f8f2;
        }
    """)
