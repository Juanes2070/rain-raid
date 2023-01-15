import download_satellite_module
import out_box
import default_values

class Satelite_Elements:
    def __init__(self, root, frame):
        self.root = root
        self.satellite_frame = frame

        self.out_textbox = out_box.OutTexbox(self.root,self.satellite_frame)

        self.down_satellite_module = download_satellite_module.Module(self.root,
                                                                      self.satellite_frame,
                                                                      self.out_textbox.out_textbox)


        default_values.set_sat_default_values(self)
