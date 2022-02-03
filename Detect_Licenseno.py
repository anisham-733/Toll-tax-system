from tkinter.constants import NW
import cv2
import tkinter
from tkinter import  Tk, Toplevel, filedialog
from tkinter.ttk import *
from tkinter import messagebox
import pytesseract as pyt
import numpy as np
from PIL import Image, ImageTk
import SearchVehicle
class main:
    
    def loc(self,states,state):
        self.updated_no=self.e1.get()
        state_up=self.updated_no[0:2]
        print(self.updated_no)
        state_label=tkinter.Label(self.Labelframe,text='Recognised State : ',
                    font=("Helvetica",22,'bold'),background='#262626',foreground='#F9A826')
        state_label.place(relx=0.06,rely=0.66)
        ans=tkinter.Label(self.Labelframe,font=("Helvetica",22,'bold'),background='#262626',
                    foreground='white')
        ans.place(relx=0.55,rely=0.66)
        try:
            ans.config(text=states[state_up])
        except:
            ans.config(text="State not recognised")
        self.b3=tkinter.Button(self.root,text="Next",font=("Helvetica",18,'bold') ,borderwidth=2,
                        relief='groove', bg='#238636', activebackground='#238636', 
                        activeforeground='#ffffff',
                        foreground='#ffffff',
                        command=lambda:SearchVehicle.Vehicle_Plate(self.root,self.updated_no,self.tid1))
        self.b3.place(relx=0.82,rely=0.85,relwidth=0.12,relheight=0.08)
        
        
    def Detection(self):
        
        self.F1=tkinter.Frame(self.root,background='#262626')
        
                
        self.F1.place(relx=0.01,rely=0.2,relwidth=0.98,relheight=0.8)
        
        states = {"DL": 'Delhi', "KA": 'Karnataka',"AP":"Andhra Pradesh","CH":"Chandigarh","PY":"Puducherry","LD":"Lakshadweep","LA":"Ladakh"
            ,"JK":"Jammu and Kashmir","DD":"Daman and Diu","DN":"Dadra and Nagar Haveli","AN":"Andaman and Nicobar Islands","WB":"West Bengal"
            ,"UK":"Uttarakhand0","UP":"Uttar Pradesh","TR":"Tripura","TS":"Telangana","TN":"Tamil Nadu","SK":"Sikkim","RJ":"Rajasthan","PB":"Punjab"
            ,"OD":"Odisha","NL":"Nagaland","MZ":"Mizoram","ML":"Meghalaya","MN":"Manipur","MH":"Maharashtra","MP":"Madhya Pradesh",
            "KL":"Kerala","JH":"Jharkhand","HP":"Himachal Pradesh","HR":"Haryana","GJ":"Gujarat","GA":"Goa","CJ":"Chattisgarh","BR":"Bihar"
            ,"AS":"Assam","AR":"Arunachal Pradesh"}
        
        if len(self.filename) != 0:
                
                image = cv2.imread(self.filename)
                image=cv2.resize(image,(700,480))
                pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

                plateCascade = cv2.CascadeClassifier('russian_noplate.xml')
                print(plateCascade)

                getCoordinates = plateCascade.detectMultiScale(image=image, scaleFactor=1.1,
                                                            minNeighbors=4)  # returns 4 args-x,y,w,h

                for (x, y, w, h) in getCoordinates:
                    a, b = (int(0.02 * image.shape[0]), int(0.025 * image.shape[1]))
                    plate = image[y:y + h, x:x + w]

                    # image processing
                    kernal = np.ones((1, 1), np.uint8)  # 1*1 matrix
                    plate = cv2.dilate(src=plate, kernel=kernal, iterations=1)
                    plate = cv2.erode(src=plate, kernel=kernal, iterations=1)
                    plateGray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)  
                    # convert image to b/w
                    
                    
                    (thresh, plate) = cv2.threshold(plateGray, 127, 255,
                                                    cv2.THRESH_BINARY_INV)  # threshold image
                    
                    text = pyt.image_to_string(plate)
                    
                    
                    text = ''.join(e for e in text if e.isalnum())  # remove blank spaces
                    state = text[0:2]
                       
                cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(51, 51, 255), thickness=2)
                cv2.rectangle(image,(x,y-40),(x+w,y),(51,51,255),-1)
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
               
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                imagetk = ImageTk.PhotoImage(image=image)
                
                self.detect_img=tkinter.Label(self.F1)
                self.detect_img.place(relx=0.02,rely=0)
                self.detect_img.imagetk = imagetk
                self.detect_img.configure(image=imagetk)
                self.label1=tkinter.Label(self.F1,text="Detected License Plate",
                            font=("Helvetica",28,'bold'),foreground='#F9A826',background='#262626')
                self.label1.place(relx=0.12,rely=0.75)

                plate=cv2.cvtColor(plate,cv2.COLOR_BGR2RGB)
                plate=Image.fromarray(plate)
                imagetk1=ImageTk.PhotoImage(plate)

                self.Labelframe=tkinter.LabelFrame(self.F1,text="Classify Image",borderwidth=3,bd=5,labelanchor=NW,
                                        font=('Helvetica',32,'bold')
                                        ,background='#262626',foreground="#58A6FF")
                self.Labelframe.place(relx=0.52,rely=0,relwidth=0.46,relheight=0.7)

                self.ocr=tkinter.Label(self.Labelframe,text="OCR image : ",background='#262626',foreground='#F9A826',
                                        font=("Helevetica",22,'bold'))
                self.ocr.place(relx=0.06,rely=0.08)
                self.plate_img=tkinter.Label(self.Labelframe)
                self.plate_img.place(relx=0.45,rely=0.08,relwidth=0.45,relheight=0.17)
                self.plate_img.imagetk1 = imagetk1
                self.plate_img.configure(image=imagetk1)
                
                recog_label=tkinter.Label(self.Labelframe,text="License Number :",font=('Helvetica',22,'bold'),
                                            background='#262626',foreground='#F9A826')
                recog_label.place(relx=0.06,rely=0.4)
                #Add a style
                self.s=Style()

                #Pick a theme
                self.s.theme_use("default")

                self.s.map('TCombobox', selectbackground=[('readonly', '#21262D')]) #161b22
                self.s.map('TCombobox', fieldbackground=[('readonly','#21262D')])
                self.s.map('TCombobox', selectforeground=[('readonly', '#C9D1D9')])

                self.e1=Entry(self.Labelframe,font=('Helvetica',22,'bold'),foreground='#262626',
                                    background='#F0F6FC', cursor="xterm #0000FF")
                self.e1.place(relx=0.46,rely=0.4,relwidth=0.34,relheight=0.084) 
                self.e1.insert(0,text)
                
                
                self.edit=tkinter.Button(self.Labelframe,text="Modify",font=("Helvetica",14,'bold'),bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',
                                foreground='#ffffff', command=lambda:self.loc(states,state))

                self.edit.place(relx=0.82,rely=0.4,relheight=0.088,relwidth=0.18)
                
                
    def chooseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(('jpg', '*.jpg'), ("png", "*.png"), ('jpeg', '*.jpeg')))
        if len(self.filename) != 0:
            
            self.b1.config(text=self.filename)
        else:
            messagebox.showinfo("", "Image is Not Selected",parent=self.root)
        
    def __init__(self,tollid):
        print(tollid)
        self.tid1=tollid
        self.root = Toplevel()
        self.root.resizable(0,0)
        self.root.configure(background='#262626')
        self.root.state("zoomed")
        self.root.title('License Plate recognition')
        self.root.iconbitmap("icons/add_winicon.ico")
        self.l=tkinter.Label(self.root, text="Select Image ",font=("Helvetica",20,'bold'),foreground='#58A6FF',
                background="#262626")

        self.l.place(relx=0.09,rely=0.04)
        self.b1 = tkinter.Button(self.root, text="Click here to Choose file (.png,.jpg)",
                                 font=("Helvetica", 18), foreground='#262626',
                                 background='#F0F6FC', command=self.chooseFile)

        
        self.b1.place(relx=0.24,rely=0.04,relwidth=0.47,relheight=0.06)
        self.b2 =tkinter.Button(self.root, text="Start Detection", font=("Helvetica", 16, 'bold'), borderwidth=2,
                         relief='groove', bg='#238636', activebackground='#238636', activeforeground='#ffffff',
                         foreground='#ffffff',command=self.Detection) 
        self.b2.place(relx=0.74,rely=0.04,relwidth=0.14,relheight=0.06)

        self.root.grab_set()
        self.root.transient()
        self.root.mainloop()
