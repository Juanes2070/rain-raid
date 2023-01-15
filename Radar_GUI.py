import default_values
import download_ideam_module
import ref_to_pp_module
import raw_to_nc_module
import polar_to_geo_module
import out_box


class Radar_Elements:

    def __init__(self, root, frame):
        self.root = root
        self.radar_frame = frame

        self.out_textbox = out_box.OutTexbox(root,
                                             self.radar_frame)

        self.download_ideam_module = download_ideam_module.Module(root,
                                                                  self.radar_frame,
                                                                  self.out_textbox.out_textbox)
        self.ref_to_pp_module = ref_to_pp_module.Module(root,
                                                        self.radar_frame,
                                                        self.out_textbox.out_textbox)

        self.raw_to_nc_module = raw_to_nc_module.Module(root,
                                                        self.radar_frame,
                                                        self.out_textbox.out_textbox)

        self.polar_to_geo_module = polar_to_geo_module.Module(root,
                                                              self.radar_frame,
                                                              self.out_textbox.out_textbox)

        default_values.set_default_values(self)
