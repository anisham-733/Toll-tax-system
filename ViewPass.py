from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from pymysql import paramstyle
from connection import *
class main:
    def get(self):
        conn=connect()
        cur=conn.cursor()
        stat="select * from monthlypass"
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

    def upadtePass(self,):
        self.id = self.e1.get()
        self.vehtype = self.combo1.get()
        self.price = self.e2.get()
        #self.description = self.e4.get()
        conn=connect()
        cr=conn.cursor()
        
        q="update monthlypass set vehicle_category='{}',monthly_pass = '{}' where id='{}'".format(self.vehtype,self.price,self.id)
        cr.execute(q)
        #ans=cr.fetchone()
        conn.commit()
        self.get()
        
        messagebox.showinfo("","Updation done successfully",parent=self.update)
        self.update.destroy()
        self.get()

    def deletePass(self):
        self.id = self.e1.get()
        conn = connect()
        cr = conn.cursor()
        q = 'delete from monthlypass where id="{}"'.format(self.id)
        cr.execute(q)
        conn.commit()
        self.get()
        
        messagebox.showinfo("", "Deleted successfully",parent=self.update)
        self.update.destroy()

    def __init__(self):
        self.root=Toplevel()
        
        self.root.resizable(0,0)
        self.root.title("Montly Pass Fares")
        self.root.configure(background="#262626")
        width = 1000
        height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.root.iconbitmap('icons/toll_price.ico')
        Label(self.root,text="Monthly Pass Tollway Fares",font=("helvetica",42,"bold"),
                    foreground="#F0F6FC",background='#262626').place(relx=0.04,rely=0.02)
       
        #Add style
        self.s = ttk.Style()

       
        
        # Pick a theme
        self.s.theme_use("default")
        #Treeview Configurations
        self.s.configure('Treeview', font=('Helvetica', 16), rowheight=37,borderwidth=2,bordercolor='white',background='#21262D',
                         foreground='#F0F6FC', fieldbackground='#21262D')
        self.s.configure('Treeview.Heading', font=("Helvetica", 18, "bold"), rowheight=30,
                         foreground='#F0F6FC',bordercolor='white',borderwidth=2,background='#21262D')
        # Change selected color
        self.s.map('Treeview', background=[('selected','#21262DF')])
        self.s.map('Treeview.Heading', background=[('selected', '#21262D')])

        col =("ID","Vehicle Category","Monthly tax amount")

        self.t1=ttk.Treeview(self.root,columns=col)
        self.t1.column('ID',width=80)
        self.t1.column('Vehicle Category',width=220)
        self.t1.column("Monthly tax amount",width=180)
        #Treeview
        
       # k=150
        for i in col:
            self.t1.heading(i,text=i)


        self.t1["show"]="headings"
        self.t1.place(relx=0.1,rely=0.22,relwidth=0.8,relheight=0.6)
        self.get()
        #binding things ,event when we double click on the mouse,2nd arg func is passed
        self.t1.bind('<Double-1>',self.onDoubleClick)

        #create menu bar
        self.menu=Menu(self.root)
        self.root.config(menu=self.menu)
        #submenu
        self.modify=Menu(self.menu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
        self.menu.add_cascade(label="Modify",font=('Helvetica',12),menu=self.modify)
        #
        self.modify.add_command(label="Add New Pass",command=self.addWin)

        self.menu.add_cascade(label="Double-click the record for updation/delete ",state=DISABLED,
                                font=('Helvetica',12,'bold'),menu=self.modify)

        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.root,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.root.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.025,relheight=0.05)
        
        self.root.grab_set()
        self.root.transient()
        self.root.mainloop()


    def onDoubleClick(self,event): #whenever we use binding we need to pas an event
        # self.root.destroy()
        #item func of Treeview takes focus func as first arg,values(which will return all the values in the selected item)
        self.items=self.t1.item(self.t1.focus())['values'] #focus func returns selected row in Treeview
        # Self.items will fetch email and role
        #print("hi,",self.items)
        print(self.items[1])

        self.update_win()

    #update window
    def update_win(self):
        
        self.update = Toplevel()
        self.update.iconbitmap('icons/toll_price.ico')
        self.update.title("Modification of Monthly Pass amount")
        self.update.resizable(0, 0)
        #self.update.geometry('800x650')
        self.update.configure(background="#262626")
        width = 800
        height = 650
        screen_width = self.update.winfo_screenwidth()
        screen_height = self.update.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.update.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.update.iconbitmap('icons/toll_price.ico')
        Label(self.update, text="Modify Monthly Pass fares",foreground="#F0F6FC",
                        background='#262626', font=("Helvetica", 42, "bold")).place(relx=0.04, rely=0.02)
        Label(self.update, text="Id ", font=("Helvetica", 20, 'bold'),
              foreground="#58A6FF",background='#262626').place(relx=0.09, rely=0.25)

        self.e1=Entry(self.update,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e1.place(relx=0.46,rely=0.24,relwidth=0.48,relheight=0.06)
        self.e1.config(insertbackground='black')

        Label(self.update, text="Vehicle category ", font=("Helvetica", 20, 'bold'), foreground="#58A6FF",
                        background='#262626').place(relx=0.09, rely=0.36)

       
        col=('Car/Jeep/Van','Light Commercial vehicles','Bus/Truck','3-axle vehicles',
                    '4 to 6 axle vehicles','Heavy vehicles','7 or more axle vehicles')
       
       #Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly','#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])
            
        self.combo1=ttk.Combobox(self.update,values=col,font=("Helvetica",16),background='#F0F6FC',foreground='#262626',
                            width=28,state='readonly')
        self.combo1.place(relx=0.46,rely=0.36,relwidth=0.48,relheight=0.06)

        Label(self.update, text="Monthly Pass Fare ", font=("Helvetica", 20, 'bold'),foreground="#58A6FF",
                        background='#262626').place(relx=0.09, rely=0.48)
        # entrybox for price
        self.e2=Entry(self.update,font=("Helvetica",18),background='#F0F6FC',foreground='#3D1F1D',cursor="xterm #0000FF")
        self.e2.place(relx=0.46,rely=0.48,relwidth=0.48,relheight=0.06)
        self.e2.config(insertbackground='black')


        self.b1 = Button(self.update, text="Update", font=("Helvetica", 18, 'bold'), relief='groove',bg='#238636',
                     activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff', command=self.upadtePass)
        self.b1.place(relx=0.4,rely=0.76,relwidth=0.2,relheight=0.1) 

        self.b2 = Button(self.update, text="Delete", font=("Helvetica", 19, 'bold'), relief='groove',bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff', command=self.deletePass)
        self.b2.place(relx=0.7,rely=0.76,relwidth=0.2,relheight=0.1) 
        #print(self.items)
        curr = col.index((self.items[1]))  # index func returns index
        print(curr)
        self.combo1.current(curr)  # default value in combobox ,current func takes index a number as argument
        self.e1.insert(0, self.items[0])
        self.e1.config(state='readonly')
        self.e2.insert(0, self.items[2])
        self.update.grab_set()
        self.update.transient()

        self.update.mainloop()

        

    def check(self):
        self.vehtype = self.txt1.get()
        self.price = self.txt2.get()
        conn = connect()
        cr = conn.cursor()
        if  self.vehtype == "" or self.price == "":
            messagebox.showerror("", "Please Enter Data !!",parent=self.root)
        else:
            q = "select * from monthlypass where vehicle_category='{}'".format(self.vehtype)
            cr.execute(q)
            ans = cr.fetchone()
            if ans == None:
                q = "insert into monthlypass value ('','{}','{}')".format(self.vehtype, self.price)
                cr.execute(q)
                conn.commit()
                self.get()
                messagebox.showinfo("", "Monthly  Pass registered successfully !!",parent=self.add)
                self.add.destroy()
            else:
                messagebox.showerror("", "Monthly pass already registered for the automobile",parent=self.add)

    #-------Add Window
    def addWin(self):
        self.add = Toplevel()
        self.add.iconbitmap('icons/toll_price.ico')
        self.add.resizable(0, 0)
        self.add.title("Add a new Monthly pass")
        self.add.configure(background="#262626")
        width = 800
        height = 500
        screen_width = self.add.winfo_screenwidth()
        screen_height = self.add.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.add.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.add.iconbitmap("icons/toll_price.ico")

        Label(self.add, text="Register Monthly Pass", font=("Helvetica", 42, "bold"), foreground="#F0F6FC",
                        background='#262626').place(relx=0.04, rely=0.02)

        columns=('Car/Jeep/Van','Light Commercial vehicles','Bus/Truck','3-axle vehicles',
                    '4 to 6 axle vehicles','Heavy vehicles','7 or more axle vehicles')

        Label(self.add,text="Select Vehicle Category", font=("Helvetica", 20, 'bold'),foreground="#58A6FF",
                        background='#262626').place(relx=0.09, rely=0.28)

         # Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly','#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])

        self.txt1=ttk.Combobox(self.add,values=columns, state="readonly",font=("Helvetica", 16),foreground='#262626',width=28)
        self.txt1.place(relx=0.52,rely=0.28,relwidth=0.44,relheight=0.08)

        Label(self.add, text="Monthly Pass Amount ", font=("Helvetica", 20, 'bold'),foreground="#58A6FF",
                        background='#262626').place(relx=0.09, rely=0.44)
        self.txt2 = Entry(self.add, font=("Helvetica", 16),foreground='#262626',background='#F0F6FC')
        self.txt2.place(relx=0.52,rely=0.44,relwidth=0.44,relheight=0.08)
        self.txt2.config(insertbackground='black')

        self.b1=Button(self.add, text="Add Monthly pass",font=("Helvetica",16,'bold'), borderwidth=2,
                        relief='groove',bg='#238636',activebackground='#238636',activeforeground='#ffffff',
                        foreground='#ffffff',command=self.check)

        self.b1.place(relx=0.6,rely=0.64,relwidth=0.34,relheight=0.14)
        self.add.grab_set()
        self.add.transient()
        self.add.mainloop()


#------------------------------
# main()