import tkinter as tk
import tkinter.ttk as ttk
import res_path
from hover_info import CreateToolTip
from PIL import ImageTk,Image

class Satelite_Elements:
	def __init__(self, root, frame):
		# Default values
		w_path_def = r"D:\Downloads\chirps_test/"
		mask_path_def = r"D:\GDrive\U\TESIS\SIG\Cartografía base\Esta_Extent.shp"

		self.root = root
		self.satelite_frame = frame

		self.out_folder_path = tk.StringVar()
		self.coord_sys = tk.StringVar()
		self.username = tk.StringVar()
		self.password = tk.StringVar()
		self.start_date = tk.StringVar()
		self.end_date = tk.StringVar()
		self.mission = tk.StringVar()

		self.input_parameters_frame = ttk.Frame(self.satelite_frame)
		self.input_parameters_frame.configure(height='100', width='120')
		self.input_parameters_frame.grid(column='0', row='0',padx='5')

		self.mission_select = ttk.Combobox(self.input_parameters_frame)
		self.mission_select.configure(cursor='arrow', exportselection='true', state='readonly',
										textvariable=self.mission)
		#TODO colocar los nombres completos de las misiones
		self.mission_select.configure(values='"IMERG" "CHIRPS"', width='60')
		self.mission_select.set("IMERG")
		self.mission_select.grid(column='1', row='0',columnspan='2')
		self.mission_select.rowconfigure('2', pad='10')

		self.mission_label = ttk.Label(self.input_parameters_frame)
		self.mission_label.configure(text='Satelite')
		self.mission_label.grid(column='0', row='0', sticky='e')

		self.working_directory_entry = ttk.Entry(self.input_parameters_frame)
		self.working_directory_entry.configure(cursor='arrow', width='56', textvariable=self.out_folder_path)
		self.working_directory_entry.grid(column='1', row='1', sticky='ew')
		self.out_folder_path.set(w_path_def)

		self.working_directory_button = ttk.Button(self.input_parameters_frame)
		self.working_directory_button.configure(text='...', width='5')
		self.working_directory_button.grid(column='2', row='1', sticky='w')

		self.working_directory_label = ttk.Label(self.input_parameters_frame)
		self.working_directory_label.configure(text='Guardar en')
		self.working_directory_label.grid(column='0', row='1', sticky='e')


		self.coord_sys_select = ttk.Combobox(self.input_parameters_frame)
		self.coord_sys_select.configure(cursor='arrow', exportselection='true', state='readonly',
										textvariable=self.coord_sys)
		self.coord_sys_select.configure(values='"MAGNA Colombia Bogota" "WGS 1984 UTM ZONE 18N"', width='60')
		self.coord_sys_select.set("MAGNA Colombia Bogota")
		self.coord_sys_select.grid(column='1', row='2', sticky='w',columnspan='2')
		self.coord_sys_select.rowconfigure('2', pad='10')

		self.coord_sys_label = ttk.Label(self.input_parameters_frame)
		self.coord_sys_label.configure(font='TkDefaultFont', text='Sistema coordenado')
		self.coord_sys_label.grid(column='0', row='2', sticky='e')
		self.coord_sys_label.rowconfigure('2', pad='10')

		self.main_button = ttk.Button(self.satelite_frame)
		self.main_button.configure(text='Ejecutar', width='10')
		self.main_button.grid(column='2', columnspan='2', row='3', sticky='ew')

		# TODO bloquear el cuadro de texto
		self.out_text = tk.Text(self.satelite_frame)
		self.out_text.configure(background='#dddddd', height='14', insertunfocussed='none', state='normal')
		self.out_text.grid(column='0', row='1', sticky='nsew', padx='5', pady='5',columnspan='3')

		self.progressbar = ttk.Progressbar(self.satelite_frame)
		self.progressbar.configure(length='450', orient='horizontal')
		self.progressbar.grid(column='0', columnspan='2', row='3', sticky='ew', padx='5')

#----------------------------------------------------------------------------------------------------------------------------
		self.secondary_parameters_frame = ttk.Frame(self.satelite_frame)
		self.secondary_parameters_frame.configure(height='200', width='120')
		self.secondary_parameters_frame.grid(column='1', pady='5', row='0',columnspan='2',sticky='nsew')

		self.separator = ttk.Separator(self.secondary_parameters_frame, orient='vertical')
		self.separator.grid(column='0', row='0', sticky="ns", padx='5', rowspan='5')

		self.separator = ttk.Separator(self.secondary_parameters_frame, orient='horizontal')
		self.separator.grid(column='0', row='0', sticky="ew", padx='5', columnspan='5')

		self.separator = ttk.Separator(self.secondary_parameters_frame, orient='horizontal')
		self.separator.grid(column='0', row='2', sticky="ew", pady='5',padx='5', columnspan='3')

		self.separator = ttk.Separator(self.secondary_parameters_frame, orient='horizontal')
		self.separator.grid(column='0', row='4', sticky="ew", padx='5', columnspan='5')

		self.separator = ttk.Separator(self.secondary_parameters_frame, orient='vertical')
		self.separator.grid(column='2', row='0', sticky="ns", padx='5', rowspan='5')

		self.top_method_parameters_frame = ttk.Frame(self.secondary_parameters_frame)
		self.top_method_parameters_frame.configure(height='200', width='120')
		self.top_method_parameters_frame.grid(column='1', row='3', columnspan='1', sticky='nsew')

		self.bottom_method_parameters_frame = ttk.Frame(self.secondary_parameters_frame)
		self.bottom_method_parameters_frame.configure(height='200', width='120')
		self.bottom_method_parameters_frame.grid(column='1', row='1', columnspan='1', sticky='nsew')

#		self.separator = ttk.Separator(self.top_method_parameters_frame, orient='vertical')
#		self.separator.grid(column='4', row='0', sticky="ns", padx='5', rowspan='5')


# ___________________________________________________________________#
		self.login_frame = ttk.Frame(self.top_method_parameters_frame)
		self.login_frame.configure(height='200', width='120')
		self.login_frame.grid(column='1', pady='5', row='0', sticky='nsew')

		self.relacion_label = ttk.Label(self.login_frame)
		self.relacion_label.configure(text='Login EarthData')
		self.relacion_label.grid(column='0', row='0', padx='0',sticky='w')

		img_path = res_path.resource_path("img/question_icon.png")

		self.q_mark = ImageTk.PhotoImage(Image.open(img_path))
		self.relacion_label_q = ttk.Label(master=self.login_frame, image=self.q_mark)
		self.relacion_label_q.grid(column='1', row='0', sticky='w')

		CreateToolTip(self.relacion_label_q, text='Más información')

		self.username_label = ttk.Label(self.login_frame)
		self.username_label.configure(text='Usuario')
		self.username_label.grid(column='0', row='1', sticky='w')

		self.username_entry = ttk.Entry(self.login_frame)
		self.username_entry.configure(cursor='arrow', width='25', textvariable=self.username)
		self.username_entry.grid(column='1', row='1', sticky='w')
		self.username.set('juanes2070@gmail.com')

		self.password_label = ttk.Label(self.login_frame)
		self.password_label.configure(text='Contraseña')
		self.password_label.grid(column='0', row='2', sticky='w')

		self.password_entry = ttk.Entry(self.login_frame)
		self.password_entry.configure(cursor='arrow', width='25', textvariable=self.password)
		self.password_entry.grid(column='1', row='2', sticky='w')
		self.password.set('Test123456')

		self.date_frame = ttk.Frame(self.bottom_method_parameters_frame)
		self.date_frame.configure(height='200', width='120')
		self.date_frame.grid(column='0', pady='5', row='0', sticky='nsew')

		self.date_label = ttk.Label(self.date_frame)
		self.date_label.configure(text='Periodo')
		self.date_label.grid(column='0', row='0', sticky='w')

		self.start_date_label = ttk.Label(self.date_frame)
		self.start_date_label.configure(text='Fecha inical')
		self.start_date_label.grid(column='0', row='1', sticky='w')

		self.start_date_entry = ttk.Entry(self.date_frame)
		self.start_date_entry.configure(cursor='arrow', width='25', textvariable=self.start_date)
		self.start_date_entry.grid(column='1', row='1', sticky='e')
		self.start_date.set('01/01/2020')

		self.end_date_label = ttk.Label(self.date_frame)
		self.end_date_label.configure(text='Fecha final')
		self.end_date_label.grid(column='0', row='2', sticky='w')
		self.end_date.set('02/01/2020')

		self.end_date_entry = ttk.Entry(self.date_frame)
		self.end_date_entry.configure(cursor='arrow', width='25', textvariable=self.end_date)
		self.end_date_entry.grid(column='1', row='2', sticky='e')

