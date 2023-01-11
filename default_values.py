def set_default_values(radar_gui):

    radar_gui.download_ideam_module.gui.start_date.set('16/09/2020')
    radar_gui.download_ideam_module.gui.end_date.set('16/09/2020')
    radar_gui.download_ideam_module.gui.interval.set('60')
    radar_gui.download_ideam_module.gui.interp_options.set("No interpolar")
    radar_gui.download_ideam_module.gui.out_download_folder_path.set('D:/Downloads/AWS_TEST/')

    radar_gui.ref_to_pp_module.gui.a_zr_var.set('259.008942391')
    radar_gui.ref_to_pp_module.gui.b_zr_var.set('1.4362062245')
    radar_gui.ref_to_pp_module.gui.m_disd_var.set('0.86339721868')
    radar_gui.ref_to_pp_module.gui.b_disd_var.set('2.71095329831')
    radar_gui.ref_to_pp_module.gui.trunc_var.set('52')
    radar_gui.ref_to_pp_module.gui.in_ref_to_pp_folder_path.set('D:/Downloads/20210301/')
    radar_gui.ref_to_pp_module.gui.out_ref_to_pp_folder_path.set('D:/Downloads/SALIDA_RADAR/')

    radar_gui.raw_to_nc_module.gui.out_raw_to_nc_folder_path.set('D:/Downloads/AWS_TEST/nc_out/')
    radar_gui.raw_to_nc_module.gui.in_raw_to_nc_folder_path.set('D:/Downloads/AWS_TEST/RAW/')

    radar_gui.polar_to_geo_module.gui.in_polflat_folder_path.set('D:/Downloads/netCDF4/')