import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)

class ThroughputApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Throughput calculator")
        self.layout = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Enter data to calculate the throughput:")
        self.layout.addWidget(self.label)

        self.initiate_data_field()
        self.initiate_calculate_button()
        self.initiate_output_field()

        self.setLayout(self.layout)

    def calculate_throughput(self):
        try:
            throughput = (float(self.number_of_people_field.text()) * float(self.area_field.text()) -
                          (float(self.bler_field.text()) / float(self.jakis_field.text())))
            self.result_label.setText(f"Throughput: {throughput}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers.")

    def initiate_calculate_button(self):
        self.calc_tp_button = QPushButton("Calculate Throughput")
        self.calc_tp_button.clicked.connect(self.calculate_throughput)
        self.layout.addWidget(self.calc_tp_button)

    def initiate_output_field(self):
        self.result_label = QLabel("Throughput: ")
        self.layout.addWidget(self.result_label)

    def initiate_data_field(self):
        self.number_of_people_field = QLineEdit()
        self.number_of_people_field.setPlaceholderText("Number of people")
        self.layout.addWidget(self.number_of_people_field)

        self.area_field = QLineEdit()
        self.area_field.setPlaceholderText("Area (in square meters)")
        self.layout.addWidget(self.area_field)

        self.bler_field = QLineEdit()
        self.bler_field.setPlaceholderText("Bler area")
        self.layout.addWidget(self.bler_field)

        self.jakis_field = QLineEdit()
        self.jakis_field.setPlaceholderText("Jakis area")
        self.layout.addWidget(self.jakis_field)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThroughputApp()
    window.show()
    sys.exit(app.exec_())