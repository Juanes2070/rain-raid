import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)

        text_str = 'Software desarrollado por Juanes Marín en el marco del programa de investigación\n' \
                   '“Vulnerabilidad, resiliencia y riesgo de comunidades y cuencas abastecedoras afectadas\n ' \
                   'por fenómenos de deslizamientos y avalanchas” código 1118-852-71251. \n' \
                   'Proyecto “Funciones para estimación de vulnerabilidad por desabastecimiento hídrico \n' \
                   'debido a deslizamiento y avalanchas: Caso microcuencas piloto del suroeste antioqueño”, \n' \
                   'contrato 80740-492-2020 celebrado entre Fiduprevisora y la Universidad de Medellín,\n' \
                   'con recursos del Fondo Nacional de Financiamiento para la ciencia,la tecnología y la innovación,\n' \
                   '“Fondo Francisco José de Caldas”.\n\n ' \
                   'Los valores de calibración por defecto para la relación ZR fueron tomados de: \n' \
                   'Sepúlveda, J. (2016). Estimación cuantitativa de precipitación a partir de \n' \
                   'la información de Radar Meteorológico del Área Metropolitana del Valle de Aburrá, \n' \
                   'MS thesis, Universidad Nacional de Colombia, Sede Medellín, available at: \n' \
                   'http://bdigital.unal.edu.co/54581/'

        self.about_label = ttk.Label(self.window)
        self.about_label.configure(text=text_str, justify=tk.CENTER)
        self.about_label.grid(row=0, column=0)

        self.close_button = ttk.Button(self.window)
        self.close_button.configure(text='Salir', command=self.window.destroy)
        self.close_button.grid(row=1, column=0, sticky='ew')
