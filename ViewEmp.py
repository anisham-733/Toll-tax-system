from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

from connection import *


class main:
   
    def get(self):
        conn=connect()
        cur=conn.cursor()
        stat="select email,role from admin"
        cur.execute(stat)
        res=cur.fetchall()
        # print(res)
        x=[]
        for row in res:
            lst=list(row)
            # print(lst)
            x.append(lst)
        for k in self.t1.get_children():
            self.t1.delete(k) #deleting all the records in treeview all at once after refreshing or opening the window more than once
        count=0
        for i in x:
            self.t1.insert("",index=count,values=i)
            count+=1
    def search(self):
        self.t1.delete(*self.t1.get_children())
        conn=connect()
        cur=conn.cursor()
        stat="select email,role from admin"
        cur.execute(stat)
        res=cur.fetchall() #tuple of tuples
        # print(res)
        x=[]
        i=0
        for row in res:
            if self.entry.get() in row[0]:
                l=list(row) #list
                x.append(l)#list of lists
        
        for rows in x:
            self.t1.insert("",index=i,values=rows)
            i+=1
    
    def __init__(self):
        
        self.root=Toplevel()
        width=850
        height=650
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        
        self.root.title("Employees' Record")
        
        self.root.resizable(0,0)
        self.root.configure(background='#262626')
        # Icon of View Employees window
        self.root.iconbitmap('icons/emp1.ico')
        Label(self.root,text='Registered Employees',foreground="white",background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
       
        Label(self.root,text="Enter Email to search",font=("Helvetica",20,'bold'),foreground="#58A6FF",background="#262626").place(relx=0.04,rely=0.23)
        
        
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
        
        col=('Email','Role')

        self.frame=Frame(self.root)
        self.t1=ttk.Treeview(self.frame,columns=col)

        for i in col:
            print(i)
            self.t1.heading(i,text=i)

        self.t1['show']="headings"
        self.frame.place(relx=0.1,rely=0.34,relwidth=0.8,relheight=0.6)
        self.t1.place(relx=0,rely=0,relwidth=1,relheight=1)
        # self.t1.place(relx=0.1,rely=0.34,relwidth=0.8,relheight=0.6)

         #Vertical SCrollbar
        self.scroll = ttk.Scrollbar(self.frame, orient ="vertical", 
                           command = self.t1.yview)
        self.scroll.pack(side ='right', fill ='both')
  
        # Configuring treeview
        self.t1.configure(yscrollcommand = self.scroll.set)
  
        self.get()

        #binding things ,event when we double click on the mouse,2nd arg func is passed
        self.t1.bind('<Double-1>',self.onDoubleClick)

        #Search button
        img=ImageTk.PhotoImage(Image.open("search1.png"))
        self.img_button=Button(self.root,image=img,background='#262626',command=self.search)
        self.img_button.place(relx=0.835,rely=0.23,relheight=0.06,relwidth=0.05)

        refresh_img=ImageTk.PhotoImage(Image.open("refresh1.png"))
        self.img1_button=Button(self.root,image=refresh_img,background='#262626',command=self.get)
        self.img1_button.place(relx=0.89,rely=0.23,relheight=0.06,relwidth=0.05)

        #Entry box for search
        self.entry=Entry(self.root,background='white',font=('Helvetica',19),foreground='black')
        self.entry.place(rely=0.23,relx=0.4,relwidth=0.42,relheight=0.06)

        #Create a menu bar
        self.menu=Menu(self.root)
        self.root.config(menu=self.menu)
        #submenu
        self.modify=Menu(self.menu,foreground='white',background='#262626',activebackground='#0077B6',borderwidth=0,tearoff=0)
        self.menu.add_cascade(label="Modify",font=('Helvetica',12),menu=self.modify)

        self.modify.add_command(label='Add Employee',command= self.add_main)
        self.update_del=Menu(self.menu,tearoff=0)
        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.root,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.root.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.025,relheight=0.05)
        self.menu.add_cascade(label="Double-click the record for updation/deletion",font=('Helvetica',12,'bold'),state=DISABLED,menu=self.update_del)

        self.root.resizable(0,0)

        self.root.grab_set()
        self.root.transient()
        self.root.mainloop()
    def Update_Emp(self):
        self.email=self.e1.get()
        self.password=self.e2.get()
        self.role=self.combo1.get()
        conn=connect()
        cur=conn.cursor()
        stat='update admin set password="{}", role="{}" where email="{}"'.format(self.password, self.role, self.email)
        cur.execute(stat)
        # res=cur.fetchone()
        # for i in res:
        #     print(i)
        conn.commit()
        self.get()
        
        self.update.destroy()
        messagebox.showinfo("","Updation done succesfully",parent=self.root)
    def Delete_Emp(self):
        self.email = self.e1.get()
        conn = connect()
        cr = conn.cursor()
        q = 'delete from admin where email="{}"'.format(self.email)
        cr.execute(q)
        conn.commit()
        self.get()
        messagebox.showinfo("","Deleted successfully",parent=self.root)
        self.update.destroy()
        
    def add(self):
        conn=connect()
        cur=conn.cursor()

        self.email=self.txt1.get()
        self.password=self.txt2.get()
        self.role=self.txt3.get()
        if self.email=='' or self.password=='' or self.role=='':
            messagebox.showerror("","Please add the fields",parent=self.root)
        else:
                

            stat='select * from admin where email="{}"'.format(self.email)
            cur.execute(stat)
            res=cur.fetchone()
            if res==None:
                insert='insert into admin values("{}","{}","{}")'.format(self.email,self.password,self.role)
                cur.execute(insert)
                conn.commit()
                self.get()
                messagebox.showinfo("","Record added successfully",parent=self.root)
                
                self.top.destroy()
            else:
                messagebox.showerror("","User already registered",parent=self.root)
                        
    def add_main(self):
        self.top=Toplevel()
        width=650
        height=650
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.top.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        
        self.top.resizable(0,0)
        self.top.transient()
        self.top.grab_set()
        self.top.configure(background="#262626")
        self.top.iconbitmap("add_winicon.ico")
        self.top.title("Registration of a Toll booth worker")

        Label(self.top,text="Add Record",foreground="white",background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
        
        Label(self.top,text="Enter Email : ",font=('Helvetica',22,'bold'),foreground="#58A6FF"
                    ,background="#262626").place(relx=0.19,rely=0.22)

        self.txt1=Entry(self.top,font=("Helvetica",16),background='white',foreground='#3D1F1D')
        self.txt1.place(relx=0.27,rely=0.32,relwidth=0.50,relheight=0.06)

        Label(self.top, text="Enter Password : ",font=("Helvetica",22,'bold'),foreground="#58A6FF",
                    background="#262626").place(relx=0.19, rely=0.42)

        self.txt2 = Entry(self.top,background='white',foreground='#3D1F1D',show="*",font=("Helvetica",16))
        self.txt2.place(relx=0.27, rely=0.52,relwidth=0.50,relheight=0.06)
        
        Label(self.top, text="Select Role : ",font=("Helvetica",22,'bold'),foreground="#58A6FF",
                    background="#262626").place(relx=0.19, rely=0.62)

        self.txt3=ttk.Combobox(self.top,values=('Super Admin','Admin'),background='white',
                    foreground='#3D1F1D',width=28,state='readonly',font=("Helvetica",16))
                    
        self.txt3.place(relx=0.27,rely=0.72,relwidth=0.50,relheight=0.06)

         #Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', 'white')])
        self.s.map('TCombobox', fieldbackground=[('readonly','white')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#3D1F1D')])
           
        self.b1=Button(self.top, text="Register",font=("Helvetica",16,'bold'), borderwidth=2,relief='groove',bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff', command=self.add)
        self.b1.place(relx=0.72,rely=0.88,relwidth=0.2,relheight=0.1)
        self.top.grab_set()
        self.top.mainloop()


    



    
    
    
    def onDoubleClick(self,event): #whenever we use binding we need to pas an event
        # self.root.destroy()
        #item func of Treeview takes focus func as first arg,values(which will return all the values in the selected item)
        self.items=self.t1.item(self.t1.focus())['values'] #focus func returns selected row in Treeview
        # Self.items will fetch email and role
        print("hi,",self.items)
        print(self.items[1])
        conn=connect()
        cur=conn.cursor()
        stat="select password from admin where email='{}'".format(self.items[0])

        cur.execute(stat)
        
        p=cur.fetchone()
        print(p)
        
    
    # Update window
    
        self.update=Toplevel()
        self.update.title("Updation of Employee's record")
        self.update.resizable(0,0)
        width=650
        height=650
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.update.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        
        self.update.configure(background="#262626")
        self.root.iconbitmap('emp1.ico')
        
        Label(self.update,text="Modify Record",foreground="#F0F6FC",background='#262626',
                font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
        
        Label(self.update,text="Email  ",font=("Helvetica",22,'bold'),foreground="#58A6FF",
                background="#262626").place(relx=0.09,rely=0.30)
        
        self.e1=Entry(self.update,font=("Helvetica",18),background='#F0F6FC',foreground='#3D1F1D')
        self.e1.place(relx=0.42,rely=0.30,relwidth=0.50,relheight=0.06)

        Label(self.update,text="Password  ",font=("Helvetica",22,'bold'),foreground="#58A6FF",
                background="#262626").place(relx=0.09,rely=0.40)
        
        self.e2=Entry(self.update,show='*',font=("Helvetica",18),background='#F0F6FC',foreground='#3D1F1D')
        self.e2.place(relx=0.42,rely=0.40,relwidth=0.50,relheight=0.06)

        Label(self.update,text="Role  ",font=("Helvetica",22,'bold'),foreground="#58A6FF",
                    background="#262626").place(relx=0.09,rely=0.50)
        
        col=['Super Admin','Admin']
        self.combo1=ttk.Combobox(self.update,values=col,font=("Helvetica",18),width=28,background='#262626',
                    foreground='white',state='readonly')
        self.combo1.place(relx=0.42,rely=0.50,relwidth=0.50,relheight=0.06)

        #Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly','#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])

        self.b1=Button(self.update,text="Update",font=("Helvetica",18,'bold'),relief='groove',borderwidth=2,
                        bg='#238636',activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command= self.Update_Emp)
        self.b1.place(relx=0.21,rely=0.68,relwidth=0.2,relheight=0.1)

        self.b2 = Button(self.update, text="Delete", font=("Helvetica", 18, 'bold'),relief='groove',borderwidth=2,
                        bg='#238636',activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command= self.Delete_Emp)
        self.b2.place(relx=0.60, rely=0.68, relwidth=0.2, relheight=0.1)

        print(self.items)
         #default value in combobox ,current func takes index a number as argument

        current=col.index(self.items[1]) #index func returns index

        print(current)
        self.combo1.current(current) #default value in combobox ,current func takes index a number as argument

        self.e1.insert(0,self.items[0])
        self.e1.config(state='readonly')
        self.e2.insert(0,p)
        self.update.transient(self.root)
        self.update.grab_set()
        self.update.mainloop()
    
# obj=main()


# tkk.tree.focus returns the selected item row in the Treeview. If nothing is selected then it returns an empty string (“”).
# ttk.tree.item() takes tkk.tree.focus as an argument followed by ‘value‘. This will return all the values in the selected item. These values are returned in a tuple.