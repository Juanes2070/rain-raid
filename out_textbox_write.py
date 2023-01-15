import tkinter as tk


def write(textbox: tk.Text, text: str, delete_prev: bool = False):
    textbox.configure(state='normal')
    if delete_prev:
        textbox.delete('1.0', tk.END)
    if text != '':
        textbox.insert(tk.END, text)
        textbox.configure(state='disabled')
        textbox.see(tk.END)
