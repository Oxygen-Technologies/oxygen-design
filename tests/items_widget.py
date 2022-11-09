import sys

from PySide2.QtWidgets import QWidget, QApplication

from ui.items_base_widget import Ui_ItemsWidget


class ItemsWidget(Ui_ItemsWidget, QWidget):
    def __init__(self, parent=None):
        super(ItemsWidget, self).__init__(parent)

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ItemsWidget()
    widget.show()
    sys.exit(app.exec_())
