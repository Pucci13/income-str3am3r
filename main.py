import sys
from PySide6.QtWidgets import QApplication, QDialog
from main_window_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.addIncome.clicked.connect(self.on_add_income_clicked)

    

    def on_add_income_clicked(self):
        incomeDialog = QDialog()
        incomeDialog.exec()
        print("Add income button clicked!")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

