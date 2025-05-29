import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QCheckBox,
    QVBoxLayout,
)
import constants


class ThroughputApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Throughput calculator")
        self.layout = QVBoxLayout()
        self.init_ui()
        self.setFixedWidth(550)  # 300

    def init_ui(self):
        self.label = QLabel("Enter data to calculate" "\nthe throughput:")
        self.layout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.initiate_data_field()
        self.initiate_calculate_button()
        self.initiate_output_field()
        self.mode_field.setCurrentText("TDD")
        self.setLayout(self.layout)
        self.CP = 14

    def calculate_throughput(self):
        try:
            base_throughput = self.calculate_base_throughput()
            print(self.mode_field.currentText())
            if self.mode_field.currentText() == "TDD":
                downlink_throughput = self.calculate_specific_throughput(
                    base_throughput, "downlink"
                )
                uplink_throughput = self.calculate_specific_throughput(
                    base_throughput, "uplink"
                )

                self.result_label.setText(
                    f"Summary Throughut: {base_throughput} Mbps \n"
                    f"Downlink: {str(round(downlink_throughput, 2))} Mbps \n"
                    f"Uplink: {str(round(uplink_throughput, 2))} Mbps"
                )
            else:
                self.result_label.setText(f"Throghput: {base_throughput} Mbps")
        except ValueError:
            self.result_label.setText("Please enter valid numbers.")

    def calculate_base_throughput(self):
        base_throughput = (
            (
                (
                    constants.bandwidth[self.bandwidth_field.currentText()]
                    * 12
                    * self.CP
                    # * constants.modulation[self.modulation_field.currentText()]
                    * constants.MCS[self.mcs_field.currentText()][0]
                    * constants.MCS[self.mcs_field.currentText()][1]
                )
                # * float(self.coding_rate_field.text())
                * constants.antennas[self.antennas_field.currentText()]
            )
            * ((1 - float(constants.OVERHEAD[self.mode_field.currentText()][self.antennas_field.currentText()])))/ 1000)
        return base_throughput

    def calculate_specific_throughput(
        self, base_throughput, specific_throughput_string
    ):
        specific_throughput = (
            base_throughput
            * (
                (
                    float(
                        constants.tdd_uplink_downlink_conf[
                            self.tdd_uplink_downlink_conf_field.currentText()
                        ][specific_throughput_string]
                    )
                    + float(
                        constants.tdd_uplink_downlink_conf[
                            self.tdd_uplink_downlink_conf_field.currentText()
                        ]["special"]
                    )
                    * (
                        float(
                            constants.tdd_special_subframe_conf[
                                self.tdd_special_subframe_conf_field.currentText()
                            ][specific_throughput_string]
                        )
                        / 14
                    )
                )
            )
            / 10
        )
        return specific_throughput

    def initiate_calculate_button(self):
        self.calc_tp_button = QPushButton("Calculate Throughput")
        self.calc_tp_button.clicked.connect(self.calculate_throughput)
        self.layout.addWidget(self.calc_tp_button)

    def initiate_output_field(self):
        self.result_label = QLabel("Throughput: ")
        self.layout.addWidget(self.result_label)

    def handle_switch_toggle(self, state):
        print(state)
        if state == 2:
            self.CP = 12
        else:
            self.CP = 14

    def initiate_data_field(self):
        mode_label = QLabel("Mode:")
        self.layout.addWidget(mode_label)
        self.mode_field = QComboBox()
        self.mode_field.addItems(constants.mode)
        self.mode_field.currentTextChanged.connect(self.on_mode_change)
        self.layout.addWidget(self.mode_field)

        mcs_label = QLabel("MCS:")
        self.layout.addWidget(mcs_label)
        self.mcs_field = QComboBox()
        self.mcs_field.addItems(constants.MCS.keys())
        self.layout.addWidget(self.mcs_field)
        self.mcs_field.setCurrentText("0")

        # modulation_label = QLabel("Modulation:")
        # self.layout.addWidget(modulation_label)
        # self.modulation_field = QComboBox()
        # self.modulation_field.addItems(constants.modulation.keys())
        # self.layout.addWidget(self.modulation_field)
        # self.mode_field.setCurrentText("64QAM")

        # coding_rate_label = QLabel("Coding Rate:")
        # self.layout.addWidget(coding_rate_label)
        # self.coding_rate_field = QLineEdit()
        # self.coding_rate_field.setPlaceholderText(f"{constants.coding_rate[self.modulation_field.currentText()][0]} - "
        #                                    f"{constants.coding_rate[self.modulation_field.currentText()][1]}")
        # self.layout.addWidget(self.coding_rate_field)

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
        
        self.switch = QCheckBox("Extended CyclicPrefix")  # Label optional
        self.switch.setChecked(False)  # default state
        
        self.switch.setStyleSheet('''
            QCheckBox::indicator {
                width: 40px;
                height: 20px;
            }
            QCheckBox::indicator:unchecked {
                border-radius: 10px;
                background-color: #c40808;
            }
            QCheckBox::indicator:checked {
                border-radius: 10px;
                background-color: #00cc66;
            }
        ''')

        self.layout.addWidget(self.switch)

        # Optionally connect to a method to handle toggle changes:
        self.switch.stateChanged.connect(self.handle_switch_toggle)

        # overhead_label = QLabel("Overhead (in %):")
        # self.layout.addWidget(overhead_label)
        # self.overhead_field = QLineEdit()
        # self.overhead_field.setPlaceholderText("overhead in %")
        # self.layout.addWidget(self.overhead_field)
        # self.mode_field.setCurrentText("0")

    # add new field for TDD Uplink/downlink configuration and special subframe
    def on_mode_change(self, mode):
        if mode == "TDD":
            self.tdd_uplink_downlink_conf_label = QLabel(
                "TDD uplink/downlink configuration: "
            )
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_uplink_downlink_conf_label)
            self.tdd_uplink_downlink_conf_field = QComboBox()
            self.tdd_uplink_downlink_conf_field.addItems(
                constants.tdd_uplink_downlink_conf.keys()
            )
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_uplink_downlink_conf_field)

            self.tdd_special_subframe_conf_label = QLabel(
                "TDD special subframe configuration: "
            )
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_special_subframe_conf_label)
            self.tdd_special_subframe_conf_field = QComboBox()
            self.tdd_special_subframe_conf_field.addItems(
                constants.tdd_special_subframe_conf.keys()
            )
            insert_index = self.layout.count() - 2
            self.layout.insertWidget(insert_index, self.tdd_special_subframe_conf_field)
        else:
            self.layout.removeWidget(self.tdd_uplink_downlink_conf_label)
            self.tdd_uplink_downlink_conf_label.deleteLater()

            self.layout.removeWidget(self.tdd_uplink_downlink_conf_field)
            self.tdd_uplink_downlink_conf_field.deleteLater()

            self.layout.removeWidget(self.tdd_special_subframe_conf_label)
            self.tdd_special_subframe_conf_label.deleteLater()

            self.layout.removeWidget(self.tdd_special_subframe_conf_field)
            self.tdd_special_subframe_conf_field.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThroughputApp()
    window.show()
    sys.exit(app.exec_())
