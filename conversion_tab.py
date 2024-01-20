from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSlot
import subprocess
import os

class ConversionTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Description text box
        self.descriptionTextBox = QTextEdit()
        self.descriptionTextBox.setReadOnly(True)
        # You can set the description text here
        self.descriptionTextBox.setText("Description of the tab's functionality...")
        layout.addWidget(self.descriptionTextBox)
        
        # Convert MIDI to CSV button
        self.convertMidiToCsvButton = QPushButton('Convert MIDI to CSV')
        self.convertMidiToCsvButton.clicked.connect(self.convertMidiToCsv)
        layout.addWidget(self.convertMidiToCsvButton)
        
        # Convert CSV to MIDI button
        self.convertCsvToMidiButton = QPushButton('Convert CSV to MIDI')
        self.convertCsvToMidiButton.clicked.connect(self.convertCsvToMidi)
        layout.addWidget(self.convertCsvToMidiButton)

    @pyqtSlot()
    def convertMidiToCsv(self):
        script_path = os.path.join("miditocsv", "midiPyBatcher.py")
        subprocess.Popen(['python', script_path, '-bm'])

    @pyqtSlot()
    def convertCsvToMidi(self):
        script_path = os.path.join("miditocsv", "midiPyBatcher.py")
        subprocess.Popen(['python', script_path, '-bt'])
