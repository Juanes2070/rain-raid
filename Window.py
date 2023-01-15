import tkinter as tk
import tkinter.ttk as ttk
import Satelite_GUI
import Radar_GUI
import rain_raid_menu


class MainWindow:
    def __init__(self, master=None):
        self.root = tk.Tk(master)
        self.root.wm_title("Rain-raid")
        self.root.resizable(False, False)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.menu = rain_raid_menu.Menu(self.root)

        self.radar_frame = ttk.Frame(self.notebook)
        self.sat_frame = ttk.Frame(self.notebook)

        self.Sat_Panel = Satelite_GUI.Satelite_Elements(self.root, self.sat_frame)
        self.Radar_Panel = Radar_GUI.Radar_Elements(self.root, self.radar_frame)

        self.notebook.add(self.radar_frame, text='Radar Tools')
        self.notebook.add(self.sat_frame, text='Satellite Tools')

    def start(self):
        self.root.mainloop()
