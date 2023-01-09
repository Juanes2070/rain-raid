        self.polflat_frame = ttk.Frame(self.download_ideam_frame)
        self.polflat_frame.configure(height='100', width='120',borderwidth = '1', relief='ridge',padding='5')
        #self.polflat_frame.grid(column='0', row='1',sticky='ew')

        self.polflat_title = ttk.Label(self.polflat_frame)
        self.polflat_title.configure(text="Conversion de coordenadas polares a geográficas")
        self.polflat_title.grid(row='0',column='0',columnspan='3')

        self.in_polflat_folder_label = ttk.Label(self.polflat_frame)
        self.in_polflat_folder_label.configure(text="Archivos de entrada")
        self.in_polflat_folder_label.grid(column='0', row='1')

        self.in_polflat_folder_entry = ttk.Entry(self.polflat_frame)
        self.in_polflat_folder_entry.configure(cursor='arrow', width='27', textvariable=self.in_polflat_folder_path)
        self.in_polflat_folder_entry.grid(column='1', row='1', sticky='ew')
        self.in_polflat_folder_path.set('D:/Downloads/pyart_out/')

        self.in_polflat_folder_button = ttk.Button(self.polflat_frame)
        self.in_polflat_folder_button.configure(text='...', width='5')
        self.in_polflat_folder_button.grid(column='2', row='1', sticky='e')

        self.out_polflat_folder_label = ttk.Label(self.polflat_frame)
        self.out_polflat_folder_label.configure(text="Carpeta de salida")
        self.out_polflat_folder_label.grid(column='0', row='2')

        self.out_polflat_folder_entry = ttk.Entry(self.polflat_frame)
        self.out_polflat_folder_entry.configure(cursor='arrow', width='27', textvariable=self.out_polflat_folder_path)
        self.out_polflat_folder_entry.grid(column='1', row='2', sticky='ew')
        self.out_polflat_folder_path.set('D:/Downloads/polar/')

        self.out_polflat_folder_button = ttk.Button(self.polflat_frame)
        self.out_polflat_folder_button.configure(text='...', width='5')
        self.out_polflat_folder_button.grid(column='2', row='2', sticky='e')

        self.polflat_main_button = ttk.Button(self.polflat_frame)
        self.polflat_main_button.configure(text='Ejecutar', width='5')
        self.polflat_main_button.grid(column='0', row='3', columnspan='3', sticky='ew')

#------------------------------------------------------------------------------------------------

        self.raw_to_nc_frame = ttk.Frame(self.right_frame)
        self.raw_to_nc_frame.configure(width='120', borderwidth='1', relief='ridge', padding='5')
        #self.raw_to_nc_frame.grid(column='0', row='0', sticky='ew')

        self.raw_to_nc_title = ttk.Label(self.raw_to_nc_frame)
        self.raw_to_nc_title.configure(text="Procesamiento de Archivos RAW")
        self.raw_to_nc_title.grid(row='0', column='0', columnspan='3')

        self.in_raw_to_nc_folder_label = ttk.Label(self.raw_to_nc_frame)
        self.in_raw_to_nc_folder_label.configure(text="Carpeta de archivos RAW")
        self.in_raw_to_nc_folder_label.grid(column='0', row='1')

        self.in_raw_to_nc_folder_entry = ttk.Entry(self.raw_to_nc_frame)
        self.in_raw_to_nc_folder_entry.configure(cursor='arrow', width='27', textvariable=self.in_raw_to_nc_folder_path)
        self.in_raw_to_nc_folder_entry.grid(column='1', row='1', sticky='ew')
        self.in_raw_to_nc_folder_path.set('D:/Downloads/pyart_test/')

        self.in_raw_to_nc_folder_button = ttk.Button(self.raw_to_nc_frame)
        self.in_raw_to_nc_folder_button.configure(text='...', width='5')
        self.in_raw_to_nc_folder_button.grid(column='2', row='1', sticky='e')

        self.out_raw_to_nc_folder_label = ttk.Label(self.raw_to_nc_frame)
        self.out_raw_to_nc_folder_label.configure(text="Carpeta de archivos nc")
        self.out_raw_to_nc_folder_label.grid(column='0', row='2')

        self.out_raw_to_nc_folder_entry = ttk.Entry(self.raw_to_nc_frame)
        self.out_raw_to_nc_folder_entry.configure(cursor='arrow', width='27', textvariable=self.out_raw_to_nc_folder_path)
        self.out_raw_to_nc_folder_entry.grid(column='1', row='2', sticky='ew')
        self.out_raw_to_nc_folder_path.set('D:/Downloads/pyart_out/')

        self.out_raw_to_nc_folder_button = ttk.Button(self.raw_to_nc_frame)
        self.out_raw_to_nc_folder_button.configure(text='...', width='5')
        self.out_raw_to_nc_folder_button.grid(column='2', row='2', sticky='e')

        self.raw_to_nc_main_button = ttk.Button(self.raw_to_nc_frame)
        self.raw_to_nc_main_button.configure(text='Ejecutar', width='5')
        self.raw_to_nc_main_button.grid(column='0', row='3', columnspan='3', sticky='ew')

        # ---------------------------------------------------------------------------------------------------------------