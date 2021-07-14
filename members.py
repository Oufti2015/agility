from PyQt6 import QtWidgets  # import PyQt6 widgets
import sys

# Create the application object
app = QtWidgets.QApplication(sys.argv)

# Create the form object
first_window = QtWidgets.QWidget()

first_window.setGeometry(50, 50, 800, 600)
# Set window size
# first_window.resize(800, 600)

# Set the form title
first_window.setWindowTitle("Berger Club Arlonais Members")

# Show form
first_window.show()

# Run the program
sys.exit(app.exec())
