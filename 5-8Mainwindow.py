# -*- coding: utf-8 -*-  
from PyQt4.QtCore import *  
from PyQt4.QtGui import *
import All
import Wp
import Fc
import Fc_Wp
import sys  
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class InputDlg(QDialog):   
    def __init__(self,parent=None):  
        super(InputDlg,self).__init__(parent)
        self.setWindowTitle(self.tr("Wide-field Imaging Simulator"))
        self.setWindowIcon(QIcon('shao5.jpg'))
        self.resize( 490, 480 )
        
        label1=QLabel(self.tr(""))
        self.modeComboBox = QComboBox()
        self.modeComboBox.insertItem(0, self.tr("--------mode choose--------"))
        self.modeComboBox.insertItem(1, self.tr("all"))
        self.modeComboBox.insertItem(2, self.tr("facet-wprojection"))
        self.modeComboBox.insertItem(3, self.tr("wprojection"))
        self.modeComboBox.insertItem(4, self.tr("faceting"))
        runButton=QPushButton("OK")
        #runButton.setStyleSheet("background-color: rgb(30, 144, 250);")
        self.connect(runButton,SIGNAL("clicked()"),self.modeRun)

        layout=QGridLayout()
        layout.addWidget(label1,0,0)
        layout.addWidget(self.modeComboBox,1,0,1,1)  
        layout.addWidget(runButton,1,1,1,1)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.drawPixmap(0, 0, 490, 480, QPixmap("jiemian.jpg"))
        painter.end()
    def modeRun(self):
        m = str(self.modeComboBox.currentText())
        if m=="all":
            self.another =All.InputDlg()
            self.another.show()
        elif m=="facet-wprojection":
            self.theother =Fc_Wp.InputDlg()
            self.theother.show()    
        elif m=="wprojection":
            self.another =Wp.InputDlg()
            self.another.show()
        elif m=="faceting":
            self.theother =Fc.InputDlg()
            self.theother.show()
        elif m=="--------mode choose--------":
            QMessageBox.information(self,"Information",self.tr("Please choose a mode type!"))
        
    def closeEvent(self, event):
        reply =QMessageBox.question(self, 'Message',"Are you sure to quit?",QMessageBox.Yes,QMessageBox.No)
        if reply ==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
                 
app=QApplication(sys.argv)  
form=InputDlg()  
form.show()  
app.exec_()  
