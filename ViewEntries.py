from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *

class Entries_main:
    global conn,cr
    conn=connect()
    cr=conn.cursor()
    def insert_values(self):
        stat_entries=f"select vehicleid,toll_id,entry_date,entry_time,entry_type from entry"
        cr.execute(stat_entries)
        result=cr.fetchall()
        x = []
        for row in result:
            lst = list(row)
            x.append(lst)
        print(x)
        for k in self.tree.get_children():
            self.tree.delete(k)
        count = 0
        
        for i in x:
            self.tree.insert('', index=count, values=i)

    def __init__(self):
        self.root=Toplevel()
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.title("Registered vehicle entries ")
        self.root.iconbitmap('icons/tollpanel.ico')
        self.root.configure(background='#262626')
        self.label_frame=LabelFrame(self.root,text='Automobile Entries Record',borderwidth=3,bd=5,labelanchor=NW,font=('Helvetica',42,'bold')
                                    ,background='#262626',foreground="#F0F6FC")
        self.label_frame.place(relx=0.04,rely=0.02,relwidth=0.9,relheight=0.75)

        
        #Add a style
        self.s=ttk.Style()

        def fixed_map(option):
        
            return [elm for elm in self.s.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]
        
        self.s.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
        #Pick a theme
        self.s.theme_use("default")

        #Configure Treeview colors
        self.s.configure('Treeview',bordercolor='white',borderwidth=2,background='#21262D',
                            font=("Helvetica",16),foreground='#F0F6FC',rowheight=37,fieldbackground='#21262D')
        self.s.configure('Treeview.Heading',font=("Helvetica",18,"bold"),rowheight=30,
                            foreground='#F0F6FC',bordercolor='white',borderwidth=2,background='#21262D')
        #Change selected color
        self.s.map('Treeview',background=[('selected','#21262DF')])
        self.s.map('Treeview.Heading',background=[('selected','#21262D')])
        col=('Vehicle id','Toll id','Entry Date','Entry Time','Journey type')
        self.tree=ttk.Treeview(self.label_frame,columns=col)
        self.tree.place(relx=0,rely=0.07,relheight=0.93,relwidth=1)
        self.insert_values()
        #Vertical SCrollbar
        self.scroll = ttk.Scrollbar(self.tree, orient ="vertical",command = self.tree.yview)
        self.scroll.pack(side ='right', fill ='y')
  
        # Configuring treeview
        self.tree.configure(yscrollcommand = self.scroll.set)
        
        self.tree.column('Vehicle id',width=100)
        self.tree.column('Toll id',width=100)
        self.tree.column('Entry Date',width=150)
        self.tree.column('Entry Time',width=150)
        self.tree.column('Journey type',width=180)
        
        

        for i in col:
            print(i)
            self.tree.heading(i,text=i)

        self.tree['show']="headings"

        self.back=Button(self.root,text='Back to Dashboard',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.root.destroy)
        self.back.place(relx=0.08,rely=0.85,relheight=0.08,relwidth=0.2)
        self.root.grab_set()
        self.root.transient()
        self.root.mainloop()


# Entries_main()