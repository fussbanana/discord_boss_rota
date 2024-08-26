# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    Qt,
)
from PySide6.QtWidgets import (
    QLineEdit,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QWidget,
)


class Ui_BossRota(object):
    def setupUi(self, BossRota):
        if not BossRota.objectName():
            BossRota.setObjectName("BossRota")
        BossRota.resize(479, 289)
        self.centralwidget = QWidget(BossRota)
        self.centralwidget.setObjectName("centralwidget")
        self.line_edit_boss = QLineEdit(self.centralwidget)
        self.line_edit_boss.setObjectName("line_edit_boss")
        self.line_edit_boss.setGeometry(QRect(20, 20, 131, 30))
        self.line_edit_boss.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_edit_rota = QLineEdit(self.centralwidget)
        self.line_edit_rota.setObjectName("line_edit_rota")
        self.line_edit_rota.setGeometry(QRect(20, 60, 131, 30))
        self.line_edit_rota.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_edit_battletag = QLineEdit(self.centralwidget)
        self.line_edit_battletag.setObjectName("line_edit_battletag")
        self.line_edit_battletag.setGeometry(QRect(20, 100, 131, 30))
        self.line_edit_battletag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_create = QPushButton(self.centralwidget)
        self.button_create.setObjectName("button_create")
        self.button_create.setGeometry(QRect(20, 140, 131, 30))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(180, 20, 300, 130))
        self.button_copy = QPushButton(self.centralwidget)
        self.button_copy.setObjectName("button_copy")
        self.button_copy.setGeometry(QRect(20, 180, 131, 30))
        BossRota.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BossRota)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 479, 27))
        BossRota.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BossRota)
        self.statusbar.setObjectName("statusbar")
        BossRota.setStatusBar(self.statusbar)

        self.retranslateUi(BossRota)

        QMetaObject.connectSlotsByName(BossRota)

    # setupUi

    def retranslateUi(self, BossRota):
        BossRota.setWindowTitle(
            QCoreApplication.translate("BossRota", "BossRota", None)
        )
        # if QT_CONFIG(tooltip)
        self.line_edit_boss.setToolTip(
            QCoreApplication.translate("BossRota", "Boss to fight", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.line_edit_boss.setText("")
        self.line_edit_boss.setPlaceholderText(
            QCoreApplication.translate("BossRota", "Boss", None)
        )
        # if QT_CONFIG(tooltip)
        self.line_edit_rota.setToolTip(
            QCoreApplication.translate("BossRota", "How many rounds?", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.line_edit_rota.setText("")
        self.line_edit_rota.setPlaceholderText(
            QCoreApplication.translate("BossRota", "Rota", None)
        )
        self.line_edit_battletag.setText(
            QCoreApplication.translate("BossRota", "Coco#23711", None)
        )
        self.line_edit_battletag.setPlaceholderText(
            QCoreApplication.translate("BossRota", "Battletag", None)
        )
        self.button_create.setText(
            QCoreApplication.translate("BossRota", "Create", None)
        )
        self.textEdit.setPlaceholderText(
            QCoreApplication.translate(
                "BossRota",
                "------\nBoss\nRota\nBattletag\n------",
                None,
            )
        )
        self.button_copy.setText(QCoreApplication.translate("BossRota", "Copy", None))

    # retranslateUi
