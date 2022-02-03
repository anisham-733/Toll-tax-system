from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from connection import *


class Toll_main:
    
    def search(self):
        self.t1.delete(*self.t1.get_children())
        # "Toll id",'Toll Plaza Name','City','State'
        conn=connect()
        cur=conn.cursor()
        q='select tollid,toll_name,city,state,email from tollplaza'
        cur.execute(q)
        res=cur.fetchall()
        print(res)
        x=[]
        i=0
        flag=0
        for row in res:
            if self.cb.get() == "Toll id":
                if self.e1.get().capitalize() in str(row[0]):
                    l=list(row)
                    x.append(l)
                    flag=1


            elif self.cb.get()=="Toll Plaza Name":
                if self.e1.get().capitalize() in row[1]:
                    print(row[1])
                    l=list(row)
                    x.append(l)
                    flag=1
            elif self.cb.get()=='City':
                if self.e1.get().capitalize() in row[2]:
                    l=list(row)
                    x.append(l)
                    flag=1
            elif self.cb.get()=='State':
                if self.e1.get().capitalize() in row[3]:
                    l=list(row)
                    x.append(l)
                    flag=1          
            else:
                messagebox.showerror("","No Option Selected")


        for r in x:
            
            self.t1.insert("",index=i,values=r)
            i=i+1
        if flag == 1:
            messagebox.showinfo("", "Data Found",parent=self.root)
        else:
            messagebox.showerror("", "No data found",parent=self.root)


    def refresh(self):
        self.get()

    
    
    def get(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select tollid,toll_name,city,state,email from tollplaza'
        cr.execute(q)
        result = cr.fetchall()
        x = []
        for row in result:
            lst = list(row)
            x.append(lst)
        for k in self.t1.get_children():
            self.t1.delete(k)
        count = 0
        
        for i in x:
            self.t1.insert('', index=count, values=i)
            
            count += 1
    def __init__(self):
        self.root=Toplevel()
        width=1400
        height=800
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        # self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.title("Toll Plaza")
        self.root.configure(background='#262626')
        self.root.iconbitmap('icons/tollplaza1.ico')
        Label(self.root,text='National Toll Plaza Details',foreground="#F0F6FC",
                        background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)

        Label(self.root,text='Select field to search',foreground="#58A6FF",
                        background='#262626',font=("Helvetica",20,"bold")).place(relx=0.04,rely=0.23)
        
        self.cb=ttk.Combobox(self.root,values=("Toll id",'Toll Plaza Name','City','State')
                        ,state='readonly',font=('Helvetica',18))
        self.cb.place(relx=0.27,rely=0.23,relwidth=0.25,relheight=0.06)

        #Add a style
        self.s=ttk.Style()

        #Pick a theme
        self.s.theme_use("default")
        self.s.map('TCombobox', selectbackground=[('readonly', '#21262D')]) 
        self.s.map('TCombobox', fieldbackground=[('readonly','#21262D')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#C9D1D9')])

        self.e1=Entry(self.root,font=('Helvetica',18),foreground='#262626',background='#F0F6FC', cursor="xterm #0000FF")
        self.e1.place(relx=0.55,rely=0.23,relwidth=0.27,relheight=0.06)

        self.e1.insert(0,'Search')

        def entry_clear(e):
            if self.e1.get()=='Search':
                self.e1.delete(0,END)
        #Bind the entry boxes
        self.e1.bind("<Button-1>",entry_clear)
        self.e1.config(insertbackground='black')

        img=ImageTk.PhotoImage(Image.open("search1.png"))
        self.img_button=Button(self.root,image=img,background='#171515',activebackground='#171515',command=self.search)
        self.img_button.place(relx=0.78,rely=0.23,relheight=0.06,relwidth=0.04)

        refresh_img=ImageTk.PhotoImage(Image.open("refresh1.png"))
        self.img1_button=Button(self.root,image=refresh_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.refresh)
        self.img1_button.place(relx=0.84,rely=0.23,relheight=0.06,relwidth=0.04)

        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.root,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.root.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.015,relheight=0.03)

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
        

        col = ('Toll id','Toll Plaza Name','City','State','Email')
        self.frame=Frame(self.root)
        
        self.t1=ttk.Treeview(self.frame,columns=col)
        
         
        self.t1.column('Toll id',width=100)
        self.t1.column('Toll Plaza Name',width=260)
        self.t1.column('City',width=200)
        self.t1.column('State',width=200)
        
        self.t1.column('Email',width=300)

        for i in col:
            print(i)
            self.t1.heading(i,text=i)

        self.t1['show']="headings"

          
        self.frame.place(relx=0.06,rely=0.36,relwidth=0.9,relheight=0.47)
        self.t1.place(relx=0,rely=0,relwidth=1,relheight=1)

        
        
        self.get()

       
        self.root.grab_set()
        self.root.transient()
        


        self.root.mainloop()

# Toll_main()
