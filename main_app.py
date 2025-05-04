import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
)
import constants
from constants import bandwidth


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
        mode_label = QLabel("Mode:")
        self.layout.addWidget(mode_label)
        self.mode_field = QComboBox()
        self.mode_field.addItems(constants.mode)
        self.mode_field.currentTextChanged.connect(self.on_mode_change)
        self.layout.addWidget(self.mode_field)
        self.mode_field.setCurrentText("FDD")

        modulation_label = QLabel("Modulation:")
        self.layout.addWidget(modulation_label)
        self.modulation_field = QComboBox()
        self.modulation_field.addItems(constants.modulation.keys())
        self.layout.addWidget(self.modulation_field)
        self.mode_field.setCurrentText("64QAM")

        coding_rate_label = QLabel("Coding Rate:")
        self.layout.addWidget(coding_rate_label)
        self.coding_rate_label = QLineEdit()
        self.coding_rate_label.setPlaceholderText(f"{constants.coding_rate[self.modulation_field.currentText()][0]} - "
                                           f"{constants.coding_rate[self.modulation_field.currentText()][1]}")
        self.layout.addWidget(self.coding_rate_label)

        bandwidth_label = QLabel("BW:")
        self.layout.addWidget(bandwidth_label)
        self.bandwidth_field = QComboBox()
        self.bandwidth_field.addItems(constants.bandwidth.keys())
        self.layout.addWidget(self.bandwidth_field)

        antennas_label = QLabel("Antennas:")
        self.layout.addWidget(antennas_label)
        self.antennas_field = QComboBox()
        self.antennas_field.addItems(constants.antennas.keys())
        self.layout.addWidget(self.antennas_field)

        overhead_label = QLabel("Overhead (in %):")
        self.layout.addWidget(overhead_label)
        self.overhead_field = QLineEdit()
        self.overhead_field.setPlaceholderText("overhead in %")
        self.layout.addWidget(self.overhead_field)

    # add new field for TDD Uplink/downlink configuration and special subframe
    def on_mode_change(self, mode):
        if mode == "TDD":
            self.tdd_uplink_downlink_conf_label = QLabel("TDD uplink/downlink configuration: ")
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_uplink_downlink_conf_label)
            self.tdd_downlink_conf_field = QComboBox()
            self.tdd_downlink_conf_field.addItems(constants.tdd_uplink_downlink_conf.keys())
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_downlink_conf_field)

            self.tdd_special_subframe_conf_label = QLabel("TDD special subframe configuration: ")
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_special_subframe_conf_label)
            self.tdd_special_subframe_conf_field = QComboBox()
            self.tdd_special_subframe_conf_field.addItems(constants.tdd_special_subframe_conf.keys())
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_special_subframe_conf_field)
        else:
            self.layout.removeWidget(self.tdd_uplink_downlink_conf_label)
            self.tdd_uplink_downlink_conf_label.deleteLater()

            self.layout.removeWidget(self.tdd_downlink_conf_field)
            self.tdd_downlink_conf_field.deleteLater()

            self.layout.removeWidget(self.tdd_special_subframe_conf_label)
            self.tdd_special_subframe_conf_field.deleteLater()

            self.layout.removeWidget(self.tdd_special_subframe_conf_field)
            self.tdd_special_subframe_conf_field.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThroughputApp()
    window.show()
    sys.exit(app.exec_())