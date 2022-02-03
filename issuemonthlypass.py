from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from pymysql import cursors
from connection import *
from datetime import date
from datetime import timedelta
from datetime import datetime

class issue_pass():
    def get(self):
        global conn,cur
        conn=connect()
        cur=conn.cursor()
        # conn = connect()
        # cur = conn.cursor()
        stat = "select id,date_of_issue,expirydate,fare_type from issuemonthlypass"
        cur.execute(stat)
        res = cur.fetchall()
        # print(res)
        x = []
        for row in res:
            lst = list(row)
            # print(lst)
            x.append(lst)
        for k in self.t1.get_children():
            self.t1.delete(k)  # deleting all the records in treeview all at once after refreshing or opening the window more than once
        count = 0
        for i in x:
            self.t1.insert('', index=count, values=i)

            count += 1

    def get_vehicleid(self):
        # conn = connect()
        # cur = conn.cursor()
        stat = "select id,vehicle_no from vehicle_reg where journey_type='Monthly Pass'"
        cur.execute(stat)
        res = cur.fetchall()
        x = []
        for row in res:
            lst = list(row)
            #print(lst)
            x.append(lst)
        

        return x

    def get_passid(self):
        # conn = connect()
        # cur = conn.cursor()
        stat = "select id,vehicle_category from monthlypass"
        cur.execute(stat)
        res = cur.fetchall()
        x = []
        for row in res:
            lst = list(row)
            # print(lst)
            x.append(lst)
        #print(x)

        return x
    def Add_issuedpass(self):
        # conn= connect()
        # cur=conn.cursor()
        self.vid=self.combo11.get()
        self.pid=self.combo22.get()
        self.date_is=self.tt1.get()
        self.date_ex=self.tt2.get()
        self.faret=self.combo33.get()
        if self.vid=='' or self.pid=='' or self.date_is=='' or self.date_ex=='' or self.faret=='':
            messagebox.showerror("",'Please enter the data!')
        else:
            stat='select vehicleid from issuemonthlypass where vehicleid="{}"'.format(self.vid)
            cur.execute(stat)
            res=cur.fetchone()
            if res==None:
                stat1='insert into issuemonthlypass values("","{}","{}","{}","{}","{}")'.format(self.vid,self.pid,self.date_is,self.date_ex,self.faret)
                cur.execute(stat1)
                conn.commit()
                messagebox.showinfo("","Pass Issued successfully!!")
                self.get()
                self.a.destroy()
            else:
                messagebox.showerror("","Pass already Issued!")



    def __init__(self):
        self.root = Tk()
       
        self.root.resizable(0, 0)
        self.root.title("Issue Monthly Pass to Vehicles")
        self.root.configure(background="#262626")
        width = 1000
        height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.root.iconbitmap('icons/add_winicon.ico')
        Label(self.root,text="Record of Issued Passes",font=("helvetica",42,"bold"),foreground="#F0F6FC",background='#262626').place(relx=0.04,rely=0.02)
        col = ('Id', 'Date of Issue', 'Date of Expiry', 'Payment mode')

        self.frame=Frame(self.root)
        self.t1 = ttk.Treeview(self.frame, columns=col)
        self.t1.column('Id', width=80)
        self.t1.column('Date of Issue', width=150)
        self.t1.column('Date of Expiry', width=150)
        self.t1.column('Payment mode', width=170)
        for i in col:
            self.t1.heading(i,text=i)

        self.t1['show']="headings"
        # Add a style
        self.s = ttk.Style()
        # Pick a theme
        self.s.theme_use("default")

        #Configure Treeview colors
        self.s.configure('Treeview',bordercolor='white',borderwidth=2,background='#21262D',
                            font=("Helvetica",16),foreground='#F0F6FC',rowheight=37,fieldbackground='#21262D')
        self.s.configure('Treeview.Heading',font=("Helvetica",18,"bold"),rowheight=30,
                            foreground='#F0F6FC',bordercolor='white',borderwidth=2,background='#21262D')
        #Change selected color
        self.s.map('Treeview',background=[('selected','#21262DF')])
        self.s.map('Treeview.Heading',background=[('selected','#21262D')])

        self.frame.place(relx=0.08,rely=0.24,relwidth=0.85,relheight=0.6)
        self.t1.place(relx=0,rely=0,relwidth=1,relheight=1)

        #Vertical SCrollbar
        self.scroll = ttk.Scrollbar(self.frame, orient ="vertical", 
                           command = self.t1.yview)
        self.scroll.pack(side ='right', fill ='y')
  
        # Configuring treeview
        self.t1.configure(yscrollcommand = self.scroll.set)
        # self.t1.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.6)
        self.get()

        # Create a menu bar
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        # submenu
        self.modify = Menu(self.menu, foreground='#ffffff', background='#0D1117', activebackground='#0D1117',
                           borderwidth=0, tearoff=0)
        self.menu.add_cascade(label="Add", font=('Helvetica', 12), menu=self.modify)

        self.modify.add_command(label='Issue monthly pass',command=self.Add_win)
        self.root.mainloop()
#Add window....

    def Add_win(self):
        self.a = Toplevel(self.root)
        width = 800
        height = 750
        screen_width = self.a.winfo_screenwidth()
        screen_height = self.a.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.a.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.a.resizable(0, 0)

        self.a.configure(background="#262626")
        self.a.iconbitmap("icons/add_Winicon.ico")
        self.a.title("Register a monthly pass to vehicle owner")

        Label(self.a, text="Issue Monthly Pass", foreground='#F0F6FC', background='#262626',
              font=("Helvetica", 42, "bold")).place(relx=0.04, rely=0.02)

        Label(self.a, text=" Vehicle ID : ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.24)
        # Add a style
        self.s = ttk.Style()

        # Pick a theme
        self.s.theme_use("default")

        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])
        col=self.get_vehicleid()
        self.combo11 = ttk.Combobox(self.a, values=col, foreground='#262626',
                                    width=28, state='readonly', font=("Helvetica", 16))
        self.combo11.place(relx=0.45, rely=0.24, relwidth=0.42, relheight=0.06)

        Label(self.a, text="Pass Id :  ", font=('Helvetica', 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.34)

        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])
        col1=self.get_passid()
        self.combo22 = ttk.Combobox(self.a, values=col1, foreground='#262626',
                                    width=28, state='readonly', font=("Helvetica", 16))
        self.combo22.place(relx=0.45, rely=0.34, relwidth=0.42, relheight=0.06)
        Label(self.a, text="Date of Issue : ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09, rely=0.44)
        self.tt1 = Entry(self.a, font=("Helvetica", 16), background='#F0F6FC', foreground='#262626')
        self.tt1.place(relx=0.45, rely=0.44, relwidth=0.42, relheight=0.06)
        self.tt1.config(insertbackground='black')

        Label(self.a, text="Date of Expiry :", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.54)
        self.tt2 = Entry(self.a, font=("Helvetica", 16), background='#F0F6FC', foreground='#262626')#,command='datetime.now()')
        self.tt2.place(relx=0.45, rely=0.54, relwidth=0.42, relheight=0.06)
        self.tt2.config(insertbackground='black')


        Label(self.a, text="Payment mode  ", font=('Helvetica', 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.64)
        # Add a style
        self.s = ttk.Style()

        # Pick a theme
        self.s.theme_use("default")

        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])
        self.combo33 = ttk.Combobox(self.a, values=('Prepaid'), foreground='#262626',
                                   width=28, state='readonly', font=("Helvetica", 16))
        self.combo33.place(relx=0.45, rely=0.64, relwidth=0.42, relheight=0.06)
        self.b1 = Button(self.a, text="ADD ", font=("Helvetica", 18, 'bold'), borderwidth=2,relief='groove', bg='#238636',
            activebackground='#238636', activeforeground='#ffffff',foreground='#ffffff',command=self.Add_issuedpass)

        self.b1.place(relx=0.7, rely=0.8, relwidth=0.17, relheight=0.085)
        self.a.transient(self.root)
        self.a.grab_set()
        exdate=date.today()+timedelta(days=30)
        print(exdate)
        self.tt1.insert(0,date.today())
        self.tt1.config(state='readonly')
        self.tt2.insert(0, exdate)
        self.tt2.config(state='readonly')

        self.a.mainloop()


        #self.root.mainloop()


#----------------------------------------
# issue_pass()



