import sys
from window import *


def main():
    
    app = QApplication(sys.argv)

    start_wind = MainWindow()

    start_wind.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()