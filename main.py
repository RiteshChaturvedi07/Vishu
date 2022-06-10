from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

w=Tk()
w.geometry('350x500')
w.title("  Tkinter Login ")
w.resizable(0,0)


#Making gradient frame
j=0
r=10
for i in range(100):
    c=str(222222+r)
    Frame(w,width=10,height=500,bg="#"+c).place(x=j,y=0)   
    j=j+10                                                  
    r=r+1

Frame(w,width=250,height=400,bg='white').place(x=50,y=50)


l1=Label(w,text='Email',bg='white')
l=('cursive',13)
l1.config(font=l)
l1.place(x=80,y=200)

#e1 entry for username entry
e1=Entry(w,width=20,border=0)
l=('Consolas',13)
e1.config(font=l)
e1.place(x=80,y=230)

#e2 entry for password entry
e2=Entry(w,width=20,border=0,show='*')
e2.config(font=l)
e2.place(x=80,y=310)


l2=Label(w,text='Password',bg='white')
l=('cursive',13)
l2.config(font=l)
l2.place(x=80,y=280)


###lineframe on entry

Frame(w,width=180,height=2,bg='#141414').place(x=80,y=332)
Frame(w,width=180,height=2,bg='#141414').place(x=80,y=252)

from PIL import ImageTk,Image




#label1.place(x=115, y=50)


#Command   #password and Usernamee 
def cmd():
    if e1.get()=='' and e2.get()=='':
        messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
        
        my_w = tk.Tk()
        my_w.title('Uplode Notice')
        my_w.geometry("400x300")  # Size of the window 
        my_w.title('www.plus2net.com')
        my_font1=('times', 18, 'bold')
        l1 = tk.Label(my_w,text='Add Student Data with Photo',width=30,font=my_font1)  
        l1.grid(row=1,column=1)
        b1 = tk.Button(my_w, text='Upload File', 
        width=20,command = lambda:upload_file())
        b1.grid(row=2,column=1) 

        def upload_file():
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = ImageTk.PhotoImage(file=filename)
            b2 =tk.Button(my_w,image=img) # using Button 
            b2.grid(row=3,column=1)

        my_w.mainloop()
        
        
        
    else:
        messagebox.showwarning("LOGIN FAILED","        PLEASE TRY AGAIN        ")


#Button_with hover effect
def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text=text,
                   width=20,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                         
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=cmd)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)


bttn(80,375,'Login','white','#000')


w.mainloop()

