from tkinter import *
from tkinter import ttk
import csv
import tkinter.ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from connection import *


class Vehicle_main:
    global conn,cr
    conn = connect()
    cr = conn.cursor()
    def get(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select * from vehicle_reg'
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
            self.t1.insert('', index=count, values=i,tags=('color',))
            self.t1.tag_configure('color', background='#21262D',foreground="#F0F6FC")
            
            count += 1

    def add_veh(self):
        self.vno=self.en1.get()
        self.name=self.en2.get()
        self.cno=self.en3.get()
        self.vehicletype=self.combo1.get()
        self.journey_type=self.combo2.get()
        self.taxtype=self.combo3.get()
       

        
        if self.combo1.get()=="" and self.combo2.get()==""  and self.en1.get() == "" and  self.en2.get() == "" and  self.en3.get() == "" and self.combo3.get()=='':
            messagebox.showerror("","Kindly Enter the data in the form",parent=self.top)
        elif self.combo1.get()=="" or self.combo2.get()=="" or self.combo3.get()=='' :
            messagebox.showerror("","Kindly choose from the given values",parent=self.top)
        elif self.en1.get() == "" or  self.en2.get() == "" or  self.en3.get() == "":
            messagebox.showerror('','Kindly enter the data in every field',parent = self.top)
            
        elif self.en3.get().isnumeric()==False or len(self.en3.get())>10 or len(self.en3.get())<10:
            
            messagebox.showerror("","Enter valid contact number",parent=self.top)    
        else:
            q="select * from vehicle_reg where vehicle_no='{}'".format(self.vno)
            cr.execute(q)
            res=cr.fetchone()
            if res==None:
                q="insert into vehicle_reg(vehicle_no,ownername,vehicle_category,journey_type,tax_type,contactno) values('{}','{}','{}','{}','{}','{}')".format(self.vno,self.name,self.vehicletype,self.journey_type,self.taxtype,self.cno)
                cr.execute(q)
                conn.commit()
                self.get()

                messagebox.showinfo("","Vehicle registered successfully",parent=self.top)
                self.top.destroy()

        

            else:
                messagebox.showerror("Sorry","Vehicle already registered",parent=self.top)
                self.en1.delete(0,END)
                self.en2.delete(0,END)
                self.en3.delete(0,END) 
                self.combo1.set('')
                self.combo2.set('') 
                     
    def add_main(self):
        self.top=Toplevel()
        self.top.resizable(0,0)
        self.top.title('Automobile Registration Form')
        self.top.configure(background='#262626')
        self.top.iconbitmap("icons/add_winicon.ico")
        width=800
        height=750
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.top.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        Label(self.top,text='Registration Form',foreground="#F0F6FC",
                        background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)

        Label(self.top,text="License plate no. ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.24)
        self.en1=Entry(self.top,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en1.place(relx=0.42,rely=0.24,relwidth=0.50,relheight=0.06)
        self.en1.config(insertbackground='black')

        Label(self.top,text="Automobile owner ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.34)
        self.en2=Entry(self.top,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en2.place(relx=0.42,rely=0.34,relwidth=0.50,relheight=0.06)
        self.en2.config(insertbackground='black')

        Label(self.top,text="Vehicle category ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.44)
        #Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly','#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])

        columns1=('Car/Jeep/Van','Light Commercial vehicles','Bus/Truck','3-axle vehicles',
                    '4 to 6 axle vehicles','Heavy vehicles','7 or more axle vehicles')
        
        self.combo1=ttk.Combobox(self.top,values=columns1,foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.combo1.place(relx=0.42,rely=0.44,relwidth=0.50,relheight=0.06)

        Label(self.top,text="Journey type ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.54)
        columns2=('Single','Return','Monthly Pass')
        
        self.combo2=ttk.Combobox(self.top,values=columns2,background='#F0F6FC',foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.combo2.place(relx=0.42,rely=0.54,relwidth=0.50,relheight=0.06)

        Label(self.top,text="Account type ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.64)
        columns3=('Prepaid','Postpaid')
        
        self.combo3=ttk.Combobox(self.top,values=columns3,background='#F0F6FC',foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.combo3.place(relx=0.42,rely=0.64,relwidth=0.50,relheight=0.06)

        Label(self.top,text="Contact Number",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.74)
        self.en3=Entry(self.top,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en3.place(relx=0.42,rely=0.74,relwidth=0.50,relheight=0.06)
        self.en3.config(insertbackground='black')

        self.submit=Button(self.top,text='Submit',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.add_veh)
        self.submit.place(relx=0.7,rely=0.88,relwidth=0.2,relheight=0.1) 

        self.top.transient()
        self.top.grab_set()
        self.top.mainloop()

    def search(self):
        self.t1.delete(*self.t1.get_children())
        conn=connect()
        cur=conn.cursor()
        q='select * from vehicle_reg'
        cur.execute(q)
        res=cur.fetchall()
        print(res)
        x=[]
        i=0
        flag=0
        for row in res:
            if self.cb.get() == "Vehicle category":
                if self.e1.get().capitalize() in row[3]:
                    l=list(row)
                    x.append(l)
                    flag=1

            elif self.cb.get() == "Journey type":
                if self.e1.get().capitalize() in row[4]:
                    l=list(row)
                    x.append(l)
                    flag=1


            elif self.cb.get()=="License Plate Number":
                if self.e1.get().upper() in str(row[1]):
                    print(row[1])
                    l=list(row)
                    x.append(l)
                    flag=1
            elif self.cb.get()=='Automobile owner':
                if self.e1.get().capitalize() in row[2]:
                    l=list(row)
                    x.append(l)
                    flag=1
            elif self.cb.get()=='Account type for payment of tariff':
                if self.e1.get().capitalize() in row[5]:
                    l=list(row)
                    x.append(l)
                    flag=1
            elif self.cb.get()=='Contact Number':
                if self.e1.get() in str(row[6]):
                    l=list(row)
                    x.append(l)
                    flag=1
                


            else:
                messagebox.showerror("","No Option Selected",self.regis)


        for r in x:
            
            self.t1.insert("",index=i,values=r)
            i=i+1
        if flag == 1:
            messagebox.showinfo("","Data Found",parent=self.regis)
            
        else:
            messagebox.showerror("", "No data found",parent=self.regis)

    def refresh(self):
        self.get()
    def export_csv(self):


        with open ("Vehicles_Registered.csv","w",newline='') as myfile:
             if self.t1.get_children()==():
                    messagebox.showerror("Error"," No vehicles registered",parent=self.regis)      
             else:
                w=csv.writer(myfile,delimiter=',')
                heading=['Id','License plate number','Automobile owner','Vehicle category''Journey type','Account type','Contact no.']
                w.writerow(heading)
                for child in self.t1.get_children():
                    w.writerow(self.t1.item(child)["values"])
                messagebox.showinfo("Export records to CSV file","Records written and successfully saved to 'Vehicles_Registered.csv' file",parent=self.regis)  
            
    def __init__(self):
        # self.root=root
        self.regis=Toplevel()
       
        self.regis.state('zoomed')
        
        self.regis.resizable(0,0)
        
        self.regis.configure(background='#262626')
        self.regis.iconbitmap('icons/tollpanel.ico')
       
        self.regis.title("Registered vehicles on FASTag Toll PLaza")

        Label(self.regis,text='Registered vehicles',foreground="#F0F6FC",
                        background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
                        
        Label(self.regis,text='Choose field to search',foreground="#58A6FF",
                        background='#262626',font=("Helvetica",20,"bold")).place(relx=0.04,rely=0.23)
        
        self.cb=ttk.Combobox(self.regis,values=('License Plate Number','Automobile owner','Vehicle category','Journey type','Account type for payment of tariff',
                                'Contact Number'),state='readonly',font=('Helvetica',18))
        self.cb.place(relx=0.3,rely=0.23,relwidth=0.3,relheight=0.06)

        #Add a style
        self.s=ttk.Style()

        #Pick a theme
        self.s.theme_use("default")

            
        self.s.map('TCombobox', selectbackground=[('readonly', '#21262D')]) #161b22
        self.s.map('TCombobox', fieldbackground=[('readonly','#21262D')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#C9D1D9')])

        self.e1=Entry(self.regis,font=('Helvetica',18),foreground='#262626',background='#F0F6FC', cursor="xterm #0000FF")
        self.e1.place(relx=0.62,rely=0.23,relwidth=0.3,relheight=0.06)

        self.e1.insert(0,'Search')

        def entry_clear(e):
            if self.e1.get()=='Search':
                self.e1.delete(0,END)
        #Bind the entry boxes
        self.e1.bind("<Button-1>",entry_clear)
        self.e1.config(insertbackground='black')

        img=ImageTk.PhotoImage(Image.open("search1.png"))
        self.img_button=Button(self.regis,image=img,background='#171515',activebackground='#171515',command=self.search)
        self.img_button.place(relx=0.88,rely=0.23,relheight=0.06,relwidth=0.04)

        refresh_img=ImageTk.PhotoImage(Image.open("refresh1.png"))
        self.img1_button=Button(self.regis,image=refresh_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.refresh)
        self.img1_button.place(relx=0.93,rely=0.23,relheight=0.06,relwidth=0.04)

        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.regis,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.regis.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.015,relheight=0.03)

        
        
        #Add a style
        self.s=ttk.Style()

       
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
        

        col = ('Id','License plate number','Automobile owner','Vehicle category','Journey type','Account type','Contact no.')
        self.frame=Frame(self.regis)
        
        self.t1=ttk.Treeview(self.frame,columns=col)
        
        self.t1.column('Id',width=150)
        self.t1.column('License plate number',width=280)

        self.t1.column('Vehicle category',width=300)
        self.t1.column('Automobile owner',width=290)
        self.t1.column('Journey type',width=220)
        self.t1.column('Account type',width=190)
        self.t1.column('Contact no.',width=200)

        for i in col:
            print(i)
            self.t1.heading(i,text=i)

        self.t1['show']="headings"
        scrollbar_horizontal = ttk.Scrollbar(self.frame, orient='horizontal', command = self.t1.xview)    
        scrollbar_vertical = ttk.Scrollbar(self.frame, orient='vertical', command = self.t1.yview)   
        scrollbar_horizontal.pack(side='bottom', fill=X)    
        scrollbar_vertical.pack(side='right', fill=Y)

        self.t1.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)

        self.frame.place(relx=0.1,rely=0.36,relwidth=0.82,relheight=0.5)
        self.t1.place(relx=0,rely=0,relwidth=1,relheight=1)

        
        self.get()
        self.t1.bind('<Double-1>',self.onDoubleClick)

        self.export=Button(self.regis,text='Export to CSV',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.export_csv)
        self.export.place(relx=0.78,rely=0.89,relwidth=0.15,relheight=0.1)                
        
        #Create a menu bar
        self.menu=Menu(self.regis)
        self.regis.config(menu=self.menu)
        #submenu
        self.modify=Menu(self.menu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
        self.menu.add_cascade(label="Modify",font=('Helvetica',12),menu=self.modify)

        self.modify.add_command(label='Register a vehicle',command= self.add_main)
        self.update_del=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Double-click the record for updation/deletion",font=('Helvetica',12,'bold'),state=DISABLED,menu=self.update_del)


        self.regis.grab_set()
        self.regis.transient()
        self.regis.mainloop()
    def update_db(self):
        self.id = self.e1.get()
        self.vehicle_no = self.e2.get()
        self.vehicle_owner = self.e3.get()
        self.vehicle_cat=self.c1.get()
        self.acc_type=self.c2.get()
        self.contact_no=self.e4.get()
        conn = connect()
        cr = conn.cursor()
        q = 'update vehicle_reg set ownername="{}",vehicle_category="{}",tax_type="{}",contactno="{}" where vehicle_no="{}" and id="{}"'.format(self.vehicle_owner, self.vehicle_cat,self.acc_type,self.contact_no,self.vehicle_no,self.id)

        cr.execute(q)
        conn.commit()
        self.get()
        
        messagebox.showinfo("","Updation done succesfully",parent=self.update)
        self.update.destroy()
    def delete_db(self):
        self.vehicle_no= self.e2.get()
        conn = connect()
        cr = conn.cursor()
        q = 'delete from vehicle_reg where vehicle_no="{}"'.format(self.vehicle_no)
        cr.execute(q)
        conn.commit()
        self.get()
        messagebox.showinfo("","Deleted successfully",parent=self.update)
        self.update.destroy()
        
    def onDoubleClick(self, event):
        self.items = self.t1.item(self.t1.focus())['values']
        print(self.items)
        conn = connect()
        cr = conn.cursor()
        q = 'select * from vehicle_reg where vehicle_no="{}"'.format(self.items[1])
        cr.execute(q)
        result = cr.fetchone()

        #Update window
        self.update = Toplevel()
        self.update.configure(background='#262626')
        width=850
        height=810
        screen_width=self.update.winfo_screenwidth()
        screen_height=self.update.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.update.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.update.iconbitmap("icons/update_win.ico")
        self.update.title('Updation of Automobile features')
        self.update.resizable(0,0)

        Label(self.update,text="Update Automobile details",foreground="#F0F6FC",
                        background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
        
        Label(self.update,text=" Registration Id",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.2)
        self.ee1=Entry(self.update,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.ee1.place(relx=0.42,rely=0.2,relwidth=0.50,relheight=0.06)
        self.ee1.config(insertbackground='black')
        
        
        
        Label(self.update,text="License plate no. ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.3)
        self.e2=Entry(self.update,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e2.place(relx=0.42,rely=0.3,relwidth=0.50,relheight=0.06)
        self.e2.config(insertbackground='black')

        Label(self.update,text="Automobile owner ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.4)
        self.e3=Entry(self.update,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e3.place(relx=0.42,rely=0.4,relwidth=0.50,relheight=0.06)
        self.e3.config(insertbackground='black')

        Label(self.update,text="Vehicle category ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.5)
         #Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly','#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])

        columns1=('Car/Jeep/Van','Light Commercial vehicles','Bus/Truck','3-axle vehicles',
                    '4 to 6 axle vehicles','Heavy vehicles','7 or more axle vehicles')
        
        self.c1=ttk.Combobox(self.update,values=columns1,background='#F0F6FC',foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.c1.place(relx=0.42,rely=0.5,relwidth=0.50,relheight=0.06)

        Label(self.update,text="Account type ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.6)
        columns2=('Prepaid','Postpaid')
        
        self.c2=ttk.Combobox(self.update,values=columns2,background='#F0F6FC',foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.c2.place(relx=0.42,rely=0.6,relwidth=0.50,relheight=0.06)

        Label(self.update,text="Journey type ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.7)
        columns3=('Single','Return','Monthly Pass')
        
        self.c3=ttk.Combobox(self.update,values=columns3,background='#F0F6FC',foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.c3.place(relx=0.42,rely=0.7,relwidth=0.50,relheight=0.06)

        Label(self.update,text="Contact Number",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.8)
        self.e4=Entry(self.update,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e4.place(relx=0.42,rely=0.8,relwidth=0.50,relheight=0.06)
        self.e4.config(insertbackground='black')

        

        self.ee1.insert(0,self.items[0])
        self.ee1.config(state='readonly')
        self.e2.insert(0,self.items[1])
        self.e2.config(state='readonly')
        self.e3.insert(0,self.items[2])

        current1=columns1.index(self.items[3])
        self.c1.current(current1)

        current2=columns2.index(self.items[5])
        self.c2.current(current2)

        current3=columns3.index(self.items[4])
        self.c3.current(current3)

        self.e4.insert(0,self.items[6])

        self.u1=Button(self.update,text='Update',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.update_db)
        self.u1.place(relx=0.25,rely=0.91,relwidth=0.2,relheight=0.08)   
       
        self.u1=Button(self.update,text='Delete',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.delete_db)
        self.u1.place(relx=0.55,rely=0.91,relwidth=0.2,relheight=0.08)   

        

        self.update.transient()
        self.update.grab_set()
        self.update.mainloop()
# Vehicle_main()