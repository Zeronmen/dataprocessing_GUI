# These are the files that need to be imported

from tkinter import * # Python 3
# from Tkinter import * # Python 2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Start_Window:
    
    def __init__(self,master):
        
        self.info = StringVar()
        self.info.set("holder")
        
        master.wm_title("Photovoltaic Characteristics")
        
        main_frame = Frame(master, width=250, height=250)

        statement_label = Label(main_frame,text='Photovoltaic data processing\n and analysis')
        statement_label.place(anchor=CENTER,relx=0,rely=0,x=125,y=90)

        infobar = Label(master,textvariable=self.info,relief=SUNKEN, anchor=W)
        infobar.pack(side=BOTTOM,fill=X)

        control_frame = Frame(main_frame)
        b = Button(control_frame,text='Process Data', width=20)
        b.bind("<Enter>",self.infoupdate_process)
        b.bind("<Leave>",self.infoupdate_reset)
        b.grid(row=0)
        
        Label(control_frame,width=10).grid(row=1)
        
        b = Button(control_frame,text='Analyze Data', width=20)
        b.bind("<Enter>",self.infoupdate_analysis)
        b.bind("<Leave>",self.infoupdate_reset)
        b.grid(row=2)
        
        control_frame.place(anchor=CENTER,relx=0,rely=0,x=125,y=150)
        main_frame.pack()
        
    def infoupdate_process(self,event):
        self.info.set("process")    
        
    def infoupdate_analysis(self,event):
        self.info.set("analysis")
        
    def infoupdate_reset(self,event):
        self.info.set("holder")


class Processing_Window:
	
	def __init__(self,master):
		
		self.info = StringVar()
		self.info.set("holder")		

		top = Toplevel()
		top.title("Processing Menu")

		main_frame = Frame(top, width=1600,height=1000)
		main_frame.pack()

		infobar = Label(top, textvariable=self.info,relief=SUNKEN,anchor=W)
		infobar.pack(side=BOTTOM,fill=X)

		process_frame = Frame(main_frame,width=100,height=400,bd=2, relief=SUNKEN)
		process_frame.place(x=1200,y=600)
		l = Label(process_frame, text="Batchnumber")
		l.grid(column=0,row=0, padx=2, pady=2,sticky=W)
		e = Entry(process_frame)
		e.grid(column=1,row=0, padx=2, pady=2)
		l = Label(process_frame,text="Batchsize")
		l.grid(column=0,row=1, padx=2, pady=2,sticky=W)
		e = Entry(process_frame)
		e.grid(column=1,row=1, padx=2, pady=2)
		b = Button(process_frame,text="Run",width=10)
		b.grid(column=1, row=2, padx=2, pady=2,sticky=W)

		recur_frame = Frame(main_frame, width=490,height=570 ,bd=2,relief=SUNKEN)
		recur_frame.place(x=1085,y=5)

		
		# Fix how the controls are layed out. Not great
		recur_control = Frame(recur_frame,bd=2,relief=SUNKEN,width=520)
		recur_control.place(x=0,y=490)
		l = Label(recur_control,text="Batchnumber")
		l.grid(column=0,row=0,sticky=W,pady=1)
		l = Label(recur_control,text="Devicenumber")
		l.grid(column=1,row=0,sticky=W,pady=1)
		l = Label(recur_control,text="Pixelnumber")
		l.grid(column=2,row=0,sticky=W,pady=1)
		
		e = Entry(recur_control)
		e.grid(column=0,row=1,pady=1)
		e = Entry(recur_control)
		e.grid(column=1,row=1,pady=1)
		e = Entry(recur_control)
		e.grid(column=2,row=1,pady=1)

		b =Button(recur_control, text="Graph",width=15)
		b.grid(column=0,row=3,pady=1)


		recur_fig = Figure(figsize=(490/100,490/100),dpi=100)
		recur_plot = recur_fig.add_subplot(1,1,1)

		recur_canvas = FigureCanvasTkAgg(recur_fig, recur_frame)
		recur_canvas.show()
		recur_canvas.get_tk_widget().place(x=0,y=0)

		recur_canvas._tkcanvas.place(x=0,y=0)
		

		graph_frame = Frame(main_frame,width=1055,height=1000)
		graph_frame.place(x=5,y=0)		

		graph1_frame = Frame(graph_frame,width=1055,height=490, bd=2,relief=SUNKEN)
		graph1_frame.grid(row=0,padx=2,pady=5)

		graph1_control = Frame(graph1_frame,bd=2,relief=SUNKEN,width=1055)
		graph1_control.place(y=450)

		l = Label(graph1_control,text="Batchnumber")
		l.pack(side=LEFT,pady=2,padx=2)
		e = Entry(graph1_control)
		e.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph1_control, text="Graph")
		b.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph1_control,text="Export")
		b.pack(side=LEFT,pady=2,padx=2)

		graph1_fig = Figure(figsize=(1055/100,450/100),dpi=100)
		graph1_plot = graph1_fig.add_subplot(1,1,1)

		graph1_canvas = FigureCanvasTkAgg(graph1_fig, graph1_frame)
		graph1_canvas.show()
		graph1_canvas._tkcanvas.place(x=0,y=0)

		graph2_frame = Frame(graph_frame,width=1055,height=490, bd=2,relief=SUNKEN)
		graph2_frame.grid(row=1,padx=2,pady=5)

		graph2_fig = Figure(figsize=(1055/100,450/100),dpi=100)
		graph2_plot = graph2_fig.add_subplot(1,1,1)

		graph2_canvas = FigureCanvasTkAgg(graph2_fig, graph2_frame)
		graph2_canvas.show()
		graph2_canvas._tkcanvas.place(x=0,y=0)

		graph2_control = Frame(graph2_frame,bd=2,relief=SUNKEN,width=1055)
		graph2_control.place(y=450)

		l = Label(graph2_control,text="Batchnumber")
		l.pack(side=LEFT,pady=2,padx=2)
		e = Entry(graph2_control)
		e.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph2_control, text="Graph")
		b.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph2_control,text="Export")
		b.pack(side=LEFT,pady=2,padx=2)

		



