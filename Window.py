import tkinter as tk
import tkinter.ttk as ttk
import Satelite_GUI
import Radar_GUI
import Satellite_Functions


class MainWindow:
    def __init__(self, master=None):
        # Main notebook
        self.root = tk.Tk(master)  # Makes the window
        self.root.wm_title("Rain-raid")  # Makes the title that will appear in the top left
        self.root.config(background="#FFFFFF")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        # self.radar_frame = ttk.Frame(self.notebook)
        self.radar_frame = ttk.Frame(self.notebook)
        self.sat_frame = ttk.Frame(self.notebook)

        # self.RadarPanel = Radar_GUI.Radar_Elements(self.root, self.radar_frame)
        self.Sat_Panel = Satelite_GUI.Satelite_Elements(self.root, self.sat_frame)
        self.Radar_Panel = Radar_GUI.Radar_Elements(self.root, self.radar_frame)

        # self.notebook.add(self.radar_frame, text='Radar')
        self.notebook.add(self.radar_frame, text='Radar Tools')

        # self.notebook.add(self.sat_frame, text='Satellite')

        def miss_click(*args):
            Satellite_Functions.mission_click(self.Sat_Panel)
        self.Sat_Panel.main_button.configure(
            command=lambda: Satellite_Functions.run(self.Sat_Panel))
        self.Sat_Panel.mission.trace('w', miss_click)


    def start(self):
        self.root.mainloop()  # start monitoring and updating the GUI
