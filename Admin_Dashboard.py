from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import ViewVehicles
import ViewEntries
import ViewTransactions
import changeAdminPass
import ViewPrice
import ViewPass
import TollPlaza
import TollManage
import login
import checkmain
from PIL import ImageTk,Image
import json 

class Dashboard:
        def logout(self):
               self.root.destroy()
        def __init__(self):
                self.root=Toplevel()
                        
                self.root.title("Adminstrator Toll Information Panel")
                self.root.state("zoomed")
                self.root.configure(background='#262626')
                bg=ImageTk.PhotoImage(Image.open("Admin_bg2.jpg"))

                Label(self.root,image=bg,background='#262626').place(relx=0.01,rely=0.03,relheight=1.2,relwidth=0.98)
                self.root.iconbitmap('icons/Admin_panel2.ico')
                Label(self.root,text='National Highways Authority of India',foreground="white",background="#262626",
                                        font=('Helvetica',42,'bold')).place(relx=0.04,rely=0.02)
                Label(self.root,text='Toll Information System ',foreground="#58A6FF",background="#262626",
                                        font=('Helvetica',38,'bold')).place(relx=0.04,rely=0.12)
                dashmenu=Menu(self.root)
                self.root.config(menu=dashmenu)
                register=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                fares=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                ent=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                employee=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                tollplaza=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                profile=Menu(dashmenu,foreground='#ffffff',background='#0D1117',activebackground='#0D1117',borderwidth=0,tearoff=0)
                dashmenu.add_cascade(label="Entries & Transactions",menu=ent)
                        
                dashmenu.add_cascade(label="Registered vehicles",menu=register)
                dashmenu.add_cascade(label="Fares",menu=fares)
                dashmenu.add_cascade(label="Registered Toll plazas",menu=tollplaza)
                dashmenu.add_cascade(label="Toll Plaza Administration",menu=employee)
                dashmenu.add_cascade(label="Profile",menu=profile)
                ent.add_command(label="Automobile entries record",activebackground="#262626",command=ViewEntries.Entries_main)
                ent.add_command(label="Daily Transactions record",activebackground="#262626",command=ViewTransactions.Trans_main)
                register.add_command(label="View vehicles",activebackground="#262626",command=ViewVehicles.Vehicle_main)
                fares.add_command(label="Regular fares",activebackground="#262626",command=ViewPrice.View_main)
                fares.add_command(label="Monthly pass fares",activebackground="#262626",command=ViewPass.main)
                tollplaza.add_command(label="View Toll Booths",activebackground="#262626",command=TollPlaza.Toll_main)
                
                employee.add_command(label="Add a Toll booth",activebackground="#262626",command=TollManage.Manage)
                profile.add_command(label="Change Administrator password",activebackground="#262626",command=changeAdminPass.changePass)
                profile.add_command(label="Exit the application",activebackground="#262626",command=self.logout)
                        
                        
                self.root.grab_set()
                self.root.transient()
                
                self.root.mainloop()


# Dashboard()        