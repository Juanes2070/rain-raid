import tkinter as tk
from tkinter import ttk


def open_settings_window(self):

    self.settings_window = tk.Toplevel(self.root)
    self.settings_window.title('Configuración modelo de precipitación')

    self.settings_frame = ttk.Frame(self.settings_window)
    self.settings_frame.grid(row='0', column='0')

#-----------------------------------------------------------------------------------------

    self.zr_param_frame = ttk.Frame(self.settings_frame)
    self.zr_param_frame.configure(borderwidth = '1', relief='ridge',padding='5')
    self.zr_param_frame.grid(row='0', column='0')

    self.zr_param_label = ttk.Label(self.zr_param_frame)
    self.zr_param_label.configure(text = 'Parámetros relación ZR')
    self.zr_param_label.grid(row='0', column='0', columnspan='2')

    self.a_zr_label = ttk.Label(self.zr_param_frame)
    self.a_zr_label.configure(text='a')
    self.a_zr_label.grid(row='1', column='0',sticky='e')

    self.a_zr_entry = ttk.Entry(self.zr_param_frame)
    self.a_zr_entry.configure(width='15',textvariable=self.a_zr_var)
    self.a_zr_entry.grid(row='1', column='1')

    self.b_zr_label = ttk.Label(self.zr_param_frame)
    self.b_zr_label.configure(text='b')
    self.b_zr_label.grid(row='2', column='0',sticky='e')

    self.b_zr_entry = ttk.Entry(self.zr_param_frame)
    self.b_zr_entry.configure(width='15', textvariable=self.b_zr_var)
    self.b_zr_entry.grid(row='2', column='1')

#-----------------------------------------------------------------------------------------

    self.disd_param_frame = ttk.Frame(self.settings_frame)
    self.disd_param_frame.configure(borderwidth='1', relief='ridge', padding='5')
    self.disd_param_frame.grid(row='0', column='1')

    self.disd_param_label = ttk.Label(self.disd_param_frame)
    self.disd_param_label.configure(text='Ajuste por disdrómetro')
    self.disd_param_label.grid(row='0', column='0', columnspan='2')

    self.m_disd_label = ttk.Label(self.disd_param_frame)
    self.m_disd_label.configure(text='m')
    self.m_disd_label.grid(row='1', column='0', sticky='w')

    self.m_disd_entry = ttk.Entry(self.disd_param_frame)
    self.m_disd_entry.configure(width='15', textvariable=self.m_disd_var)
    self.m_disd_entry.grid(row='1', column='1', sticky='ew')

    self.b_disd_label = ttk.Label(self.disd_param_frame)
    self.b_disd_label.configure(text='b')
    self.b_disd_label.grid(row='2', column='0', sticky='w')

    self.b_disd_entry = ttk.Entry(self.disd_param_frame)
    self.b_disd_entry.configure(width='15', textvariable=self.b_disd_var)
    self.b_disd_entry.grid(row='2', column='1',sticky='ew')


#-----------------------------------------------------------------------------------------

    self.additional_param_frame = ttk.Frame(self.settings_frame)
    self.additional_param_frame.configure(borderwidth='1', relief='ridge', padding='5')
    self.additional_param_frame.grid(row='1', column='0',columnspan='2')

    self.additional_param_label = ttk.Label(self.additional_param_frame)
    self.additional_param_label.configure(text='Otros Ajustes')
    self.additional_param_label.grid(row='0', column='0', columnspan='2',sticky='w')

    self.trunc_label = ttk.Label(self.additional_param_frame)
    self.trunc_label.configure(text='Valor máximo de reflectividad')
    self.trunc_label.grid(row='1', column='0', sticky='w')

    self.trunc_entry = ttk.Entry(self.additional_param_frame)
    self.trunc_entry.configure(width='15', textvariable=self.trunc_var)
    self.trunc_entry.grid(row='1', column='1', sticky='ew')


    self.interp_options_combox = ttk.Combobox(self.additional_param_frame)
    self.interp_options_combox.configure(cursor='arrow', exportselection='true',
                                         textvariable=self.interp_options)

    self.interp_label = ttk.Label(self.additional_param_frame)
    self.interp_label.configure(text='Interpolación')
    self.interp_label.grid(row='2', column='0', sticky='w')

    self.interp_options_combox.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
    self.interp_options_combox.grid(column='1', row='2', sticky='ew')
    self.interp_options.set("No interpolar")




