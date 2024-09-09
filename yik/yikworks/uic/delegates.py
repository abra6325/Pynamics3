from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox


class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, items, parent=None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        # Create a QComboBox as the editor
        comboBox = QComboBox(parent)
        comboBox.addItems(self.items)
        return comboBox

    def setEditorData(self, editor, index):
        # Set the data from the model to the combo box
        value = index.model().data(index, Qt.EditRole)
        editor.setCurrentText(value)

    def setModelData(self, editor, model, index):
        # Update the model with the selected data from the combo box
        model.setData(index, editor.currentText(), Qt.EditRole)