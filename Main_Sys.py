from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import login
import ViewVehicles
import ViewEntries
import ViewTransactions
import issuemonthlypass
import changeEmpPass
import ViewPrice
import ViewPass
import TollPlaza
import ViewEmp
import Detect_Licenseno
import Login_Toll

from PIL import ImageTk,Image
import checkmain
master=Tk()

class main:
        def exit(self):
                master.destroy()
                
        def __init__(self):
                
                master.withdraw()
                master.title("Adminstrator")
                master.state('zoomed')
                master.config(bg='#262626')
                master.title("Toll Plaza Dashboard")
                master.iconbitmap('icons/tollpanel.ico')
                Label(master,text='National Highways Authority of India',foreground="white",background="#262626",
                                font=('Helvetica',42,'bold')).place(relx=0.04,rely=0.02)
                Label(master,text='Toll Information System ',foreground="#58A6FF",background="#262626",
                                font=('Helvetica',38,'bold')).place(relx=0.04,rely=0.12)

                Label(master,text="Who's using the application ?",foreground='#58A6ff',background='#262626',
                                font=('Helvetica',18,'bold','underline')).place(relx=0.40,rely=0.36)

                img=ImageTk.PhotoImage(Image.open("login.jpg"))
                self.img_button=Button(master,background='#262626',activebackground='#262626',highlightcolor='#F0F6FC',
                                        borderwidth=3,relief=GROOVE).place(relx=0.26,rely=0.45,relwidth=0.22,relheight=0.46)
                self.box1=Button(master,image=img,activebackground='#262626',background='#262626',borderwidth=0,
                                        command= login.login_main).place(relx=0.28,rely=0.48,relwidth=0.18,relheight=0.36)
              
                
                self.l1=Label(master,text="Administrator",font=("Helvetica",30,'bold'),foreground='white'
                                ,background='#262626').place(relx=0.28,rely=0.82,relwidth=0.18,relheight=0.07)
                img1=ImageTk.PhotoImage(Image.open("workers.jpg"))
                self.img1_button=Button(master,background='#262626',activebackground='#262626',highlightcolor='#F0F6FC'
                                ,borderwidth=3,relief=GROOVE).place(relx=0.56,rely=0.45,relwidth=0.22,relheight=0.46)
                self.box2=Button(master,image=img1,activebackground='#262626',background='#262626',
                                borderwidth=0,command= Login_Toll.Login_Tollmain).place(relx=0.58,rely=0.48,relwidth=0.18,relheight=0.36)
               
                
                self.l2=Label(master,text="Toll Agents",font=("Helvetica",30,'bold'),foreground='white'
                                ,background='#262626').place(relx=0.6,rely=0.82,relwidth=0.14,relheight=0.07)
                
                Button(master,text="Exit the Application",bg='#262626',borderwidth=0,activebackground='#262626', activeforeground='#238636',
                         foreground='#238636',font=('Helvetica',22,'bold'),command=master.destroy).place(relx=0.8,rely=0.94,relwidth=0.18,relheight=0.05)
                
                master.mainloop()

logged_in,user=checkmain.check_loginstatus()
print(logged_in)
def logout():
                checkmain.change_loginstatus(status=False,id=None)
                # root_win.destroy()
                master.destroy()
                # login.login_main()
                
def log_true():
                        root_win = Frame(master,background='#262626')
                        master.title("Toll Booth Panel")
                        master.state("zoomed")
                        master.minsize(1200,800)
                        bg=ImageTk.PhotoImage(Image.open("toll1.jpg"))
                        master.iconbitmap("icons/tollplaza1.ico")
                        img=ImageTk.PhotoImage(Image.open("NH.png"))
                        img_button=Button(master,image=img).place(relx=0.04,rely=0.02,relwidth=0.12,relheight=0.18) 

                        Label(root_win,image=bg,background='#262626').place(relx=0.01,rely=0.04,relheight=1.2,relwidth=0.98)
                        
                        #self.root.configure(background='#262626')
                        Label(root_win, text='National Highways Authority of India', foreground="white", background="#262626",
                        font=('Helvetica', 42, 'bold')).place(relx=0.18, rely=0.02)
                        Label(root_win, text='Toll Information System ', foreground="#58A6FF", background="#262626",
                        font=('Helvetica', 38, 'bold')).place(relx=0.18, rely=0.12)

                        dashmenu=Menu(master)
                        master.configure(menu=dashmenu,bg='#262626')
                        ent=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                        chimage=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                        regist=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                        pas=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                        fares=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                        plaza=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                        profile=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)

                        dashmenu.add_cascade(label="Entries & Transactions",menu=ent)
                        dashmenu.add_cascade(label="Licence plate detection",menu=chimage)
                        dashmenu.add_cascade(label="Registered Vehicles",menu=regist)
                        dashmenu.add_cascade(label="Issue Monthly Pass",menu=pas)
                        dashmenu.add_cascade(label="Fares",menu=fares)
                        dashmenu.add_cascade(label="Toll Plaza",menu=plaza)
                        dashmenu.add_cascade(label="Profile", menu=profile)

                        ent.add_command(label="Automobile entries record",activebackground="#262626",command=ViewEntries.Entries_main)
                        ent.add_command(label="Daily Transactions record",activebackground="#262626",command=ViewTransactions.Trans_main)

                        chimage.add_command(label="Choose Vehicle Image",activebackground="#262626",command=lambda:Detect_Licenseno.main(user))

                        regist.add_command(label="View Vehicles",activebackground="#262626",command=ViewVehicles.Vehicle_main)

                        pas.add_command(label="Registered Passes",activebackground="#262626",command=issuemonthlypass.issue_pass)

                        fares.add_command(label="Regular fares",activebackground="#262626",command=ViewPrice.View_main)
                        fares.add_command(label="Monthly pass fares",activebackground="#262626",command=ViewPass.main)

                        plaza.add_command(label="View Toll Booths",activebackground="#262626",command=TollPlaza.Toll_main)

                        profile.add_command(label="Change password",activebackground="#262626",command=changeEmpPass.changePass)
                        profile.add_command(label="Logout",activebackground="#262626",command=logout)
                        profile.add_command(label="Exit",activebackground="#262626",command=root_win.destroy)
                        root_win.place(relx=0,rely=0,relwidth=1,relheight=1)
                        root_win.mainloop()

if logged_in ==  False:
        main()
        
else:
        log_true()
        
