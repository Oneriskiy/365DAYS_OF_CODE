from PyQt6.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QRadioButton,
                             QTextEdit,
                            QScrollArea
                             )

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path
from utils import *

logo_path = Path(__file__).parent / 'photo' / 'logo.png'
logo_label  = QLabel()
logo = QPixmap(str(logo_path))


logo_label.setPixmap(logo)


button = QPushButton("send")
text = QLineEdit()
light_swither = QRadioButton('light theme')
dark_swither = QRadioButton('dark theme')

def switch_theme():
    if dark_swither.isChecked():
        apply_dark_theme(window)
    elif light_swither.isChecked():
        apply_styles_page_one(logo_label, window, light_swither, dark_swither, text, button, success, chat)


text.setPlaceholderText("input the message")
chat = QTextEdit()
success = QLabel()

button.setFixedWidth(400)
text.setFixedWidth(400)
chat.setFixedWidth(400)
light_swither.setFixedSize(200, 30)
dark_swither.setFixedSize(200, 30)


scaled = logo.scaled(250, 400,
                           Qt.AspectRatioMode.KeepAspectRatio,
                           Qt.TransformationMode.SmoothTransformation)
logo_label.setPixmap(scaled)

layout.addWidget(logo_label, 0, 0)
switch_layout.addWidget(light_swither)
switch_layout.addWidget(dark_swither)
layout.addWidget(text, 1, 0, alignment=Qt.AlignmentFlag.AlignVCenter)
layout.addWidget(button, 3, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
layout.addWidget(success, 4, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
layout.addWidget(chat,  5, 0, alignment=Qt.AlignmentFlag.AlignHCenter)

layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
light_swither.toggled.connect(switch_theme)
dark_swither.toggled.connect(switch_theme)

apply_styles_page_one(logo_label, window, light_swither, dark_swither, text, button, success, chat)
