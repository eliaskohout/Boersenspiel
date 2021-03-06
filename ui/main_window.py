# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(851, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_portfolio = QtWidgets.QWidget()
        self.tab_portfolio.setObjectName("tab_portfolio")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_portfolio)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_portfolio)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_gekaufteAktien = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_gekaufteAktien.setObjectName("listWidget_gekaufteAktien")
        self.horizontalLayout.addWidget(self.listWidget_gekaufteAktien)
        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_begruessung = QtWidgets.QLabel(self.tab_portfolio)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_begruessung.setFont(font)
        self.label_begruessung.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_begruessung.setObjectName("label_begruessung")
        self.verticalLayout_2.addWidget(self.label_begruessung)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_portfolio)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_guthaben = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_guthaben.setFont(font)
        self.label_guthaben.setObjectName("label_guthaben")
        self.gridLayout_3.addWidget(self.label_guthaben, 1, 0, 1, 1)
        self.label_depotwert = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_depotwert.setFont(font)
        self.label_depotwert.setObjectName("label_depotwert")
        self.gridLayout_3.addWidget(self.label_depotwert, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_portfolio)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.listWidget_historie = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_historie.setObjectName("listWidget_historie")
        self.gridLayout_12.addWidget(self.listWidget_historie, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_portfolio, "")
        self.tab_suche = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_suche.sizePolicy().hasHeightForWidth())
        self.tab_suche.setSizePolicy(sizePolicy)
        self.tab_suche.setAutoFillBackground(False)
        self.tab_suche.setObjectName("tab_suche")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_suche)
        self.gridLayout_2.setContentsMargins(50, 20, 50, 20)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_suche)
        self.splitter_2.setAutoFillBackground(False)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(15)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 25))
        self.splitter.setAutoFillBackground(False)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.plainTextEdit_aktiensuche = QtWidgets.QPlainTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_aktiensuche.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_aktiensuche.setSizePolicy(sizePolicy)
        self.plainTextEdit_aktiensuche.setMaximumSize(QtCore.QSize(16777215, 25))
        self.plainTextEdit_aktiensuche.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_aktiensuche.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_aktiensuche.setTabChangesFocus(True)
        self.plainTextEdit_aktiensuche.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_aktiensuche.setPlainText("")
        self.plainTextEdit_aktiensuche.setOverwriteMode(False)
        self.plainTextEdit_aktiensuche.setBackgroundVisible(False)
        self.plainTextEdit_aktiensuche.setObjectName("plainTextEdit_aktiensuche")
        self.pushButton_aktiensuche = QtWidgets.QPushButton(self.splitter)
        self.pushButton_aktiensuche.setObjectName("pushButton_aktiensuche")
        self.listWidget_suchergebnis = QtWidgets.QListWidget(self.splitter_2)
        self.listWidget_suchergebnis.setObjectName("listWidget_suchergebnis")
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_suche, "")
        self.tab_einstellungen = QtWidgets.QWidget()
        self.tab_einstellungen.setEnabled(True)
        self.tab_einstellungen.setObjectName("tab_einstellungen")
        self.groupBox_ordergebueren_aendern = QtWidgets.QGroupBox(self.tab_einstellungen)
        self.groupBox_ordergebueren_aendern.setEnabled(True)
        self.groupBox_ordergebueren_aendern.setGeometry(QtCore.QRect(360, 140, 331, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_ordergebueren_aendern.sizePolicy().hasHeightForWidth())
        self.groupBox_ordergebueren_aendern.setSizePolicy(sizePolicy)
        self.groupBox_ordergebueren_aendern.setMaximumSize(QtCore.QSize(1000, 1000))
        self.groupBox_ordergebueren_aendern.setObjectName("groupBox_ordergebueren_aendern")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_ordergebueren_aendern)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox_OrderGebuehr = QtWidgets.QSpinBox(self.groupBox_ordergebueren_aendern)
        self.spinBox_OrderGebuehr.setMaximum(100)
        self.spinBox_OrderGebuehr.setObjectName("spinBox_OrderGebuehr")
        self.horizontalLayout_4.addWidget(self.spinBox_OrderGebuehr)
        self.label_waehrung_ordergebuehren = QtWidgets.QLabel(self.groupBox_ordergebueren_aendern)
        self.label_waehrung_ordergebuehren.setObjectName("label_waehrung_ordergebuehren")
        self.horizontalLayout_4.addWidget(self.label_waehrung_ordergebuehren)
        self.pushButton_refresh_Gebuehr = QtWidgets.QPushButton(self.groupBox_ordergebueren_aendern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh_Gebuehr.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh_Gebuehr.setSizePolicy(sizePolicy)
        self.pushButton_refresh_Gebuehr.setObjectName("pushButton_refresh_Gebuehr")
        self.horizontalLayout_4.addWidget(self.pushButton_refresh_Gebuehr)
        self.groupBox_depotguthaben_aendern = QtWidgets.QGroupBox(self.tab_einstellungen)
        self.groupBox_depotguthaben_aendern.setGeometry(QtCore.QRect(360, 20, 331, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_depotguthaben_aendern.sizePolicy().hasHeightForWidth())
        self.groupBox_depotguthaben_aendern.setSizePolicy(sizePolicy)
        self.groupBox_depotguthaben_aendern.setObjectName("groupBox_depotguthaben_aendern")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_depotguthaben_aendern)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_Depotguthaben = QtWidgets.QSpinBox(self.groupBox_depotguthaben_aendern)
        self.spinBox_Depotguthaben.setMaximum(100000000)
        self.spinBox_Depotguthaben.setSingleStep(10000)
        self.spinBox_Depotguthaben.setObjectName("spinBox_Depotguthaben")
        self.horizontalLayout_2.addWidget(self.spinBox_Depotguthaben)
        self.label_waehrung_depotguthaben_aendern = QtWidgets.QLabel(self.groupBox_depotguthaben_aendern)
        self.label_waehrung_depotguthaben_aendern.setObjectName("label_waehrung_depotguthaben_aendern")
        self.horizontalLayout_2.addWidget(self.label_waehrung_depotguthaben_aendern)
        self.pushButton_refresh_DepotGuthaben = QtWidgets.QPushButton(self.groupBox_depotguthaben_aendern)
        self.pushButton_refresh_DepotGuthaben.setObjectName("pushButton_refresh_DepotGuthaben")
        self.horizontalLayout_2.addWidget(self.pushButton_refresh_DepotGuthaben)
        self.groupBox_profile = QtWidgets.QGroupBox(self.tab_einstellungen)
        self.groupBox_profile.setGeometry(QtCore.QRect(10, 130, 331, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_profile.sizePolicy().hasHeightForWidth())
        self.groupBox_profile.setSizePolicy(sizePolicy)
        self.groupBox_profile.setObjectName("groupBox_profile")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_profile)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_profil_loeschen = QtWidgets.QPushButton(self.groupBox_profile)
        self.pushButton_profil_loeschen.setObjectName("pushButton_profil_loeschen")
        self.gridLayout_11.addWidget(self.pushButton_profil_loeschen, 2, 1, 1, 1)
        self.pushButton_neues_profil = QtWidgets.QPushButton(self.groupBox_profile)
        self.pushButton_neues_profil.setObjectName("pushButton_neues_profil")
        self.gridLayout_11.addWidget(self.pushButton_neues_profil, 2, 2, 1, 1)
        self.listWidget_profile = QtWidgets.QListWidget(self.groupBox_profile)
        self.listWidget_profile.setObjectName("listWidget_profile")
        self.gridLayout_11.addWidget(self.listWidget_profile, 4, 0, 1, 3)
        self.pushButton_profil_laden = QtWidgets.QPushButton(self.groupBox_profile)
        self.pushButton_profil_laden.setObjectName("pushButton_profil_laden")
        self.gridLayout_11.addWidget(self.pushButton_profil_laden, 2, 0, 1, 1)
        self.groupBox_waehrung = QtWidgets.QGroupBox(self.tab_einstellungen)
        self.groupBox_waehrung.setGeometry(QtCore.QRect(360, 250, 331, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_waehrung.sizePolicy().hasHeightForWidth())
        self.groupBox_waehrung.setSizePolicy(sizePolicy)
        self.groupBox_waehrung.setObjectName("groupBox_waehrung")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_waehrung)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.plainTextEdit_Waehrung = QtWidgets.QPlainTextEdit(self.groupBox_waehrung)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_Waehrung.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_Waehrung.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_Waehrung.setFont(font)
        self.plainTextEdit_Waehrung.setObjectName("plainTextEdit_Waehrung")
        self.gridLayout_6.addWidget(self.plainTextEdit_Waehrung, 0, 0, 1, 1)
        self.pushButton_refresh_waehrung = QtWidgets.QPushButton(self.groupBox_waehrung)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh_waehrung.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh_waehrung.setSizePolicy(sizePolicy)
        self.pushButton_refresh_waehrung.setObjectName("pushButton_refresh_waehrung")
        self.gridLayout_6.addWidget(self.pushButton_refresh_waehrung, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_einstellungen)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 331, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_ticker_aktualisieren = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_ticker_aktualisieren.setGeometry(QtCore.QRect(20, 30, 121, 22))
        self.pushButton_ticker_aktualisieren.setObjectName("pushButton_ticker_aktualisieren")
        self.tabWidget.addTab(self.tab_einstellungen, "")
        self.tab_aktieninfo = QtWidgets.QWidget()
        self.tab_aktieninfo.setEnabled(True)
        self.tab_aktieninfo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_aktieninfo.setObjectName("tab_aktieninfo")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_aktieninfo)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_aktieninfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.spinBox_anzahlKaufen = QtWidgets.QSpinBox(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_anzahlKaufen.setFont(font)
        self.spinBox_anzahlKaufen.setObjectName("spinBox_anzahlKaufen")
        self.pushButton_kaufen = QtWidgets.QPushButton(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_kaufen.sizePolicy().hasHeightForWidth())
        self.pushButton_kaufen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_kaufen.setFont(font)
        self.pushButton_kaufen.setObjectName("pushButton_kaufen")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtWidgets.QSplitter(self.tab_aktieninfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.spinBox_anzahlVerkaufen = QtWidgets.QSpinBox(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_anzahlVerkaufen.setFont(font)
        self.spinBox_anzahlVerkaufen.setObjectName("spinBox_anzahlVerkaufen")
        self.pushButton_verkaufen = QtWidgets.QPushButton(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_verkaufen.sizePolicy().hasHeightForWidth())
        self.pushButton_verkaufen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_verkaufen.setFont(font)
        self.pushButton_verkaufen.setObjectName("pushButton_verkaufen")
        self.verticalLayout.addWidget(self.splitter_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_preis = QtWidgets.QLabel(self.tab_aktieninfo)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_preis.setFont(font)
        self.label_preis.setAlignment(QtCore.Qt.AlignCenter)
        self.label_preis.setObjectName("label_preis")
        self.horizontalLayout_3.addWidget(self.label_preis)
        self.pushButton_preis = QtWidgets.QPushButton(self.tab_aktieninfo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_preis.setFont(font)
        self.pushButton_preis.setObjectName("pushButton_preis")
        self.horizontalLayout_3.addWidget(self.pushButton_preis)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_imBesitz = QtWidgets.QLabel(self.tab_aktieninfo)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_imBesitz.setFont(font)
        self.label_imBesitz.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imBesitz.setObjectName("label_imBesitz")
        self.verticalLayout.addWidget(self.label_imBesitz)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.plotWidget = PlotWidget(self.tab_aktieninfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_5.addWidget(self.plotWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_aktieninfo, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.plainTextEdit_aktiensuche.textChanged.connect(self.pushButton_aktiensuche.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "B??rsenspiel"))
        self.groupBox.setTitle(_translate("Form", "Aktiendepot"))
        self.label_begruessung.setText(_translate("Form", "Hallo, Bob!"))
        self.groupBox_2.setTitle(_translate("Form", "Depot??bersicht"))
        self.label_guthaben.setText(_translate("Form", "234.00???"))
        self.label_depotwert.setText(_translate("Form", "000.00 ???"))
        self.groupBox_3.setTitle(_translate("Form", "Historie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_portfolio), _translate("Form", "Portfolio"))
        self.plainTextEdit_aktiensuche.setPlaceholderText(_translate("Form", "Suche nach Aktien..."))
        self.pushButton_aktiensuche.setText(_translate("Form", "Suche"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_suche), _translate("Form", "Suchen"))
        self.groupBox_ordergebueren_aendern.setTitle(_translate("Form", " Ordergeb??hren ??ndern (Preis je Aktienverkauf und -kauf):"))
        self.label_waehrung_ordergebuehren.setText(_translate("Form", "            Euro"))
        self.pushButton_refresh_Gebuehr.setText(_translate("Form", "Refresh"))
        self.groupBox_depotguthaben_aendern.setTitle(_translate("Form", "Depotguthaben ??ndern:"))
        self.label_waehrung_depotguthaben_aendern.setText(_translate("Form", "            Euro"))
        self.pushButton_refresh_DepotGuthaben.setText(_translate("Form", "Refresh"))
        self.groupBox_profile.setTitle(_translate("Form", "Profile"))
        self.pushButton_profil_loeschen.setText(_translate("Form", "L??schen"))
        self.pushButton_neues_profil.setText(_translate("Form", "Neu"))
        self.pushButton_profil_laden.setText(_translate("Form", "Laden"))
        self.groupBox_waehrung.setTitle(_translate("Form", "W??hrung"))
        self.pushButton_refresh_waehrung.setText(_translate("Form", "Refresh"))
        self.groupBox_4.setTitle(_translate("Form", "Allgemeines"))
        self.pushButton_ticker_aktualisieren.setText(_translate("Form", "Ticker aktualisieren"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_einstellungen), _translate("Form", "Einstellungen"))
        self.pushButton_kaufen.setText(_translate("Form", "Kaufen"))
        self.pushButton_verkaufen.setText(_translate("Form", "Verkaufen"))
        self.label_preis.setText(_translate("Form", "0 ???"))
        self.pushButton_preis.setText(_translate("Form", "Preis"))
        self.label_imBesitz.setText(_translate("Form", "Im Besitz: 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_aktieninfo), _translate("Form", "Aktieninfo"))
from pyqtgraph import PlotWidget
