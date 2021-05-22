import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='debug.log', level=logging.DEBUG)

from gui.main_window import MainWindow
from PySide2.QtWidgets  import QApplication, QMainWindow
import sys

logging.info("===============================================")
logging.info("====================Start wiopt================")

if (__name__ == '__main__'):
  try:
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
  except:
    logging.error("Unexpected error: {}".format(sys.exc_info()[0]))


# from image.resizer import ImageResizer
# resizer = ImageResizer('../test/1.png', 200)
# resizer.resize_with_width(1200)