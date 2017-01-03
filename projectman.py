# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\projectman.ui'
#
# Created: Wed Apr 29 15:41:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import sqlite3
tagslist=[]
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class TableWidget( QtGui.QTableWidget ) :
    row=0
    col=0
    def __init__(self,parent=None):
        QtGui.QTableWidget.__init__(self,parent)
        self.createmenu()
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows) 
               
    def createmenu(self):        
        self.dizenAction = QtGui.QAction("add", self,
                triggered=self.add)
        self.samevaluesAction = QtGui.QAction("samevalues", self,
                triggered=self.samevalues)
        self.selectAction = QtGui.QAction("select", self,
                triggered=self.select)  
        self.unselectAction = QtGui.QAction("unselect", self,
                triggered=self.unselect)  
        self.popMenu = QtGui.QMenu(self)        
        self.popMenu.addAction(self.dizenAction)
        self.popMenu.addAction(self.samevaluesAction)
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.selectAction) 
        self.popMenu.addAction(self.unselectAction) 
        self.popMenu.setParent(self)       
    def mousePressEvent( self, e ) :
        if e.button() == QtCore.Qt.RightButton :  
            temp = self.itemAt( e.pos() )            
            if temp != None :                                  
                self.row =  temp.row()
                self.col=temp.column()
                self.popMenu.exec_(QtGui.QCursor.pos())                  
                
        QtGui.QTableWidget.mousePressEvent( self, e )
#        aItem=QtGui.QTableWidgetItem()
#        aItem.checkState()
    def add(self): 
        rows=[]
        for idx in self.selectionModel().selectedRows():
            rows.append(idx.row())  
        print(rows,len(rows))                   
        curitem=self.item(self.row,self.col)
        if curitem!=None: 
            try:
                strint=int(curitem.text())           
                for row in range(self.row,self.rowCount()):
                    if(self.item(row,self.col)==None):
                        item = QtGui.QTableWidgetItem()
                        self.setItem(row,self.col,item)                
                    self.item(row,self.col).setText(str(strint))
                    strint+=1
            except Exception as e:
                print(str(e))
                  
    def samevalues(self):
        curitem=self.item(self.row,self.col)
        if curitem!=None: 
            try:
                strint=int(curitem.text())           
                for row in range(self.row,self.rowCount()):
                    if(self.item(row,self.col)==None):
                        item = QtGui.QTableWidgetItem()
                        self.setItem(row,self.col,item)                
                    self.item(row,self.col).setText(str(strint))                        
            except Exception as e:
                print(str(e))
    def select(self): 
        rows=[]
        for idx in self.selectionModel().selectedRows():
            rows.append(idx.row())                 
        try:
            if(len(rows)<1):         
                for row in range(self.row,self.rowCount()):
                    if(self.item(row,0)!=None):  
                        self.item(row,0).setCheckState(QtCore.Qt.Checked)
            else:
                for row in rows:
                    if(self.item(row,0)!=None):  
                        self.item(row,0).setCheckState(QtCore.Qt.Checked)
                                    
                                
        except Exception as e:
            print(str(e))
    def unselect(self):                
        rows=[]
        for idx in self.selectionModel().selectedRows():
            rows.append(idx.row())                 
        try:
            if(len(rows)<1):         
                for row in range(self.row,self.rowCount()):
                    if(self.item(row,0)!=None):  
                        self.item(row,0).setCheckState(QtCore.Qt.Unchecked)
            else:
                for row in rows:
                    if(self.item(row,0)!=None):  
                        self.item(row,0).setCheckState(QtCore.Qt.Unchecked)
                    
        except Exception as e:
            print(str(e))

class Ui_MainWindow(QtGui.QMainWindow):
    filename = 'project.dat'   
    dbopened=False   
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)
    def __init__( self ) :
        QtGui.QWidget.__init__(self)
        
        self.setObjectName(_fromUtf8("MainWindow"))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(800, 600)
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        self.menuTags = QtGui.QMenu(self.menubar)
        self.menuTags.setObjectName(_fromUtf8("menuTags"))
        self.menuChannel = QtGui.QMenu(self.menubar)
        self.menuChannel.setObjectName(_fromUtf8("menuChannel"))
        self.menuProtocol = QtGui.QMenu(self.menubar)
        self.menuProtocol.setObjectName(_fromUtf8("menuProtocol"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(self)
        self.toolBar.setAutoFillBackground(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(self)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(self)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSave = QtGui.QAction(self)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(self)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAdd_project = QtGui.QAction(self)
        self.actionAdd_project.setObjectName(_fromUtf8("actionAdd_project"))
        self.actionFind_project = QtGui.QAction(self)
        self.actionFind_project.setObjectName(_fromUtf8("actionFind_project"))
        self.actionAdd_Tag = QtGui.QAction(self)
        self.actionAdd_Tag.setObjectName(_fromUtf8("actionAdd_Tag"))
        self.actionFind_tags = QtGui.QAction(self)
        self.actionFind_tags.setObjectName(_fromUtf8("actionFind_tags"))
        self.actionAdd_channel = QtGui.QAction(self)
        self.actionAdd_channel.setObjectName(_fromUtf8("actionAdd_channel"))
        self.actionFind_channel = QtGui.QAction(self)
        self.actionFind_channel.setObjectName(_fromUtf8("actionFind_channel"))
        self.actionAdd_protocol = QtGui.QAction(self)
        self.actionAdd_protocol.setObjectName(_fromUtf8("actionAdd_protocol"))
        self.actionFind_protocol = QtGui.QAction(self)
        self.actionFind_protocol.setObjectName(_fromUtf8("actionFind_protocol"))
        self.actionAdd_devicetag = QtGui.QAction(self)
        self.actionAdd_devicetag.setObjectName(_fromUtf8("actionAdd_devicetag"))        
        self.actionAbout = QtGui.QAction(self)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(self)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuProject.addAction(self.actionAdd_project)
        self.menuProject.addAction(self.actionFind_project)
        self.menuTags.addAction(self.actionAdd_Tag)
        self.menuTags.addAction(self.actionFind_tags)
        self.menuChannel.addAction(self.actionAdd_channel)
        self.menuChannel.addAction(self.actionFind_channel)
        self.menuProtocol.addAction(self.actionAdd_protocol)
        self.menuProtocol.addAction(self.actionFind_protocol)
        self.menuProtocol.addAction(self.actionAdd_devicetag)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuTags.menuAction())
        self.menubar.addAction(self.menuChannel.menuAction())
        self.menubar.addAction(self.menuProtocol.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction()) 
               
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), self.close)

        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), self.file_open)
      
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), self.help_about)
     
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), self.file_close)
      
        QtCore.QObject.connect(self.actionAdd_project, QtCore.SIGNAL(_fromUtf8("triggered()")), self.add_project)
        QtCore.QObject.connect(self.actionAdd_channel, QtCore.SIGNAL(_fromUtf8("triggered()")), self.add_chan)
        QtCore.QObject.connect(self.actionAdd_protocol, QtCore.SIGNAL(_fromUtf8("triggered()")), self.add_pro)
        QtCore.QObject.connect(self.actionFind_project, QtCore.SIGNAL(_fromUtf8("triggered()")), self.find_project)
        QtCore.QObject.connect(self.actionFind_protocol, QtCore.SIGNAL(_fromUtf8("triggered()")), self.find_protocol)
        QtCore.QObject.connect(self.actionFind_channel, QtCore.SIGNAL(_fromUtf8("triggered()")), self.find_channel)
        QtCore.QObject.connect(self.actionAdd_devicetag, QtCore.SIGNAL(_fromUtf8("triggered()")), self.addprototags)
        QtCore.QObject.connect(self.actionAdd_Tag, QtCore.SIGNAL(_fromUtf8("triggered()")), self.Add_Tag)
        QtCore.QObject.connect(self.actionFind_tags, QtCore.SIGNAL(_fromUtf8("triggered()")), self.find_tags)
        
        self.setWindowTitle(_translate("MainWindow", "projectMan", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuProject.setTitle(_translate("MainWindow", "project", None))
        self.menuTags.setTitle(_translate("MainWindow", "tags", None))
        self.menuChannel.setTitle(_translate("MainWindow", "channel", None))
        self.menuProtocol.setTitle(_translate("MainWindow", "protocol", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionAdd_project.setText(_translate("MainWindow", "add project", None))
        self.actionAdd_project.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionFind_project.setText(_translate("MainWindow", "find project", None))
        self.actionAdd_Tag.setText(_translate("MainWindow", "add tags", None))
        self.actionFind_tags.setText(_translate("MainWindow", "find tags", None))
        self.actionAdd_channel.setText(_translate("MainWindow", "add channel", None))
        self.actionFind_channel.setText(_translate("MainWindow", "find channel", None))
        self.actionAdd_protocol.setText(_translate("MainWindow", "add protocol", None))
        self.actionFind_protocol.setText(_translate("MainWindow", "find protocol", None))
        self.actionAdd_devicetag.setText(_translate("MainWindow", "add protocoltag", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))
        self.actionHelp.setText(_translate("MainWindow", "help", None)) 
        QtCore.QMetaObject.connectSlotsByName(self) 
        if os.path.exists(self.filename):
            self.statusbar.showMessage(self.filename)
            self.database= sqlite3.connect(self.filename)
            self.dbopened=True
            self.database.close()      
    def file_open(self):
#        msgBox = QtGui.QMessageBox()
#        msgBox.setText("The document has been modified.")
#        msgBox.setInformativeText("Do you want to save your changes?")
#        msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
#        msgBox.setDefaultButton(QtGui.QMessageBox.Save)
#        ret = msgBox.exec_()
#        print(ret)
        try:
            self.filename = QtGui.QFileDialog.getOpenFileName(None, 'open file', './')
            if os.path.exists(self.filename):
                self.statusbar.showMessage(self.filename)
                self.database= sqlite3.connect(self.filename)
                self.dbopened=True
                self.database.close()
            else:
                QtGui.QMessageBox.information(None, 'Message', 'database ' + self.filename + 'is not exist!', QtGui.QMessageBox.Yes)
        except IOError as e:
            QtGui.QMessageBox.warning( self, "Message", "warning: can not open database"+self.filename, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
    def help_about(self):
        QtGui.QMessageBox.about(None, 'projectman', "project man is a commi project configure software!")
    def file_close(self):
        if not self.dbopened:
            return
        result=QtGui.QMessageBox.question(None, 'projectman', 'close database '+os.path.basename(self.filename),QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if result==QtGui.QMessageBox.Yes:
            self.dbopened=False
    def add_project(self):         
        if self.dbopened:
            Ui_add_project.database=self.filename
            self.add_projectui=Ui_add_project()                          
            self.add_projectui.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!")  
    def add_chan(self):
        if self.dbopened:
            Ui_add_chan.database=self.filename
            self.add_chan=Ui_add_chan()
            self.add_chan.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!")     
    def add_pro(self):         
        if self.dbopened:
            Ui_add_pro.database=self.filename
            self.add_pro=Ui_add_pro()                          
            self.add_pro.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!") 
    def Add_Tag(self):         
        if self.dbopened:
            Ui_ADD_TAGS.database=self.filename
            self.add_pro=Ui_ADD_TAGS()                          
            self.add_pro.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!") 
    def find_project(self):     
        if self.dbopened:
            Ui_Find_Project.database=self.filename
            self.find_pro=Ui_Find_Project()                          
            self.find_pro.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!")    
    def find_protocol(self):
        if self.dbopened:            
            Ui_Find_Protocol.database=self.filename
            self.find_protocoldlg=Ui_Find_Protocol()                          
            self.find_protocoldlg.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!")
    def find_channel(self):
        if self.dbopened:
            Ui_Find_Chan.database=self.filename
            self.find_channeldlg=Ui_Find_Chan()                          
            self.find_channeldlg.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!") 
    def find_tags(self):
        if self.dbopened:
            Ui_Find_Tags.database=self.filename
            self.find_tagsdlg=Ui_Find_Tags()                          
            self.find_tagsdlg.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!")   
    def addprototags(self):
        if self.dbopened:
            Ui_Find_DevTags.database=self.filename
            self.pro_tagsdlg=Ui_Find_DevTags()                          
            self.pro_tagsdlg.exec_()
        else:
            QtGui.QMessageBox.information(None, "infomation", "database is not open!")             

class Ui_add_project(QtGui.QDialog):
    database=''
    def __init__(self, parent=None):  
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("add_project"))
        self.resize(483, 407)
        self.name = QtGui.QLineEdit(self)
        self.name.setGeometry(QtCore.QRect(180, 50, 201, 20))
        self.name.setObjectName(_fromUtf8("name"))    
#       枚举项目类型   
        self.comtype = QtGui.QComboBox(self)
        strlist=['collect','retransfer']   
        self.comtype.addItems(strlist)        
        self.comtype.setGeometry(QtCore.QRect(180, 90, 201, 22))
        self.comtype.setObjectName(_fromUtf8("type"))     
        self.beused = QtGui.QCheckBox(self)
        self.beused.setGeometry(QtCore.QRect(190, 160, 89, 16))
        self.beused.setObjectName(_fromUtf8("beused"))
        
        self.beprotocol = QtGui.QCheckBox(self)
        self.beprotocol.setGeometry(QtCore.QRect(190, 200, 110, 16))
        self.beprotocol.setObjectName(_fromUtf8("beprotocol"))
        
        self.bemessage = QtGui.QCheckBox(self)
        self.bemessage.setGeometry(QtCore.QRect(190, 240, 110, 16))
        self.bemessage.setObjectName(_fromUtf8("bemessage"))
        self.can = QtGui.QPushButton(self)
        self.can.setGeometry(QtCore.QRect(120, 330, 75, 23))
        self.can.setObjectName(_fromUtf8("can"))
        self.cancel = QtGui.QPushButton(self)
        self.cancel.setGeometry(QtCore.QRect(280, 330, 75, 23))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 80, 221))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)     
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)    
        QtCore.QObject.connect(self.can, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onOK)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
         
        self.setWindowTitle(_translate("add_project", "Add_Project", None))
        self.beused.setText(_translate("add_project", "used", None))
        self.beprotocol.setText(_translate("add_project", "save protocol", None))
        self.bemessage.setText(_translate("add_project", "save message", None))
        self.can.setText(_translate("add_project", "ok", None))
        self.cancel.setText(_translate("add_project", "cancel", None))
        self.label.setText(_translate("add_project", "Project Name", None))       
        self.label_2.setText(_translate("add_project", "Type", None))       
        self.label_4.setText(_translate("add_project", "Save Protocol", None))
        self.label_5.setText(_translate("add_project", "used", None))
        self.label_6.setText(_translate("add_project", "Save message", None))  
        QtCore.QMetaObject.connectSlotsByName(self)
    def onclose(self):
        self.close()
    def onOK(self):
        db=sqlite3.connect(self.database)            
        comtype=self.comtype.currentText()       
        bp=self.beprotocol.checkState()  
        bu=self.beused.checkState() 
        if bu==2:
            bu=1
        ncomType=1 
        if(comtype=='collect'):
            ncomType=1   
        elif(comtype=='retransfer'):
            ncomType=2  
        if bp==2:
            bp=1
        bm=self.bemessage.checkState()
        if bm==2:
            bm=1
        strname=self.name.text()      
       
        if not strname.strip():
            QtGui.QMessageBox.information(None,'Project Man','name is not NULL')
            return  
        try:
            cur = db.cursor()               
            cur.execute('insert into project(name,type,protolog,infolog,inuse)\
                values(\'%s\',%d,%d,%d,%d)'%(strname,ncomType,bp,bm,bu))
            db.commit()           
            QtGui.QMessageBox.information(None,'Project Man','add project sucessed!')
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))
        finally:
            db.close()   
            self.close()     

class Ui_add_chan(QtGui.QDialog):
    database=''
    def __init__(self, parent=None):  
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("add_chan"))
        self.resize(666, 383)
        self.ok = QtGui.QPushButton(self)
        self.ok.setGeometry(QtCore.QRect(140, 340, 75, 23))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.cancel = QtGui.QPushButton(self)
        self.cancel.setGeometry(QtCore.QRect(470, 340, 75, 23))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 50, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(60, 140, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(60, 170, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(60, 200, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(60, 230, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(370, 50, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(370, 80, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(370, 120, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(370, 150, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.Baud = QtGui.QLineEdit(self)
        self.Baud.setGeometry(QtCore.QRect(470, 50, 141, 20))
        self.Baud.setObjectName(_fromUtf8("Baud"))
        self.paritybit = QtGui.QLineEdit(self)
        self.paritybit.setGeometry(QtCore.QRect(470, 80, 141, 20))
        self.paritybit.setObjectName(_fromUtf8("paritybit"))
        self.stopbit = QtGui.QLineEdit(self)
        self.stopbit.setGeometry(QtCore.QRect(470, 110, 141, 20))
        self.stopbit.setObjectName(_fromUtf8("stopbit"))
        self.databit = QtGui.QLineEdit(self)
        self.databit.setGeometry(QtCore.QRect(470, 140, 141, 20))
        self.databit.setObjectName(_fromUtf8("databit"))
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(370, 190, 54, 12))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.readtimeout = QtGui.QLineEdit(self)
        self.readtimeout.setGeometry(QtCore.QRect(470, 180, 141, 20))
        self.readtimeout.setObjectName(_fromUtf8("readtimeout"))
        self.label_13 = QtGui.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(370, 220, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.status = QtGui.QLineEdit(self)
        self.status.setGeometry(QtCore.QRect(470, 220, 141, 20))
        self.status.setObjectName(_fromUtf8("status"))
        self.label_14 = QtGui.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(370, 260, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.isused = QtGui.QCheckBox(self)
        self.isused.setGeometry(QtCore.QRect(470, 260, 71, 16))
        self.isused.setObjectName(_fromUtf8("isused"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(70, 260, 54, 12))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 40, 135, 251))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ChanName = QtGui.QLineEdit(self.layoutWidget)
        self.ChanName.setObjectName(_fromUtf8("ChanName"))
        self.verticalLayout.addWidget(self.ChanName)
        self.ChanDesc = QtGui.QComboBox(self.layoutWidget)
        self.ChanDesc.setObjectName(_fromUtf8("ChanDesc"))
        typeList=['CHAN_RS232','CHAN_RS485','CHAN_UDP','CHAN_TCPCLI','CHAN_TCPSVR','CHAN_NULL']
        self.ChanDesc.addItems(typeList)
        self.verticalLayout.addWidget(self.ChanDesc)
        self.LocalIP = QtGui.QLineEdit(self.layoutWidget)
        self.LocalIP.setObjectName(_fromUtf8("LocalIP"))
        self.verticalLayout.addWidget(self.LocalIP)
        self.LocalPort = QtGui.QLineEdit(self.layoutWidget)
        self.LocalPort.setObjectName(_fromUtf8("LocalPort"))
        self.verticalLayout.addWidget(self.LocalPort)
        self.RemoteIp = QtGui.QLineEdit(self.layoutWidget)
        self.RemoteIp.setObjectName(_fromUtf8("RemoteIp"))
        self.verticalLayout.addWidget(self.RemoteIp)
        self.RemotePort = QtGui.QLineEdit(self.layoutWidget)
        self.RemotePort.setObjectName(_fromUtf8("RemotePort"))
        self.verticalLayout.addWidget(self.RemotePort)
        self.SerialPort = QtGui.QLineEdit(self.layoutWidget)
        self.SerialPort.setObjectName(_fromUtf8("SerialPort"))
        self.verticalLayout.addWidget(self.SerialPort)
        self.timer = QtGui.QLineEdit(self.layoutWidget)
        self.timer.setObjectName(_fromUtf8("timer"))
        self.verticalLayout.addWidget(self.timer)
        self.label_16 = QtGui.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(60, 300, 54, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(160, 300, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        db=sqlite3.connect(self.database)
#解决字段值为汉字
        db.text_factory=str               
        cur = db.cursor()       
        cursor = cur.execute('select name from project order by name')
        res = cursor.fetchall()
        for row in res:            
            self.comboBox.addItems(row)
        self.database=self.database

        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QObject.connect(self.ok, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onOk)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle(_translate("add_chan", "Dialog", None))
        self.ok.setText(_translate("add_chan", "Ok", None))
        self.cancel.setText(_translate("add_chan", "Cancel", None))
        self.label.setText(_translate("add_chan", "ChanName", None))
        self.label_2.setText(_translate("add_chan", "Type", None))
        self.label_3.setText(_translate("add_chan", "Local Ip", None))
        self.label_4.setText(_translate("add_chan", "Local Port", None))
        self.label_5.setText(_translate("add_chan", "Remote Ip", None))
        self.label_6.setText(_translate("add_chan", "RemotePort", None))
        self.label_7.setText(_translate("add_chan", "Serial Port", None))
        self.label_8.setText(_translate("add_chan", "Baud", None))
        self.label_9.setText(_translate("add_chan", "paritybit", None))
        self.label_10.setText(_translate("add_chan", "stopbit", None))
        self.label_11.setText(_translate("add_chan", "databit", None))
        self.label_12.setText(_translate("add_chan", "readtimeout", None))
        self.label_13.setText(_translate("add_chan", "status", None))
        self.label_14.setText(_translate("add_chan", "isused", None))
        self.isused.setText(_translate("add_chan", "isused", None))
        self.label_15.setText(_translate("add_chan", "timer", None))
        self.Baud.setText(_translate("add_chan", "9600", None))
        self.paritybit.setText(_translate("add_chan", "1", None))
        self.stopbit.setText(_translate("add_chan", "1", None))
        self.databit.setText(_translate("add_chan", "1", None))
        self.readtimeout.setText(_translate("add_chan", "1", None))
        self.LocalIP.setText(_translate("add_chan", "127.0.0.1", None))
        self.LocalPort.setText(_translate("add_chan", "502", None))
        self.SerialPort.setText(_translate("add_chan", "com1", None))
        self.timer.setText(_translate("add_chan", "1", None))
        self.RemotePort.setText(_translate("add_chan", "502", None))
        self.RemoteIp.setText(_translate("add_chan", "0", None))  
        self.status.setText(_translate("add_chan", "1", None))  
        self.label_16.setText(_translate("add_chan", "Project", None))
    def onclose(self):
        self.close()
    def onOk(self):
        try:
            db=sqlite3.connect(self.database) 
            strchanname=self.ChanName.text()
            if not strchanname.strip():
                QtGui.QMessageBox.information(None,'Project Man','name is not NULL!')
                return
            strdesc=self.ChanDesc.currentText()
            strlocalip=self.LocalIP.text()
            strlocalport=self.LocalPort.text()
            strrip=self.RemoteIp.text()
            strrport=self.RemotePort.text()
            strserport=self.SerialPort.text()
            strtimer=self.timer.text()
            strbaud=self.Baud.text()
            strstopbit=self.stopbit.text()
            strparitybit=self.paritybit.text()
            strdbbit=self.databit.text()
            strreadtimeout=self.readtimeout.text()
            strstatus=self.status.text()
            beused=self.isused.checkState()
            projname=self.comboBox.currentText()
            strWhere=(projname,);
            if beused==2:
                beused=1
            cur = db.cursor()
            cur.execute("select id from project where name=?",strWhere)
            res=cur.fetchone()
            if len(res)>0:
                projid=res[0]           
            cur.execute('insert into channel(name,type,ipaddr,port,ipaddrdest,portdest,com,baud,parity,stopbit,bytesize,timeout,state,inuse,period,projid)values(\'%s\',\'%s\',\'%s\',%d,\'%s\',%d,\'%s\',%d,%d,%d,%d,%d,%d,%d,%d,%d)'
                        %(strchanname,strdesc,strlocalip,int(strlocalport),strrip,int(strrport),strserport,int(strbaud),int(strparitybit),int(strstopbit),int(strdbbit),int(strreadtimeout),int(strstatus),int(beused),int(strtimer),int(projid)))
            db.commit()                
            cur.execute("select id from channel where name=?",(strchanname,))  
            res=cur.fetchone()
            if len(res)>0:
                chanid=res[0]    
            cur.execute("update project set chanid=? where id=?",(chanid,projid,))  
            db.commit()   
            QtGui.QMessageBox.information(None,'Project Man','add channel successed!')            
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))
        finally:
            db.close()
            self.close()

class Ui_add_pro(QtGui.QDialog):
    database='' 
    def __init__(self, parent=None):  
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("add_pro"))
        
        self.resize(630, 386)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(90, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.ProName = QtGui.QLineEdit(self)
        self.ProName.setGeometry(QtCore.QRect(180, 30, 211, 20))
        self.ProName.setObjectName(_fromUtf8("ProName"))
        self.ProDesc = QtGui.QLineEdit(self)
        self.ProDesc.setGeometry(QtCore.QRect(180, 70, 211, 20))
        self.ProDesc.setObjectName(_fromUtf8("ProDesc"))
        self.Config = QtGui.QLineEdit(self)
        self.Config.setGeometry(QtCore.QRect(180, 100, 431, 20))
        self.Config.setObjectName(_fromUtf8("Config"))
        self.DevAddr = QtGui.QLineEdit(self)
        self.DevAddr.setGeometry(QtCore.QRect(180, 130, 211, 20))
        self.DevAddr.setObjectName(_fromUtf8("DevAddr"))
        self.CanControl = QtGui.QCheckBox(self)
        self.CanControl.setGeometry(QtCore.QRect(180, 170, 71, 16))
        self.CanControl.setObjectName(_fromUtf8("CanControl"))
        self.Timer = QtGui.QLineEdit(self)
        self.Timer.setGeometry(QtCore.QRect(180, 190, 211, 20))
        self.Timer.setObjectName(_fromUtf8("Timer"))
        self.BeUsed = QtGui.QCheckBox(self)
        self.BeUsed.setGeometry(QtCore.QRect(180, 230, 71, 16))
        self.BeUsed.setObjectName(_fromUtf8("BeUsed"))
        self.CanReg = QtGui.QCheckBox(self)
        self.CanReg.setGeometry(QtCore.QRect(180, 260, 71, 16))
        self.CanReg.setObjectName(_fromUtf8("CanReg"))
        self.Status = QtGui.QLineEdit(self)
        self.Status.setGeometry(QtCore.QRect(180, 290, 71, 16))
        self.Status.setObjectName(_fromUtf8("Status"))
        
        self.tagsource = QtGui.QComboBox(self)
        self.tagsource.setGeometry(QtCore.QRect(350, 290, 90, 16))
        self.tagsource.setObjectName(_fromUtf8("tagsource"))
        self.tagsourcelabel = QtGui.QLabel(self)
        self.tagsourcelabel.setGeometry(QtCore.QRect(260, 290, 90, 16))
        self.tagsourcelabel.setObjectName(_fromUtf8("tagsource"))
        self.tagsourcelabel.setText(_translate("add_pro", "tagsource", None))
        
        self.chan = QtGui.QComboBox(self)
        self.chan.setGeometry(QtCore.QRect(530, 290, 90, 16))
        self.chan.setObjectName(_fromUtf8("chan"))
        self.chanlabel = QtGui.QLabel(self)
        self.chanlabel.setGeometry(QtCore.QRect(450, 290, 90, 16))
        self.chanlabel.setObjectName(_fromUtf8("chanlabel"))
        self.chanlabel.setText(_translate("add_pro", "chan", None))
        
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(90, 30, 68, 281))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 340, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onok)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle(_translate("add_pro", "add protocol", None))
        self.pushButton.setText(_translate("add_pro", "OK", None))
        self.CanControl.setText(_translate("add_pro", "YK", None))
        self.BeUsed.setText(_translate("add_pro", "isused", None))
        self.CanReg.setText(_translate("add_pro", "YT", None))
        self.Status.setText(_translate("add_pro", "1", None))
        self.label.setText(_translate("add_pro", "ProName", None))
        self.label_2.setText(_translate("add_pro", "ProLL", None))
        self.label_3.setText(_translate("add_pro", "Config", None))
        self.label_4.setText(_translate("add_pro", "deviceaddr", None))
        self.label_5.setText(_translate("add_pro", "YK", None))
        self.label_6.setText(_translate("add_pro", "timer", None))
        self.label_7.setText(_translate("add_pro", "isused", None))
        self.label_8.setText(_translate("add_pro", "YT", None))
        self.label_9.setText(_translate("add_pro", "state", None))
        self.pushButton_2.setText(_translate("add_pro", "Cancel", None))
        db=sqlite3.connect(self.database)               
        cur = db.cursor()       
        cursor = cur.execute('select distinct tagsource from tag order by tagsource')
        res = cursor.fetchall()
        for row in res:            
            self.tagsource.addItems(row)
        cursor = cur.execute('select name  from device order by name')
        res = cursor.fetchall()
        for row in res:            
            self.chan.addItems(row)
        db.close()
    def onclose(self):
        self.close()
    def onok(self):
        db=sqlite3.connect(self.database) 
        strProName=self.ProName.text()       
        strProDesc=self.ProDesc.text()
        strConfig=self.Config.text()
        strDevAddr=self.DevAddr.text()
        strTimer=self.Timer.text()
        bc=self.CanControl.checkState()
        tagsource=self.tagsource.currentText()
        if bc==2:
            bc=1
        bu=self.BeUsed.checkState()
        if bu==2:
            bu=1
        br=self.CanReg.checkState()
        if br==2:
            br=1
        state=self.Status.text()            
        if not strProName.strip():
            QtGui.QMessageBox.information(None,'Project Man','name is not NULL')
            return
        if not strProDesc.strip():
            strProDesc=''        
        if not strConfig.strip():
            strConfig=''    
        if not strTimer.strip():
            strTimer=0
        if not strDevAddr.strip():
            strDevAddr=0
        if not tagsource.strip():
            tagsource=''    
        channame=self.chan.currentText()
        cur=db.cursor()         
        curror=cur.execute('select id  from device where name=?',(channame,))
        res=curror.fetchone()
        chanid=0
        if res!=None:
            if len(res)>0:
                chanid=res[0]                    
        try:
            cur = db.cursor()   
            cur.execute('insert into device(name,chanid,protodll,protocfg,isyk,addr,period,inuse,commstate,tagsource,isyt)\
                values(\'%s\',%d,\'%s\',\'%s\',%d,%d,%d,%d,%d,\'%s\',%d)'
                %(strProName,chanid,strProDesc,strConfig,int(bc),int(strDevAddr),int(strTimer),int(bu),int(state),tagsource,int(br)))
            db.commit()
            QtGui.QMessageBox.information(None,'Project Man','add protocol sucessed!')
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))            
        finally:
            db.close()   
            self.close()  

class Ui_Find_Project(QtGui.QDialog):
    database=''  
    def __init__(self, parent=None):  
        QtGui.QDialog.__init__(self, parent) 
        self.setObjectName(_fromUtf8("Find_Pro"))
        self.resize(920, 579)
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 900, 491))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()        
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)            
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(120, 530, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 530, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 530, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.delete)   
        QtCore.QMetaObject.connectSlotsByName(self)     

        self.setWindowTitle(_translate("Find_Pro", "Find_Pro", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Find_Pro", "projectid", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Find_Pro", "name", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Find_Pro", "type", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Find_Pro", "chanid", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Find_Pro", "inuse", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Find_Pro", "protolog", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Find_Pro", "infolog", None))       
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Find_Pro", "selected", None))
        self.pushButton.setText(_translate("Find_Pro", "保存", None))
        self.pushButton_2.setText(_translate("Find_Pro", "取消", None))
        self.pushButton_3.setText(_translate("Find_Pro", "删除", None))
        try:
            db=sqlite3.connect(self.database)
            cur = db.cursor() 
            rescom=cur.execute('select name,id from channel')
            rescom=cur.fetchall()                    
            res=cur.execute('select id,name,type,chanid,inuse,protolog,infolog from project order by id')
            res = cur.fetchall()      
            i=0      
            strlist=['collect','retransfer'] 
            if len(res)>0:           
                self.tableWidget.setRowCount(len(res))
                for row in res:                    
                    for j in range(self.tableWidget.columnCount()-1):
                        if(j==3):
                            chanindex=-1
                            index=0
                            abc=QtGui.QComboBox()
                            namelist=list()
                            ilist=list()                           
                            for k in rescom:              
                                namelist.append(k[0])
                                ilist.append(k[1])
                                if(row[j]!=None):
                                    if(k[1]==int(row[j])):
                                        chanindex=index                                         
                                index=index+1
                            abc.addItems(namelist)    
                            abc.setCurrentIndex(chanindex)
#                            abc.setCurrentIndex()              
                            self.tableWidget.setCellWidget(i,j+1,abc)                        
                        elif(j==2):                             
                            abc=QtGui.QComboBox()                            
                            abc.addItems(strlist)
                            if(row[j]==1):
                                abc.setCurrentText(strlist[0])
                            else:
                                abc.setCurrentText(strlist[1])                                                         
                            self.tableWidget.setCellWidget(i,j+1,abc)
                        else:
                            newItem = QtGui.QTableWidgetItem(str(row[j]))                             
                            if(j==1)or(j==0):
                                newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)                           
                            self.tableWidget.setItem(i,j+1,newItem)  
                    newItem = QtGui.QTableWidgetItem()
                    newItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(i,0,newItem)
                    i=i+1  
                                               
        except Exception as e:
            QtGui.QMessageBox.information(None, 'error', str(e)) 
        finally:
            db.close()
    def onclose(self):
        self.close()
    def delete(self):
        reply = QtGui.QMessageBox.question(self, "question",'are you sure delete the selected records?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
        if reply == QtGui.QMessageBox.No:
            return
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):                    
                    projectid=int(self.tableWidget.item(i, 1).text())                    
                    self.cur.execute('delete from project where id=%d'%(projectid))
                    db.commit()  
            QtGui.QMessageBox.information(None,'Project Man','delete projects sucessed!')         
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))
        finally:
            db.close()  
            self.close()
    def save(self):
        rowcount=self.tableWidget.rowCount()
        try:
            chanid=0            
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):
                    if( self.tableWidget.cellWidget(i, 4).currentText().strip()):
                        rescom=self.cur.execute('select id from channel where name=\'%s\''%self.tableWidget.cellWidget(i, 4).currentText())
                        rescom=self.cur.fetchone()
                        chanid=int(rescom[0])  

                    projectid=int(self.tableWidget.item(i, 1).text())                    
                    strtype=self.tableWidget.cellWidget(i, 3).currentText()
                    if(strtype=='collect'):
                        ncomType=1   
                    elif(strtype=='retransfer'):
                        ncomType=2 
                    bs=int(self.tableWidget.item(i, 5).text())
                    bm=int(self.tableWidget.item(i, 6).text())
                    bu=int(self.tableWidget.item(i, 7).text())
                    self.cur.execute('update project set type=%d,inuse=%d,protolog=%d,infolog=%d,chanid=%d where id=%d'%(ncomType,bs,bm,bu,chanid,projectid))
                    db.commit()  
                    self.cur.execute('update channel set projid=? where id=?',(projectid,chanid,))
                    db.commit()  
            QtGui.QMessageBox.information(self,'project man','save records success!' )         
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))
        finally:
            db.close()  
            self.close()    

class Ui_Find_Protocol(QtGui.QDialog):
    database=''   
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setObjectName(_fromUtf8("Find_Protocol"))
        self.resize(902, 522)
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 871, 441))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(90, 480, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 480, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.delete)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle(_translate("Find_Protocol", "Find_Protocol", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Find_Protocol", "protoid", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Find_Protocol", "proNmae", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Find_Protocol", "chanid", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Find_Protocol", "protodll", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Find_Protocol", "protocfg", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Find_Protocol", "addr", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Find_Protocol", "YK", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Find_Protocol", "YT", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Find_Protocol", "period", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Find_Protocol", "commstate", None))        
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Find_Protocol", "inuse", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Find_Protocol", "tagsource", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Find_Protocol", "select", None))
        self.pushButton.setText(_translate("Find_Protocol", "Save", None))
        self.pushButton_2.setText(_translate("Find_Protocol", "Delete", None))
        self.pushButton_3.setText(_translate("Find_Protocol", "Cancel", None))  
           
        try:
            db=sqlite3.connect(self.database)            
            cur = db.cursor()                
            res=cur.execute('select id,name,chanid,protodll,protocfg,addr,isyk,isyt,period,commstate,inuse,tagsource from device order by id')
            res = cur.fetchall()            
            tagsource=cur.execute('select distinct tagsource from tag')
            tagsource=cur.fetchall()    
            i=0 
            if len(res)>0: 
                self.tableWidget.setRowCount(len(res))
                for row in res:     
                    for j in range(self.tableWidget.columnCount()-1): 
                        if(j==11):
                            combox=QtGui.QComboBox()
                            for tagsoutcerow in tagsource:#                                
                                combox.addItems(tagsoutcerow)                              
                            combox.setCurrentText(str(row[j]))                                                   
                            self.tableWidget.setCellWidget(i,j+1,combox)
                        elif(j==2):
                            combox=QtGui.QComboBox()
                            cur1=db.cursor()
                            cur2=db.cursor()
                            cur1.execute('select name from channel order by name')
                            cur2.execute('select name from channel where id=?',(row[j],))
                            allchannel=cur1.fetchall()
                            onechannel=cur2.fetchone()
                            if allchannel!=None:
                                if len(allchannel)>0:
                                    for names in allchannel:
                                        combox.addItems(names) 
                            if onechannel!=None:
                                combox.setCurrentText(str(onechannel[0]))
                            else:
                                combox.setCurrentText(str(row[j]))                                                   
                            self.tableWidget.setCellWidget(i,j+1,combox)
                        else: 
                            newItem = QtGui.QTableWidgetItem(str(row[j]) )                        
                            if(j==0):
                                newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                            if(j==1):
                                newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)                       
                            self.tableWidget.setItem(i,j+1,newItem)
                    newItem = QtGui.QTableWidgetItem() 
                    newItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(i,0,newItem)       
                    i=i+1                                 
        except Exception as e:
            QtGui.QMessageBox.information(None, 'error', str(e)) 
        finally:
            db.close()
    def onclose(self):
        self.close()
    def save(self):
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):                               
                    id=int(self.tableWidget.item(i, 1).text())                   
                    channame=self.tableWidget.cellWidget(i, 3).currentText()
                    chanid=0
                    cur1=db.cursor()
                    cur1.execute('select id from channel where name=?',(channame,))
                    idrow=cur1.fetchone()
                    if idrow!=None:
                        chanid=idrow[0]
                    protodll=self.tableWidget.item(i, 4).text()
                    protocfg=self.tableWidget.item(i, 5).text()
                    addr=int(self.tableWidget.item(i, 6).text())
                    isyk=int(self.tableWidget.item(i, 7).text())
                    isyt=int(self.tableWidget.item(i, 8).text())
                    period=int(self.tableWidget.item(i, 9).text())
                    commstate=int(self.tableWidget.item(i, 10).text())
                    inuse=int(self.tableWidget.item(i, 11).text())
                    tagsource=self.tableWidget.cellWidget(i, 12).currentText()
                    sql='update device set protodll=\'%s\',protocfg=\'%s\',chanid=%d,addr=%d,isyk=%d,isyt=%d,period=%d,commstate=%d,inuse=%d ,tagsource=\'%s\' where id=%d'%(protodll,protocfg,chanid,addr,isyk,isyt,period,commstate,inuse,tagsource,id)
                    print(sql)
                    self.cur.execute(sql)                    
                    db.commit()  
            QtGui.QMessageBox.information(self,'project man','save records success!' )         
        except Exception as e:
            QtGui.QMessageBox.information(self,'project man',str(e) )
        finally:
            db.close()  
            self.close()
    def delete(self):
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):                               
                    proid=int(self.tableWidget.item(i, 1).text()) 
                    sql='delete from protocol where proid=%d'%(proid)
                    self.cur.execute(sql)                  
            db.commit()  
            QtGui.QMessageBox.information(self,'project man','delete records success!' )         
        except Exception as e:
            print(str(e))
        finally:
            db.close()  
            self.close()
  
class Ui_Find_Chan(QtGui.QDialog):
    database=''   
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("Find_Chan"))
        self.resize(913, 579)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 530, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 530, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 530, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 891, 491))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)  
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)         
        try:
            db=sqlite3.connect(self.database)          
            cur = db.cursor() 
            strsql='select id,name,type,projid,ipaddr,port,ipaddrdest,portdest,com,baud,parity,stopbit,bytesize,timeout,state,inuse,period from channel order by id'                    
            res=cur.execute(strsql)
            res = cur.fetchall()             
            i=0 
            if len(res)>0:    
                self.tableWidget.setRowCount(len(res))
                for row in res:                    
                    for j in range(self.tableWidget.columnCount()-1):  
                        if(j==2):
                            newItem = QtGui.QComboBox()
                            typeid=row[j]                            
                            typeList=['CHAN_RS232','CHAN_RS485','CHAN_UDP','CHAN_TCPCLI','CHAN_TCPSVR','CHAN_NULL']
                            newItem.addItems(typeList)                            
                            newItem.setCurrentText(typeList[typeid-1])
                            self.tableWidget.setCellWidget(i,j+1,newItem)  
                        elif (j==3):
                            newItem = QtGui.QComboBox()
                            cur1 = db.cursor() 
                            cur2 = db.cursor()
                            prores=cur1.execute("select name from project where id=%d"%row[j])
                            prores=cur1.fetchone()
                            pronames=cur2.execute("select name from project ")
                            pronames=cur2.fetchall()
                            if len(pronames)>0:
                                for rows in pronames:
                                    newItem.addItems(rows)
                            newItem.setCurrentText(prores[0]) 
                            self.tableWidget.setCellWidget(i,j+1,newItem)                          
                        else:  
                            newItem = QtGui.QTableWidgetItem(str(row[j]))    
                            if(j==0 or j==1):
                                newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)                             
                            self.tableWidget.setItem(i,j+1,newItem)
                    newItem = QtGui.QTableWidgetItem() 
                    newItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(i,0,newItem)       
                    i=i+1                                 
        except Exception as e:
            QtGui.QMessageBox.information(None, 'error', str(e)) 
        finally:
            db.close()
     
        self.setWindowTitle(_translate("Find_Chan", "Find_Chan", None))
        self.pushButton.setText(_translate("Find_Chan", "Save", None))
        self.pushButton_2.setText(_translate("Find_Chan", "Delete", None))
        self.pushButton_3.setText(_translate("Find_Chan", "Cancel", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Find_Chan", "chanid", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Find_Chan", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Find_Chan", "type", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Find_Chan", "projid", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Find_Chan", "ipaddr", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Find_Chan", "port", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Find_Chan", "ipaddrdest", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Find_Chan", "portdest", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Find_Chan", "com", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Find_Chan", "baud", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Find_Chan", "parity", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Find_Chan", "stopbit", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Find_Chan", "bytesize", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Find_Chan", "timeout", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Find_Chan", "state", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Find_Chan", "inuse", None))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Find_Chan", "period", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Find_Chan", "select", None))        
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.delete)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QMetaObject.connectSlotsByName(self)
    def onclose(self):
        self.close()
    def save(self):
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)             
            self.cur = db.cursor()
            for i in range(rowcount):                
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):                               
                    chanid=int(self.tableWidget.item(i, 1).text())                   
                    type=self.tableWidget.cellWidget(i,3).currentText()
#typeList=['CHAN_RS232','CHAN_RS485','CHAN_UDP','CHAN_TCPCLI','CHAN_TCPSVR','CHAN_NULL']
                    if(type=='CHAN_RS232'):
                        typeid=1
                    elif(type=='CHAN_RS485'):
                        typeid=2
                    elif(type=='CHAN_UDP'):
                        typeid=3
                    elif(type=='CHAN_TCPCLI'):
                        typeid=4
                    elif(type=='CHAN_TCPSVR'):
                        typeid=5
                    elif(type=='CHAN_NULL'):
                        typeid=6
                    proname=self.tableWidget.cellWidget(i,4).currentText()
                    cur=db.cursor()
                    cur.execute("select id from project where name=?",(proname,))
                    prores=cur.fetchone()
                    proid=prores[0]
                    ipaddr=self.tableWidget.item(i, 5).text()
                    port=int(self.tableWidget.item(i, 6).text())
                    ipaddrdest=self.tableWidget.item(i, 7).text()
                    portdest=int(self.tableWidget.item(i, 8).text())
                    com=self.tableWidget.item(i, 9).text()
                    baud=int(self.tableWidget.item(i, 10).text())
                    parity=int(self.tableWidget.item(i,11).text())
                    stopbit=int(self.tableWidget.item(i, 12).text())
                    bytesize=int(self.tableWidget.item(i,13).text())
                    timeout=int(self.tableWidget.item(i, 14).text())
                    state=int(self.tableWidget.item(i, 15).text())
                    inuse=int(self.tableWidget.item(i, 16).text())
                    period=int(self.tableWidget.item(i, 17).text())
                    sql='update channel set type=%d,projid=%d,ipaddr=\'%s\',port=%d,ipaddrdest=\'%s\',portdest=%d,\
                    com=\'%s\',baud=%d,parity=%d,stopbit=%d ,\
                    bytesize=%d ,timeout=%d ,state=%d ,inuse=%d,period=%d  where id=%d'\
                    %(typeid,proid,ipaddr,port,ipaddrdest,portdest,com,baud,parity,stopbit,\
                      bytesize,timeout,state,inuse,period,chanid)
                    print(sql)                  
                    self.cur.execute(sql) 
                    cur.execute('update project set chanid=? where id=?',(chanid,proid,))                   
                    db.commit()  
            QtGui.QMessageBox.information(self,'project man','save records success!' )         
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))
        finally:
            db.close()  
            self.close()
    def delete(self):
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):                               
                    chanid=int(self.tableWidget.item(i, 1).text()) 
                    sql='delete from channel where id=%d'%(chanid)
                    self.cur.execute(sql)                  
            db.commit()  
            QtGui.QMessageBox.information(self,'project man','delete records success!' )         
        except Exception as e:
            QtGui.QMessageBox.information(None,'Project Man',str(e))
        finally:
            db.close()  
            self.close()
 
class Ui_ADD_TAGS(QtGui.QDialog):
    database=''
    def __init__(self, parent=None):  
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1500, 632)
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 1450, 541))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        
#        item = QtGui.QTableWidgetItem()
#        self.tableWidget.setHorizontalHeaderItem(35, item)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(170, 580, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 580, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 580, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))  
#        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy)
             
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addtag)  
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)  
#        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested()")), self.save)

        self.setWindowTitle(_translate("Dialog", "Add tags", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "datatype", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "isAlarm", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "statypeid", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "isCalc", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "calc", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "hLimit", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "hhLimit", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "lLimit", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "llLimit", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "timeout", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "unit", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "isArc", None))
#        item = self.tableWidget.horizontalHeaderItem(13)
#        item.setText(_translate("Dialog", "expand2", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "arcInter", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "arcType", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Dialog", "cmpDev", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Dialog", "tagsource", None))        
        
        self.pushButton.setText(_translate("Dialog", "Add", None))
        self.pushButton_2.setText(_translate("Dialog", "Save", None))
        self.pushButton_3.setText(_translate("Dialog", "Cancel", None))
        
        QtCore.QMetaObject.connectSlotsByName(self)          
#        if(self.tableWidget.rowCount()<1):
#            self.tableWidget.setRowCount(1)
    def onclose(self):
        self.close()
    def addtag(self):
        db=sqlite3.connect(self.database)
        cur=db.cursor()
        cur.execute('select distinct tagsource from tag order by name')
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        i=self.tableWidget.rowCount()  
        newItem = QtGui.QComboBox()
        tagsourcenames=cur.fetchall()
        
        if tagsourcenames!=None:
            if len(tagsourcenames)>0:
                for rows in tagsourcenames:
                    newItem.addItems(rows) 
        self.tableWidget.setCellWidget(i-1,16,newItem) 
        tadtypelist=['digital','analog']
        newItem = QtGui.QComboBox()
        newItem.addItems(tadtypelist)  
        self.tableWidget.setCellWidget(i-1,1,newItem) 
        
        newItem=QtGui.QCheckBox(self)
        self.tableWidget.setCellWidget(i-1,2,newItem)
        newItem.setText(_translate("add_pro", "isAlarm", None))
        
        newItem=QtGui.QCheckBox(self)
        self.tableWidget.setCellWidget(i-1,4,newItem)
        newItem.setText(_translate("add_pro", "isCalc", None))
        
        newItem=QtGui.QCheckBox(self)
        self.tableWidget.setCellWidget(i-1,12,newItem)
        newItem.setText(_translate("add_pro", "isArc", None))
        
        db.close()             
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()   
    def save(self):
        try:
            db=sqlite3.connect(self.database)
            rowcount=self.tableWidget.rowCount()
            record=dict()              
            for row in range(rowcount):
                strsql="insert into tag (name"
                record.clear()
                itemobj=self.tableWidget.item(row,0)#第一列不应该为空
                if itemobj!=None:
                    strvalue="values(\'%s\'"%itemobj.text()
                    print(self.tableWidget.columnCount())
                    for col in range(1,self.tableWidget.columnCount()):
                        if(col==16):
                            strname=self.tableWidget.cellWidget(row, 16).currentText()
                           
                        elif (col==1):
                            strname=self.tableWidget.cellWidget(row, 1).currentText()
                            if(strname=='digital'):
                                strname='1'
                            else:
                                strname='2'
                        elif (col==2):
                            if(self.tableWidget.cellWidget(row, 2).checkState() == QtCore.Qt.Checked):
                                strname='1'
                            else:
                                strname='0'
                        elif (col==4):
                            if(self.tableWidget.cellWidget(row, 4).checkState() == QtCore.Qt.Checked):
                                strname='1'
                            else:
                                strname='0'
                        elif (col==12):
                            if(self.tableWidget.cellWidget(row, 12).checkState() == QtCore.Qt.Checked):
                                strname='1'
                            else:
                                strname='0'
                        else:          
                            itemcolobj=self.tableWidget.item(row,col)                      
                            if itemcolobj!=None:
                                strname=itemcolobj.text()                                
                        strtitle=self.tableWidget.horizontalHeaderItem(col).text()                                      
                        record[str(strtitle)]=strname  
                    for k in record:                    
                        colname=",%s"%k
                        strsql+=colname
                        strvalue+=",\'%s\'"%record[k]
                    strsql+=")"+strvalue+")"
                    print(strsql)
                    cur=db.cursor()
                    cur.execute(strsql)
                    db.commit()     
            QtGui.QMessageBox.information(self,'project man','add tags successed!')
        except Exception as e:
            QtGui.QMessageBox.information(self,'project man',str(e))
        finally:
            db.close()
            
            self.close()

class Ui_Find_Tags(QtGui.QDialog):
    database=''
    def __init__(self, parent=None):  
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1190, 707)
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 1161, 621))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
#        item = QtGui.QTableWidgetItem()
#        self.tableWidget.setHorizontalHeaderItem(35, item)
        
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "datatype", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "isAlarm", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "statypeid", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "isCalc", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "calc", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "hLimit", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "hhLimit", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "lLimit", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "llLimit", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "timeout", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "unit", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "isArc", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "arcInter", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Dialog", "arcType", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Dialog", "cmpDev", None))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Dialog", "tagsource", None))  
                
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "select", None)) 
        
        
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 20, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(740, 20, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(650, 30, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))        
        QtCore.QMetaObject.connectSlotsByName(self)
   
        self.setWindowTitle(_translate("Dialog", "Find Tags", None))
        self.pushButton.setText(_translate("Dialog", "Save", None))
        self.pushButton_2.setText(_translate("Dialog", "Delete", None))
        self.pushButton_3.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_4.setText(_translate("Dialog", "Find", None))
        self.label.setText(_translate("Dialog", "TagSource", None))
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onclose)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)  
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.delete) 
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.findtags)
        
        db=sqlite3.connect(self.database)               
        cur = db.cursor()       
        cursor = cur.execute('select distinct tagsource from tag order by tagsource')
        res = cursor.fetchall()
        for row in res:            
            self.comboBox.addItems(row)
        db.close() 
        
    def delete(self):
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):                               
                    tagname=self.tableWidget.item(i, 1).text() 
                   
                    sql='delete from tag where name=\'%s\''%(tagname)                                     
                    self.cur.execute(sql)                  
            db.commit()  
            QtGui.QMessageBox.information(self,'project man','delete records success!' )         
        except Exception as e:
            QtGui.QMessageBox.information(self,'project man',str(e))
        finally:
            db.close()  
            self.close()
    def save(self):
        try:
            db=sqlite3.connect(self.database)
            rowcount=self.tableWidget.rowCount()
            record=dict()
            writedot=False                         
            for row in range(rowcount):
                writedot=False 
                strsql="update tag set "
                strend=" where name=\'%s\'"%self.tableWidget.item(row,1).text() 
                record.clear()                
                if self.tableWidget.item(row,0).checkState()==QtCore.Qt.Checked:
                    for col in range(1,self.tableWidget.columnCount()):
                        if(col==17):
                            strname=self.tableWidget.cellWidget(row,col).currentText()
                        else:
                            itemcolobj=self.tableWidget.item(row,col)                
                            if itemcolobj!=None:                            
                                strname=itemcolobj.text()
                        strtitle=self.tableWidget.horizontalHeaderItem(col).text() 
                        if strname.strip(): 
                            record[str(strtitle)]=strname 
                        else:
                            record[str(strtitle)]='0'                                 
                    for k in record:                    
                        colname="%s=\'%s\'"%(k,record[k]) 
                        if writedot==False:
                            strsql+=''+colname
                            writedot=True
                        else:
                            strsql+=','+colname
                    strsql+=strend 
                    print(strsql)
                    cur=db.cursor()
                    cur.execute(strsql)
                    db.commit()     
            QtGui.QMessageBox.information(self,'project man','svae tags successed!')
        except Exception as e:
            QtGui.QMessageBox.information(self,'project man',str(e))                       
        finally:
            db.close()            
            self.close()
    def onclose(self):
        self.close()
    def findtags(self):
        self.tableWidget.setRowCount(0)
        strsource=self.comboBox.currentText()        
        strsql="select name,datatype,isAlarm,statypeid,isCalc,calc,hLimit,hhLimit,lLimit,llLimit,timeout,unit,isArc,arcInter,arcType,cmpDev,tagsource from tag where tagsource=\'%s\'"%strsource      
        db=sqlite3.connect(self.database)               
        cur = db.cursor()    
        cur1 = db.cursor()     
        cursor = cur.execute(strsql)
        cur1.execute('select distinct tagsource from tag order by name')
        tagsourcenames=cur1.fetchall()   
        res = cursor.fetchall()
        rowcount=len(res)
        index=0
        if(rowcount>0):
            self.tableWidget.setRowCount(rowcount)
            for row in res:
                for j in range(1,self.tableWidget.columnCount()-1):
                    if row[j-1]==None:
                        newItem = QtGui.QTableWidgetItem('' )
                    else:
                        newItem = QtGui.QTableWidgetItem(str(row[j-1]) )                                                
                    if(j==0):
                        newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)  
                    elif(j==16):
                        newItem=QtGui.QComboBox()        
                        if tagsourcenames!=None:
                            if len(tagsourcenames)>0:
                                for rows in tagsourcenames:
                                    newItem.addItems(rows) 
                        newItem.setCurrentText(str(row[16]))
                        self.tableWidget.setCellWidget(index,17,newItem) 
                    else:                                    
                        self.tableWidget.setItem(index,j,newItem) 
                newItem = QtGui.QTableWidgetItem() 
                newItem.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(index,0,newItem)     
                index+=1       
        db.close()

class Ui_Find_DevTags(QtGui.QDialog):
    database=''      
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1388, 678)        
        
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1371, 571))
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()        
        self.tableWidget.setHorizontalHeaderItem(14, item)
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(30, 30, 331, 50))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.combchan = QtGui.QComboBox(self.widget)
        self.combchan.setObjectName(_fromUtf8("combchan"))
        self.gridLayout.addWidget(self.combchan, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.combotype = QtGui.QComboBox(self.widget)
        self.combotype.setObjectName(_fromUtf8("combotype"))
        self.gridLayout.addWidget(self.combotype, 0, 3, 1, 1)
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setGeometry(QtCore.QRect(390, 30, 450, 50))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_find = QtGui.QPushButton(self.widget1)
        self.pushButton_find.setObjectName(_fromUtf8("pushButton_find"))
        self.horizontalLayout.addWidget(self.pushButton_find)
        self.pushButton_save = QtGui.QPushButton(self.widget1)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_add = QtGui.QPushButton(self.widget1)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButto_del = QtGui.QPushButton(self.widget1)
        self.pushButto_del.setObjectName(_fromUtf8("pushButto_del"))
        self.horizontalLayout.addWidget(self.pushButto_del)
        
        self.pushButton_cancel = QtGui.QPushButton(self.widget1)
#       self.pushButton_cancel.setGeometry(QtCore.QRect(720, 30, 71, 50))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        
        QtCore.QObject.connect(self.pushButto_del, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deltag)
        QtCore.QObject.connect(self.pushButton_save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancel)
        QtCore.QObject.connect(self.pushButton_find, QtCore.SIGNAL(_fromUtf8("clicked()")), self.findtag)
        QtCore.QObject.connect(self.pushButton_add, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add)
        QtCore.QMetaObject.connectSlotsByName(self)
    
        self.setWindowTitle(_translate("Dialog", "Dialog", None))
#        self.pushButton_cancel.setText(_translate("Dialog", "cancel", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "id", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "tagname", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "type", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "offset", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "reverse", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "coef", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "limit", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "addr", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "func", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "expint1", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "expint2", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "expflt1", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "expflt2", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "expstr", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "selected", None))
        self.label.setText(_translate("Dialog", "channel", None))
        self.label_2.setText(_translate("Dialog", "type", None))
        self.pushButton_find.setText(_translate("Dialog", "find", None))
        self.pushButton_save.setText(_translate("Dialog", "save", None))
        self.pushButton_add.setText(_translate("Dialog", "add", None))
        self.pushButto_del.setText(_translate("Dialog", "del", None))
        self.pushButton_cancel.setText(_translate("Dialog", "cancel", None))
        typelist=['YX','YC','YT','YK']
        self.combotype.addItems(typelist) 
        db=sqlite3.connect(self.database)    
        cur=db.cursor(); 
        cur.execute('select name from device order by name')
        rows=cur.fetchall()
        if(rows!=None):
            for row in rows:
                self.combchan.addItems(row)
        db.close()
    def deltag(self):
        rowcount=self.tableWidget.rowCount()
        try:           
            db=sqlite3.connect(self.database)
            self.cur = db.cursor()
            for i in range(rowcount):   
                if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked): 
                    if (self.tableWidget.item(i, 1).text()!=None and int(self.tableWidget.item(i, 1).text())>0):                        
                        id=int(self.tableWidget.item(i, 1).text())                                       
                        sql='delete from devtag where id=%d'%(id)                                                  
                        self.cur.execute(sql)
            db.commit()  
             
            QtGui.QMessageBox.information(self,'project man','delete records success!' )         
        except Exception as e:
            QtGui.QMessageBox.information(self,'project man',str(e))
        finally:
            db.close()  
            self.close()  
    def save(self):
        devicename=self.combchan.currentText()
        db=sqlite3.connect(self.database)    
        cur=db.cursor(); 
        cur.execute('select id from device where name=?',(devicename,))
        devid=0
        id=0
        typeid=1     
        typename=self.combotype.currentText()
        if(typename=='YX'):
            typeid=1
        elif(typename=='YC'):
            typeid=2
        elif(typename=='YK'):
            typeid=3
        elif(typename=='YT'):
            typeid=4
        row=cur.fetchone()
        if(row!=None):
            devid=row[0]
        try:    
            rowcount=self.tableWidget.rowCount()                        
            for row in range(rowcount): 
                recordcols=[]            
                if(self.tableWidget.item(row,0).checkState() == QtCore.Qt.Checked):
                    itemobj=self.tableWidget.item(row,1)#第一列不应该为空
                    value=itemobj.text()
                    if (itemobj.text()!=None and int(value)>0):
                        recordcols=[]   
                        strsql="update devtag set offset=?,reverse=?,coef=?,llimit=?,addr=?,func=?,expint1=?,expint2=?,expflt1=?,expflt2=?,expstr=? where id=?"
                        id=itemobj.text()
                        for col in range(4,self.tableWidget.columnCount()):                                  
                            itemcolobj=self.tableWidget.item(row,col)                      
                            if itemcolobj!=None:
                                recordcols.append(itemcolobj.text())
                        recordcols.append(id)                       
                    else:
                        recordcols=[]
                        strsql="insert into devtag(tagid,type,protoid,offset,reverse,coef,llimit,addr,func,expint1,expint2,expflt1,expflt2,expstr) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"                  
                        tagname=self.tableWidget.item(row,2).text()
                        curtagid=db.cursor(); 
                        curtagid.execute('select id from tag where name=\'%s\''%tagname) 
                        rowtagid=curtagid.fetchone()
                        if(rowtagid!=None):
                            tagid=rowtagid[0]
                        recordcols.append(tagid) 
                        recordcols.append(typeid) 
                        recordcols.append(devid)                    
                        for col in range(4,self.tableWidget.columnCount()):                                  
                            itemcolobj=self.tableWidget.item(row,col)                      
                            if itemcolobj!=None:
                                recordcols.append(itemcolobj.text())
                    cur.execute(strsql,recordcols)
                    db.commit()     
            QtGui.QMessageBox.information(self,'project man','save devtags successed!')
        except Exception as e:
            QtGui.QMessageBox.information(self,'project man',str(e))
        finally:
            db.close()
            
            self.close()            
       
    def cancel(self):
        self.close() 
    def add(self): 
        typeid=1     
        typename=self.combotype.currentText()
        if(typename=='YX'):
            typeid=1
        elif(typename=='YC'):
            typeid=2
        elif(typename=='YK'):
            typeid=3
        elif(typename=='YT'):
            typeid=4       
        Ui_Find_AllTags.database=self.database   
        self.uiAdd=Ui_Find_AllTags()                                      
        self.uiAdd.exec_()    
        rowcount=self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowcount+len(tagslist))        
        for tagname in tagslist: 
            for j in range(self.tableWidget.columnCount()):
                    if(j==3):
                        newItem = QtGui.QTableWidgetItem(str(typeid))
                    else:
                        newItem = QtGui.QTableWidgetItem('0')                         
                    if(j==1  or j==3):
                        newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                    elif(j==2):                            
                        newItem = QtGui.QTableWidgetItem(tagname)
                        newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(rowcount,j,newItem)  
                    newItem = QtGui.QTableWidgetItem('') 
                    newItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(rowcount,0,newItem) 
            rowcount+=1                
    def findtag(self):
        self.tableWidget.setRowCount(0)
        typeid=1     
        typename=self.combotype.currentText()
        if(typename=='YX'):
            typeid=1
        elif(typename=='YC'):
            typeid=2
        elif(typename=='YK'):
            typeid=3
        elif(typename=='YT'):
            typeid=4
        devicename=self.combchan.currentText()
        db=sqlite3.connect(self.database)    
        cur=db.cursor(); 
        cur.execute('select id from device where name=?',(devicename,))
        devid=0
        row=cur.fetchone()
        if(row!=None):
            devid=row[0]
        sql='select id,tagid,type,offset,reverse,coef,llimit,addr,func,expint1,expint2,expflt1,expflt2,expstr from devtag where type=%d and protoid=%d'%(typeid,devid)
        print(sql)
        cur.execute(sql)
        i=0
        res=cur.fetchall()
        if(res!=None):
            if len(res)>0: 
                self.tableWidget.setRowCount(len(res))
                for row in res:     
                    for j in range(self.tableWidget.columnCount()-1): 
                        if row[j-1]==None:
                            newItem = QtGui.QTableWidgetItem('' )
                        else:
                            newItem = QtGui.QTableWidgetItem(str(row[j]) ) 
                        
                        if(j==0 or j==2):
                            newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                        elif(j==1):                            
                            curname=db.cursor()
                            curname.execute('select name from tag where id=?',(row[j],))
                            res=curname.fetchone()
                            if(res!=None):
                                newItem = QtGui.QTableWidgetItem(res[0] )
                                newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                        self.tableWidget.setItem(i,j+1,newItem)  
                    newItem = QtGui.QTableWidgetItem() 
                    newItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(i,0,newItem) 
                    i=i+1
        db.close()
        return 

class Ui_Find_AllTags(QtGui.QDialog):
    database='' 
    def  unselect(self):
        rowcount=self.tableWidget.rowCount()
        for i in range(rowcount):
            if(self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked):
                self.tableWidget.item(i,0).setCheckState(QtCore.Qt.Unchecked)  
    def select(self):
        rowcount=self.tableWidget.rowCount()
        for i in range(rowcount):
            if(self.tableWidget.item(i, 0).checkState() != QtCore.Qt.Checked):
                self.tableWidget.item(i,0).setCheckState(QtCore.Qt.Checked)  
    def ok(self):  
        global  tagslist
        tagslist=[]
        rowcount=self.tableWidget.rowCount()        
        for i in range(rowcount):
            if(self.tableWidget.item(i, 0).checkState()== QtCore.Qt.Checked):  
                tagslist.append(self.tableWidget.item(i, 1).text())
        self.close()
    def find(self):
        self.tableWidget.setRowCount(0)
        tagsourde=self.combotagsource.currentText() 
        datatype=self.combotype.currentText() 
        datatypeid=0
        if(datatype=='digital'):
            datatypeid=1
        elif(datatype=='analog'):
            datatypeid=2
        db=sqlite3.connect(self.database)
        cur = db.cursor()
        strsql=""
        if(datatype=='all'):
            strsql="select name,datatype,tagsource from tag where tagsource=\'%s\'"%tagsourde
        else:
            strsql="select name,datatype,tagsource from tag where tagsource=\'%s\' and datatype=%d"%(tagsourde,datatypeid)
        print(strsql)
        cur.execute(strsql)
        res = cur.fetchall()
        rowcount=len(res)
        index=0
        if(rowcount>0):
            self.tableWidget.setRowCount(rowcount)
            for row in res:
                for j in range(0,self.tableWidget.columnCount()-1):
                    if row[j]==None:
                        newItem = QtGui.QTableWidgetItem('' )
                    else:
                        newItem = QtGui.QTableWidgetItem(str(row[j]) )                                                
                    if(j==0):
                        newItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)                      
                                                       
                    self.tableWidget.setItem(index,j+1,newItem) 
                newItem = QtGui.QTableWidgetItem() 
                newItem.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(index,0,newItem)     
                index+=1       
        db.close()
    def cancel(self):
        global  tagslist 
        tagslist=[]
        self.close()
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)        
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1388, 678)        
        self.tableWidget = TableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1371, 571))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        
        
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(30, 30, 331, 50))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.combotype = QtGui.QComboBox(self.widget)
        self.combotype.setObjectName(_fromUtf8("combotype"))
        self.gridLayout.addWidget(self.combotype, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.combotagsource = QtGui.QComboBox(self.widget)
        self.combotagsource.setObjectName(_fromUtf8("combotagsource"))
        self.gridLayout.addWidget(self.combotagsource, 0, 3, 1, 1)
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setGeometry(QtCore.QRect(390, 30, 320, 50))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_find = QtGui.QPushButton(self.widget1)
        self.pushButton_find.setObjectName(_fromUtf8("pushButton_find"))
        self.horizontalLayout.addWidget(self.pushButton_find)
        self.pushButton_select = QtGui.QPushButton(self.widget1)
        self.pushButton_select.setObjectName(_fromUtf8("pushButton_select"))
        self.horizontalLayout.addWidget(self.pushButton_select)
        self.pushButton_unselect = QtGui.QPushButton(self.widget1)
        self.pushButton_unselect.setObjectName(_fromUtf8("pushButton_unselect"))
        self.horizontalLayout.addWidget(self.pushButton_unselect)
        self.pushButto_ok = QtGui.QPushButton(self.widget1)
        self.pushButto_ok.setObjectName(_fromUtf8("pushButto_ok"))
        self.horizontalLayout.addWidget(self.pushButto_ok)        
        
        self.pushButton_cancel = QtGui.QPushButton(self.widget1)        
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)   
        
        self.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_cancel.setText(_translate("Dialog", "cancel", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "datatype", None))
        item = self.tableWidget.horizontalHeaderItem(3)        
        item.setText(_translate("Dialog", "tagsource", None))  
                
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "select", None)) 
        self.label.setText(_translate("Dialog", "tag type", None))
        self.label_2.setText(_translate("Dialog", "tag source", None))
        self.pushButton_find.setText(_translate("Dialog", "find", None))
        self.pushButton_select.setText(_translate("Dialog", "select", None))
        self.pushButton_unselect.setText(_translate("Dialog", "unselect", None))
        self.pushButto_ok.setText(_translate("Dialog", "ok", None))
        
        tadtypelist=['all','digital','analog']        
        self.combotype.addItems(tadtypelist)  
        
        db=sqlite3.connect(self.database)               
        cur = db.cursor()       
        cursor = cur.execute('select distinct tagsource from tag order by tagsource')
        res = cursor.fetchall()
        for row in res:            
            self.combotagsource.addItems(row)
            
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancel)
        QtCore.QObject.connect(self.pushButton_find, QtCore.SIGNAL(_fromUtf8("clicked()")), self.find)
        QtCore.QObject.connect(self.pushButton_select, QtCore.SIGNAL(_fromUtf8("clicked()")), self.select)
        QtCore.QObject.connect(self.pushButton_unselect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.unselect)
        QtCore.QObject.connect(self.pushButto_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ok)
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.showMaximized()
    app.exec_()
    