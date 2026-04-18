import sys
import random
import PySide6
from copy import deepcopy
from logic import skillChoice, levelUp, availableSkills, skillUp

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QFrame, QScrollArea, QFileDialog, QToolButton,
    QSizePolicy, QMessageBox
)

from hero import Heroes
from skills import skillset

#GUI done with AI bec lazy for Visuals.

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hero Siege Randomizer")
        self.resize(1200, 700)

        self.heroChoice = None
        self.skills = []
        self.buildLog = []

        self.setup_ui()

    # -----------------------------
    # UI
    # -----------------------------
    def setup_ui(self):
        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(10, 10, 10, 10)
        mainLayout.setSpacing(10)

        # LEFT
        self.leftFrame = QFrame()
        self.leftFrame.setStyleSheet("""
            QFrame {
                background-color: #2b2b2b;
                border: 1px solid #555;
                border-radius: 8px;
            }
        """)
        self.leftLayout = QVBoxLayout(self.leftFrame)
        self.leftLayout.setContentsMargins(15, 15, 15, 15)
        self.leftLayout.setSpacing(12)

        self.btnHero = QPushButton("Randomize Hero")
        self.btnSkills = QPushButton("Randomize Skills")
        self.btnExport = QPushButton("Export Build")

        for btn in [self.btnHero, self.btnSkills, self.btnExport]:
            btn.setMinimumHeight(45)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    font-size: 15px;
                    font-weight: bold;
                    border: 1px solid #666;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #5a5a5a;
                }
                QPushButton:pressed {
                    background-color: #333;
                }
            """)
            self.leftLayout.addWidget(btn)

        self.heroNameLabel = QLabel("No Hero selected")
        self.heroNameLabel.setAlignment(Qt.AlignCenter)
        self.heroNameLabel.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        self.leftLayout.addWidget(self.heroNameLabel)

        self.heroImage = QLabel()
        self.heroImage.setFixedSize(200, 250)
        self.heroImage.setAlignment(Qt.AlignCenter)
        self.heroImage.setStyleSheet("""
            QLabel {
                background-color: #1a1a1a;
                border: 1px solid #666;
                border-radius: 6px;
            }
        """)
        self.heroImage.setVisible(False)
        self.leftLayout.addWidget(self.heroImage, alignment=Qt.AlignCenter)

        self.statusLabel = QLabel("Waiting...")
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setStyleSheet("""
            QLabel {
                color: #dcdcdc;
                font-size: 13px;
                padding: 8px;
                background-color: #1e1e1e;
                border-radius: 6px;
            }
        """)
        self.leftLayout.addWidget(self.statusLabel)

        self.leftLayout.addStretch()

        # RIGHT
        self.rightFrame = QFrame()
        self.rightFrame.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border: 1px solid #555;
                border-radius: 8px;
            }
        """)
        self.rightLayout = QVBoxLayout(self.rightFrame)
        self.rightLayout.setContentsMargins(10, 10, 10, 10)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("border: none;")

        self.scrollContent = QWidget()
        self.scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollLayout.setContentsMargins(5, 5, 5, 5)
        self.scrollLayout.setSpacing(10)
        self.scrollLayout.addStretch()

        self.scrollArea.setWidget(self.scrollContent)
        self.rightLayout.addWidget(self.scrollArea)

        mainLayout.addWidget(self.leftFrame, 1)
        mainLayout.addWidget(self.rightFrame, 3)

        # SIGNALS
        self.btnHero.clicked.connect(self.randomize_hero)
        self.btnSkills.clicked.connect(self.randomize_skills)
        self.btnExport.clicked.connect(self.export_build)

    
    # -----------------------------
    # HERO BUTTON
    # -----------------------------
    def randomize_hero(self):
        selectedHero = random.choice(Heroes)
        self.heroChoice = selectedHero.copy()
        self.skills = skillChoice(self.heroChoice)
        self.buildLog = []

        self.heroNameLabel.setText(self.heroChoice["name"])
        self.statusLabel.setText(
            f"Hero selected: {self.heroChoice['name']}\n"
            f"Internal Level: {self.heroChoice['heroLevel']}"
        )

        image_path = self.heroChoice["image"]
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            self.heroImage.setText("No Image")
            self.heroImage.setPixmap(QPixmap())
        else:
            self.heroImage.setPixmap(
                pixmap.scaled(137, 170, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
            self.heroImage.setText("")

        self.heroImage.setVisible(True)
        self.clear_skill_sections()

    # -----------------------------
    # SKILL BUTTON
    # -----------------------------
    def randomize_skills(self):
        if self.heroChoice is None:
            QMessageBox.warning(self, "No Hero", "You need to randomize a hero first.")
            return

        self.heroChoice["heroLevel"] = 0
        self.skills = skillChoice(self.heroChoice)
        self.buildLog = []

        while levelUp(self.heroChoice):
            available = availableSkills(self.heroChoice, self.skills)
            chosenSkill = skillUp(available)

            if chosenSkill is None:
                self.statusLabel.setText("No available skills left. Build stopped early.")
                break

            self.buildLog.append({
                "heroLevel": self.heroChoice["heroLevel"],
                "skillName": chosenSkill["name"],
                "skillLevel": chosenSkill["currentLevel"],
                "image": chosenSkill["image"]
            })

        self.statusLabel.setText(
            f"Hero: {self.heroChoice['name']}\n"
            f"Finished build to level {self.heroChoice['heroLevel']}\n"
            f"Total rolls: {len(self.buildLog)}"
        )

        self.render_build()

    # -----------------------------
    # RENDER BUILD
    # -----------------------------
    def clear_skill_sections(self):
        while self.scrollLayout.count():
            item = self.scrollLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.scrollLayout.addStretch()

    def render_build(self):
        self.clear_skill_sections()

        grouped = {}
        for start in range(1, 101, 10):
            end = min(start + 9, 100)
            grouped[f"{start}-{end}"] = []

        for entry in self.buildLog:
            lvl = entry["heroLevel"]
            block_start = ((lvl - 1) // 10) * 10 + 1
            block_end = min(block_start + 9, 100)
            grouped[f"{block_start}-{block_end}"].append(entry)

        # remove old stretch
        if self.scrollLayout.count() > 0:
            last_item = self.scrollLayout.itemAt(self.scrollLayout.count() - 1)
            if last_item and last_item.spacerItem():
                self.scrollLayout.takeAt(self.scrollLayout.count() - 1)

        for block_name, entries in grouped.items():
            section = self.create_skill_section(f"Level {block_name}", entries)
            self.scrollLayout.addWidget(section)

        self.scrollLayout.addStretch()

    def create_skill_section(self, title, entries):
        outerFrame = QFrame()
        outerFrame.setStyleSheet("""
            QFrame {
                background-color: #252525;
                border: 1px solid #444;
                border-radius: 8px;
            }
        """)
        outerLayout = QVBoxLayout(outerFrame)
        outerLayout.setContentsMargins(8, 8, 8, 8)
        outerLayout.setSpacing(8)

        headerButton = QToolButton()
        headerButton.setText(title)
        headerButton.setCheckable(True)
        headerButton.setChecked(True)
        headerButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        headerButton.setStyleSheet("""
            QToolButton {
                background-color: #383838;
                color: white;
                font-size: 15px;
                font-weight: bold;
                padding: 8px;
                border: 1px solid #555;
                border-radius: 6px;
                text-align: left;
            }
            QToolButton:hover {
                background-color: #4b4b4b;
            }
        """)
        outerLayout.addWidget(headerButton)

        contentWidget = QWidget()
        contentLayout = QHBoxLayout(contentWidget)
        contentLayout.setContentsMargins(5, 5, 5, 5)
        contentLayout.setSpacing(8)

        for entry in entries:
            card = self.create_skill_card(entry)
            contentLayout.addWidget(card)

        contentLayout.addStretch()

        headerButton.toggled.connect(contentWidget.setVisible)

        outerLayout.addWidget(contentWidget)
        return outerFrame

    def create_skill_card(self, entry):
        card = QFrame()
        card.setFixedWidth(80)
        card.setStyleSheet("""
            QFrame {
                background-color: #111;
                border: 1px solid #666;
                border-radius: 6px;
            }
        """)
        cardLayout = QVBoxLayout(card)
        cardLayout.setContentsMargins(4, 4, 4, 4)
        cardLayout.setSpacing(4)

        imgLabel = QLabel()
        imgLabel.setFixedSize(66, 66)
        imgLabel.setAlignment(Qt.AlignCenter)
        imgLabel.setStyleSheet("""
            QLabel {
                background-color: #0b0b0b;
                border: 1px solid #444;
            }
        """)

        pixmap = QPixmap(entry["image"])
        if pixmap.isNull():
            imgLabel.setText("No Img")
        else:
            imgLabel.setPixmap(
                pixmap.scaled(66, 66, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

        levelLabel = QLabel(f"Lv {entry['heroLevel']}")
        levelLabel.setAlignment(Qt.AlignCenter)
        levelLabel.setStyleSheet("color: white; font-size: 11px; font-weight: bold;")

        nameLabel = QLabel(entry["skillName"])
        nameLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setWordWrap(True)
        nameLabel.setStyleSheet("color: #dcdcdc; font-size: 10px;")

        skillLevelLabel = QLabel(f"+{entry['skillLevel']}")
        skillLevelLabel.setAlignment(Qt.AlignCenter)
        skillLevelLabel.setStyleSheet("color: #9fe870; font-size: 11px; font-weight: bold;")

        cardLayout.addWidget(imgLabel, alignment=Qt.AlignCenter)
        cardLayout.addWidget(levelLabel)
        cardLayout.addWidget(nameLabel)
        cardLayout.addWidget(skillLevelLabel)

        return card

    # -----------------------------
    # EXPORT
    # -----------------------------
    def export_build(self):
        if not self.heroChoice or not self.buildLog:
            QMessageBox.information(self, "Nothing to export", "No build has been generated yet.")
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,
            "Export Build",
            f"{self.heroChoice['name']}_build.txt",
            "Text Files (*.txt)"
        )

        if not filePath:
            return

        with open(filePath, "w", encoding="utf-8") as file:
            file.write(f"Hero: {self.heroChoice['name']}\n")
            file.write(f"Final Level: {self.heroChoice['heroLevel']}\n")
            file.write("=" * 40 + "\n")

            for entry in self.buildLog:
                file.write(
                    f"Level {entry['heroLevel']}: "
                    f"{entry['skillName']} -> Skill Level {entry['skillLevel']}\n"
                )

        QMessageBox.information(self, "Export complete", "Build exported successfully.")


