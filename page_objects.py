# These are the files that need to be imported

# from tkinter import * # Python 3
# # from Tkinter import * # Python 2

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