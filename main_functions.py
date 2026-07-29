import tkinter as tk
from tkinter import messagebox
from logic import encryption_logic
from KCollections.style_collection import THEME

# --- FUNCIONES DE LÓGICA DE NEGOCIO ---

def ejecutar(ent_p, ent_k):
    """ Maneja la acción del botón DESCIFRAR """
    res = encryption_logic(ent_k.get())
    if res:
        ent_p.config(state='normal')
        ent_p.delete(0, tk.END)
        ent_p.insert(0, res)
        ent_p.config(state='readonly')
    else:
        messagebox.showwarning("Formato", "Key no válida")

def copiar(root, ent_p, btn_c):
    """ Copia el resultado y da feedback visual temporal """
    root.clipboard_clear()
    root.clipboard_append(ent_p.get())
    btn_c.config(text="¡COPIADO!", bg=THEME["btn_active"], fg=THEME["bg"])
    # Vuelve al estado original tras 1.5 segundos
    root.after(1500, lambda: btn_c.config(
        text="COPIAR PASSWORD", 
        bg=THEME["btn_bg"], 
        fg=THEME["text"]
    ))
