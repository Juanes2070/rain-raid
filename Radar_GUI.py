import tkinter as tk
import default_values
import download_ideam_module
import ref_to_pp_module
import raw_to_nc_module
import polar_to_geo_module


class Radar_Elements:

    def __init__(self, root, frame):
        self.root = root
        self.radar_frame = frame

        self.out_textbox = tk.Text(self.radar_frame)
        self.out_textbox.configure(background='#dddddd',
                                   cursor='arrow',
                                   relief='flat',
                                   height='10',
                                   width=42,
                                   state='disabled')
        self.out_textbox.grid(row=10, column=0, sticky='nsew', pady='5', padx='5')

        self.download_ideam_module = download_ideam_module.Module(root,
                                                                  self.radar_frame,
                                                                  self.out_textbox)
        self.ref_to_pp_module = ref_to_pp_module.Module(root,
                                                        self.radar_frame,
                                                        self.out_textbox)

        self.raw_to_nc_module = raw_to_nc_module.Module(root,
                                                        self.radar_frame,
                                                        self.out_textbox)

        self.polar_to_geo_module = polar_to_geo_module.Module(root,
                                                              self.radar_frame,
                                                              self.out_textbox)

        default_values.set_default_values(self)
