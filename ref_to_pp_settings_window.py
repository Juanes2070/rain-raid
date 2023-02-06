import tkinter as tk
from tkinter import ttk


class SettingsWindow():
    def __init__(self, root):
        self.gui = root
        self.def_values_var = tk.BooleanVar()
        self.settings_window = tk.Toplevel(self.gui.root)
        self.settings_window.title('Configuración modelo de precipitación')

        self.settings_frame = ttk.Frame(self.settings_window)
        self.settings_frame.grid(row=0, column=0, padx=5, pady=5)

        # -----------------------------------------------------------------------------------------

        self.def_values_frame = ttk.Frame(self.settings_frame)
        self.def_values_frame.grid(row=0, column=0, columnspan=2)

        self.def_values_box = ttk.Checkbutton(self.def_values_frame)
        self.def_values_box.configure(text='Utilizar valores de calibración radar SIATA',
                                        variable=self.def_values_var)
        self.def_values_box.grid(row=0, column=0)
        self.def_values_var.trace('w', lambda a, b, c: set_default_values())


        def set_default_values():

            if self.def_values_var.get():
                self.gui.a_zr_var.set('259')
                self.gui.b_zr_var.set('1.4362')
                self.gui.m_disd_var.set('0.8633')
                self.gui.b_disd_var.set('2.7109')
                self.gui.trunc_var.set('52')
                self.warning_label_1.grid(row=3, column=0, columnspan=2)
                self.warning_label_2.grid(row=4, column=0, columnspan=2)
            else:
                self.gui.a_zr_var.set('')
                self.gui.b_zr_var.set('')
                self.gui.m_disd_var.set('')
                self.gui.b_disd_var.set('')
                self.gui.trunc_var.set('')
                self.warning_label_1.grid_forget()
                self.warning_label_2.grid_forget()

        # -----------------------------------------------------------------------------------------

        self.zr_param_frame = ttk.Frame(self.settings_frame)
        self.zr_param_frame.configure(borderwidth=1, relief='ridge', padding='5')
        self.zr_param_frame.grid(row=1, column=0)

        self.zr_param_label = ttk.Label(self.zr_param_frame)
        self.zr_param_label.configure(text='Parámetros relación ZR')
        self.zr_param_label.grid(row=0, column=0, columnspan=2)

        self.a_zr_label = ttk.Label(self.zr_param_frame)
        self.a_zr_label.configure(text='a')
        self.a_zr_label.grid(row=1, column=0, sticky='e')

        self.a_zr_entry = ttk.Entry(self.zr_param_frame)
        self.a_zr_entry.configure(width=15, textvariable=self.gui.a_zr_var)
        self.a_zr_entry.grid(row=1, column=1)

        self.b_zr_label = ttk.Label(self.zr_param_frame)
        self.b_zr_label.configure(text='b')
        self.b_zr_label.grid(row=2, column=0, sticky='e')

        self.b_zr_entry = ttk.Entry(self.zr_param_frame)
        self.b_zr_entry.configure(width=15, textvariable=self.gui.b_zr_var)
        self.b_zr_entry.grid(row=2, column=1)

        # -----------------------------------------------------------------------------------------

        self.disd_param_frame = ttk.Frame(self.settings_frame)
        self.disd_param_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.disd_param_frame.grid(row=1, column=1)

        self.disd_param_label = ttk.Label(self.disd_param_frame)
        self.disd_param_label.configure(text='Ajuste por disdrómetro')
        self.disd_param_label.grid(row=0, column=0, columnspan=2)

        self.m_disd_label = ttk.Label(self.disd_param_frame)
        self.m_disd_label.configure(text='m')
        self.m_disd_label.grid(row=1, column=0, sticky='w')

        self.m_disd_entry = ttk.Entry(self.disd_param_frame)
        self.m_disd_entry.configure(width=15, textvariable=self.gui.m_disd_var)
        self.m_disd_entry.grid(row=1, column=1, sticky='ew')

        self.b_disd_label = ttk.Label(self.disd_param_frame)
        self.b_disd_label.configure(text='b')
        self.b_disd_label.grid(row=2, column=0, sticky='w')

        self.b_disd_entry = ttk.Entry(self.disd_param_frame)
        self.b_disd_entry.configure(width=15, textvariable=self.gui.b_disd_var)
        self.b_disd_entry.grid(row=2, column=1, sticky='ew')

        # -----------------------------------------------------------------------------------------

        self.additional_param_frame = ttk.Frame(self.settings_frame)
        self.additional_param_frame.configure(borderwidth='1', relief='ridge', padding=5)
        self.additional_param_frame.grid(row=2, column=0, columnspan=2)

        self.additional_param_label = ttk.Label(self.additional_param_frame)
        self.additional_param_label.configure(text='Otros Ajustes')
        self.additional_param_label.grid(row=0, column=0, columnspan=2, sticky='w')

        self.trunc_label = ttk.Label(self.additional_param_frame)
        self.trunc_label.configure(text='Valor máximo de reflectividad')
        self.trunc_label.grid(row=1, column=0, sticky='w')

        self.trunc_entry = ttk.Entry(self.additional_param_frame)
        self.trunc_entry.configure(width=15, textvariable=self.gui.trunc_var)
        self.trunc_entry.grid(row=1, column=1, sticky='ew')

        self.delta_t_label = ttk.Label(self.additional_param_frame)
        self.delta_t_label.configure(text='Delta de tiempo (min)')
        self.delta_t_label.grid(row=2, column=0, sticky='w')

        self.delta_t_entry = ttk.Entry(self.additional_param_frame)
        self.delta_t_entry.configure(width=15, textvariable=self.gui.delta_t_var)
        self.delta_t_entry.grid(row=2, column=1, sticky='ew')

        self.save_button = ttk.Button(self.additional_param_frame)
        self.save_button.configure(text='Guardar', command=self.settings_window.destroy)
        self.save_button.grid(row=5, column=0, columnspan=2, sticky='ew')

        self.warning_label_1 = ttk.Label(self.additional_param_frame)
        self.warning_label_1.configure(text='Estos parámetros de calibración', foreground='red')
        self.warning_label_2 = ttk.Label(self.additional_param_frame)
        self.warning_label_2.configure(text='son para el radar del SIATA', foreground='red')



