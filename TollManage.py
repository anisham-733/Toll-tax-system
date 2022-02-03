from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from connection import *
import random
import smtplib
import string
class Manage:
    def email_transmit(self):
          
          con=smtplib.SMTP("smtp.gmail.com",587)
          #connect to server
          con.starttls()
          self.em = self.e6.get()
          self.pasw = self.e2.get()
          #start a secure connection
          id=[self.em]
          con.login("ad.toll456@gmail.com","tollpass123") # Admin sender mail
          
          if  self.em == '':
            messagebox.showerror('', 'Please Enter the email',parent=self.toll)
          else:
                conn=connect()
                cr=conn.cursor()
                q='select tollid from tollplaza where email="{}"'.format(self.em)
                cr.execute(q)
                self.res=cr.fetchone()
            
                if self.res==None:
                  messagebox.showerror('', 'Invalid email or\nplease first register toll on entered email',parent=self.toll)
                else:   
                   
                  message="Dear employee,\n The Login details for Employee Dashboard are \n Tollid : {} \n Password : {} \n".format(self.res[0],self.pasw)
                   
                #send mail
                  con.sendmail("ad.toll456@gmail.com",id,message)
                  con.quit()
                  messagebox.showinfo("Send mail","The Toll Plaza  has been successfully send the credentials",parent=self.toll)
                  self.e1.delete(0, END)
                  self.e2.delete(0, END)
                  self.e3.delete(0, END)
                  self.e4.delete(0, END)
                  self.e5.delete(0, END)
                  self.e6.delete(0, END)
    def ranpass(self):
          self.pas = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+
                             string.digits, k = 8))
          #print(self.pas)                   
          return self.pas
    def register_tollinfo(self):
        self.id=self.e5.get()
        self.name = self.e1.get()
        self.password = self.e2.get()
        self.city = self.e3.get()
        self.state = self.e4.get()
        
        self.email = self.e6.get()

        conn = connect()
        cr = conn.cursor()
        
        if self.name == '' or  self.city == '' or self.state == '' or self.id == '' or self.email == '':
            messagebox.showerror('', 'Please Enter the data',parent=self.toll)
        
        else:
            q = 'select * from tollplaza where tollid="{}"'.format(self.id)
            cr.execute(q)
            result = cr.fetchone()
            if result == None:
                q = 'insert into tollplaza values("{}","{}","{}","{}","{}","{}")'.format(self.id,self.name, self.password, self.city, self.state, self.email)
                cr.execute(q)
                conn.commit()
                if self.e2.get()!=None:
                  messagebox.showinfo("","Password successfully allotted to the toll.",parent=self.toll)
        
                messagebox.showinfo('', 'Toll added successfully',parent=self.toll)
                
            else:
                messagebox.showerror('', 'Toll Already Registered',parent=self.toll)
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e3.delete(0, END)
                self.e4.delete(0, END)
                self.e5.delete(0, END)
                self.e6.delete(0, END)
    def __init__(self):
        self.toll = Toplevel()
        self.toll.resizable(0, 0)
        self.toll.title('Registration of Toll booth')
        self.toll.configure(background='#262626')
        width = 800
        height = 750
        screen_width = self.toll.winfo_screenwidth()
        screen_height = self.toll.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.toll.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.toll.iconbitmap('icons/tollplaza1.ico')

        Label(self.toll, text='Add Toll booth', foreground="#F0F6FC",
              background='#262626', font=("Helvetica", 42, "bold")).place(relx=0.04, rely=0.02)

        Label(self.toll, text="Toll Name ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.34)
        self.e1 = Entry(self.toll, font=("Helvetica", 18), foreground='#262626',
                         background='#F0F6FC', cursor="xterm #0000FF")
        self.e1.place(relx=0.42, rely=0.34, relwidth=0.50, relheight=0.06)
     
        self.e1.config(insertbackground='black')
        Label(self.toll, text="Password ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.44)
        self.e2 = Entry(self.toll, font=("Helvetica", 18), foreground='#262626',
                         background='#F0F6FC', cursor="xterm #0000FF")
        self.e2.place(relx=0.42, rely=0.44, relwidth=0.50, relheight=0.06)
        self.e2.config(insertbackground='black')
        self.pw=self.ranpass()
        self.e2.insert(0,self.pw)
       
        Label(self.toll, text="City ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.54)

        self.e3 = Entry(self.toll, font=("Helvetica", 18), foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")

        self.e3.place(relx=0.42, rely=0.54, relwidth=0.50, relheight=0.06)
        self.e3.config(insertbackground='black')

        Label(self.toll, text="State ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.64)

        self.e4 = Entry(self.toll, font=("Helvetica", 18), foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e4.place(relx=0.42, rely=0.64, relwidth=0.50, relheight=0.06)
        self.e4.config(insertbackground='black')

        Label(self.toll, text="Toll id", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.24)
        self.e5 = Entry(self.toll, font=("Helvetica", 18), foreground='#262626',
                         background='#F0F6FC', cursor="xterm #0000FF")
        self.e5.place(relx=0.42, rely=0.24, relwidth=0.50, relheight=0.06)
        self.e5.config(insertbackground='black')
        Label(self.toll, text="Email ", font=("Helvetica", 20, 'bold'), foreground='#58A6FF',
              background="#262626").place(relx=0.09, rely=0.74)
        self.e6 = Entry(self.toll, font=("Helvetica", 18), foreground='#262626',
                        background='#F0F6FC', cursor="xterm #0000FF")
        self.e6.place(relx=0.42, rely=0.74, relwidth=0.50, relheight=0.06)
        self.e6.config(insertbackground='black')

        self.submit = Button(self.toll, text='Submit', font=("Helvetica", 18, 'bold'), bg='#238636',
                             activebackground='#238636', activeforeground='#ffffff', foreground='#ffffff',
                             command=self.register_tollinfo)
        self.submit.place(relx=0.7, rely=0.88, relwidth=0.2, relheight=0.1)

        self.semail = Button(self.toll, text='Send Credentials', font=("Helvetica", 18, 'bold'), bg='#238636',
                             activebackground='#238636', activeforeground='#ffffff', foreground='#ffffff',command=self.email_transmit)
        self.semail.place(relx=0.2, rely=0.88, relwidth=0.35, relheight=0.1)

        
        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.toll,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.toll.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.025,relheight=0.03)
 
        
        self.toll.transient()
        self.toll.grab_set()
        self.toll.mainloop()

# Manage()       