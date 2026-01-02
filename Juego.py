#AUTOR :deybi code##
#Proyecto personal#
import tkinter as tk
import random

# ====== CONFIGURACION DE DISEÑO ======
BG = "#0f1226"          # fondo
CARD = "#171a33"        # panel
ACCENT = "#7c5cff"      # morado
ACCENT2 = "#2dd4bf"     # verde/agua
TEXT = "#ffffff"        # texto
MUTED = "#c7c7d1"       # texto suave
DANGER = "#ff4d6d"      # rojo

FONT_T = ("Segoe UI", 16, "bold")
FONT_H = ("Segoe UI", 13, "bold")
FONT_B = ("Segoe UI", 11)
FONT_BTN = ("Segoe UI", 11, "bold")

OPCIONES = ["Piedra", "Papel", "Tijera"]
EMOJI = {"Piedra": "🪨", "Papel": "📄", "Tijera": "✂️"}

def resultado(usuario, ia):
    if usuario == ia:
        return "Empate 🤝"
    if (usuario == "Piedra" and ia == "Tijera") or (usuario == "Papel" and ia == "Piedra") or (usuario == "Tijera" and ia == "Papel"):
        return "¡Ganaste! 🎉"
    return "Perdiste 😢"

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Piedra Papel Tijera vs IA")
        self.geometry("420x420")
        self.resizable(False, False)
        self.configure(bg=BG)

        self.user_score = 0
        self.ia_score = 0

        self.menu = tk.Frame(self, bg=BG)
        self.game = tk.Frame(self, bg=BG)

        self._build_menu()
        self._build_game()
        self.show_menu()

    # ---------- Ayudantes de UI ----------
    def btn(self, parent, text, command, color=ACCENT):
        return tk.Button(
            parent, text=text, command=command,
            bg=color, fg=TEXT, activebackground=color, activeforeground=TEXT,
            bd=0, highlightthickness=0,
            font=FONT_BTN, padx=16, pady=10, cursor="hand2"
        )

    def card(self, parent):
        f = tk.Frame(parent, bg=CARD, bd=0, highlightthickness=0)
        return f

    # ---------- MENU ----------
    def _build_menu(self):
        tk.Label(self.menu, text="🎮 Piedra • Papel • Tijera", bg=BG, fg=TEXT, font=FONT_T).pack(pady=18)
        tk.Label(self.menu, text="Juega contra la IA 🤖", bg=BG, fg=MUTED, font=FONT_B).pack(pady=2)

        box = self.card(self.menu)
        box.pack(pady=20, padx=24, fill="x")

        tk.Label(box, text="Menú", bg=CARD, fg=TEXT, font=FONT_H).pack(pady=(16, 8))

        self.btn(box, "▶ Jugar", self.show_game, color=ACCENT).pack(pady=8)
        self.btn(box, "🔄 Reiniciar marcador", self.reset_score, color=ACCENT2).pack(pady=8)
        self.btn(box, "❌ Salir", self.destroy, color=DANGER).pack(pady=(8, 16))

        tk.Label(self.menu, text="Tip: intenta adivinar el patrón de la IA 😉", bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(pady=10)

    # ---------- JUEGO ----------
    def _build_game(self):
        top = self.card(self.game)
        top.pack(pady=16, padx=24, fill="x")

        tk.Label(top, text="🧑 Jugador  vs  🤖 IA", bg=CARD, fg=TEXT, font=FONT_H).pack(pady=(14, 6))

        self.score_lbl = tk.Label(top, text="Tú 0  |  IA 0", bg=CARD, fg=MUTED, font=FONT_B)
        self.score_lbl.pack(pady=(0, 14))

        mid = self.card(self.game)
        mid.pack(pady=10, padx=24, fill="x")

        tk.Label(mid, text="Elige tu jugada", bg=CARD, fg=TEXT, font=FONT_H).pack(pady=(14, 10))

        row = tk.Frame(mid, bg=CARD)
        row.pack(pady=(0, 14))

        for op in OPCIONES:
            b = tk.Button(
                row,
                text=f"{EMOJI[op]}\n{op}",
                command=lambda o=op: self.play(o),
                bg=BG, fg=TEXT, activebackground=BG, activeforeground=TEXT,
                bd=0, highlightthickness=0,
                font=("Segoe UI", 11, "bold"),
                width=9, height=3, cursor="hand2"
            )
            b.pack(side="left", padx=8)

        self.info_lbl = tk.Label(self.game, text="", bg=BG, fg=TEXT, font=FONT_B, justify="center")
        self.info_lbl.pack(pady=8)

        self.result_lbl = tk.Label(self.game, text="", bg=BG, fg=ACCENT2, font=("Segoe UI", 12, "bold"), justify="center")
        self.result_lbl.pack(pady=8)

        bottom = tk.Frame(self.game, bg=BG)
        bottom.pack(pady=12)

        self.btn(bottom, "⬅ Volver al menú", self.show_menu, color=ACCENT).pack(side="left", padx=8)
        self.btn(bottom, "🔄 Reiniciar", self.reset_round, color=ACCENT2).pack(side="left", padx=8)

    # ---------- Aciones ----------
    def show_menu(self):
        self.game.pack_forget()
        self.menu.pack(fill="both", expand=True)

    def show_game(self):
        self.menu.pack_forget()
        self.game.pack(fill="both", expand=True)

    def reset_score(self):
        self.user_score = 0
        self.ia_score = 0
        self.update_score()
        self.reset_round()

    def reset_round(self):
        self.info_lbl.config(text="")
        self.result_lbl.config(text="")

    def update_score(self):
        self.score_lbl.config(text=f"Tú {self.user_score}  |  IA {self.ia_score}")

    def play(self, user_choice):
        ia_choice = random.choice(OPCIONES)
        res = resultado(user_choice, ia_choice)

        if "Ganaste" in res:
            self.user_score += 1
        elif "Perdiste" in res:
            self.ia_score += 1

        self.update_score()
        self.info_lbl.config(text=f"Tú: {EMOJI[user_choice]} {user_choice}\nIA: {EMOJI[ia_choice]} {ia_choice}")
        self.result_lbl.config(text=res)

if __name__ == "__main__":
    GameApp().mainloop()

