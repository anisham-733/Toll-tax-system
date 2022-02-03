from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import ViewVehicles
import ViewEntries
import ViewTransactions
import issuemonthlypass
import changeEmpPass
import ViewPrice
import ViewPass
import TollPlaza
import ViewEmp
import Login_Toll

import checkmain
from PIL import ImageTk,Image
import Detect_Licenseno
class emp_Dashboard:

    def logout(self):
      checkmain.change_loginstatus(status=False,id=None)
      self.root.destroy()
    def __init__(self,tollid):
      print(tollid)
      self.root = Toplevel()
      self.root.title("Toll Booth Panel")
      self.root.state("zoomed")
      self.root.minsize(1200, 800)
      self.root.iconbitmap("icons/tollplaza1.ico")
         #self.root.configure(background='#262626')
      self.root.configure(background='#262626')
      bg=ImageTk.PhotoImage(Image.open("toll1.jpg"))
      Label(self.root,image=bg,background='#262626').place(relx=0.01,rely=0.04,relheight=1.2,relwidth=0.98)
      
      img=ImageTk.PhotoImage(Image.open("NH.png"))
      self.img_button=Button(self.root,image=img).place(relx=0.04,rely=0.02,relwidth=0.1,relheight=0.18)         
      Label(self.root, text='National Highways Authority of India', foreground="white", background="#262626",
            font=('Helvetica', 42, 'bold')).place(relx=0.16, rely=0.02)
      Label(self.root, text='Toll Information System ', foreground="#58A6FF", background="#262626",
              font=('Helvetica', 38, 'bold')).place(relx=0.16, rely=0.12)

      dashmenu=Menu(self.root)
      self.root.configure(menu=dashmenu,bg='#262626')
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

      chimage.add_command(label="Choose Vehicle Image",activebackground="#262626",command=lambda:Detect_Licenseno.main(tollid))

      regist.add_command(label="View Vehicles",activebackground="#262626",command=ViewVehicles.Vehicle_main)

      pas.add_command(label="Registered Passes",activebackground="#262626",command=issuemonthlypass.issue_pass)

      fares.add_command(label="Regular fares",activebackground="#262626",command=ViewPrice.View_main)
      fares.add_command(label="Monthly pass fares",activebackground="#262626",command=ViewPass.main)

      plaza.add_command(label="View Toll Booths",activebackground="#262626",command=TollPlaza.Toll_main)

      profile.add_command(label="Change password",activebackground="#262626",command=changeEmpPass.changePass)
      profile.add_command(label="Logout",activebackground="#262626",command=self.logout)
      profile.add_command(label="Exit",activebackground="#262626",command=self.root.destroy)
      self.root.mainloop()

