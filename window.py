from PyQt5 import QtWidgets
app = QtWidgets.QApplication([])



window = QtWidgets.QWidget()
window.setWindowTitle('FASS playerz')

L1 = QtWidgets.QLabel(window)
L1.setText('<h1>hello world</h1>')
L1.move(50,50)



window.setGeometry(1000,500,600,200)
window.show()
app.exec_()


