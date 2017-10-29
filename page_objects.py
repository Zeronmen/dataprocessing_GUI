# These are the files that need to be imported

try:
	from tkinter import * # Python 3
except ImportError:
	from Tkinter import * # Python 2

import process_data as pd
import analyze_data as ad
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Start_Window:
    
    def __init__(self,master):
        
        self.master = master
        self.info = StringVar()
        self.info.set("holder")
        
        self.master.wm_title("Photovoltaic Characteristics")
        
        main_frame = Frame(self.master, width=250, height=250)
        main_frame.pack()

        statement_label = Label(main_frame,text='Photovoltaic data processing\n and analysis')
        statement_label.place(anchor=CENTER,relx=0,rely=0,x=125,y=90)

        infobar = Label(self.master,textvariable=self.info,relief=SUNKEN, anchor=W)
        infobar.pack(side=BOTTOM,fill=X)

        control_frame = Frame(main_frame)
        b = Button(control_frame,text='Process Data', width=20,command=self.openwindow_process)
        b.bind("<Enter>",self.infoupdate_process)
        b.bind("<Leave>",self.infoupdate_reset)
        b.grid(row=0)
        Label(control_frame,width=10).grid(row=1)
        b = Button(control_frame,text='Analyze Data', width=20)
        # b = Button(control_frame,text='Analyze Data', width=20, command=self.openwindow_analysis)
        b.bind("<Enter>",self.infoupdate_analysis)
        b.bind("<Leave>",self.infoupdate_reset)
        b.grid(row=2)

        control_frame.place(anchor=CENTER,relx=0,rely=0,x=125,y=150)

    def openwindow_process(self):
        process_win = Processing_Window(self.master)
    
    # def openwindow_analysis(self):
        # analysis_win = Analysis_Window(self.master)
   
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

		self.loc = StringVar()
		self.loc.set("holder")

		width =	master.winfo_screenwidth()
		height = master.winfo_screenheight()	

		top = Toplevel()
		top.title("Processing Menu")
		top.geometry("%ix%i" % (width,height))

		main_frame = Frame(top)
		main_frame.pack(fill=BOTH,expand=True)
		main_frame.columnconfigure(0, weight=75)
		main_frame.columnconfigure(1,weight=25)
		main_frame.rowconfigure(0,weight=50)
		main_frame.rowconfigure(1,weight=50)

		infobar = Label(top, textvariable=self.info,relief=SUNKEN,anchor=W)
		infobar.pack(side=BOTTOM,fill=X)

		process_frame = Frame(main_frame,bd=2, relief=SUNKEN)
		process_frame.grid(column=1,row=1,pady=5,padx=5,sticky=N+S+E+W)
		self.process_batchnumber = IntVar()
		self.process_batchsize = IntVar()
		
		l = Label(process_frame, text="Batchnumber")
		l.grid(column=0,row=0, padx=2, pady=2,sticky=W)
		e = Entry(process_frame,textvariable=self.process_batchnumber)
		e.grid(column=1,row=0, padx=2, pady=2)
		l = Label(process_frame,text="Batchsize")
		l.grid(column=0,row=1, padx=2, pady=2,sticky=W)
		e = Entry(process_frame,textvariable=self.process_batchsize)
		e.grid(column=1,row=1, padx=2, pady=2)
		b = Button(process_frame,text="Run",width=10,
                    command=self.run_process_batch)
		b.bind("<Enter>",self.infoupdate_runprocess)
		b.bind("<Leave>",self.infoupdate_reset)
		b.grid(column=1, row=2, padx=2, pady=2,sticky=W)

		recur_frame = Frame(main_frame,bd=2)
		recur_frame.bind("<Enter>",self.locupdate_recur)
		recur_frame.grid(column=1,row=0,pady=5,padx=5,sticky=N+S+E+W)

		recur_fig = Figure(figsize=(490/100,450/100),dpi=100)
		self.recur_plot = recur_fig.add_subplot(1,1,1)

		self.recur_canvas = FigureCanvasTkAgg(recur_fig, recur_frame)
		self.recur_canvas.show()
		self.recur_canvas.get_tk_widget().pack(side=TOP,fill=X)
		self.recur_canvas._tkcanvas.pack(side=TOP,fill=X)

		
		recur_control = Frame(recur_frame,bd=2,relief=SUNKEN)
		recur_control.pack(side=TOP,fill=X)
		self.recur_batchnumber = IntVar()
		self.recur_devicenumber = IntVar()
		self.recur_pixelnumber = IntVar()
		self.recur_pixelnumber.set(1)
		

		l = Label(recur_control,text="Batchnumber")
		l.grid(column=0,row=0,sticky=W,pady=1)
		l = Label(recur_control,text="Devicenumber")
		l.grid(column=1,row=0,sticky=W,pady=1)

		entry_single = Frame(recur_control)
		e = Entry(entry_single,width=10,textvariable=self.recur_batchnumber)
		e.pack()
		entry_single.grid(column=0,row=1,padx=1,stick=W)
		entry_single = Frame(recur_control)
		e = Entry(entry_single,width=10,textvariable=self.recur_devicenumber)
		e.pack()
		entry_single.grid(column=1,row=1,padx=1,stick=W)


		b = Button(recur_control, text="Graph",width=5,command=self.run_RecCur)
		b.bind("<Enter>",self.infoupdate_recurgraph)
		b.bind("<Leave>",self.infoupdate_reset)
		b.grid(column=2,row=0,rowspan=2,pady=1,padx=1)
		b = Button(recur_control,text="Previous",width=5,command=self.recur_previous)
		b.bind("<Enter>",self.infoupdate_previous)
		b.bind("<Leave>",self.infoupdate_reset)
		b.grid(column=3,row=0,rowspan=2,pady=1,padx=1)
		b = Button(recur_control,text="Next",width=5,command=self.recur_next)
		b.bind("<Enter>",self.infoupdate_next)
		b.bind("<Leave>",self.infoupdate_reset)
		b.grid(column=4,row=0,rowspan=2,pady=1,padx=1)
		

		graph1_frame = Frame(main_frame,bd=2)
		graph1_frame.bind("<Enter>",self.locupdate_graph1)
		graph1_frame.grid(column=0, row=0, pady=5,sticky=N+S+W+E)
		self.graph1_batchnumber = IntVar()
		self.graph1_devicenumber = IntVar()
		self.graph1_pixelnumber = IntVar()
		self.graph1_pixelnumber.set(1)


		graph1_fig = Figure(figsize=(1055/100,450/100),dpi=100)
		self.graph1_plot1 = graph1_fig.add_subplot(1,1,1)

		self.graph1_canvas = FigureCanvasTkAgg(graph1_fig, graph1_frame)
		self.graph1_canvas.show()
		self.graph1_canvas.get_tk_widget().pack(side=TOP,fill=BOTH)
		self.graph1_canvas._tkcanvas.pack(side=TOP,fill=BOTH)

		graph1_control = Frame(graph1_frame,bd=2,relief=SUNKEN)
		graph1_control.pack(side=LEFT)

		l = Label(graph1_control,text="Batchnumber")
		l.pack(side=LEFT,pady=2,padx=2)
		e = Entry(graph1_control,width=10,textvariable=self.graph1_batchnumber)
		e.pack(side=LEFT,pady=2,padx=2)
		l = Label(graph1_control,text="Devicenumber")
		l.pack(side=LEFT,pady=2,padx=2)
		e = Entry(graph1_control,width=10,textvariable=self.graph1_devicenumber)
		e.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph1_control, text="Graph",command=self.graph1_run)
		b.bind("<Enter>",self.infoupdate_graph)
		b.bind("<Leave>",self.infoupdate_reset)
		b.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph1_control,text="Previous",command=self.graph1_previous)
		b.pack(side=LEFT,pady=2,padx=2)
		b.bind("<Enter>",self.infoupdate_previous)
		b.bind("<Leave>",self.infoupdate_reset)
		b = Button(graph1_control,text="Next",command=self.graph1_next)
		b.pack(side=LEFT,pady=2,padx=2)
		b.bind("<Enter>",self.infoupdate_next)
		b.bind("<Leave>",self.infoupdate_reset)
		b = Button(graph1_control,text="Export",command=self.graph1_export)
		b.bind("<Enter>",self.infoupdate_export)
		b.bind("<Leave>",self.infoupdate_reset)
		b.pack(side=LEFT,pady=2,padx=2)

		graph2_frame = Frame(main_frame,bd=2)		
		graph2_frame.bind("<Enter>",self.locupdate_graph2)
		graph2_frame.grid(column=0,row=1,pady=5,sticky=N+S+E+W)
		self.graph2_batchnumber = IntVar()
		self.graph2_devicenumber = IntVar()
		self.graph2_pixelnumber = IntVar()
		self.graph2_pixelnumber.set(1)

		graph2_fig = Figure(figsize=(1055/100,450/100),dpi=100)
		self.graph2_plot1 = graph2_fig.add_subplot(1,1,1)

		self.graph2_canvas = FigureCanvasTkAgg(graph2_fig, graph2_frame)
		self.graph2_canvas.show()
		self.graph2_canvas.get_tk_widget().pack(side=TOP,fill=BOTH)
		self.graph2_canvas._tkcanvas.pack(side=TOP,fill=X)

		graph2_control = Frame(graph2_frame,bd=2,relief=SUNKEN)
		graph2_control.pack(side=LEFT)

		l = Label(graph2_control,text="Batchnumber")
		l.pack(side=LEFT,pady=2,padx=2)
		e = Entry(graph2_control,width=10,textvariable=self.graph2_batchnumber)
		e.pack(side=LEFT,pady=2,padx=2)
		l = Label(graph2_control,text="Devicenumber")
		l.pack(side=LEFT,pady=2,padx=2)
		e = Entry(graph2_control,width=10,textvariable=self.graph2_devicenumber)
		e.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph2_control, text="Graph",command=self.graph2_run)
		b.bind("<Enter>",self.infoupdate_graph)
		b.bind("<Leave>",self.infoupdate_reset)
		b.pack(side=LEFT,pady=2,padx=2)
		b = Button(graph2_control,text="Previous",command=self.graph2_previous)
		b.pack(side=LEFT,pady=2,padx=2)
		b.bind("<Enter>",self.infoupdate_previous)
		b.bind("<Leave>",self.infoupdate_reset)
		b = Button(graph2_control,text="Next",command=self.graph2_next)
		b.pack(side=LEFT,pady=2,padx=2)
		b.bind("<Enter>",self.infoupdate_next)
		b.bind("<Leave>",self.infoupdate_reset)
		b = Button(graph2_control,text="Export",command=self.graph2_export)
		b.bind("<Enter>",self.infoupdate_export)
		b.bind("<Leave>",self.infoupdate_reset)
		b.pack(side=LEFT,pady=2,padx=2)

		
	def infoupdate_recurgraph(self,event):
	     self.info.set("Graphs the Recur graph of selected data")

	def infoupdate_runprocess(self,event):
	     self.info.set("Processes selected batch")

	def locupdate_recur(self,event):
            self.loc.set("the Rectification Curve")
	
	def locupdate_graph1(self,event):
	     self.loc.set("Graph 1")
	
	def locupdate_graph2(self,event):
	     self.loc.set("Graph 2")

	def infoupdate_graph(self,event):
	     self.info.set("graphs selected data on %s" % self.loc.get())

	def infoupdate_previous(self,event):
            self.info.set("scrolls to the previous device on %s" % self.loc.get())
    
	def infoupdate_next(self,event):
            self.info.set("scrolls to next device on %s" % self.loc.get())

	def infoupdate_export(self,event):
	     self.info.set("Exports %s" % self.loc.get())		

	def infoupdate_reset(self,event):
	     self.info.set("holder")
	     
	def run_process_batch(self):
            pd.process_batch(self.process_batchnumber.get(),self.process_batchsize.get())
	
	def run_RecCur(self):
            data = ad.RecCur(self.recur_batchnumber.get(),self.recur_devicenumber.get(),self.recur_pixelnumber.get())
            self.recur_plot.cla()
            self.recur_plot.plot(data[0],data[1])
            self.recur_canvas.show()
	
	def recur_next(self):
            hold = ((self.recur_pixelnumber.get() + 1) % 5)
            if hold == 0:
                hold = 1
            self.recur_pixelnumber.set(hold)  
            self.run_RecCur()
	
	def recur_previous(self):
            hold = ((self.recur_pixelnumber.get() - 1) % 5)
            if hold == 0:
            	hold = 4
            self.recur_pixelnumber.set(hold)
            self.run_RecCur() 

	def graph1_run(self):
            data = ad.IVdata(self.graph1_batchnumber.get(),self.graph1_devicenumber.get(),self.graph1_pixelnumber.get())
            self.graph1_plot1.cla()
            self.graph1_plot1.plot(data[0],data[1])
            self.graph1_canvas.show()

	def graph1_next(self):
            hold = ((self.graph1_pixelnumber.get()+1)%5)
            if hold == 0:
                hold =1
            self.graph1_pixelnumber.set(hold)
            self.graph1_run()

	def graph1_previous(self):
            hold = ((self.graph1_pixelnumber.get()-1)%5)
            if hold == 0:
                hold =4
            self.graph1_pixelnumber.set(hold)
            self.graph1_run()

	def graph1_export(self):
            ad.makeplots(self.graph1_batchnumber.get(),'A')
            ad.makeplots(self.graph1_batchnumber.get(),'E')

	def graph2_run(self):
            data = ad.IVdata(self.graph2_batchnumber.get(),self.graph2_devicenumber.get(),self.graph2_pixelnumber.get())
            self.graph2_plot1.cla()
            self.graph2_plot1.plot(data[0],data[1])
            self.graph2_canvas.show()

	def graph2_next(self):
			hold = ((self.graph2_pixelnumber.get()+1)%5)
			if hold == 0:
				hold =1
			self.graph2_pixelnumber.set(hold)
			self.graph2_run()

	def graph2_previous(self):
            hold = ((self.graph2_pixelnumber.get()-1)%5)
            if hold == 0:
                hold =4
            self.graph2_pixelnumber.set(hold)
            self.graph2_run()

	def graph2_export(self):
            ad.makeplots(self.graph2_batchnumber.get(),'A')
            ad.makeplots(self.graph2_batchnumber.get(),'E')