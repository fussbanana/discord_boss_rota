# controller.py
from PySide6.QtWidgets import QApplication


class BossRotaController:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()
        self.border_top = "╔══════════════════════════╗"
        self.border_bottom = "╚══════════════════════════╝"

    def setup_connections(self):
        self.ui.button_create.clicked.connect(self.create_rota)
        self.ui.button_copy.clicked.connect(self.copy_rota)

    def create_rota(self):
        boss_text = self.ui.line_edit_boss.text()
        rota_text = self.ui.line_edit_rota.text()
        battletag_text = self.ui.line_edit_battletag.text()

        # HTML-Formatierung für zentrierten Text
        formatted_text = f"""
            <div style="text-align: center;">
                {self.border_top}<br>
                LFG Tormented {boss_text}<br>
                ({rota_text}x)<br>
                {battletag_text}<br>
                {self.border_bottom}
            </div>
        """

        self.ui.textEdit.setHtml(formatted_text)

    def copy_rota(self):
        boss_text = self.ui.line_edit_boss.text()
        rota_text = self.ui.line_edit_rota.text()
        battletag_text = self.ui.line_edit_battletag.text()

        # Textzeilen mit Tabulatoren
        lines = [
            "╔══════════════════════════╗",
            f"\tLFG Tormented {boss_text}",
            f"\t({rota_text}x)",
            f"\t{battletag_text}",
            "╚══════════════════════════╝"
        ]

        # Verbinde die Zeilen mit Zeilenumbrüchen
        formatted_text = "\n".join(lines)

        # Kopiere den Text in die Zwischenablage
        clipboard = QApplication.clipboard()
        clipboard.setText(formatted_text)
