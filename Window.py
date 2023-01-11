import tkinter as tk
import tkinter.ttk as ttk
import Satelite_GUI
import Radar_GUI



class MainWindow:
    def __init__(self, master=None):
        # Main notebook
        self.root = tk.Tk(master)  # Makes the window
        self.root.wm_title("Rain-raid")  # Makes the title that will appear in the top left
        self.root.config(background="#FFFFFF")
        self.root.resizable(False, False)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.radar_frame = ttk.Frame(self.notebook)
        self.sat_frame = ttk.Frame(self.notebook)

        self.Sat_Panel = Satelite_GUI.Satelite_Elements(self.root, self.sat_frame)
        self.Radar_Panel = Radar_GUI.Radar_Elements(self.root, self.radar_frame)

        self.notebook.add(self.sat_frame, text='Satellite Tools')
        self.notebook.add(self.radar_frame, text='Radar Tools')

    def start(self):
        self.root.mainloop()  # start monitoring and updating the GUI
