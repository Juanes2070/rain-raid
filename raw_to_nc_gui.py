from tkinter import ttk

class Gui:
    def __init__(self,radar_gui):
        self.Radar_Panel = radar_gui
        self.Radar_Panel.in_raw_to_nc_folder_label = ttk.Label(self.Radar_Panel.raw_to_nc_content)

        self.Radar_Panel.in_raw_to_nc_folder_label.configure(text="Carpeta de archivos RAW")
        self.Radar_Panel.in_raw_to_nc_folder_label.grid(column='0', row='1')

        self.Radar_Panel.in_raw_to_nc_folder_entry = ttk.Entry(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.in_raw_to_nc_folder_entry.configure(cursor='arrow', width='27',
                                                             textvariable=self.Radar_Panel.in_raw_to_nc_folder_path)
        self.Radar_Panel.in_raw_to_nc_folder_entry.grid(column='1', row='1', sticky='ew')

        self.Radar_Panel.in_raw_to_nc_folder_button = ttk.Button(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.in_raw_to_nc_folder_button.configure(text='...', width='5')
        self.Radar_Panel.in_raw_to_nc_folder_button.grid(column='2', row='1', sticky='e')

        self.Radar_Panel.out_raw_to_nc_folder_label = ttk.Label(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.out_raw_to_nc_folder_label.configure(text="Carpeta de archivos nc")
        self.Radar_Panel.out_raw_to_nc_folder_label.grid(column='0', row='2')

        self.Radar_Panel.out_raw_to_nc_folder_entry = ttk.Entry(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.out_raw_to_nc_folder_entry.configure(cursor='arrow', width='27',
                                                              textvariable=self.Radar_Panel.out_raw_to_nc_folder_path)
        self.Radar_Panel.out_raw_to_nc_folder_entry.grid(column='1', row='2', sticky='ew')


        self.Radar_Panel.out_raw_to_nc_folder_button = ttk.Button(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.out_raw_to_nc_folder_button.configure(text='...', width='5')
        self.Radar_Panel.out_raw_to_nc_folder_button.grid(column='2', row='2', sticky='e')

        self.Radar_Panel.raw_to_nc_main_button = ttk.Button(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.raw_to_nc_main_button.configure(text='Ejecutar', width='5')
        self.Radar_Panel.raw_to_nc_main_button.grid(column='0', row='3', columnspan='3', sticky='ew')

