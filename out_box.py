from tkinter import ttk
import tkinter as tk


class OutTexbox:
    def __init__(self, root, radar_frame, height):

        self.root = root
        self.radar_frame = radar_frame

        self.out_frame = ttk.Frame(self.radar_frame)
        self.out_frame.grid(row=4, column=0,sticky='s')

        self.out_textbox = tk.Text(self.out_frame)
        self.out_textbox.configure(background='#dddddd',
                                   cursor='arrow',
                                   relief='flat',
                                   height=height,
                                   width=41,
                                   state='disabled')
        self.out_textbox.grid(row=0, column=0, sticky='nsew', pady='2')

        self.scroll_bar = ttk.Scrollbar(self.out_frame)
        self.scroll_bar.configure(command=self.out_textbox.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns', pady='2')
        self.out_textbox['yscrollcommand'] = self.scroll_bar.set


