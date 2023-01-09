from tkinter import ttk

class Gui:
    def __init__(self,radar_gui):
        self.radar_gui = radar_gui
        self.radar_gui.in_raw_to_nc_folder_label = ttk.Label(self.radar_gui.raw_to_nc_content)

        self.radar_gui.in_raw_to_nc_folder_label.configure(text="Carpeta de archivos RAW")
        self.radar_gui.in_raw_to_nc_folder_label.grid(column='0', row='1')

        self.radar_gui.in_raw_to_nc_folder_entry = ttk.Entry(self.radar_gui.raw_to_nc_content)
        self.radar_gui.in_raw_to_nc_folder_entry.configure(cursor='arrow', width='27',
                                                           textvariable=self.radar_gui.in_raw_to_nc_folder_path)
        self.radar_gui.in_raw_to_nc_folder_entry.grid(column='1', row='1', sticky='ew')
        self.radar_gui.in_raw_to_nc_folder_path.set('D:/Downloads/pyart_test/')

        self.radar_gui.in_raw_to_nc_folder_button = ttk.Button(self.radar_gui.raw_to_nc_content)
        self.radar_gui.in_raw_to_nc_folder_button.configure(text='...', width='5')
        self.radar_gui.in_raw_to_nc_folder_button.grid(column='2', row='1', sticky='e')

        self.radar_gui.out_raw_to_nc_folder_label = ttk.Label(self.radar_gui.raw_to_nc_content)
        self.radar_gui.out_raw_to_nc_folder_label.configure(text="Carpeta de archivos nc")
        self.radar_gui.out_raw_to_nc_folder_label.grid(column='0', row='2')

        self.radar_gui.out_raw_to_nc_folder_entry = ttk.Entry(self.radar_gui.raw_to_nc_content)
        self.radar_gui.out_raw_to_nc_folder_entry.configure(cursor='arrow', width='27',
                                                            textvariable=self.radar_gui.out_raw_to_nc_folder_path)
        self.radar_gui.out_raw_to_nc_folder_entry.grid(column='1', row='2', sticky='ew')
        self.radar_gui.out_raw_to_nc_folder_path.set('D:/Downloads/pyart_out/')

        self.radar_gui.out_raw_to_nc_folder_button = ttk.Button(self.radar_gui.raw_to_nc_content)
        self.radar_gui.out_raw_to_nc_folder_button.configure(text='...', width='5')
        self.radar_gui.out_raw_to_nc_folder_button.grid(column='2', row='2', sticky='e')

        self.radar_gui.raw_to_nc_main_button = ttk.Button(self.radar_gui.raw_to_nc_content)
        self.radar_gui.raw_to_nc_main_button.configure(text='Ejecutar', width='5')
        self.radar_gui.raw_to_nc_main_button.grid(column='0', row='3', columnspan='3', sticky='ew')

