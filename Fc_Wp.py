# -*- coding: utf-8 -*- 
from PyQt4.QtCore import *  
from PyQt4.QtGui import *
import sys
import os

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class InputDlg(QDialog):
    def __init__(self,parent=None):  
        super(InputDlg,self).__init__(parent)
        self.resize(400, 200)
        
        self.labell = QLabel( "Please enter the Fc-Wp simulation number:" )
        self.labell.setFont(QFont('Roman times',9,QFont.Bold))
        pe = QPalette()
        pe.setColor(QPalette.WindowText,Qt.white)
        
        self.textField1 =QLineEdit()
        self.okButton =QPushButton( "OK" )
        self.cancalButton =QPushButton( "Cancel" )
        self.connect( self.okButton, SIGNAL( 'clicked()' ), self.OnOk )
        self.connect( self.cancalButton,SIGNAL( 'clicked()' ), self.OnCancel )
        self.text_edit=QTextEdit()
        palette1=QPalette(self)
        palette1.setBrush(self.backgroundRole(),QBrush(QPixmap('shao4.jpg')))
        self.setPalette(palette1)
        layout=QGridLayout()
        layout.addWidget( self.labell , 0, 0 )
        layout.addWidget( self.textField1 , 0, 1 )
        layout.addWidget( self.okButton , 0, 2)
        layout.addWidget( self.cancalButton , 0, 4 )
        layout.addWidget( self.text_edit,1,0,1,0)
        self.setLayout(layout)  
        self.setWindowTitle("Model: Fc-Wp")
        self.setWindowIcon(QIcon('shao5.jpg'))
    def OnOk( self ):
        N=int(self.textField1.text())
        fn = []
        wn = []
        for i in range(N):
            numb1,ok=QInputDialog.getText(self,self.tr("FacetingNum"),self.tr("please enter the "+str(i+1)+"st number of faceting:"),QLineEdit.Normal,self.text_edit.toPlainText())  
            if ok and (not numb1.isEmpty()):
                fn.append(int(numb1))
            elif numb1.isEmpty():
                QMessageBox.information(self,"Information",self.tr("Please input again!"))
                return
            numb2,ok=QInputDialog.getText(self,self.tr("WprojectionNum"),self.tr("please enter the "+str(i+1)+"st number of wprojection:"),QLineEdit.Normal,self.text_edit.toPlainText())  
            if ok and (not numb2.isEmpty()):
                wn.append(int(numb2))
            elif numb2.isEmpty():
                QMessageBox.information(self,"Information",self.tr("Please input again!"))
                return
            #self.text_edit.setText("the "+str(i+1)+"st number is  "+str(numb))
        self.text_edit.setText("your enter numbers of faceting are  "+str(fn)+'\n'+"your enter numbers of wrojection are  "+str(wn)+'\n')
        
	f = open('parameters_wf.txt','w')
	f.write(str(N))
	f.write(' ')
	for i in range(len(wn)):
	    f.write(str(fn[i]))
	    f.write(' ')
	    f.write(str(wn[i]))
	    f.write(' ')
	f.close()
	os.system('casa -c wide_field_sim_wf.py')



    def OnCancel( self ):
        self.textField1.setText('')
        self.text_edit.setText('')
        
#app=QApplication(sys.argv)  
#form=InputDlg()  
#form.show()  
#app.exec_()  
