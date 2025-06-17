#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QComboBox,
    QPushButton, QVBoxLayout, QGridLayout
)

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo com PyQt")
        self.init_ui()

    def init_ui(self):
        layout_principal = QVBoxLayout()
        layout_grade = QGridLayout()

        # Primeira linha: QTextEdit
        self.text_edit_1 = QTextEdit()
        self.text_edit_2 = QTextEdit()
        layout_grade.addWidget(self.text_edit_1, 0, 0)
        layout_grade.addWidget(self.text_edit_2, 0, 1)

        # Segunda linha: QComboBox
        self.combo_1 = QComboBox()
        self.combo_2 = QComboBox()
        # Apenas como exemplo: adicionando itens
        self.combo_1.addItems(["Opção A", "Opção B", "Opção C"])
        self.combo_2.addItems(["Item 1", "Item 2", "Item 3"])
        layout_grade.addWidget(self.combo_1, 1, 0)
        layout_grade.addWidget(self.combo_2, 1, 1)

        # Botão
        self.tranlate = QPushButton("➔Translate➔")

        # Adicionando layouts
        layout_principal.addLayout(layout_grade)
        layout_principal.addWidget(self.tranlate)

        self.setLayout(layout_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())

