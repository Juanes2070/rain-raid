from tkinter import ttk


class Gui:
    def __init__(self, radar_gui):
        self.Radar_Panel = radar_gui
        self.Radar_Panel.in_raw_to_nc_folder_label = ttk.Label(self.Radar_Panel.raw_to_nc_content)

        self.Radar_Panel.in_raw_to_nc_folder_label.configure(text="Carpeta de archivos RAW:")
        self.Radar_Panel.in_raw_to_nc_folder_label.grid(column=0, row=1, sticky='w')

        self.Radar_Panel.in_raw_to_nc_folder_entry = ttk.Entry(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.in_raw_to_nc_folder_entry.configure(cursor='arrow', width=48,
                                                             textvariable=self.Radar_Panel.in_raw_to_nc_folder_path)
        self.Radar_Panel.in_raw_to_nc_folder_entry.grid(column=0, row=2, sticky='ew')

        self.Radar_Panel.in_raw_to_nc_folder_button = ttk.Button(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.in_raw_to_nc_folder_button.configure(text='...', width=5)
        self.Radar_Panel.in_raw_to_nc_folder_button.grid(column=1, row=2, sticky='e')

        self.Radar_Panel.out_raw_to_nc_folder_label = ttk.Label(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.out_raw_to_nc_folder_label.configure(text="Guardar en:")
        self.Radar_Panel.out_raw_to_nc_folder_label.grid(column=0, row=3, sticky='w')

        self.Radar_Panel.out_raw_to_nc_folder_entry = ttk.Entry(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.out_raw_to_nc_folder_entry.configure(cursor='arrow', width=48,
                                                              textvariable=self.Radar_Panel.out_raw_to_nc_folder_path)
        self.Radar_Panel.out_raw_to_nc_folder_entry.grid(column=0, row=4, sticky='ew')

        self.Radar_Panel.out_raw_to_nc_folder_button = ttk.Button(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.out_raw_to_nc_folder_button.configure(text='...', width=5)
        self.Radar_Panel.out_raw_to_nc_folder_button.grid(column=1, row=4, sticky='e')

        self.Radar_Panel.pol_flat_conversion_frame = ttk.Frame(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.pol_flat_conversion_frame.grid(row=5, column=0, sticky='w', columnspan=2)

        self.Radar_Panel.nc_conversion_checkbox = ttk.Checkbutton(self.Radar_Panel.pol_flat_conversion_frame)
        self.Radar_Panel.nc_conversion_checkbox.configure(text='Convertir a sistema geográfico',
                                                          variable=self.Radar_Panel.raw_to_nc_conversion)
        self.Radar_Panel.nc_conversion_checkbox.grid(row=0, column=0, sticky='w')

        self.Radar_Panel.nc_interp_options_select = ttk.Combobox(self.Radar_Panel.pol_flat_conversion_frame)
        self.Radar_Panel.nc_interp_options_select.configure(cursor='arrow',
                                                            exportselection=True,
                                                            state='disabled',
                                                            textvariable=self.Radar_Panel.raw_to_nc_interpolate)

        self.Radar_Panel.nc_interp_options_select.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
        self.Radar_Panel.nc_interp_options_select.grid(column=1, row=0, sticky='ew')
        self.Radar_Panel.raw_to_nc_interpolate.set("No interpolar")

        self.Radar_Panel.raw_to_nc_main_button = ttk.Button(self.Radar_Panel.raw_to_nc_content)
        self.Radar_Panel.raw_to_nc_main_button.configure(text='Ejecutar', width=5)
        self.Radar_Panel.raw_to_nc_main_button.grid(column=0, row=6, columnspan=3, sticky='ew')
