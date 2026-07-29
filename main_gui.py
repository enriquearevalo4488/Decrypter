import tkinter as tk
from KCollections.style_collection import THEME, FONTS
import main_functions as actions


class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()


        # 1. OCULTAR LA VENTANA INMEDIATAMENTE
        self.withdraw()

        # 2. CONFIGURAMOS E INTERFAZ
        self.title("Decrypter")
        self.configure(bg=THEME["bg"])
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.0) # Para fade-in


        # Centrado y Tamaño
        w, h = 400, 380
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(False, False)

        self.setup_ui()
        # 4. MOSTRAR LA VENTANA Y HACER FADE-IN
        self.deiconify() # Hace que la ventana vuelva a ser visible
        self.fade_in()

    def setup_ui(self):
        tk.Label(self, text="Decrypter", font=FONTS["title"], bg=THEME["bg"], fg=THEME["accent"]).pack(pady=(25, 10))

        # Input
        tk.Label(self, text="INPUT KEY", font=FONTS["label"], bg=THEME["bg"], fg=THEME["text"]).pack()
        self.ent_k = tk.Entry(self, width=30, font=FONTS["data"], bg=THEME["entry_bg"], fg="white", bd=0, justify="center", insertbackground="white")
        self.ent_k.pack(pady=5, ipady=8)

        # Botón Descifrar
        self.btn_d = tk.Button(self, text="DESCIFRAR", font=FONTS["btn"], bg=THEME["btn_bg"], fg=THEME["text"], bd=0, cursor="hand2", width=18, command=lambda: actions.ejecutar(self.ent_p, self.ent_k))
        self.btn_d.pack(pady=15, ipady=5)

        # Output
        tk.Label(self, text="PASSWORD GENERADA", font=FONTS["label"], bg=THEME["bg"], fg=THEME["text"]).pack()
        self.ent_p = tk.Entry(self, width=30, font=FONTS["data"], bg=THEME["entry_bg"], fg="white", 
                              bd=0, justify="center", state="readonly", readonlybackground=THEME["entry_bg"])
        self.ent_p.pack(pady=5, ipady=8)

        # Botón Copiar
        self.btn_c = tk.Button(self, text="COPIAR PASSWORD", font=FONTS["label"], bg=THEME["btn_bg"], fg=THEME["text"],
                               bd=1, relief="flat", cursor="hand2", width=20,
                               command=lambda: actions.copiar(self, self.ent_p, self.btn_c))
        self.btn_c.pack(pady=15)

    def fade_in(self, alpha=0.0):
        if alpha < 1.0:
            alpha += 0.1
            self.attributes("-alpha", alpha)
            self.after(30, self.fade_in, alpha)



if __name__ == "__main__":
    app = AppWindow()
    app.mainloop()