import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import requests
  
class LoadingGif(object):
    def mainUI(self, FrontWindow):
        FrontWindow.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)  
        FrontWindow.setAttribute(Qt.WA_TranslucentBackground)
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(480, 480)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")
  
        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 480))
        self.label.setMinimumSize(QtCore.QSize(480, 480))
        self.label.setMaximumSize(QtCore.QSize(480, 480))
        self.label.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)
  
        # Loading the GIF
        r = requests.get("https://i.giphy.com/ZE5DmCqNMr3yDXq1Zu.gif", allow_redirects=True)
        open('yes.gif', 'wb').write(r.content)
        self.movie = QMovie('yes.gif')
        self.label.setMovie(self.movie)
  
        self.startAnimation()
  
    # Start Animation
  
    def startAnimation(self):
        self.movie.start()
  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
  
  
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
demo = LoadingGif()
demo.mainUI(window)
window.show()
sys.exit(app.exec_())
