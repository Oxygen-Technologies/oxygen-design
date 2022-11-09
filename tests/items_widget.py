import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QApplication

from oxygen_design import OxygenDesign
from ui.items_base_widget import Ui_ItemsWidget


class ItemsWidget(Ui_ItemsWidget, QWidget):
    def __init__(self, parent=None):
        super(ItemsWidget, self).__init__(parent)
        oxygen_design = OxygenDesign()
        self.setupUi(self)

        self.setWindowTitle('🚀 {old}'.format(old=self.windowTitle()))
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        self.setWindowIconText('')
        self.setStyleSheet(oxygen_design.get_basic_styles())
        self.label.setText('🏳‍🌈 {old} 🛰'.format(old=self.label.text()))
        oxygen_design.load_style(self.pushButton_4, 'button-normal')
        oxygen_design.load_style(self.pushButton_3, 'button-dashed')
        oxygen_design.load_style(self.pushButton_2, 'button-danger')
        self.pushButton_2.setText('🚪 {old}'.format(old=self.pushButton_2.text()))

        self.pushButton_2.clicked.connect(lambda: self.close())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ItemsWidget()
    widget.show()
    sys.exit(app.exec_())
