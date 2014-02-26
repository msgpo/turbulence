#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import needed libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from tools_ import * 

_translate = QtCore.QCoreApplication.translate

#Detect what processes you're running for DE/WM specific slides.
tintStatus = utils_detector.detectTint() #Tint
kwinStatus = utils_detector.detectKwin() #Kwin
plasmaStatus = utils_detector.detectPlasma() #Plasma
nitrogenStatus = utils_detector.detectNitrogen() #Nitrogen
openboxStatus = utils_detector.detectOpenBox() #Openbox
kdeStatus = utils_detector.detectKde() #Kde

#Configure normal widgets
def widgetConfigurer(widgetType, xPos, yPos, xSize, ySize, name, image=None, styleSheet=None):
    widgetType.setGeometry(QtCore.QRect(xPos, yPos, xSize, ySize))
    widgetType.setObjectName(name)
    
    if image is not None:
        widgetType.setPixmap(QtGui.QPixmap(image))
        
    if styleSheet is not None:
        widgetType.setStyleSheet(styleSheet)
        
#Configure widgets held in a layout
def layoutConfigurer(name, widgetType, minW, minH, maxH, maxW, flat, focus, image, position=False):
    widgetType.setObjectName(name)
    if minW or minH is not None:
        widgetType.setMinimumSize(QtCore.QSize(minW, minH))
    
    if maxH or maxW is not None:
        widgetType.setMaximumSize(QtCore.QSize(maxH, maxW))
        
    if flat:
        widgetType.setFlat(True)
    
    if focus:
        widgetType.setFocusPolicy(QtCore.Qt.NoFocus)
    
    if image:
        widgetType.setPixmap(QtGui.QPixmap(image))
        
    if position:
        widgetType.setAlignment(QtCore.Qt.AlignCenter)
        

#Create static widgets that are the same on all pages        
def createStaticWidgets(parent):
    global blackBackground; blackBackground = QtWidgets.QLabel(parent)
    global headerBack; headerBack = QtWidgets.QLabel(parent)
    global turbulenceLogo; turbulenceLogo = QtWidgets.QLabel(parent)
    global menuBackg; menuBackg = QtWidgets.QLabel(parent)
    global footerBack; footerBack = QtWidgets.QLabel(parent)
    
    staticWidgets = {
        "blackBackground": [blackBackground, -14, 0, 891, 625, "blackBackground", "/usr/share/turbulence/images/manjaro-grey/background.jpg"],
        "headerBack": [headerBack, -20, 10, 921, 71, "headerBack", "/usr/share/turbulence/images/manjaro-grey/header.png"],
        "turbulenceLogo": [turbulenceLogo, 20, 20, 51, 51, "turbulenceLogo", "/usr/share/turbulence/images/manjaro-grey/turbulence.png"],
        "menuBackg": [menuBackg, -20, 90, 901, 41, "menuBackg", None],
        "footerBack": [footerBack, 0, 570, 861, 51, "footerBack", None]
    }
    
    for widgetName, widgetSettings in staticWidgets.items():
        widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])

    return blackBackground, headerBack, turbulenceLogo, menuBackg, footerBack

#Begins to main class
class Ui_MainWindow(QtCore.QObject):
    def setupUi(self, MainWindow):
        
        #Determines the sizes of the menu container based on the DE/WM
        #This is important due to the differences in font rendering.
        #If neither KDE or Openbox, defaults to KDE Settings.
        if kdeStatus:
            lMinW = 20
            lMinH = 87
            lMaxW = 511
            lMaxH = 43
        elif openboxStatus:
            lMinW = 20
            lMinH = 83
            lMaxW = 511
            lMaxH = 50
        else:
            lMinW = 20
            lMinH = 87
            lMaxW = 511
            lMaxH = 43
            
        #Grabs the stylesheet
        styleSheetFile = open("/usr/share/turbulence/stylesheets/manjarogrey.qss", "r")
        self.styleData = styleSheetFile.read()
        styleSheetFile.close()
      
        #Sets up the main window
        MainWindow.setObjectName("Turbulence")
        MainWindow.resize(839, 594)
        MainWindow.setMinimumSize(QtCore.QSize(839, 594))
        MainWindow.setMaximumSize(QtCore.QSize(839, 594))
        MainWindow.setWindowIcon(QtGui.QIcon('/usr/share/turbulence/images/manjaro-grey/turbulence.png'))
        MainWindow.setStyleSheet(self.styleData)
        
        forwardIcon = QtGui.QIcon()
        forwardIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cancelIcon = QtGui.QIcon()
        cancelIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        previousIcon = QtGui.QIcon()
        previousIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/arrowreverse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        finishIcon = QtGui.QIcon()
        finishIcon.addPixmap(QtGui.QPixmap("/usr/share/turbulence/images/manjaro-grey/checkmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Defines the stacked widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        widgetConfigurer(self.stackedWidget, -10, -20, 861, 621, "stackedWidget", None, None)
        
        #Starts the first page in the stacked widget, or Manjaro welcome
        self.welcomeToManjaro = QtWidgets.QWidget()
        self.welcomeToManjaro.setObjectName("welcomeToManjaro")

        #Defines all the widgets for the first page
        createStaticWidgets(self.welcomeToManjaro)
        self.welcomeHeader = QtWidgets.QLabel(self.welcomeToManjaro)
        self.welcomeMenuContainer = QtWidgets.QWidget(self.welcomeToManjaro)
        self.welcomeMenuContainerHLayout = QtWidgets.QHBoxLayout(self.welcomeMenuContainer)
        self.welcomeButton = QtWidgets.QPushButton(self.welcomeMenuContainer)
        self.welcomeArrow = QtWidgets.QLabel(self.welcomeMenuContainer)
        self.welcomeFolders = QtWidgets.QPushButton(self.welcomeMenuContainer)
        self.welcomeMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.welcomeWhatIsManjaro = QtWidgets.QLabel(self.welcomeToManjaro)
        self.welcomeManjaroDesc = QtWidgets.QLabel(self.welcomeToManjaro)
        self.welcomeFooterContainer = QtWidgets.QWidget(self.welcomeToManjaro)
        self.welcomeFooterContainerHLayout = QtWidgets.QHBoxLayout(self.welcomeFooterContainer)
        self.welcomeFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.welcomeForward = QtWidgets.QPushButton(self.welcomeFooterContainer)
        self.welcomeCancel = QtWidgets.QPushButton(self.welcomeFooterContainer)
        
        #widget dictionary
        firstPageWidgets = {
            "welcomeHeader": [self.welcomeHeader, 80, 20, 600, 51, "welcomeHeader", None],
            "welcomeWhatIsManjaro": [self.welcomeWhatIsManjaro, 30, 180, 600, 71, "welcomeWhatIsManjaro", None],
            "welcomeManjaroDesc": [self.welcomeManjaroDesc, 70, 260, 650, 300, "welcomeManjaroDesc", None],
        }
        
        firstPageLayouts = {
            "welcomeButton": [self.welcomeButton, 0, 39, None, None, True, True, False],
            "welcomeArrow": [self.welcomeArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png"],
            "welcomeFolders": [self.welcomeFolders, 0, 39, None, None, True, True, False],
            "welcomeForward": [self.welcomeForward, 0, 34, None, None, True, True, False],
            "welcomeCancel": [self.welcomeCancel, 0, 34, None, None, True, True, False]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in firstPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
            
        for widgetName, widgetSettings in firstPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
        
        #defines all the custom settings        
        self.welcomeForward.setIcon(forwardIcon)
        self.welcomeCancel.setIcon(cancelIcon)
        self.welcomeForward.setIconSize(QtCore.QSize(28, 30))
        self.welcomeCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.welcomeMenuContainerHLayout.addWidget(self.welcomeButton)
        self.welcomeMenuContainerHLayout.addWidget(self.welcomeArrow)
        self.welcomeMenuContainerHLayout.addWidget(self.welcomeFolders)
        self.welcomeMenuContainerHLayout.addItem(self.welcomeMenuSpacer)
        
        self.welcomeFooterContainerHLayout.addWidget(self.welcomeCancel)
        self.welcomeFooterContainerHLayout.addItem(self.welcomeFooterSpacer)
        self.welcomeFooterContainerHLayout.addWidget(self.welcomeForward)
        
        self.welcomeMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
        self.welcomeFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        
        self.welcomeManjaroDesc.setTextFormat(QtCore.Qt.RichText)
        self.welcomeManjaroDesc.setWordWrap(True)
        
        #adds the first page
        self.stackedWidget.addWidget(self.welcomeToManjaro)
        
        #Hooks up the button handlers
        self.welcomeFolders.clicked.connect(self.handleButtonNext)
        self.welcomeForward.clicked.connect(self.handleButtonNext)
        self.welcomeCancel.clicked.connect(MainWindow.close)
        
        #Translates, or sets the text to the widgets
        self.welcomeHeader.setText(_translate("MainWindow", "Welcome To Manjaro!"))
        self.welcomeButton.setText(_translate("MainWindow", "Welcome"))
        self.welcomeFolders.setText(_translate("MainWindow", "Folders"))
        self.welcomeWhatIsManjaro.setText(_translate("MainWindow", "What is Manjaro?"))
        self.welcomeManjaroDesc.setText(_translate("MainWindow", """<b>Manjaro</b> is a sleek and fast distro, featuring benefits from the popular Arch OS, along with ease of use. Developed in Austria, France, and Germany, Manjaro aims at new users, and experienced users.\n<br><br>\nSome of Manjaro's features are:\n<ul>\n<li>Speed, power, and efficiency</li>\n<li>Access to the very latest cutting and bleeding edge software</li>\n<li>A ‘rolling release’ development model that provides the most up-to-date system possible without the need to install new versions</li>\n<li>Access to the Arch User Repository (AUR).</li>\n</ul>\nFor newcomers, a user-friendly installer is provided, and the system itself is designed to work fully straight out of the box. For more experienced, and adventurous users, Manjaro also offers the configurability and versatility to be shaped and moulded in every respect to suit personal taste and preference.\n<br><br>\nOver these next few steps, Turbulence will guide you through customizing your new copy of Manjaro."""))
        self.welcomeCancel.setText(_translate("MainWindow", "Cancel"))
        self.welcomeForward.setText(_translate("MainWindow", "Forward"))
         
        #Starts the second page in the stacked widget.
        self.folders = QtWidgets.QWidget()
        self.folders.setObjectName("folders")
        
        #Defines all the widget for the second page
        createStaticWidgets(self.folders)
        
        self.folderHeader = QtWidgets.QLabel(self.folders)
        self.folderMenuContainer = QtWidgets.QWidget(self.folders)
        self.folderMenuContainerHLayout = QtWidgets.QHBoxLayout(self.folderMenuContainer)
        self.folderMenu = QtWidgets.QPushButton(self.folderMenuContainer)
        self.folderArrow = QtWidgets.QLabel(self.folderMenuContainer)
        self.folderThemes = QtWidgets.QPushButton(self.folderMenuContainer)
        self.folderMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderFooterContainer = QtWidgets.QWidget(self.folders)
        self.folderFooterContainerHLayout = QtWidgets.QHBoxLayout(self.folderFooterContainer)
        self.folderCancel = QtWidgets.QPushButton(self.folderFooterContainer)
        self.folderFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderForward = QtWidgets.QPushButton(self.folderFooterContainer)
        self.folderPrevious = QtWidgets.QPushButton(self.folderFooterContainer)
        self.folderIcon = QtWidgets.QLabel(self.folders)
        self.folderDesc = QtWidgets.QLabel(self.folders)
        self.folderContentsUpper = QtWidgets.QWidget(self.folders)
        self.folderContentsUpperLayout = QtWidgets.QGridLayout(self.folderContentsUpper)
        self.folderIcon1 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon2 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon3 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon4 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon5 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon6 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon7 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderIcon8 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader1 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader2 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader3 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader4 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader5 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader6 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader7 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderHeader8 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName1 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName2 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName3 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName4 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName5 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName6 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName7 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderName8 = QtWidgets.QLabel(self.folderContentsUpper)
        self.folderActive1 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive2 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive3 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive4 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive5 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive6 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive7 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderActive8 = QtWidgets.QCheckBox(self.folderContentsUpper)
        self.folderContentsUpperSpacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderContentsUpperSpacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.folderContentsUpperSpacer3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        if kwinStatus and tintStatus:
            self.folderThemes.setText(_translate("MainWindow", "Themes"))
        elif kwinStatus:
            self.folderThemes.setText(_translate("MainWindow", "Themes"))
        elif tintStatus:
            self.folderThemes.setText(_translate("MainWindow", "Tint 2"))
        else:
            self.folderThemes.setText(_translate("MainWindow", "Finish"))

        #widget dictionary.
        secondPageWidgets = {
            "folderHeader": [self.folderHeader, 80, 20, 600, 51, "folderHeader", None],
            "folderIcon": [self.folderIcon, 40, 150, 61, 61, "folderIcon", "/usr/share/turbulence/images/manjaro-grey/foldericons/folder.png"],
            "folderDesc": [self.folderDesc, 110, 160, 591, 51, "folderDesc", None]
        }
        
        secondPageLayouts = {
            "folderMenu": [self.folderMenu, 0, 39, None, None, True, True, False, False],
            "folderArrow": [self.folderArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
            "folderThemes": [self.folderThemes, 0, 39, None, None, True, True, False, False],
            "folderForward": [self.folderForward, 0, 34, None, None, True, True, False, False],
            "folderPrevious": [self.folderPrevious, 0, 34, None, None, True, True, False, False],
            "folderCancel": [self.folderCancel, 0, 34, None, None, True, True, False, False],
            "folderIcon1": [self.folderIcon1, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/desktop.png", True],
            "folderIcon2": [self.folderIcon2, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/documents.png", True],
            "folderIcon3": [self.folderIcon3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/downloads.png", True],
            "folderIcon4": [self.folderIcon4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/music.png", True],
            "folderIcon5": [self.folderIcon5, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/pictures.png", True],
            "folderIcon6": [self.folderIcon6, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/public.png", True],
            "folderIcon7": [self.folderIcon7, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/templates.png", True],
            "folderIcon8": [self.folderIcon8, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/foldericons/videos.png", True],
            "folderHeader1": [self.folderHeader1, None, None, None, None, False, False, False, False],
            "folderHeader2": [self.folderHeader2, None, None, None, None, False, False, False, False],
            "folderHeader3": [self.folderHeader3, None, None, None, None, False, False, False, False],
            "folderHeader4": [self.folderHeader4, None, None, None, None, False, False, False, False],
            "folderHeader5": [self.folderHeader5, None, None, None, None, False, False, False, False],
            "folderHeader6": [self.folderHeader6, None, None, None, None, False, False, False, False],
            "folderHeader7": [self.folderHeader7, None, None, None, None, False, False, False, False],
            "folderHeader8": [self.folderHeader8, None, None, None, None, False, False, False, False],
            "folderName1": [self.folderName1, None, None, None, None, False, False, False, True],
            "folderName2": [self.folderName2, None, None, None, None, False, False, False, True],
            "folderName3": [self.folderName3, None, None, None, None, False, False, False, True],
            "folderName4": [self.folderName4, None, None, None, None, False, False, False, True],
            "folderName5": [self.folderName5, None, None, None, None, False, False, False, True],
            "folderName6": [self.folderName6, None, None, None, None, False, False, False, True],
            "folderName7": [self.folderName7, None, None, None, None, False, False, False, True],
            "folderName8": [self.folderName8, None, None, None, None, False, False, False, True],
            "folderActive1": [self.folderActive1, None, None, None, None, False, False, False, False],
            "folderActive2": [self.folderActive2, None, None, None, None, False, False, False, False],
            "folderActive3": [self.folderActive3, None, None, None, None, False, False, False, False],
            "folderActive4": [self.folderActive4, None, None, None, None, False, False, False, False],
            "folderActive5": [self.folderActive5, None, None, None, None, False, False, False, False],
            "folderActive6": [self.folderActive6, None, None, None, None, False, False, False, False],
            "folderActive7": [self.folderActive7, None, None, None, None, False, False, False, False],
            "folderActive8": [self.folderActive8, None, None, None, None, False, False, False, False]
        }
        
        #defines all the widget parameters
        for widgetName, widgetSettings in secondPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
           
        for widgetName, widgetSettings in secondPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
        
        #defines the custom settings
        self.folderPrevious.setIcon(previousIcon)
        self.folderCancel.setIcon(cancelIcon)
        self.folderForward.setIcon(forwardIcon)
        self.folderPrevious.setIconSize(QtCore.QSize(28, 30))
        self.folderForward.setIconSize(QtCore.QSize(28, 30))
        self.folderCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.folderDesc.setWordWrap(True)
        
        self.folderMenuContainerHLayout.addWidget(self.folderMenu)
        self.folderMenuContainerHLayout.addWidget(self.folderArrow)
        self.folderMenuContainerHLayout.addWidget(self.folderThemes)
        self.folderMenuContainerHLayout.addItem(self.folderMenuSpacer)
        
        self.folderFooterContainerHLayout.addWidget(self.folderCancel)
        self.folderFooterContainerHLayout.addItem(self.folderFooterSpacer)
        self.folderFooterContainerHLayout.addWidget(self.folderPrevious)
        self.folderFooterContainerHLayout.addWidget(self.folderForward)
        
        self.folderContentsUpperLayout.addWidget(self.folderName1, 0, 0, 1, 1)
        self.folderContentsUpperLayout.addItem(self.folderContentsUpperSpacer1, 0, 1, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName2, 0, 2, 1, 1)
        self.folderContentsUpperLayout.addItem(self.folderContentsUpperSpacer2, 0, 3, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName3, 0, 4, 1, 1)
        self.folderContentsUpperLayout.addItem(self.folderContentsUpperSpacer3, 0, 5, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName4, 0, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon1, 1, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon2, 1, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon3, 1, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon4, 1, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader1, 2, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader2, 2, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader3, 2, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader4, 2, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive1, 3, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive2, 3, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive3, 3, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive4, 3, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName5, 4, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName6, 4, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName7, 4, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderName8, 4, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon5, 5, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon6, 5, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon7, 5, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderIcon8, 5, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader5, 6, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader6, 6, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader7, 6, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderHeader8, 6, 6, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive5, 7, 0, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive6, 7, 2, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive7, 7, 4, 1, 1)
        self.folderContentsUpperLayout.addWidget(self.folderActive8, 7, 6, 1, 1)
        
        self.folderMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
        self.folderFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        self.folderContentsUpper.setGeometry(QtCore.QRect(60, 230, 730, 320))
        
        #adds the second page
        self.stackedWidget.addWidget(self.folders)
        
        #Handles the button clicks.
        self.folderThemes.clicked.connect(self.handleButtonNext)
        self.folderPrevious.clicked.connect(self.handleButtonPrev)
        self.folderForward.clicked.connect(self.handleButtonNextFolders)
        self.folderCancel.clicked.connect(MainWindow.close)
        
        #Translates, or sets the text for all the widgets
        self.folderHeader.setText(_translate("MainWindow", "Folders"))
        self.folderMenu.setText(_translate("MainWindow", "Folders"))
        self.folderCancel.setText(_translate("MainWindow", "Cancel"))
        self.folderForward.setText(_translate("MainWindow", "Forward"))
        self.folderPrevious.setText(_translate("MainWindow", "Previous"))
        self.folderDesc.setText(_translate("MainWindow", "Here, you can choose which folders you want in your home directory. You have a choice from some of the most commonly used folders."))
        self.folderHeader1.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader2.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader3.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader4.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader5.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader6.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader7.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderHeader8.setText(_translate("MainWindow", "Status: Deactivated"))
        self.folderName1.setText(_translate("MainWindow", "Desktop"))
        self.folderName2.setText(_translate("MainWindow", "Documents"))
        self.folderName3.setText(_translate("MainWindow", "Downloads"))
        self.folderName4.setText(_translate("MainWindow", "Music"))
        self.folderName5.setText(_translate("MainWindow", "Pictures"))
        self.folderName6.setText(_translate("MainWindow", "Public"))
        self.folderName7.setText(_translate("MainWindow", "Templates"))
        self.folderName8.setText(_translate("MainWindow", "Videos"))
        self.folderActive1.setText(_translate("MainWindow", "Active"))
        self.folderActive2.setText(_translate("MainWindow", "Active"))
        self.folderActive3.setText(_translate("MainWindow", "Active"))
        self.folderActive4.setText(_translate("MainWindow", "Active"))
        self.folderActive5.setText(_translate("MainWindow", "Active"))
        self.folderActive6.setText(_translate("MainWindow", "Active"))
        self.folderActive7.setText(_translate("MainWindow", "Active"))
        self.folderActive8.setText(_translate("MainWindow", "Active"))
        
        
        #Checks if Kwin is running, and if so displays the kwin themer
        if kwinStatus: 
            #Starts the kwin page in the stacked widget
            self.Theme = QtWidgets.QWidget()
            self.Theme.setObjectName("Theme")
        
            createStaticWidgets(self.Theme)
            self.themeHeader = QtWidgets.QLabel(self.Theme)
            self.themeMenuContainer = QtWidgets.QWidget(self.Theme)
            self.themeMenuContainerHLayout = QtWidgets.QHBoxLayout(self.themeMenuContainer)
            self.themeMenu = QtWidgets.QPushButton(self.themeMenuContainer)
            self.themeArrow = QtWidgets.QLabel(self.themeMenuContainer)
            self.themeMenuWallpapers = QtWidgets.QPushButton(self.themeMenuContainer)
            self.themeMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeFooterContainer = QtWidgets.QWidget(self.Theme)
            self.themeFooterContainerHLayout = QtWidgets.QHBoxLayout(self.themeFooterContainer)
            self.themeCancel = QtWidgets.QPushButton(self.Theme)
            self.themeFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themePrevious = QtWidgets.QPushButton(self.Theme)
            self.themeForward = QtWidgets.QPushButton(self.Theme)
            self.themeIcon = QtWidgets.QLabel(self.Theme)
            self.themeDesc = QtWidgets.QLabel(self.Theme)
            self.themeContentsContainer = QtWidgets.QWidget(self.Theme)
            self.themeContentsContainerLayout = QtWidgets.QGridLayout(self.themeContentsContainer)
            self.themePreviewContainerLayout1 = QtWidgets.QHBoxLayout()
            self.themePreviewContainerLayout2 = QtWidgets.QHBoxLayout()
            self.themePreviewContainerLayout3 = QtWidgets.QHBoxLayout()
            self.themePreviewContainerLayout4 = QtWidgets.QHBoxLayout()
            self.themePreview1 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themePreview2 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themePreview3 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themePreview4 = QtWidgets.QLabel(self.themeContentsContainer)
            self.themeRadio1 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeRadio2 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeRadio3 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeRadio4 = QtWidgets.QRadioButton(self.themeContentsContainer)
            self.themeContentsRadioPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsRadioPush8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.themeContentsPush4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.themeContentsPush5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.themeContentsPush6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
            if tintStatus:
                 self.themeMenuWallpapers.setText(_translate("MainWindow", "Tint 2"))
            elif plasmaStatus:
                 self.themeMenuWallpapers.setText(_translate("MainWindow", "Wallpapers"))
            else:
                 self.themeMenuWallpapers.setText(_translate("MainWindow", "Finish"))
                 
            thirdPageWidgets = {
                "themeHeader": [self.themeHeader, 80, 20, 600, 51, "themeHeader", None],
                "themeIcon": [self.themeIcon, 40, 160, 61, 61, "themeIcon", "/usr/share/turbulence/images/manjaro-grey/themes/theme.png"],
                "themeDesc": [self.themeDesc, 110, 160, 591, 51, "themeDesc", None],
            }
             
            thirdPageLayouts = {
                "themeMenu": [self.themeMenu, 0, 39, None, None, True, True, False, False],
                "themeArrow": [self.themeArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
                "themeMenuWallpapers": [self.themeMenuWallpapers, 0, 39, None, None, True, True, False, False],
                "themeForward": [self.themeForward, 0, 34, None, None, True, True, False, False],
                "themePrevious": [self.themePrevious, 0, 34, None, None, True, True, False, False],
                "themeCancel": [self.themeCancel, 0, 34, None, None, True, True, False, False],
                "themePreview1": [self.themePreview1, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/air-black.png", True],
                "themePreview2": [self.themePreview2, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/cupertino-ish.png", True],
                "themePreview3": [self.themePreview3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/oxygen.png", True],
                "themePreview4": [self.themePreview4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/themes/plastik.png", True],
                "themeRadio1": [self.themeRadio1, None, None, None, None, False, False, False, False],
                "themeRadio2": [self.themeRadio2, None, None, None, None, False, False, False, False],
                "themeRadio3": [self.themeRadio3, None, None, None, None, False, False, False, False],
                "themeRadio4": [self.themeRadio4, None, None, None, None, False, False, False, False]
                
            }
        
            #defines all the widget parameters
            for widgetName, widgetSettings in thirdPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            for widgetName, widgetSettings in thirdPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
        
            #Defines the custom settings
            self.themeCancel.setIcon(cancelIcon)
            self.themeForward.setIcon(forwardIcon)
            self.themePrevious.setIcon(previousIcon)
            self.themeForward.setIconSize(QtCore.QSize(28, 30))
            self.themePrevious.setIconSize(QtCore.QSize(28, 30))
            self.themeCancel.setIconSize(QtCore.QSize(16, 16))
            
            self.themeDesc.setWordWrap(True)
        
            self.themeMenuContainerHLayout.addWidget(self.themeMenu)
            self.themeMenuContainerHLayout.addWidget(self.themeArrow)
            self.themeMenuContainerHLayout.addWidget(self.themeMenuWallpapers)
            self.themeMenuContainerHLayout.addItem(self.themeMenuSpacer)
            
            self.themeFooterContainerHLayout.addWidget(self.themeCancel)
            self.themeFooterContainerHLayout.addItem(self.themeFooterSpacer)
            self.themeFooterContainerHLayout.addWidget(self.themePrevious)
            self.themeFooterContainerHLayout.addWidget(self.themeForward)
            
            self.themePreviewContainerLayout1.addItem(self.themeContentsRadioPush1)
            self.themePreviewContainerLayout1.addWidget(self.themeRadio1)
            self.themePreviewContainerLayout1.addItem(self.themeContentsRadioPush2)
            self.themePreviewContainerLayout2.addItem(self.themeContentsRadioPush3)
            self.themePreviewContainerLayout2.addWidget(self.themeRadio2)
            self.themePreviewContainerLayout2.addItem(self.themeContentsRadioPush4)
            self.themePreviewContainerLayout3.addItem(self.themeContentsRadioPush5)
            self.themePreviewContainerLayout3.addWidget(self.themeRadio3)
            self.themePreviewContainerLayout3.addItem(self.themeContentsRadioPush6)
            self.themePreviewContainerLayout4.addItem(self.themeContentsRadioPush7)
            self.themePreviewContainerLayout4.addWidget(self.themeRadio4)
            self.themePreviewContainerLayout4.addItem(self.themeContentsRadioPush8)
            
            self.themeContentsContainerLayout.addItem(self.themeContentsPush4, 0, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush1, 1, 0, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview1, 1, 1, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush2, 1, 2, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview2, 1, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush3, 1, 4, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout1, 2, 1, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout2, 2, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush5, 3, 2, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview3, 4, 1, 1, 1)
            self.themeContentsContainerLayout.addWidget(self.themePreview4, 4, 3, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout3, 5, 1, 1, 1)
            self.themeContentsContainerLayout.addLayout(self.themePreviewContainerLayout4, 5, 3, 1, 1)
            self.themeContentsContainerLayout.addItem(self.themeContentsPush6, 6, 3, 1, 1)
            
            self.themeMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
            self.themeFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            self.themeContentsContainer.setGeometry(QtCore.QRect(10, 230, 840, 340))
        
            #Adds the third page
            self.stackedWidget.addWidget(self.Theme)
            
            #Hooks up the button handlers
            self.themeMenuWallpapers.clicked.connect(self.handleButtonNextThemes)
            self.themeCancel.clicked.connect(MainWindow.close)
            self.themeForward.clicked.connect(self.handleButtonNextThemes)
            self.themePrevious.clicked.connect(self.handleButtonPrevFolders)
            
            #Translates the text
            self.themeHeader.setText(_translate("MainWindow", "Themes"))
            self.themeMenu.setText(_translate("MainWindow", "Themes"))
            self.themeCancel.setText(_translate("MainWindow", "Cancel"))
            self.themeForward.setText(_translate("MainWindow", "Forward"))
            self.themePrevious.setText(_translate("MainWindow", "Previous"))
            self.themeDesc.setText(_translate("MainWindow", "Here you can choose what type of theme you want for your window decorations."))
            self.themeRadio1.setText("Air Black Green")
            self.themeRadio2.setText("Cuptertino-ish")
            self.themeRadio3.setText("Oxygen")
            self.themeRadio4.setText("Plastik")
            
        if tintStatus:
            #Starts the tint page in the stacked widget.
            self.Tint = QtWidgets.QWidget()
            self.Tint.setObjectName("Tint")
        
            createStaticWidgets(self.Tint)
            self.tintHeader = QtWidgets.QLabel(self.Tint)
            self.tintMenuContainer = QtWidgets.QWidget(self.Tint)
            self.tintMenuContainerHLayout = QtWidgets.QHBoxLayout(self.tintMenuContainer)
            self.tintMenu = QtWidgets.QPushButton(self.tintMenuContainer)
            self.tintArrow = QtWidgets.QLabel(self.tintMenuContainer)
            self.tintMenuWallpapers = QtWidgets.QPushButton(self.tintMenuContainer)
            self.tintMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintFooterContainer = QtWidgets.QWidget(self.Tint)
            self.tintFooterContainerHLayout = QtWidgets.QHBoxLayout(self.tintFooterContainer)
            self.tintCancel = QtWidgets.QPushButton(self.tintFooterContainer)
            self.tintFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintPrevious = QtWidgets.QPushButton(self.tintFooterContainer)
            self.tintForward = QtWidgets.QPushButton(self.tintFooterContainer)
            self.tintPositionIcon = QtWidgets.QLabel(self.Tint)
            self.tintPositionDesc = QtWidgets.QLabel(self.Tint)
            self.tintContentsContainer = QtWidgets.QWidget(self.Tint)
            self.tintContentsContainerLayout = QtWidgets.QGridLayout(self.tintContentsContainer)
            self.tintPreviewContainerLayout1 = QtWidgets.QHBoxLayout()
            self.tintPreviewContainerLayout2 = QtWidgets.QHBoxLayout()
            self.tintPreviewContainerLayout3 = QtWidgets.QHBoxLayout()
            self.tintPreviewContainerLayout4 = QtWidgets.QHBoxLayout()
            self.tintPosition1 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPosition2 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPosition3 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPosition4 = QtWidgets.QLabel(self.tintContentsContainer)
            self.tintPositionRadio1 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintPositionRadio2 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintPositionRadio3 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintPositionRadio4 = QtWidgets.QRadioButton(self.tintContentsContainer)
            self.tintContentsRadioPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsRadioPush8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tintContentsPush4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.tintContentsPush5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.tintContentsPush6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            
            if nitrogenStatus or plasmaStatus:
                self.tintMenuWallpapers.setText(_translate("MainWindow", "Wallpapers"))
            else:
                self.tintMenuWallpapers.setText(_translate("MainWindow", "Finish"))
            
            thirdPageWidgets = {
                "tintHeader": [self.tintHeader, 80, 20, 600, 51, "tintHeader", None],
                "tintPositionIcon": [self.tintPositionIcon, 40, 160, 61, 61, "tintPositionIcon", "/usr/share/turbulence/images/manjaro-grey/tint-previews/position.png"],
                "tintPositionDesc": [self.tintPositionDesc, 110, 160, 591, 51, "tintPositionDesc", None]
            }
        
            thirdPageLayouts  = {
                "tintMenu": [self.tintMenu, 0, 39, None, None, True, True, False, False],
                "tintArrow": [self.tintArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
                "tintMenuWallpapers": [self.tintMenuWallpapers, 0, 39, None, None, True, True, False, False],
                "tintForward": [self.tintForward, 0, 34, None, None, True, True, False, False],
                "tintPrevious": [self.tintPrevious, 0, 34, None, None, True, True, False, False],
                "tintCancel": [self.tintCancel, 0, 34, None, None, True, True, False, False],
                "tintPosition1": [self.tintPosition1, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/top.png", True],
                "tintPosition2": [self.tintPosition2, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/right.png", True],
                "tintPosition3": [self.tintPosition3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/bottom.png", True],
                "tintPosition4": [self.tintPosition4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/tint-previews/left.png", True],
                "tintPositionRadio1": [self.tintPositionRadio1, None, None, None, None, False, False, False, False],
                "tintPositionRadio2": [self.tintPositionRadio2, None, None, None, None, False, False, False, False],
                "tintPositionRadio3": [self.tintPositionRadio3, None, None, None, None, False, False, False, False],
                "tintPositionRadio4": [self.tintPositionRadio4, None, None, None, None, False, False, False, False]
            }
            
            #defines all the widget parameters
            for widgetName, widgetSettings in thirdPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            for widgetName, widgetSettings in thirdPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
        
            #Defines the custom settings
            self.tintCancel.setIcon(cancelIcon)
            self.tintForward.setIcon(forwardIcon)
            self.tintPrevious.setIcon(previousIcon)
            self.tintCancel.setIconSize(QtCore.QSize(16, 16))
            self.tintForward.setIconSize(QtCore.QSize(28, 30))
            self.tintPrevious.setIconSize(QtCore.QSize(28, 30))
            
            self.tintPositionDesc.setWordWrap(True)
            
            self.tintMenuContainerHLayout.addWidget(self.tintMenu)
            self.tintMenuContainerHLayout.addWidget(self.tintArrow)
            self.tintMenuContainerHLayout.addWidget(self.tintMenuWallpapers)
            self.tintMenuContainerHLayout.addItem(self.tintMenuSpacer)
            
            self.tintFooterContainerHLayout.addWidget(self.tintCancel)
            self.tintFooterContainerHLayout.addItem(self.tintFooterSpacer)
            self.tintFooterContainerHLayout.addWidget(self.tintPrevious)
            self.tintFooterContainerHLayout.addWidget(self.tintForward)
            
            self.tintPreviewContainerLayout1.addItem(self.tintContentsRadioPush1)
            self.tintPreviewContainerLayout1.addWidget(self.tintPositionRadio1)
            self.tintPreviewContainerLayout1.addItem(self.tintContentsRadioPush2)
            self.tintPreviewContainerLayout2.addItem(self.tintContentsRadioPush3)
            self.tintPreviewContainerLayout2.addWidget(self.tintPositionRadio2)
            self.tintPreviewContainerLayout2.addItem(self.tintContentsRadioPush4)
            self.tintPreviewContainerLayout3.addItem(self.tintContentsRadioPush5)
            self.tintPreviewContainerLayout3.addWidget(self.tintPositionRadio3)
            self.tintPreviewContainerLayout3.addItem(self.tintContentsRadioPush6)
            self.tintPreviewContainerLayout4.addItem(self.tintContentsRadioPush7)
            self.tintPreviewContainerLayout4.addWidget(self.tintPositionRadio4)
            self.tintPreviewContainerLayout4.addItem(self.tintContentsRadioPush8)
            
            self.tintContentsContainerLayout.addItem(self.tintContentsPush4, 0, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush1, 1, 0, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition1, 1, 1, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush2, 1, 2, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition2, 1, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush3, 1, 4, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout1, 2, 1, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout2, 2, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush5, 3, 2, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition3, 4, 1, 1, 1)
            self.tintContentsContainerLayout.addWidget(self.tintPosition4, 4, 3, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout3, 5, 1, 1, 1)
            self.tintContentsContainerLayout.addLayout(self.tintPreviewContainerLayout4, 5, 3, 1, 1)
            self.tintContentsContainerLayout.addItem(self.tintContentsPush6, 6, 3, 1, 1)
            
            self.tintMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
            self.tintFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            self.tintContentsContainer.setGeometry(QtCore.QRect(10, 230, 840, 340))
        
            #Adds the third page
            self.stackedWidget.addWidget(self.Tint)
            
            #Handles button clicks
            self.tintMenuWallpapers.clicked.connect(self.handleButtonNextTint)
            self.tintPrevious.clicked.connect(self.handleButtonPrevFolders)
            self.tintForward.clicked.connect(self.handleButtonNextTint)
            self.tintCancel.clicked.connect(MainWindow.close)
            
            #Sets text and translates widgets
            self.tintHeader.setText(_translate("MainWindow", "Tint 2"))
            self.tintMenu.setText(_translate("MainWindow", "Tint 2"))
            self.tintCancel.setText(_translate("MainWindow", "Cancel"))
            self.tintForward.setText(_translate("MainWindow", "Forward"))
            self.tintPrevious.setText(_translate("MainWindow", "Previous"))
            self.tintPositionDesc.setText(_translate("MainWindow", "Here you can choose what position you want of your Tint 2 panel."))
            self.tintPositionRadio1.setText(_translate("MainWindow", "Top"))
            self.tintPositionRadio2.setText(_translate("MainWindow", "Right"))
            self.tintPositionRadio3.setText(_translate("MainWindow", "Bottom"))
            self.tintPositionRadio4.setText(_translate("MainWindow", "Left"))
        
        if nitrogenStatus or plasmaStatus:
            #Starts code for fourth page
            self.Wallpaper = QtWidgets.QWidget()
            self.Wallpaper.setObjectName("Wallpaper")
            
            
            #defines all the widgets
            createStaticWidgets(self.Wallpaper)
            self.wallpaperHeader = QtWidgets.QLabel(self.Wallpaper)
            self.wallpaperMenuContainer = QtWidgets.QWidget(self.Wallpaper)
            self.wallpaperMenuContainerHLayout = QtWidgets.QHBoxLayout(self.wallpaperMenuContainer)
            self.wallpaperMenu = QtWidgets.QPushButton(self.wallpaperMenuContainer)
            self.wallpaperArrow = QtWidgets.QLabel(self.wallpaperMenuContainer)
            self.wallpaperMenuFinish = QtWidgets.QPushButton(self.wallpaperMenuContainer)
            self.wallpaperMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperIcon = QtWidgets.QLabel(self.Wallpaper)
            self.wallpaperDesc = QtWidgets.QLabel(self.Wallpaper)
            self.wallpaperFooterContainer = QtWidgets.QWidget(self.Wallpaper)
            self.wallpaperFooterContainerHLayout = QtWidgets.QHBoxLayout(self.wallpaperFooterContainer)
            self.wallpaperPrevious = QtWidgets.QPushButton(self.wallpaperFooterContainer)
            self.wallpaperForward = QtWidgets.QPushButton(self.wallpaperFooterContainer)
            self.wallpaperCancel = QtWidgets.QPushButton(self.wallpaperFooterContainer)
            self.wallpaperFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsContainer = QtWidgets.QWidget(self.Wallpaper)
            self.wallpaperContentsContainerLayout = QtWidgets.QGridLayout(self.wallpaperContentsContainer)
            self.wallpaperPreviewContainerLayout1 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout2 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout3 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout4 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout5 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout6 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout7 = QtWidgets.QHBoxLayout()
            self.wallpaperPreviewContainerLayout8 = QtWidgets.QHBoxLayout()
            self.wallpaper1 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper2 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper3 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper4 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper5 = QtWidgets.QLabel(self.wallpaperContentsContainer) 
            self.wallpaper6 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper7 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaper8 = QtWidgets.QLabel(self.wallpaperContentsContainer)
            self.wallpaperChoice1 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice2 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice3 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice4 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice5 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice6 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice7 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperChoice8 = QtWidgets.QRadioButton(self.wallpaperContentsContainer)
            self.wallpaperContentsRadioPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsRadioPush16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.wallpaperContentsPush6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.wallpaperContentsPush7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.wallpaperContentsPush8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            
            #Sets the wallpaper release specific wallpapers.
            if openboxStatus:
                releaseWallsOne = "/usr/share/turbulence/images/manjaro-grey/wallpapers/evodark.png"
                releaseWallsTwo = "/usr/share/turbulence/images/manjaro-grey/wallpapers/evolight.png"
                self.wallpaperChoice1.setText("Evolution Dark")
                self.wallpaperChoice2.setText("Evolution Light")
            elif kdeStatus:
                releaseWallsOne = "/usr/share/turbulence/images/manjaro-grey/wallpapers/manjarostyle.png"
                releaseWallsTwo = "/usr/share/turbulence/images/manjaro-grey/wallpapers/orangesplash.png"
                self.wallpaperChoice1.setText("Manjaro Style")
                self.wallpaperChoice2.setText("Orange Splash")
            else:
                releaseWallsOne = "/usr/share/turbulence/images/manjaro-grey/wallpapers/ozone.png"
                releaseWallsTwo = "/usr/share/turbulence/images/manjaro-grey/wallpapers/orangesplash.png"
                self.wallpaperChoice1.setText("Ozone")
                self.wallpaperChoice2.setText("Orange Splash")
                
            if openboxStatus:
                self.wallpaperMenuFinish.setText(_translate("MainWindow", "Packages"))
            else:
                self.wallpaperMenuFinish.setText(_translate("MainWindow", "Finish"))
            
            fourthPageWidgets = {
                "wallpaperHeader": [self.wallpaperHeader, 80, 20, 600, 51, "wallpaperHeader", None],
                "wallpaperIcon": [self.wallpaperIcon, 40, 160, 61, 61, "wallpaperIcon", "/usr/share/turbulence/images/manjaro-grey/wallpapers/wallpapers.png"],
                "wallpaperDesc": [self.wallpaperDesc, 110, 160, 591, 51, "wallpaperDesc", None],
                "wallpaperChoice1": [self.wallpaperChoice1, 70, 380, 81, 21, "wallpaperChoice1", None],
                "wallpaperChoice2": [self.wallpaperChoice2, 250, 380, 141, 21, "wallpaperChoice2", None],
                "wallpaperChoice3": [self.wallpaperChoice3, 480, 380, 131, 21, "wallpaperChoice3", None],
                "wallpaperChoice4": [self.wallpaperChoice4, 680, 380, 141, 21, "wallpaperChoice4", None],
                "wallpaperChoice5": [self.wallpaperChoice5, 70, 510, 81, 21, "wallpaperChoice5", None],
                "wallpaperChoice6": [self.wallpaperChoice6, 262, 510, 111, 21, "wallpaperChoice6", None],
                "wallpaperChoice7": [self.wallpaperChoice7, 477, 510, 131, 21, "wallpaperChoice7", None],
                "wallpaperChoice8": [self.wallpaperChoice8, 692, 510, 121, 21, "wallpaperChoice8", None]
            }

            fourthPageLayouts = {
                "wallpaperMenu": [self.wallpaperMenu, 0, 39, None, None, True, True, False, False],
                "wallpaperArrow": [self.wallpaperArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png", False],
                "wallpaperMenuFinish": [self.wallpaperMenuFinish, 0, 39, None, None, True, True, False, False],
                "wallpaperForward": [self.wallpaperForward, 0, 34, None, None, True, True, False, False],
                "wallpaperPrevious": [self.wallpaperPrevious, 0, 34, None, None, True, True, False, False],
                "wallpaperCancel": [self.wallpaperCancel, 0, 34, None, None, True, True, False, False],
                "wallpaper1": [self.wallpaper1, None, None, None, None, False, False, releaseWallsOne, True],
                "wallpaper2": [self.wallpaper2, None, None, None, None, False, False, releaseWallsTwo, True],
                "wallpaper3": [self.wallpaper3, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/sunsetplane.png", True],
                "wallpaper4": [self.wallpaper4, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/mountainlake.png", True],
                "wallpaper5": [self.wallpaper5, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/earthinspace.png", True],
                "wallpaper6": [self.wallpaper6, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/darkstairs.png", True],
                "wallpaper7": [self.wallpaper7, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/cherryjapan.png", True],
                "wallpaper8": [self.wallpaper8, None, None, None, None, False, False, "/usr/share/turbulence/images/manjaro-grey/wallpapers/whitetiger.png", True],
                "wallpaperChoice1": [self.wallpaperChoice1, None, None, None, None, False, False, False, False],
                "wallpaperChoice2": [self.wallpaperChoice2, None, None, None, None, False, False, False, False],
                "wallpaperChoice3": [self.wallpaperChoice3, None, None, None, None, False, False, False, False],
                "wallpaperChoice4": [self.wallpaperChoice4, None, None, None, None, False, False, False, False],
                "wallpaperChoice5": [self.wallpaperChoice5, None, None, None, None, False, False, False, False],
                "wallpaperChoice6": [self.wallpaperChoice6, None, None, None, None, False, False, False, False],
                "wallpaperChoice7": [self.wallpaperChoice7, None, None, None, None, False, False, False, False],
                "wallpaperChoice8": [self.wallpaperChoice8, None, None, None, None, False, False, False, False]
            }

            #defines all the widget parameters
            for widgetName, widgetSettings in fourthPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
            
            for widgetName, widgetSettings in fourthPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7], widgetSettings[8])
            
            #Defines all the custom settings.
            self.wallpaperPrevious.setIcon(previousIcon)
            self.wallpaperForward.setIcon(forwardIcon)
            self.wallpaperCancel.setIcon(cancelIcon)
            self.wallpaperPrevious.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperForward.setIconSize(QtCore.QSize(28, 30))
            self.wallpaperCancel.setIconSize(QtCore.QSize(16, 16))
            
            self.wallpaperDesc.setWordWrap(True)
            
            self.wallpaperMenuContainerHLayout.addWidget(self.wallpaperMenu)
            self.wallpaperMenuContainerHLayout.addWidget(self.wallpaperArrow)
            self.wallpaperMenuContainerHLayout.addWidget(self.wallpaperMenuFinish)
            self.wallpaperMenuContainerHLayout.addItem(self.wallpaperMenuSpacer)
            
            self.wallpaperFooterContainerHLayout.addWidget(self.wallpaperCancel)
            self.wallpaperFooterContainerHLayout.addItem(self.wallpaperFooterSpacer)
            self.wallpaperFooterContainerHLayout.addWidget(self.wallpaperPrevious)
            self.wallpaperFooterContainerHLayout.addWidget(self.wallpaperForward)
            
            self.wallpaperPreviewContainerLayout1.addItem(self.wallpaperContentsRadioPush1)
            self.wallpaperPreviewContainerLayout1.addWidget(self.wallpaperChoice1)
            self.wallpaperPreviewContainerLayout1.addItem(self.wallpaperContentsRadioPush2)
            self.wallpaperPreviewContainerLayout2.addItem(self.wallpaperContentsRadioPush3)
            self.wallpaperPreviewContainerLayout2.addWidget(self.wallpaperChoice2)
            self.wallpaperPreviewContainerLayout2.addItem(self.wallpaperContentsRadioPush4)
            self.wallpaperPreviewContainerLayout3.addItem(self.wallpaperContentsRadioPush5)
            self.wallpaperPreviewContainerLayout3.addWidget(self.wallpaperChoice3)
            self.wallpaperPreviewContainerLayout3.addItem(self.wallpaperContentsRadioPush6)
            self.wallpaperPreviewContainerLayout4.addItem(self.wallpaperContentsRadioPush7)
            self.wallpaperPreviewContainerLayout4.addWidget(self.wallpaperChoice4)
            self.wallpaperPreviewContainerLayout4.addItem(self.wallpaperContentsRadioPush8)
            self.wallpaperPreviewContainerLayout5.addItem(self.wallpaperContentsRadioPush9)
            self.wallpaperPreviewContainerLayout5.addWidget(self.wallpaperChoice5)
            self.wallpaperPreviewContainerLayout5.addItem(self.wallpaperContentsRadioPush10)
            self.wallpaperPreviewContainerLayout6.addItem(self.wallpaperContentsRadioPush11)
            self.wallpaperPreviewContainerLayout6.addWidget(self.wallpaperChoice6)
            self.wallpaperPreviewContainerLayout6.addItem(self.wallpaperContentsRadioPush12)
            self.wallpaperPreviewContainerLayout7.addItem(self.wallpaperContentsRadioPush13)
            self.wallpaperPreviewContainerLayout7.addWidget(self.wallpaperChoice7)
            self.wallpaperPreviewContainerLayout7.addItem(self.wallpaperContentsRadioPush14)
            self.wallpaperPreviewContainerLayout8.addItem(self.wallpaperContentsRadioPush15)
            self.wallpaperPreviewContainerLayout8.addWidget(self.wallpaperChoice8)
            self.wallpaperPreviewContainerLayout8.addItem(self.wallpaperContentsRadioPush16)
            
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush6, 0, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush1, 1, 0, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper1, 1, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush2, 1, 2, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper2, 1, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush3, 1, 4, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper3, 1, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush4, 1, 6, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper4, 1, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush5, 1, 8, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout1, 2, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout2, 2, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout3, 2, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout4, 2, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush7, 3, 2, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper5, 4, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper6, 4, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper7, 4, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addWidget(self.wallpaper8, 4, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout5, 5, 1, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout6, 5, 3, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout7, 5, 5, 1, 1)
            self.wallpaperContentsContainerLayout.addLayout(self.wallpaperPreviewContainerLayout8, 5, 7, 1, 1)
            self.wallpaperContentsContainerLayout.addItem(self.wallpaperContentsPush8, 6, 3, 1, 1)
            
            self.wallpaperMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
            self.wallpaperFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            self.wallpaperContentsContainer.setGeometry(QtCore.QRect(10, 230, 840, 340))
            
            self.stackedWidget.addWidget(self.Wallpaper)
            
            #Handles the button clicks
            self.wallpaperMenuFinish.clicked.connect(self.handleButtonNextWallpapers)
            self.wallpaperCancel.clicked.connect(MainWindow.close)
            self.wallpaperPrevious.clicked.connect(self.handleButtonPrev)
            self.wallpaperForward.clicked.connect(self.handleButtonNextWallpapers)
       
            #Sets text, or translates widgets
            self.wallpaperHeader.setText(_translate("MainWindow", "Wallpapers"))
            self.wallpaperMenu.setText(_translate("MainWindow", "Wallpapers"))
            self.wallpaperDesc.setText(_translate("MainWindow", "Here you can set which wallpaper you want."))
            self.wallpaperPrevious.setText(_translate("MainWindow", "Previous"))
            self.wallpaperForward.setText(_translate("MainWindow", "Forward"))
            self.wallpaperCancel.setText(_translate("MainWindow", "Cancel"))
            self.wallpaperChoice3.setText("Sunset Plane")
            self.wallpaperChoice4.setText("Mountain Lake")
            self.wallpaperChoice5.setText("Space")
            self.wallpaperChoice6.setText("Dark Stairs")
            self.wallpaperChoice7.setText("Cherry Japan")
            self.wallpaperChoice8.setText("Snow Leopard")
        
        
        if openboxStatus:
            #Adds the sixth page.
            self.Packages = QtWidgets.QWidget()
            self.Packages.setObjectName("Packages")
        
            #Creates all the widgets
            createStaticWidgets(self.Packages)
            
            self.packagesHeader = QtWidgets.QLabel(self.Packages)
            self.packagesMenuContainer = QtWidgets.QWidget(self.Packages)
            self.packagesMenuContainerHLayout = QtWidgets.QHBoxLayout(self.packagesMenuContainer)
            self.packagesMenu = QtWidgets.QPushButton(self.packagesMenuContainer)
            self.packagesArrow = QtWidgets.QLabel(self.packagesMenuContainer)
            self.packagesMenuFinish = QtWidgets.QPushButton(self.packagesMenuContainer)
            self.packagesMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.packagesIcon = QtWidgets.QLabel(self.Packages)
            self.packagesDesc = QtWidgets.QLabel(self.Packages)
            self.packagesFooterContainer = QtWidgets.QWidget(self.Packages)
            self.packagesFooterContainerHLayout = QtWidgets.QHBoxLayout(self.packagesFooterContainer)
            self.packagesPrevious = QtWidgets.QPushButton(self.Packages)
            self.packagesForward = QtWidgets.QPushButton(self.Packages)
            self.packagesCancel = QtWidgets.QPushButton(self.Packages)
            self.packagesFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.packagesTabs = QtWidgets.QTabWidget(self.Packages)
            self.packagesNetwork = QtWidgets.QWidget()
            self.packagesNetworkBack = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesAroraPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesAroraCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesDelugePic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesDelugeCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesChromiumPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesChromiumCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesFirefoxPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesFirefoxCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesMidoriPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesMidoriCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesOperaPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesOperaCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesTransmissionPic = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesTransmissionCheck = QtWidgets.QCheckBox(self.packagesNetwork)
            self.packagesNotActive = QtWidgets.QLabel(self.packagesNetwork)
            self.packagesMultimedia = QtWidgets.QWidget()
            self.packagesMultimediaBack = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesVlcPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesVlcCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesSmplayerPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesSmplayerCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesAudaciousPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesAudaciousCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesClemetinePic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesClementineCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesDeadbeefPic = QtWidgets.QLabel(self.packagesMultimedia)
            self.packagesDeadbeefCheck = QtWidgets.QCheckBox(self.packagesMultimedia)
            self.packagesGraphics = QtWidgets.QWidget()
            self.packagesGraphicsBack = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesBlenderPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesBlenderCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesEvincePic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesEvinceCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesGimpPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesGimpCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesGpicviewPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesGpicviewCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesViewniorPic = QtWidgets.QLabel(self.packagesGraphics)
            self.packagesViewniorCheck = QtWidgets.QCheckBox(self.packagesGraphics)
            self.packagesAccessories = QtWidgets.QWidget()
            self.packagesAccessoriesBack = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesGeanyPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesGeanyCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesHexchatPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesHexchatCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesLeafpadPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesLeafpadCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesPcmanfmPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesPcmanfmCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesSpacefmPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesSpacefmCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesTerminatorPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesTerminatorCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesThunarPic = QtWidgets.QLabel(self.packagesAccessories)
            self.packagesThunarCheck = QtWidgets.QCheckBox(self.packagesAccessories)
            self.packagesExtras = QtWidgets.QWidget()
            self.packagesExtrasBack = QtWidgets.QLabel(self.packagesExtras)
            self.packagesAurSupportPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesAurSupportCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesMultimediaSupportPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesMultimediaSupportCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesPrinterSupportPic = QtWidgets.QLabel(self.packagesExtras)
            self.packagesPrinterSupportCheck = QtWidgets.QCheckBox(self.packagesExtras)
            self.packagesInstall = QtWidgets.QWidget()
            self.packagesInstallBack = QtWidgets.QLabel(self.packagesInstall)
            self.packagesInstallButton = QtWidgets.QPushButton(self.packagesInstall)
            self.packagesCheckConnection = QtWidgets.QPushButton(self.Packages)
        
            fifthPageWidgets = {
                "packagesHeader": [self.packagesHeader, 80, 20, 600, 51, "packagesHeader", None],
                "packagesIcon": [self.packagesIcon, 40, 160, 61, 61, "packagesIcon", "/usr/share/turbulence/images/manjaro-grey/packages/packagesicon.png"],
                "packagesDesc": [self.packagesDesc, 110, 140, 650, 100, "packagesDesc", None],
                "packagesTabs": [self.packagesTabs, 60, 290, 741, 251, "packagesTabs", None],
                "packagesNetworkBack": [self.packagesNetworkBack, -14, -7, 761, 241, "packagesNetworkBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAroraPic": [self.packagesAroraPic, 20, 10, 71, 71, "packagesAroraPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/arora.png"],
                "packagesAroaCheck": [self.packagesAroraCheck, 10, 80, 111, 31, "packagesAroraCheck", None],
                "packagesChromiumPic": [self.packagesChromiumPic, 140, 10, 71, 71, "packagesChromiumPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/chromium.png"],
                "packagesChromiumCheck": [self.packagesChromiumCheck, 130, 80, 102, 31, "packagesChromiumCheck", None],
                "packagesDelugePic": [self.packagesDelugePic, 270, 10, 71, 71, "packagesDelugePic", "/usr/share/turbulence/images/manjaro-grey/packages/network/deluge.png"],
                "packagesDelugeCheck": [self.packagesDelugeCheck, 260, 80, 102, 31, "packagesDelugeCheck", None],
                "packagesFirefoxPic": [self.packagesFirefoxPic, 400, 10, 71, 71, "packagesFirefoxPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/firefox.png"],
                "packagesFirefoxCheck": [self.packagesFirefoxCheck, 390, 80, 102, 31, "packagesFirefoxCheck", None],
                "packagesMidoriPic": [self.packagesMidoriPic, 520, 10, 71, 71, "packagesMidoriPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/midori.png"],
                "packagesMidoriCheck": [self.packagesMidoriCheck, 510, 80, 121, 31, "packagesMidoriCheck", None],
                "packagesOperaPic": [self.packagesOperaPic, 640, 10, 71, 71, "packagesOperaPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/opera.png"],
                "packagesOperaCheck": [self.packagesOperaCheck, 630, 80, 102, 31, "packagesOperaCheck", None],
                "packagesTransmissionPic": [self.packagesTransmissionPic, 20, 110, 71, 71, "packagesTransmissionPic", "/usr/share/turbulence/images/manjaro-grey/packages/network/transmission.png"],
                "packagesTransmissionCheck": [self.packagesTransmissionCheck, 10, 180, 121, 31, "packagesTransmissionCheck", None],
                "packagesNotActive": [self.packagesNotActive, -10, -10, 751, 241, "packagesNotActive", None],
                "packagesMultimediaBack": [self.packagesMultimediaBack, -20, -10, 761, 241, "packagesMultimediaBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAudaciousPic": [self.packagesAudaciousPic, 20, 10, 71, 71, "packagesAudaciousPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/audacious.png"],
                "packagesAudaciousCheck": [self.packagesAudaciousCheck, 10, 80, 111, 31, "packagesAudaciousCheck", None],
                "packagesClementinePic": [self.packagesClemetinePic, 140, 10, 71, 71, "packagesClementinePic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/clementine.png"],
                "packagesClementineCheck": [self.packagesClementineCheck, 130, 80, 111, 31, "packagesClementineCheck", None],
                "packagesDeadbeefPic": [self.packagesDeadbeefPic, 270, 10, 71, 71, "packagesDeadbeefPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/deadbeef.png"],
                "packagesDeadbeefCheck": [self.packagesDeadbeefCheck, 260, 80, 111, 31, "packagesDeadbeefCheck", None],
                "packagesSmplayerPic": [self.packagesSmplayerPic, 400, 10, 71, 71, "packagesSmplayerPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/smplayer.png"],
                "packagesSmplayerCheck": [self.packagesSmplayerCheck, 390, 80, 102, 31, "packagesSmplayerCheck", None],
                "packagesVlcPic": [self.packagesVlcPic, 520, 10, 71, 71, "packagesVlcPic", "/usr/share/turbulence/images/manjaro-grey/packages/multimedia/vlc.png"],
                "packagesVlcCheck": [self.packagesVlcCheck, 510, 80, 102, 31, "packagesVlcCheck", None],
                "packagesGraphicsBack": [self.packagesGraphicsBack, -20, -10, 761, 241, "packagesGraphicsBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesBlenderPic": [self.packagesBlenderPic, 20, 10, 71, 71, "packagesBlenderPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/blender.png"],
                "packagesBlenderCheck": [self.packagesBlenderCheck, 10, 80, 111, 31, "packagesBlenderCheck", None],
                "packagesEvincePic": [self.packagesEvincePic, 140, 10, 71, 71, "packagesEvincePic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/evince.png"],
                "packagesEvinceCheck": [self.packagesEvinceCheck, 130, 80, 111, 31, "packagesEvinceCheck", None],
                "packagesGimpPic": [self.packagesGimpPic, 270, 10, 71, 71, "packagesGimpPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/gimp.png"],
                "packagesGimpCheck": [self.packagesGimpCheck, 260, 80, 111, 31, "packagesGimpCheck", None],
                "packagesGpicviewPic": [self.packagesGpicviewPic, 400, 10, 71, 71, "packagesGpicviewPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/gpicview.png"],
                "packagesGpicviewCheck": [self.packagesGpicviewCheck, 390, 80, 111, 31, "packagesGpicviewCheck", None],
                "packagesViewniorPic": [self.packagesViewniorPic, 520, 10, 71, 71, "packagesViewniorPic", "/usr/share/turbulence/images/manjaro-grey/packages/graphics/viewnior.png"],
                "packagesViewniorCheck": [self.packagesViewniorCheck, 510, 80, 111, 31, "packagesViewniorCheck", None],
                "packagesAccessoriesBack": [self.packagesAccessoriesBack, -20, -10, 761, 241, "packagesAccessoriesBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesGeanyPic": [self.packagesGeanyPic, 20, 10, 71, 71, "packagesGeanyPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/geany.png"],
                "packagesGeanyCheck": [self.packagesGeanyCheck, 10, 80, 111, 31, "packagesGeanyCheck", None],
                "packagesHexchatPic": [self.packagesHexchatPic, 140, 10, 71, 71, "packagesHexchatPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/hexchat.png"],
                "packagesHexchatCheck": [self.packagesHexchatCheck, 130, 80, 111, 31, "packagesHexchatCheck", None],
                "packagesLeafpadPic": [self.packagesLeafpadPic, 270, 10, 71, 71, "packagesLeafpadPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/leafpad.png"],
                "packagesLeafpadCheck": [self.packagesLeafpadCheck, 260, 80, 111, 31, "packagesLeafpadCheck", None],
                "packagesPcmanfmPic": [self.packagesPcmanfmPic, 400, 10, 71, 71, "packagesPcmanfmPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/pcmanfm.png"],
                "packagesPcmanfmCheck": [self.packagesPcmanfmCheck, 390, 80, 111, 31, "packagesPcmanfmCheck", None],
                "packagesSpacefmPic": [self.packagesSpacefmPic, 520, 10, 71, 71, "packagesSpacefmPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/spacefm.png"],
                "packagesSpacefmCheck": [self.packagesSpacefmCheck, 510, 80, 111, 31, "packagesSpacefmCheck", None],
                "packagesTerminatorPic": [self.packagesTerminatorPic, 640, 10, 71, 71, "packagesTerminatorPic", "/usr/share/turbulence/images/manjaro-grey/packages/accessories/terminator.png"],
                "packagesTerminatorCheck": [self.packagesTerminatorCheck, 630, 80, 111, 31, "packagesTerminatorCheck", None],
                "packagesThunarPic": [self.packagesThunarPic, 20, 110, 71, 71, "packagesThunarPic" , "/usr/share/turbulence/images/manjaro-grey/packages/accessories/thunar.png"],
                "packagesThunarCheck": [self.packagesThunarCheck, 10, 180, 111, 31, "packagesThunarCheck", None],
                "packagesExtrasBack": [self.packagesExtrasBack, -20, -10, 761, 241, "packagesExtrasBack", "/usr/share/turbulence/images/manjaro-grey/packages/packages-back.png"],
                "packagesAurSupportPic": [self.packagesAurSupportPic, 20, 10, 71, 71, "packagesAurSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/aursupport.png"],
                "packagesAurSupportCheck": [self.packagesAurSupportCheck, 10, 90, 111, 41, "packagesAurSupportCheck", None],
                "packagesMultimediaSupportPic": [self.packagesMultimediaSupportPic, 140, 10, 71, 71, "packagesMultimediaSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/multimediasupport.png"],
                "packagesMultimediaSupportCheck": [self.packagesMultimediaSupportCheck, 130, 90, 111, 34, "packagesMultimediaSupportCheck", None],
                "packagesPrinterSupportPic": [self.packagesPrinterSupportPic, 270, 10, 71, 71, "packagesPrinterSupportPic" , "/usr/share/turbulence/images/manjaro-grey/packages/extras/printersupport.png"],
                "packagesPrinterSupportCheck": [self.packagesPrinterSupportCheck, 260, 90, 111, 41, "packagesPrinterSupportCheck", None],
                "packagesInstallBack": [self.packagesInstallBack, -20, -10, 761, 241, "packagesInstallBack", None],
                "packagesInstallButton": [self.packagesInstallButton, 270, 95, 150, 30, "packagesInstallButton", None],
                "packagesCheckConnection": [self.packagesCheckConnection, 160, 400, 550, 60, "packagesCheckConnection", None]
            }
            
            fifthPageLayouts = {
                "packagesMenu": [self.packagesMenu, 0, 39, None, None, True, True, False],
                "packagesArrow": [self.packagesArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow.png"],
                "packagesMenuFinish": [self.packagesMenuFinish, 0, 39, None, None, True, True, False],
                "packagesForward": [self.packagesForward, 0, 34, None, None, True, True, False],
                "packagesPrevious": [self.packagesPrevious, 0, 34, None, None, True, True, False],
                "packagesCancel": [self.packagesCancel, 0, 34, None, None, True, True, False]
            }

            #defines all the widget parameters
            for widgetName, widgetSettings in fifthPageWidgets.items():
                widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
            for widgetName, widgetSettings in fifthPageLayouts.items():
                layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
            
            #Adds any custom widgets.
            self.packagesPrevious.setFlat(True)
            self.packagesForward.setFlat(True)
            self.packagesCancel.setFlat(True)
            self.packagesCheckConnection.setFlat(True)
            self.packagesInstallButton.setFlat(True)
            
            self.packagesDesc.setWordWrap(True)
        
            self.packagesPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesForward.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesCancel.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesCheckConnection.setFocusPolicy(QtCore.Qt.NoFocus)
            self.packagesInstallButton.setFocusPolicy(QtCore.Qt.NoFocus)
        
            self.packagesPrevious.setIcon(previousIcon)
            self.packagesForward.setIcon(forwardIcon)
            self.packagesCancel.setIcon(cancelIcon)
            self.packagesPrevious.setIconSize(QtCore.QSize(28, 30))
            self.packagesForward.setIconSize(QtCore.QSize(28, 30))
            self.packagesCancel.setIconSize(QtCore.QSize(16, 16))
         
            self.packagesNetwork.setObjectName("Network")
            self.packagesMultimedia.setObjectName("Multimedia")
            self.packagesGraphics.setObjectName("Graphics")
            self.packagesAccessories.setObjectName("Accessories")
            self.packagesExtras.setObjectName("Extras")
            self.packagesInstall.setObjectName("Install")
        
            self.packagesTabs.addTab(self.packagesNetwork, "")
            self.packagesTabs.addTab(self.packagesMultimedia, "")
            self.packagesTabs.addTab(self.packagesGraphics, "")
            self.packagesTabs.addTab(self.packagesAccessories, "")
            self.packagesTabs.addTab(self.packagesExtras, "")
            self.packagesTabs.addTab(self.packagesInstall, "")
            
            self.packagesMenuContainerHLayout.addWidget(self.packagesMenu)
            self.packagesMenuContainerHLayout.addWidget(self.packagesArrow)
            self.packagesMenuContainerHLayout.addWidget(self.packagesMenuFinish)
            self.packagesMenuContainerHLayout.addItem(self.packagesMenuSpacer)
            
            self.packagesFooterContainerHLayout.addWidget(self.packagesCancel)
            self.packagesFooterContainerHLayout.addItem(self.packagesFooterSpacer)
            self.packagesFooterContainerHLayout.addWidget(self.packagesPrevious)
            self.packagesFooterContainerHLayout.addWidget(self.packagesForward)
            
            self.packagesMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
            self.packagesFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
        
            self.packagesTabs.tabBar().setEnabled(False)
            self.stackedWidget.addWidget(self.Packages)
            
            #Handles button clicks
            self.packagesCancel.clicked.connect(MainWindow.close)
            self.packagesPrevious.clicked.connect(self.handleButtonPrev)
            self.packagesForward.clicked.connect(self.handleButtonNextPackages)
            self.packagesMenuFinish.clicked.connect(self.handleButtonNextPackages)
            self.packagesCheckConnection.clicked.connect(self.checkInternetStatus)
            self.packagesInstallButton.clicked.connect(self.handleButtonInstallPackages)
            
            #Fifth page            
            self.packagesHeader.setText(_translate("MainWindow", "Packages"))
            self.packagesMenu.setText(_translate("MainWindow", "Packages"))
            self.packagesMenuFinish.setText(_translate("MainWindow", "Finish"))
            self.packagesDesc.setText(_translate("MainWindow", "Here, you can choose what packages you would like to install. Hover over any of the packages to see a description, and select or unselect any packages you want to add or remove. Packages that are installed will be auto-selected.\n\nWhen you are done, go to the Install tab, and click \"Install\"."))
            self.packagesPrevious.setText(_translate("MainWindow", "Previous"))
            self.packagesForward.setText(_translate("MainWindow", "Forward"))
            self.packagesCancel.setText(_translate("MainWindow", "Cancel"))
            self.packagesCheckConnection.setText(_translate("MainWindow", "Check For Internet Connection"))
            self.packagesFirefoxPic.setToolTip(_translate("MainWindow", "Standalone web browser from mozilla.org"))
            self.packagesAroraPic.setToolTip(_translate("MainWindow", "Lightweight cross-platform Web browser"))
            self.packagesAroraCheck.setText("Arora")
            self.packagesChromiumPic.setToolTip(_translate("MainWindow", "The open-source project behind Google Chrome, an \n" "attempt at creating a safer, faster, and more stable browser"))
            self.packagesOperaPic.setToolTip(_translate("MainWindow", "Fast and secure web browser and Internet suite"))
            self.packagesTransmissionPic.setToolTip(_translate("MainWindow", "Fast, easy, and free BitTorrent client"))
            self.packagesFirefoxCheck.setText("Firefox")
            self.packagesMidoriPic.setToolTip(_translate("MainWindow", "Lightweight web browser (GTK2)"))
            self.packagesChromiumCheck.setText("Chomium")
            self.packagesOperaCheck.setText("Opera")
            self.packagesTransmissionCheck.setText("Transmission")
            self.packagesMidoriCheck.setText("Midori")
            self.packagesDelugePic.setToolTip(_translate("MainWindow", "A BitTorrent client with multiple user interfaces \n" "in a client/server model"))
            self.packagesDelugeCheck.setText("Deluge")
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesNetwork), _translate("MainWindow", "Network"))
            self.packagesVlcPic.setToolTip(_translate("MainWindow", "A multi-platform MPEG, VCD/DVD, and DivX player"))
            self.packagesVlcCheck.setText("VLC")
            self.packagesSmplayerPic.setToolTip(_translate("MainWindow", "A complete front-end for MPlayer"))
            self.packagesSmplayerCheck.setText("SMPlayer")
            self.packagesAudaciousPic.setToolTip(_translate("MainWindow", "Lightweight, advanced audio player focused on audio quality"))
            self.packagesAudaciousCheck.setText("Audacious")
            self.packagesClemetinePic.setToolTip(_translate("MainWindow", "A music player and library organizer"))
            self.packagesClementineCheck.setText("Clementine")
            self.packagesDeadbeefPic.setToolTip(_translate("MainWindow", "An audio player for GNU/Linux based on GTK2."))
            self.packagesDeadbeefCheck.setText("DeaDBeeF")
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesMultimedia), _translate("MainWindow", "Multimedia"))
            self.packagesBlenderPic.setToolTip(_translate("MainWindow", "A fully integrated 3D graphics creation suite"))
            self.packagesBlenderCheck.setText("Blender")
            self.packagesEvincePic.setToolTip(_translate("MainWindow", "Simply a document viewer"))
            self.packagesEvinceCheck.setText("Evince")
            self.packagesGimpPic.setToolTip(_translate("MainWindow", "GNU Image Manipulation Program"))
            self.packagesGimpCheck.setText("Gimp")
            self.packagesGpicviewPic.setToolTip(_translate("MainWindow", "Lightweight image viewer"))
            self.packagesGpicviewCheck.setText("GPicView")
            self.packagesViewniorPic.setToolTip(_translate("MainWindow", "A simple, fast and elegant image viewer program"))
            self.packagesViewniorCheck.setText("Viewnior")
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesGraphics), _translate("MainWindow", "Graphics"))
            self.packagesGeanyPic.setToolTip(_translate("MainWindow", "Fast and lightweight IDE"))
            self.packagesGeanyCheck.setText("Geany")
            self.packagesHexchatPic.setToolTip(_translate("MainWindow", "A popular and easy to use graphical IRC (chat) client"))
            self.packagesHexchatCheck.setText("Hexchat")
            self.packagesLeafpadPic.setToolTip(_translate("MainWindow", "A notepad clone for GTK+ 2.0"))
            self.packagesLeafpadCheck.setText("Leafpad")
            self.packagesPcmanfmPic.setToolTip(_translate("MainWindow", "An extremely fast and lightweight file manager"))
            self.packagesPcmanfmCheck.setText("PCManFM")
            self.packagesSpacefmPic.setToolTip(_translate("MainWindow", "Multi-panel tabbed file manager"))
            self.packagesSpacefmCheck.setText("SpaceFM")
            self.packagesTerminatorPic.setToolTip(_translate("MainWindow", "Terminal emulator that supports tabs and grids"))
            self.packagesTerminatorCheck.setText("Terminator")
            self.packagesThunarPic.setToolTip(_translate("MainWindow", "Modern file manager for Xfce"))
            self.packagesThunarCheck.setText("Thunar")
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesAccessories), _translate("MainWindow", "Accessories"))
            self.packagesAurSupportPic.setToolTip(_translate("MainWindow", "Installs yaourt, and required dependencies to access the AUR"))
            self.packagesAurSupportCheck.setText("Aur \nSupport")
            self.packagesMultimediaSupportPic.setToolTip(_translate("MainWindow", "Installs flashplugin, and required codecs for playing media"))
            self.packagesMultimediaSupportCheck.setText("Multimedia \nSupport")
            self.packagesPrinterSupportPic.setToolTip(_translate("MainWindow", "Installs manjaro-printer, and CUPS to enable printers"))
            self.packagesPrinterSupportCheck.setText("Printer \nSupport")
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesExtras), _translate("MainWindow", "Extras"))
            self.packagesTabs.setTabText(self.packagesTabs.indexOf(self.packagesInstall), _translate("MainWindow", "Install"))
            self.packagesInstallButton.setText(_translate("MainWindow", "Install"))
        
        
        #Adds the fifth and final page
        self.Finish = QtWidgets.QWidget()
        self.Finish.setObjectName("Finish")
        
        createStaticWidgets(self.Finish)
        
        self.finishHeader = QtWidgets.QLabel(self.Finish)
        self.finishMenuContainer = QtWidgets.QWidget(self.Finish)
        self.finishMenuContainerHLayout = QtWidgets.QHBoxLayout(self.finishMenuContainer)
        self.finishWallpaperMenu = QtWidgets.QPushButton(self.finishMenuContainer)
        self.finishMenu = QtWidgets.QPushButton(self.finishMenuContainer)
        self.finishArrow = QtWidgets.QLabel(self.finishMenuContainer)
        self.finishMenuSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.finishFooterContainer = QtWidgets.QWidget(self.Finish)
        self.finishFooterContainerHLayout = QtWidgets.QHBoxLayout(self.finishFooterContainer)
        self.finishCancel = QtWidgets.QPushButton(self.finishFooterContainer)
        self.finishForward = QtWidgets.QPushButton(self.finishFooterContainer)
        self.finishPrevious = QtWidgets.QPushButton(self.finishFooterContainer)
        self.finishFooterSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.finishDesc = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettings = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettingsPic = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettingsDesc = QtWidgets.QLabel(self.Finish)
        self.finishSystemSettingsButton = QtWidgets.QPushButton(self.Finish)
        self.finishHelpHead = QtWidgets.QLabel(self.Finish)
        self.finishHelpPic = QtWidgets.QLabel(self.Finish)
        self.finishHelpDesc = QtWidgets.QLabel(self.Finish)
        self.finishHelpButton = QtWidgets.QPushButton(self.Finish)
        
        if openboxStatus:
            self.finishWallpaperMenu.setText(_translate("MainWindow", "Packages"))
        elif nitrogenStatus or plasmaStatus:
            self.finishWallpaperMenu.setText(_translate("MainWindow", "Wallpapers"))
        elif tintStatus:
            self.finishWallpaperMenu.setText(_translate("MainWindow", "Tint 2"))
        elif kwinStatus:
            self.finishWallpaperMenu.setText(_translate("MainWindow", "Themes"))
        else:
            self.finishWallpaperMenu.setText(_translate("MainWindow", "Folders"))
         
        finalPageWidgets = {
            "finishHeader": [self.finishHeader, 80, 20, 600, 51, "finishHeader", None],
            "finishDesc": [self.finishDesc, 30, 150, 781, 51, "finishDesc", None],
            "finishSystemSettings": [self.finishSystemSettings, 40, 220, 500, 31, "finishSystemSettings", None],
            "finishSystemSettingsPic": [self.finishSystemSettingsPic, 70, 260, 111, 101, "finishSystemSettingsPic", "/usr/share/turbulence/images/manjaro-grey/finish/preferences-system.png"],
            "finishSystemSettingsDesc": [self.finishSystemSettingsDesc, 200, 280, 390, 31, "finishSystemSettingsDesc", None],
            "finishSystemSettingsButton": [self.finishSystemSettingsButton, 200, 310, 390, 41, "finishSystemSettingsButton", None],
            "finishHelpHead": [self.finishHelpHead, 40, 400, 500, 31, "finishHelpHead", None, None],
            "finishHelpPic": [self.finishHelpPic, 70, 440, 111, 101, "finishHelpPic", "/usr/share/turbulence/images/manjaro-grey/finish/help-icon.png"],
            "finishHelpDesc": [self.finishHelpDesc, 200, 440, 390, 51, "finishHelpDesc", None],
            "finishHelpButton": [self.finishHelpButton, 200, 490, 390, 41, "finishHelpButton", None]
        }

        fifthPageLayouts = {
            "finishWallpaperMenu": [self.finishWallpaperMenu, 0, 39, None, None, True, True, False],
            "finishArrow": [self.finishArrow, None, None, 21, 500, False, False, "/usr/share/turbulence/images/manjaro-grey/menu-arrow-reverse.png"],
            "finishMenu": [self.finishMenu, 0, 39, None, None, True, True, False],
            "finishForward": [self.finishForward, 0, 34, None, None, True, True, False],
            "finishPrevious": [self.finishPrevious, 0, 34, None, None, True, True, False],
            "finishCancel": [self.finishCancel, 0, 34, None, None, True, True, False]
        }
	
        #defines all the widget parameters
        for widgetName, widgetSettings in finalPageWidgets.items():
            widgetConfigurer(widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6])
        
        for widgetName, widgetSettings in fifthPageLayouts.items():
            layoutConfigurer(widgetName, widgetSettings[0], widgetSettings[1], widgetSettings[2], widgetSettings[3], widgetSettings[4], widgetSettings[5], widgetSettings[6], widgetSettings[7])
            
        #Defines the custom settings
        self.finishSystemSettingsButton.setFlat(True)
        self.finishHelpButton.setFlat(True)
        
        self.finishDesc.setWordWrap(True)
        self.finishSystemSettingsDesc.setWordWrap(True)
        self.finishHelpDesc.setWordWrap(True)
        
        self.finishSystemSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.finishHelpButton.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.finishCancel.setIcon(cancelIcon)
        self.finishForward.setIcon(finishIcon)
        self.finishPrevious.setIcon(previousIcon)
        self.finishForward.setIconSize(QtCore.QSize(16, 18))
        self.finishPrevious.setIconSize(QtCore.QSize(28, 30))
        self.finishCancel.setIconSize(QtCore.QSize(16, 16))
        
        self.finishMenuContainerHLayout.addWidget(self.finishWallpaperMenu)
        self.finishMenuContainerHLayout.addWidget(self.finishArrow)
        self.finishMenuContainerHLayout.addWidget(self.finishMenu)
        self.finishMenuContainerHLayout.addItem(self.finishMenuSpacer)
            
        self.finishFooterContainerHLayout.addWidget(self.finishCancel)
        self.finishFooterContainerHLayout.addItem(self.finishFooterSpacer)
        self.finishFooterContainerHLayout.addWidget(self.finishPrevious)
        self.finishFooterContainerHLayout.addWidget(self.finishForward)
            
        self.finishMenuContainer.setGeometry(QtCore.QRect(lMinW, lMinH, lMaxW, lMaxH))
        self.finishFooterContainer.setGeometry(QtCore.QRect(15, 567, 830, 51))
            
        self.stackedWidget.addWidget(self.Finish)
        
        #Handles the button click
        self.finishWallpaperMenu.clicked.connect(self.handleButtonPrev)
        self.finishHelpButton.clicked.connect(self.handleButtonLaunchHelp)
        self.finishCancel.clicked.connect(MainWindow.close)
        self.finishPrevious.clicked.connect(self.handleButtonPrev)
        self.finishForward.clicked.connect(MainWindow.close)
        
        #Translates the widgets, or sets text
        self.finishHeader.setText(_translate("MainWindow", "Congratulations!"))
        self.finishMenu.setText(_translate("MainWindow", "Finish"))
        self.finishCancel.setText(_translate("MainWindow", "Cancel"))
        self.finishForward.setText(_translate("MainWindow", "Finish"))
        self.finishPrevious.setText(_translate("MainWindow", "Previous"))
        self.finishDesc.setText(_translate("MainWindow", "All of your settings have been applied. Now, you can start enjoying Manjaro, or look at some of the programs and links below. Also, if you haven\'t already, make sure to join the Manjaro community as well!"))
        self.finishHelpHead.setText(_translate("MainWindow", "Help"))
        self.finishHelpDesc.setText(_translate("MainWindow", "For help and support, you can visit Manjaro.org for access to a terrific forum, wiki, and IRC!"))
        self.finishHelpButton.setText(_translate("MainWindow", "Launch Manjaro.org"))
        
        if kdeStatus:
            self.finishSystemSettings.setText(_translate("MainWindow", "System Settings"))
            self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of the KDE desktop, and more."))
            self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch System Settings"))
            self.finishSystemSettingsButton.clicked.connect(self.handleButtonSystemSettings)
        elif openboxStatus:
            self.finishSystemSettings.setText(_translate("MainWindow", "Customize OpenBox"))
            self.finishSystemSettingsDesc.setText(_translate("MainWindow", "Control panel to edit various aspects of OpenBox"))
            self.finishSystemSettingsButton.setText(_translate("MainWindow", "Launch Customize Look and Feel"))
            self.finishSystemSettingsButton.clicked.connect(self.handleButtonlxappearance)
        
        
        #Configures the window a bit more.
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Turbulence")
        self.stackedWidget.setCurrentIndex(0) #Sets the index for the stacked widget to 0.
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #sets the current checked boxes and status. It's at the bottom to be out of the way.
        neededDirs = folders.findKeyDir('active')
        neededFolders = {
            "DESKTOP": [self.folderActive1, self.folderHeader1],
            "DOCUMENTS": [self.folderActive2, self.folderHeader2],
            "DOWNLOAD": [self.folderActive3, self.folderHeader3],
            "MUSIC": [self.folderActive4, self.folderHeader4],
            "PICTURES": [self.folderActive5, self.folderHeader5],
            "PUBLICSHARE": [self.folderActive6, self.folderHeader6],
            "TEMPLATES": [self.folderActive7, self.folderHeader7],
            "VIDEOS": [self.folderActive8, self.folderHeader8]
        }

        for x in neededDirs:
            for y in neededDirs:
                if folders.getObject(neededDirs, y, 'bool'): 
                    neededname = folders.getObject(neededDirs, y, 'name')
                    for neededName, folderWidgets in neededFolders.items():
                        if neededName == y:
                            folderWidgets[0].setChecked(True)
                            folderWidgets[1].setText(_translate("MainWindow", "Status: Active", None))
                            break
        
        
    #Moves to next page in the stacked widget.
    def handleButtonNext(self):
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFolders')
            
            
    #Moved to the next page, but also applies to settings for folders.
    def handleButtonNextFolders(self):
        checkboxDirectoryPairs = {
            self.folderActive1: ["Desktop", "XDG_DESKTOP_DIR"],
            self.folderActive2: ["Documents", "XDG_DOCUMENTS_DIR"],
            self.folderActive3: ["Downloads", "XDG_DOWNLOAD_DIR"],
            self.folderActive4: ["Music", "XDG_MUSIC_DIR"],
            self.folderActive5: ["Pictures", "XDG_PICTURES_DIR"],
            self.folderActive6: ["Public", "XDG_PUBLICSHARE_DIR"],
            self.folderActive7: ["Templates", "XDG_TEMPLATES_DIR"],
            self.folderActive8: ["Videos", "XDG_VIDEOS_DIR"]
        }

        for checkbox, directoryPoint in checkboxDirectoryPairs.items():
            if checkbox.isChecked():
                folders.createDir(directoryPoint[0], directoryPoint[1])
                logger.writeLog('folderChosen', directoryPoint[0])
            else:
                folders.deleteDir(directoryPoint[1])
                logger.writeLog('folderNotChosen', directoryPoint[1])
            
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToThemes')

    #Moves next a page, but also applies to settings for themes.
    def handleButtonNextThemes(self):
        kwinThemes = {
            "air-black": self.themeRadio1,
            "cupertino-ish": self.themeRadio2,
            "oxygen": self.themeRadio3,
            "plastik": self.themeRadio4,
        }
            
        for themeName, themeRadio in kwinThemes.items():
            if themeRadio.isChecked():
                themes.kwinThemer(themeName)
                plasma_control.startKwin()

        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToWallpapers')
            
    #Moves next a page, but also applies to settings for tint.
    def handleButtonNextTint(self):
        Tint = {
            "top": self.tintPositionRadio1,
            "right": self.tintPositionRadio2,
            "bottom": self.tintPositionRadio3,
            "left": self.tintPositionRadio4,
        }
        
        for tintPosition, tintRadio in Tint.items():
            if tintRadio.isChecked():
                tint.panelPosition(tintPosition)
                ob_control.killTintTwoPlus()

        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToWallpapers')
    
    #Moves next a page, but also applies the wallpaper settings.
    def handleButtonNextWallpapers(self):
        if kdeStatus:
            wallpapersDict = {
                "manjarostyle": self.wallpaperChoice1,
                "orangeSplash": self.wallpaperChoice2,
                "sunsetPlane": self.wallpaperChoice3,
                "mountainLake": self.wallpaperChoice4,
                "earthInSpace": self.wallpaperChoice5,
                "darkStairs": self.wallpaperChoice6,
                "cherryJapan": self.wallpaperChoice7,
                "whiteTiger": self.wallpaperChoice8
            }
            edition = "kde"
        elif nitrogenStatus:
            wallpapersDict = {
                "evodark": self.wallpaperChoice1,
                "evolight": self.wallpaperChoice2,
                "sunsetPlane": self.wallpaperChoice3,
                "mountainLake": self.wallpaperChoice4,
                "earthInSpace": self.wallpaperChoice5,
                "darkStairs": self.wallpaperChoice6,
                "cherryJapan": self.wallpaperChoice7,
                "whiteTiger": self.wallpaperChoice8
            }
            edition = "openbox"
        else:
            wallpapersDict = {
                "ozoneTurbulence": self.wallpaperChoice1,
                "orangeSplash": self.wallpaperChoice2,
                "sunsetPlane": self.wallpaperChoice3,
                "mountainLake": self.wallpaperChoice4,
                "earthInSpace": self.wallpaperChoice5,
                "darkStairs": self.wallpaperChoice6,
                "cherryJapan": self.wallpaperChoice7,
                "whiteTiger": self.wallpaperChoice8
            }
            edition = "kde"
        
        for wallpaperName, wallpaperRadio in wallpapersDict.items():
            if wallpaperRadio.isChecked():
                wallpapers.changeWallpaperPlus(wallpaperName, edition)
                
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToPackages')

            
    def handleButtonNextPackages(self):
        index = self.stackedWidget.currentIndex() + 1
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            logger.writeLog('proceedToFinal')
    
    #Moves from the folder slide toward the package installer.
    def handleButtonInstallPackages(self):
        packagesMFI = {
            "arora": self.packagesAroraCheck, 
            "chromium": self.packagesChromiumCheck, 
            "deluge": self.packagesDelugeCheck,
            "firefox": self.packagesFirefoxCheck,
            "midori": self.packagesMidoriCheck,
            "opera": self.packagesOperaCheck, 
            "transmission-gtk": self.packagesTransmissionCheck,
            "audacious": self.packagesAudaciousCheck,
            "clementine": self.packagesClementineCheck,
            "deadbeef": self.packagesDeadbeefCheck, 
            "smplayer": self.packagesSmplayerCheck,
            "vlc": self.packagesVlcCheck,
            "blender": self.packagesBlenderCheck,
            "evince": self.packagesEvinceCheck,
            "gimp": self.packagesGimpCheck,
            "gpicview": self.packagesGpicviewCheck,
            "viewnior": self.packagesViewniorCheck,
            "geany": self.packagesGeanyCheck,
            "hexchat": self.packagesHexchatCheck,
            "leafpad": self.packagesLeafpadCheck,
            "pcmanfm": self.packagesPcmanfmCheck,
            "spacefm": self.packagesSpacefmCheck,
            "terminator": self.packagesTerminatorCheck,
            "thunar": self.packagesThunarCheck,
            "yaourt": self.packagesAurSupportCheck, #Aur support
            "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
            "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
            
        }
        #self.installButton.lower()
        packagesTBIList = []
        packagesTBRList = []
        for packageName, packageCheck in packagesMFI.items():
            if packageCheck.isChecked():
                packagesTBIList.append(packageName)
            else:
                packagesTBRList.append(packageName)
        packages.handlePackages(packagesTBIList, packagesTBRList)
	    
    def checkInternetStatus(self):
        packagesList = packages.getCurrentPackages()
        if packages.checkInternet():
            self.packagesTabs.tabBar().setEnabled(True)
            self.packagesCheckConnection.lower()
            self.packagesNotActive.lower()
            logger.writeLog("checkInternetStatusPassed")
        else:
            self.packagesCheckConnection.setText(_translate("MainWindow", "Failed. Please Try Again.", None))
            logger.writeLog("checkInternetStatusFailed")
        
        packagesMFI = {
            "arora": self.packagesAroraCheck, 
            "chromium": self.packagesChromiumCheck, 
            "deluge": self.packagesDelugeCheck,
            "firefox": self.packagesFirefoxCheck,
            "midori": self.packagesMidoriCheck,
            "opera": self.packagesOperaCheck, 
            "transmission-gtk": self.packagesTransmissionCheck,
            "audacious": self.packagesAudaciousCheck,
            "clementine": self.packagesClementineCheck,
            "deadbeef": self.packagesDeadbeefCheck, 
            "smplayer": self.packagesSmplayerCheck,
            "vlc": self.packagesVlcCheck,
            "blender": self.packagesBlenderCheck,
            "evince": self.packagesEvinceCheck,
            "gimp": self.packagesGimpCheck,
            "gpicview": self.packagesGpicviewCheck,
            "viewnior": self.packagesViewniorCheck,
            "geany": self.packagesGeanyCheck,
            "hexchat": self.packagesHexchatCheck,
            "leafpad": self.packagesLeafpadCheck,
            "pcmanfm": self.packagesPcmanfmCheck,
            "spacefm": self.packagesSpacefmCheck,
            "terminator": self.packagesTerminatorCheck,
            "thunar": self.packagesThunarCheck,
            "yaourt": self.packagesAurSupportCheck, #Aur support
            "flashplugin": self.packagesMultimediaSupportCheck, #Multimedia support
            "manjaro-printer": self.packagesPrinterSupportCheck #Printing support
        }
        packagesAI = set(packagesList).intersection(packagesMFI)
        packagesAIList = list(packagesAI)
        
        for packagesItem in packagesAIList:
            packagesMFI[packagesItem].setChecked(True)	
            
    #Moves back from the themes to folders, and reloads the settings for folders.
    def handleButtonPrevFolders(self):
        checkboxDirectoryPairs = {
            "Desktop": [self.folderActive1, self.folderHeader1],
            "Documents": [self.folderActive2, self.folderHeader2],
            "Downloads": [self.folderActive3, self.folderHeader3],
            "Music": [self.folderActive4, self.folderHeader4],
            "Pictures": [self.folderActive5, self.folderHeader5],
            "Public": [self.folderActive6, self.folderHeader6],
            "Templates": [self.folderActive7, self.folderHeader7],
            "Videos": [self.folderActive8, self.folderHeader8]
        }

        for directoryPoint, folderWidgets in checkboxDirectoryPairs.items():
            if folderWidgets[0].isChecked():
                folderWidgets[1].setText(_translate("MainWindow", "Status: Active", None))
            else:
                folderWidgets[1].setText(_translate("MainWindow", "Status: Deactivated", None))
                
        index = self.stackedWidget.currentIndex() - 1
        if index >= 0:
            self.stackedWidget.setCurrentIndex(index)
            
    def handleButtonSystemSettings(self):
        final.launchSystemSettings()
        
    def handleButtonlxappearance(self):
        final.launchAppearance()
        
    def handleButtonLaunchHelp(self):
        final.launchHelp()

    #Just moves back a page..
    def handleButtonPrev(self):
        index = self.stackedWidget.currentIndex() - 1
        if index >= 0:
            self.stackedWidget.setCurrentIndex(index)