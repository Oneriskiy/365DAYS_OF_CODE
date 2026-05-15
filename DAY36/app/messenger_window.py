from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QTextEdit
from utils import *

mainText = QLabel("Mini-Messenger")

button = QPushButton("send")
text = QLineEdit()
text.setPlaceholderText("input the message")
chat = QTextEdit()
success = QLabel()

layout.addWidget(mainText)
layout.addWidget(text)
layout.addWidget(button)
layout.addWidget(success)
layout.addWidget(chat)


apply_styles_page_one(mainText, window, text, button, success, chat)
