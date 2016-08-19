# -*- coding: utf-8 -*- 
from PyQt4.QtCore import *  
from PyQt4.QtGui import *
import os
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8")) 
class InputDlg(QDialog):
    def __init__(self,parent=None):  
        super(InputDlg,self).__init__(parent)
        self.resize(400, 100)

        self.setStyleSheet("QLabel{color:rgb(0,0,0);font-size:8;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(250,250,250);}") 
        self.labell = QLabel( "Please enter the facets number:" )
        self.label2 = QLabel( "Please enter the w-layers number:" )
        self.label3 = QLabel( "Please enter the facets number of wf:" )
        self.label4 = QLabel( "Please enter the w-layers number of wf:" )
        self.textField1 =QLineEdit()
        self.textField2 =QLineEdit()
        self.textField3 =QLineEdit()
        self.textField4 =QLineEdit()
        self.okButton =QPushButton( "OK" )
        self.cancalButton =QPushButton( "Cancel" )
        self.connect( self.okButton, SIGNAL( 'clicked()' ), self.OnOk )
        self.connect( self.cancalButton,SIGNAL( 'clicked()' ), self.OnCancel )

        palette1=QPalette(self)
        palette1.setBrush(self.backgroundRole(),QBrush(QPixmap('shao4.jpg')))
        self.setPalette(palette1)
       
        self.text_edit=QTextEdit()
        layout=QGridLayout()
        layout.addWidget( self.labell , 0, 0 )
        layout.addWidget( self.textField1 , 0, 1 )
        layout.addWidget( self.label2 , 1, 0 )
        layout.addWidget( self.textField2 , 1, 1 )
        layout.addWidget( self.label3 , 2, 0 )
        layout.addWidget( self.textField3 , 2, 1 )
        layout.addWidget( self.label4 , 3, 0 )
        layout.addWidget( self.textField4 , 3, 1 )
        layout.addWidget( self.okButton , 4, 0)
        layout.addWidget( self.cancalButton , 4, 1)
        layout.addWidget( self.text_edit,5,0,3,0) 
        
        self.setLayout(layout)  
        self.setWindowTitle(self.tr("Mode: All"))
        self.setWindowIcon(QIcon('shao5.jpg')) 
    def OnOk( self ):
        wf=[]
        fn=int(self.textField1.text())
        wn=int(self.textField2.text())
        wf.append(int(self.textField3.text()))
        wf.append(int(self.textField4.text()))
        self.text_edit.setText("your facets number is  "+str(fn)+'\n'+"your w-layers number is  "+str(wn)+'\n'
                               +"your facets number of wf is  "+str(wf[0])+'\n'+"your w-layers number of wf is "+str(wf[1])+'\n')
	
	f = open('parameters.txt','w')
	f.write(str(fn))
	f.write(' ')
  	f.write(str(wn))
	f.write(' ')
	for i in wf:
	    f.write(str(i))
	    f.write(' ')
	f.close()
	os.system('casa -c wide_field_sim_all.py')
	
    def OnCancel( self ):
        self.textField1.setText('')
        self.textField2.setText('')
        self.textField3.setText('')
        self.textField4.setText('')
        self.text_edit.setText('')

#app=QApplication(sys.argv)  
#form=InputDlg()  
#form.show()  
#app.exec_()  

