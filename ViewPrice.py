from tkinter import *
from connection import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

class View_main():
    def get(self):
        conn=connect()
        cur=conn.cursor()
        stat="select * from taxfare"
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
            self.t1.insert('', index=count, values=i)
            
            count+=1
    def update_tax(self):
        self.id=self.e1.get()
        self.v_cat=self.combo1.get()
        self.single_tax=self.e2.get()
        self.return_tax=self.e3.get()
        conn=connect()
        cur=conn.cursor()
        stat='update taxfare set vehicle_category="{}", Single="{}",Return_tax="{}" where id="{}"'.format(self.v_cat, self.single_tax, self.return_tax,self.id)
        cur.execute(stat)
        # res=cur.fetchone()
        # for i in res:
        #     print(i)
        conn.commit()
        self.get()
        
        messagebox.showinfo("","Updation done succesfully",parent=self.update)
        self.update.destroy()
    def delete_tax(self):
        self.id = self.e1.get()
        conn = connect()
        cr = conn.cursor()
        q = 'delete from taxfare where id="{}"'.format(self.id)
        cr.execute(q)
        conn.commit()
        self.get()
        messagebox.showinfo("","Deleted successfully",parent=self.update)
        self.update.destroy()
        
    def onDoubleClick(self,event):
        #whenever we use binding we need to pas an event
       
        #item func of Treeview takes focus func as first arg,values(which will return all the values in the selected item)
        
        self.items=self.t1.item(self.t1.focus())['values'] #focus func returns selected row in Treeview
        # Self.items will fetch id,vehicle_cat,single and return tax
        print(self.items) # is a list
        print(self.items[1]) #value of 2nd elt at list
        conn=connect()
        cur=conn.cursor()
       
        
    
    # Update window
    
        self.update=Toplevel()
        self.update.configure(background='#262626')
        
        width=800
        height=700
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.update.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        
        self.update.title("Updation of Tollway fares")
       
        self.update.iconbitmap('icons/toll_price.ico')
        
        Label(self.update,text="Modify Toll fares",foreground="#F0F6FC",
                        background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
        
        Label(self.update,text="Id  ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.24)
        
        self.e1=Entry(self.update,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e1.place(relx=0.46,rely=0.24,relwidth=0.46,relheight=0.06)
        self.e1.config(insertbackground='black')
        

        Label(self.update,text="Vehicle Category  ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.34)

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
        self.combo1.place(relx=0.46,rely=0.34,relwidth=0.46,relheight=0.06)

        Label(self.update,text="Single Journey Tax  ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.44)
        
        self.e2=Entry(self.update,font=("Helvetica",18),background='#F0F6FC',foreground='#3D1F1D',cursor="xterm #0000FF")
        self.e2.place(relx=0.46,rely=0.44,relwidth=0.46,relheight=0.06)
        self.e2.config(insertbackground='black')

        Label(self.update,text="Return journey tax ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                    background="#262626").place(relx=0.09,rely=0.54)
        
        self.e3=Entry(self.update,font=("Helvetica",18),background='#F0F6FC',foreground='#3D1F1D',cursor="xterm #0000FF")
        self.e3.place(relx=0.46,rely=0.54,relwidth=0.46,relheight=0.06)
        self.e3.config(insertbackground='black')


        self.b1=Button(self.update,text="Update",font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.update_tax)
        self.b1.place(relx=0.4,rely=0.76,relwidth=0.2,relheight=0.1) 


        self.b2 = Button(self.update, text="Delete", font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.delete_tax)
        self.b2.place(relx=0.7,rely=0.76,relwidth=0.2,relheight=0.1) 


        # print(self.items)
        current=col.index(self.items[1]) #index func returns index

        print(current)
        self.combo1.current(current) #default value in combobox ,current func takes index a number as argument
        print(self.items[0])
        self.e1.insert(0,self.items[0])
        self.e1.config(state='readonly')
        self.e2.insert(0,self.items[2])
        self.e3.insert(0,self.items[3])

        self.update.iconbitmap('icons/toll_price.ico')
        self.update.transient(self.root)
        self.update.grab_set()
        self.update.mainloop()
    def add_price(self):
        conn=connect()
        cur=conn.cursor()

        self.vehicle_cat=self.combo1.get()
        self.single=self.txt2.get()
        self.return_tax=self.txt3.get()
        if self.vehicle_cat=='' or self.single=='' or self.return_tax=='':
            messagebox.showerror("","Please add the fields",parent=self.a)
        else:
                

            stat='select * from taxfare where vehicle_category="{}"'.format(self.vehicle_cat)
            cur.execute(stat)
            res=cur.fetchone()
            if res==None:
                insert_stat='insert into  taxfare(vehicle_category,Single,Return_tax) values("{}","{}","{}")'.format(self.vehicle_cat,self.single,self.return_tax)
                cur.execute(insert_stat)
                conn.commit()
                # ViewPricePass.get()
                messagebox.showinfo("","Tollfare registered successfully",parent=self.a)
                self.get()
                self.a.destroy()
            else:
                messagebox.showerror("","Tollway tax already added",parent=self.a)
                        
    def Add(self):
        self.a=Toplevel()
        width=800
        height=500
        screen_width=self.a.winfo_screenwidth()
        screen_height=self.a.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.a.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.a.resizable(0,0)


       
        self.a.configure(background="#262626")
        self.a.iconbitmap("icons/toll_price.ico")
        self.a.title("Add Daily Toll fare")
        Label(self.a,text="Add Tollway Prices",foreground='#F0F6FC',background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)

        Label(self.a, text="Select Vehicle category ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.28)
        
        columns=('Car/Jeep/Van','Light Commercial vehicles','Bus/Truck','3-axle vehicles',
                    '4 to 6 axle vehicles','Heavy vehicles','7 or more axle vehicles')
        # Add a style
        self.s=ttk.Style()

         #Pick a theme
        self.s.theme_use("default")

        
        self.s.map('TCombobox', selectbackground=[('readonly', '#F0F6FC')])
        self.s.map('TCombobox', fieldbackground=[('readonly','#F0F6FC')])
        self.s.map('TCombobox', selectforeground=[('readonly', '#262626')])

       
        
        self.combo1=ttk.Combobox(self.a,values=columns,foreground='#262626',
                            width=28,state='readonly',font=("Helvetica",16))
        self.combo1.place(relx=0.52,rely=0.28,relwidth=0.42,relheight=0.06)
       
        
        Label(self.a,text="Single journey tax  ",font=('Helvetica',20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.42)
        
        self.txt2=Entry(self.a,font=("Helvetica",16),background='#F0F6FC',foreground='#262626')
        self.txt2.place(relx=0.52,rely=0.42,relwidth=0.42,relheight=0.06)
        self.txt2.config(insertbackground='black')

        Label(self.a, text="Return journey tax ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09, rely=0.56)
        self.txt3 = Entry(self.a,background='#F0F6FC',foreground='#262626',font=("Helvetica",16))
        self.txt3.place(relx=0.52, rely=0.56,relwidth=0.42,relheight=0.06)
        self.txt3.config(insertbackground='black')
       

         
           
        self.b1=Button(self.a, text="Add Price",font=("Helvetica",16,'bold'), borderwidth=2,
                        relief='groove',bg='#238636',activebackground='#238636',activeforeground='#ffffff'
                        ,foreground='#ffffff',command=self.add_price)
        self.a.iconbitmap('icons/toll_price.ico')
        self.b1.place(relx=0.7,rely=0.74,relwidth=0.2,relheight=0.1)
        self.a.transient(self.root)
        self.a.grab_set()
        self.a.mainloop()
    
                
        
    def __init__(self):
        self.root=Toplevel()
        width=1300
        height=600
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        
        
        self.root.iconbitmap('icons/toll_price.ico')
        self.root.title('Regular Toll Fares')
        self.root.configure(background='#262626')
        Label(self.root,text='Tollway Prices',foreground="#F0F6FC",background='#262626',
                    font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)
        
        col=('Id','Vehicle Category','Single Journey','Return Journey')
        self.t1=ttk.Treeview(self.root,columns=col)
        self.t1.column('Id',width=80)
        self.t1.column('Vehicle Category',width=220)
        self.t1.column('Single Journey',width=150)
        self.t1.column('Return Journey',width=150)
        #binding things ,event when we double click on the mouse,2nd arg func is passed
        self.t1.bind('<Double-1>',self.onDoubleClick)

        for i in col:
            print(i)
            # self.t1.heading(width)
            self.t1.heading(i,text=i)

        self.t1['show']="headings"
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

        
        self.t1.place(relx=0.1,rely=0.22,relwidth=0.8,relheight=0.6)
        self.get()

        #Create a menu bar
        self.menu=Menu(self.root)
        self.root.config(menu=self.menu)
        #submenu
        self.modify=Menu(self.menu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
        self.menu.add_cascade(label="Modify",font=('Helvetica',12),menu=self.modify)

        self.modify.add_command(label='Add Vehicle price',command= self.Add)
        self.update_del=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Double-click the record for updation/deletion",font=('Helvetica',12,'bold'),state=DISABLED,menu=self.update_del)
        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.root,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.root.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.015,relheight=0.05)
        
        self.root.grab_set()
        self.root.transient()
        self.root.mainloop()

# View_main()