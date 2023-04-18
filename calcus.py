import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout, QLineEdit

class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        # Ekran uchun bir QLineEdit yaratamiz
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Uchta tugma yig'indisi uchun bir GridLayout yaratamiz
        grid = QGridLayout()

        # Butun sonlarni kiritish tugmalari
        buttons = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', 'C']
        positions = [(i,j) for i in range(4) for j in range(3)]

        for position, button in zip(positions, buttons):
            if button == 'C':
                btn = QPushButton(button)
                btn.setStyleSheet('background-color: red; color: white; font-weight: bold;')
            else:
                btn = QPushButton(button)
            grid.addWidget(btn, *position)
            btn.clicked.connect(self.buttonClicked)

        # Arithmetic operator tugmalarining joylashgan yig'indisi
        operations = ['+', '-', '*', '/', '=']
        for i, operation in enumerate(operations):
            btn = QPushButton(operation)
            btn.setStyleSheet('background-color: lightgrey; font-weight: bold;')
            grid.addWidget(btn, i, 3)
            btn.clicked.connect(self.buttonClicked)

        # Qavs yaratamiz va unga uch tugmani qo'shamiz
        vbox = QVBoxLayout()
        vbox.addWidget(self.display)
        vbox.addLayout(grid)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Kalkulyator')

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Xato!')
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
