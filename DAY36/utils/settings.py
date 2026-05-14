from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget
)


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)
window.resize(500,500)