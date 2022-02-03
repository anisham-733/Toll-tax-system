
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import cv2
import numpy as np

import pytesseract as pyt
from connection import *
from datetime import date
from datetime import timedelta
from datetime import datetime
import Login_Toll
import http.client


class Vehicle_Plate:
    global conn,cr
    conn=connect()
    cr=conn.cursor()
    def send_sms(self):

        username='Anisha-mahajan'
        password='NFG0UTZT'
        message=f"Dear vehicle owner '{self.en1.get()}' .The Toll Fare amount of Rs.'{self.en4.get()}' has been successfully debited from your linked bank account on '{self.en2.get()}'.Thank you for visiting. "
        message=message.replace(" ","%20")

        
        contact=f"select contactno from vehicle_reg where vehicle_no='{self.en1.get()}'"
        cr.execute(contact)
        ree=cr.fetchone()
        cno=str(ree[0])
        
        
        mobile=f"{cno}"
        conn=http.client.HTTPConnection("server1.vmm.education")

        conn.request("GET","http://server1.vmm.education/VMMCloudMessaging/AWS_SMS_Sender?username="+username+"&password="
                        +password+"&message="+message+"&phone_numbers="+mobile)

        response=conn.getresponse()
        messagebox.showinfo("","Message has been sent to the registered contact number",parent=self.pay_fare)
        
        print(response.readlines())

    def get_vehicleid(self):
       
        i1 = "select id from vehicle_reg where vehicle_no='{}'".format(self.updated_no)
        cr.execute(i1)
        resi1 = cr.fetchone()
        
        for viid in resi1:
            return viid
        

    
    def get_passid(self):
        
        i2 = "select id from monthlypass where vehicle_category='{}'".format(self.vehicletype)
        cr.execute(i2)
        resi2 = cr.fetchone()
        for pid in resi2:
            return pid
    def Add_issuedpass(self):
       
        self.vid=self.entry11.get()
        self.pid=self.entry22.get()
        self.date_is=self.tt1.get()
        self.date_ex=self.tt2.get()
        self.faret=self.combo33.get()
        if self.vid=='' or self.pid=='' or self.date_is=='' or self.date_ex=='' or self.faret=='':
            messagebox.showerror("",'Please enter the data!')
        else:
            stat='select vehicleid from issuemonthlypass where vehicleid="{}"'.format(self.vid)
            cr.execute(stat)
            res=cr.fetchone()
            if res==None:
                stat1='insert into issuemonthlypass(vehicleid,passid,date_of_issue,expirydate,fare_type) values("{}","{}","{}","{}","{}")'.format(self.vid,self.pid,self.date_is,self.date_ex,self.faret)
                cr.execute(stat1)
                conn.commit()
                messagebox.showinfo("","Pass Issued successfully !!",parent=self.a)
                # self.get()
                self.a.destroy()
            else:
                messagebox.showerror("","Pass already Issued !",parent=self.a)


    def Add_win(self):
        self.a = Toplevel()
        width = 800
        height = 750
        screen_width = self.a.winfo_screenwidth()
        screen_height = self.a.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.a.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.a.resizable(0, 0)

        self.a.configure(background="#262626")
        self.a.iconbitmap("icons/add_winicon.ico")
        self.a.title("Register a monthly pass to vehicle owner")

        Label(self.a, text="Issue Monthly Pass", foreground='#F0F6FC', background='#262626',
              font=("Helvetica", 42, "bold")).place(relx=0.04, rely=0.02)

        Label(self.a, text=" Vehicle ID : ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.24)
       
        self.entry11 =  Entry(self.a, font=("Helvetica", 16), background='#F0F6FC', foreground='#262626')
        self.entry11.place(relx=0.45, rely=0.24, relwidth=0.42, relheight=0.06)

        insert_entry11=self.get_vehicleid()
        self.entry11.insert(0,insert_entry11)

        Label(self.a, text="Pass Id :  ", font=('Helvetica', 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.34)
       
        self.entry22 = Entry(self.a, font=("Helvetica", 16), background='#F0F6FC', foreground='#262626')
        self.entry22.place(relx=0.45, rely=0.34, relwidth=0.42, relheight=0.06)
        insert_entry22=self.get_passid()
        self.entry22.insert(0,insert_entry22)
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
        self.a.transient()
        self.a.grab_set()
        exdate=date.today()+timedelta(days=30)
        print(exdate)
        self.tt1.insert(0,date.today())
        self.tt1.config(state='readonly')
        self.tt2.insert(0, exdate)
        self.tt2.config(state='readonly')

        self.a.mainloop()
    def add_veh(self):
       
        self.name=self.owner.get()
        self.contact=self.cno.get()
        self.vehicletype=self.combo1.get()
        self.journey_type=self.combo2.get()
        self.taxtype=self.combo3.get()
        
        if self.combo1.get()=="" and self.combo2.get()==""  and self.updated_no == "" and  self.owner.get() == "" and  self.cno.get() == "" and self.combo3.get()=='':
            messagebox.showerror("","Kindly Enter the data in the form",parent=self.top)
        elif self.combo1.get()=="" or self.combo2.get()=="" or self.combo3.get()=='' :
            messagebox.showerror("","Kindly choose from the given values",parent=self.top)
        elif self.updated_no == "" or  self.owner.get() == "" or  self.cno.get() == "":
            messagebox.showerror('','Kindly enter the data in every field',parent=self.top)
            
        elif self.cno.get().isnumeric()==False or len(self.cno.get())>10 or len(self.cno.get())<10:
            
            messagebox.showerror("","Enter valid contact number",parent=self.top)    
        else:
            q="select * from vehicle_reg where vehicle_no='{}'".format(self.top)
            
            res=cr.fetchone()
            if res==None:
                q="insert into vehicle_reg(vehicle_no,ownername,vehicle_category,journey_type,tax_type,contactno) values('{}','{}','{}','{}','{}','{}')".format(self.updated_no,self.name,self.vehicletype,self.journey_type,self.taxtype,self.contact)
                cr.execute(q)
                conn.commit()

                messagebox.showinfo("","Vehicle registered successfully",parent=self.top)
               
                self.top.destroy()
                
                if self.journey_type=='Monthly Pass':
                    self.Add_win()
                    self.search_no
                   
                else:
                    self.search_no()
                

            else:
                messagebox.showerror("Sorry","Vehicle already registered",parent=self.top)
                self.no.delete(0,END)
                self.owner.delete(0,END)
               
                self.combo1.set('')
                self.combo2.set('') 
    
    def regid_veh(self):
        self.top=Toplevel()
        self.top.resizable(0,0)
        self.top.title('Automobile Registration Form')
        self.top.configure(background='#262626')
        width=800
        height=750
        self.top.iconbitmap("icons/add_winicon.ico")
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x=(screen_width/2)-(width/2)
        y=(screen_height/2)-(height/2)
        self.top.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        Label(self.top,text='Registration Form',foreground="#F0F6FC",
                        background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)

        Label(self.top,text="License plate no. ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.24)
        self.no=Entry(self.top,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.no.place(relx=0.42,rely=0.24,relwidth=0.50,relheight=0.06)
        self.no.insert(0,self.updated_no)
        self.no.config(insertbackground='black')

        Label(self.top,text="Automobile owner ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626").place(relx=0.09,rely=0.34)
        self.owner=Entry(self.top,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.owner.place(relx=0.42,rely=0.34,relwidth=0.50,relheight=0.06)
        self.owner.config(insertbackground='black')

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
        self.cno=Entry(self.top,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.cno.place(relx=0.42,rely=0.74,relwidth=0.50,relheight=0.06)
        self.cno.config(insertbackground='black')

        self.submit=Button(self.top,text='Submit',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.add_veh)
        self.submit.place(relx=0.7,rely=0.88,relwidth=0.2,relheight=0.1) 

        self.top.transient()
        self.top.grab_set()
        self.top.mainloop()


    def insert_cat(self):
        
        print(self.updated_no)
        
        query3=f"select vehicle_category from vehicle_reg where vehicle_no='{self.updated_no}'"
        cr.execute(query3)
        res3=cr.fetchone()
        print(res3)
        #return res3
        for vehicle_type in res3:
            print(vehicle_type)
            return vehicle_type

    def single(self):
        amt=self.insert_cat()
        print('category is ',amt)
        q1="select * from taxfare where vehicle_category='{}'".format(amt)
        cr.execute(q1)
        print(q1)
        re=cr.fetchone()
        print(re)
        #for fare in re:
        return re[2]
    def ret(self):
        amt=self.insert_cat()
        print('category is ',amt)
        q2="select * from taxfare where vehicle_category='{}'".format(amt)
        cr.execute(q2)
        print(q2)
        re1=cr.fetchone()
        print(re1)
        
        return re1[3]

    def insert_regularfare(self):
        
        
        query5=f"select journey_type from vehicle_reg where vehicle_no='{self.updated_no}' "
        cr.execute(query5)
        res5=cr.fetchone()
        for type in res5:
            print(type)
        if type=='Single':
           en4_ins=self.single()
           
           self.en4.insert(0,en4_ins)
        else:
            print('welcome')
            en4_ins=self.ret()
            
            self.en4.insert(0,en4_ins)
            
    def insert_fare(self):
        
        amt=self.insert_cat()
        query4="select monthly_pass from monthlypass where vehicle_category='{}'".format(amt)
        cr.execute(query4)
        res4=cr.fetchone()
        print(res4)
        for monthly_amt in res4:
            return monthly_amt
    def insert_all(self,res):
        
        self.txt3.delete(0,END)
        txt3_ins=self.insert_cat()
        print(txt3_ins)
        self.txt3.insert(0,txt3_ins)     
        for i in res:
            print(i)
                 
          

        query2=f"select issuemonthlypass.id,passid from monthlypass,issuemonthlypass where vehicleid='{i}' and passid=monthlypass.id"
            
        cr.execute(query2)
        res1=cr.fetchone()
       
        if res1==None:
                    messagebox.showerror("","No monthly pass issued",parent=self.pay_fare)
                    self.en4.delete(0,END)
                    self.insert_regularfare()
                   
        else:
                    messagebox.showinfo("",'Vehicle has been issued a monthly pass',parent=self.pay_fare)
                    self.en4.delete(0,END)
                    en4_ins1=self.insert_fare()
                    print(en4_ins1)
                    self.en4.insert(0,en4_ins1)

    def search_no(self):
        self.updated_no = self.en1.get()
        print(self.updated_no)
        print(self.en1.get())
        
        if self.en1.get()=='':
            messagebox.showwarning("","Enter License plate number",parent=self.pay_fare)
        else:
            query_id="select id from vehicle_reg where vehicle_no='{}'".format(self.updated_no)
            cr.execute(query_id)
            res=cr.fetchone()
            print(res)
            if res==None:
                messagebox.showerror(""," Vehicle not registered ",parent=self.pay_fare)
                self.txt3.delete(0,END)
                self.en4.delete(0,END)
                self.click=Button(self.pay_fare,text="Click here to Register the vehicle",font=('Helvetica',14,'underline','bold'),
                            background='#262626',foreground='#58A6FF',activebackground='#262626'
                            ,activeforeground='#58A6FF',borderwidth=0 ,command=self.regid_veh)   
                self.click.place(relx=0.62,rely=0.27,relwidth=0.24,relheight=0.04)           
                # self.insert_all(res,updated_no)

            else: 
                
                   
                messagebox.showinfo("","Vehicle is registered",parent=self.pay_fare)
                self.insert_all(res)
                
    
    
    def return_tollid(self):
        pass

    def transaction(self,en1):
        # en1-plate,date-en2,time-en2,txt3,fare-en4
        self.license_no=self.en1.get()
        self.date=self.en2.get()
        self.time=self.en3.get()
        self.vtype=self.txt3.get()
        self.payable_amt=self.en4.get()
       
        if self.en1.get()=='' or self.en2.get()=='' or self.en3.get()=='' or self.en4.get()=='' or self.txt3.get()=='':
            messagebox.showerror("","Kindly enter the fields")
        else:
            
            
            query5=f"select journey_type,id from vehicle_reg where vehicle_no='{self.updated_no}' "
            cr.execute(query5)
            ans=cr.fetchone()
            
            id=ans[1]
            journey_type=ans[0]
            
            if journey_type=='Single' or journey_type=='Return':
                
                trans_ins="insert into transaction(vehicle_id,date,time,vehicle_category,fare,toll_id) values('{}','{}','{}','{}','{}','{}')".format(id,self.date,self.time,self.vtype,self.payable_amt,self.tid)
                cr.execute(trans_ins)
                conn.commit()
                messagebox.showinfo("","Transaction done successfully",parent=self.pay_fare)

            if journey_type=='Monthly Pass' or journey_type=='Single' or journey_type =='Return':
                entry_ins=f"insert into entry (vehicleid,entry_date,entry_time,entry_type,toll_id) values ('{id}','{self.date}','{self.time}','{journey_type}','{self.tid}')"
                cr.execute(entry_ins)
                conn.commit()
                messagebox.showinfo("","Entry done successfully",parent=self.pay_fare)
    
    def __init__(self,r1,vehicleno,tollid):
        
        self.tid=tollid
        print(self.tid)
        
        r1.destroy()
        self.pay_fare = Toplevel()
        
        self.pay_fare.configure(background='#262626')
        self.pay_fare.resizable(0,0)
        self.pay_fare.state('zoomed')
        self.pay_fare.title("Detect License plate number and Send SMS regarding payment of fare")
        self.pay_fare.iconbitmap("icons/detect.ico")
        Label(self.pay_fare,text="License plate recognition and Toll collection",foreground="#F0F6FC"
                    ,background='#262626',font=("Helvetica",42,"bold")).place(relx=0.04,rely=0.02)

        Label(self.pay_fare,text="License plate number",font=("Helvetica",22,'bold'),
                    bg='#262626',foreground='#58A6FF').place(relx=0.09,rely=0.18)
        self.en1=Entry(self.pay_fare,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en1.place(relx=0.17,rely=0.26,relwidth=0.24,relheight=0.06)
        self.en1.config(insertbackground='black')
        self.en1.insert(0,vehicleno)
       
        
        self.search=Button(self.pay_fare,text='Search',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff', command=self.search_no)
        self.search.place(relx=0.44,rely=0.26,relwidth=0.16,relheight=0.06) 

        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.pay_fare,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.pay_fare.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.015,relheight=0.03)


        Label(self.pay_fare,text="Date",font=("Helvetica",22,'bold'),
                    bg='#262626',foreground='#58A6FF').place(relx=0.09,rely=0.38)

        self.en2=Entry(self.pay_fare,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en2.place(relx=0.17,rely=0.46,relwidth=0.24,relheight=0.06)
        self.en2.insert(0,date.today())
        self.en2.config(insertbackground='black')

        Label(self.pay_fare,text="Time",font=("Helvetica",22,'bold'),
                    bg='#262626',foreground='#58A6FF').place(relx=0.44,rely=0.38)


        self.en3=Entry(self.pay_fare,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en3.place(relx=0.50,rely=0.46,relwidth=0.24,relheight=0.06)
        time=datetime.now().strftime(" %I:%M:%S")
        # print(time)
        self.en3.insert(0,time)
        self.en3.config(insertbackground='black')

        Label(self.pay_fare,text="Vehicle category",font=("Helvetica",22,'bold'),
                    bg='#262626',foreground='#58A6FF').place(relx=0.09,rely=0.58)

        self.txt3=Entry(self.pay_fare,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.txt3.config(insertbackground='black')
        # self.txt3.insert(0,self.search_no(self.en1))  
               
        self.txt3.place(relx=0.17,rely=0.66,relwidth=0.24,relheight=0.06)

        Label(self.pay_fare,text="Fare amount",font=("Helvetica",22,'bold'),
                    bg='#262626',foreground='#58A6FF').place(relx=0.44,rely=0.58)
        self.en4=Entry(self.pay_fare,font=("Helvetica",18),foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.en4.place(relx=0.50,rely=0.66,relwidth=0.24,relheight=0.06)
        self.en4.config(insertbackground='black')

        self.pay=Button(self.pay_fare,text='Pay Credit amount',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=lambda: self.transaction(self.en1))
        self.pay.place(relx=0.77,rely=0.78,relwidth=0.2,relheight=0.08) 

        self.send_otp=Button(self.pay_fare,text='Send SMS',font=("Helvetica",18,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.send_sms)
        self.send_otp.place(relx=0.77,rely=0.90,relwidth=0.20,relheight=0.08)

        self.pay_fare.grab_set()
        self.pay_fare.transient()
        self.pay_fare.mainloop()

#Vehicle_Plate()