
import tkinter as tk
from tkinter import messagebox

def show_alert():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showinfo('Alerta', 'Esta é uma mensagem de alerta!')
    root.destroy()

show_alert()




