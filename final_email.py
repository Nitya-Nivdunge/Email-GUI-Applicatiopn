from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
import smtplib
from email.message import EmailMessage
import webbrowser

#Global variables
attachments = []

#Main Screen Init
root= tk.Tk()
root.title("  C184  C195  C196  ")
root.geometry('1030x680')
root.config(bg='white')

#Functions
def attachFile():
    filename = filedialog.askopenfilename(initialdir='C:/',title='Please select a file')
    attachments.append(filename)
    notif.config(font=('Courier New', 15,'bold'),fg="#0da300", text = ' ATTACHED  NO. OF  FILES  : ' + str(len(attachments)))

def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete('1.0','end')
  
def send():
    try:
        msg      = EmailMessage()
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        body     = bodyEntry.get('1.0','end')
        msg['subject'] = subject
        msg['from'] = username
        msg['to'] = to
        msg.set_content(body)

        for filename in attachments:
            filetype = filename.split('.')
            filetype = filetype[1]
            if filetype == "jpg" or filetype == "JPG" or filetype == "png" or filetype == "PNG":
                import imghdr
                with open(filename, 'rb') as f:
                    file_data = f.read()
                    image_type = imghdr.what(filename)
                msg.add_attachment(file_data, maintype='image', subtype=image_type, filename=f.name)

            else:
                with open(filename, 'rb') as f:
                    file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f.name)
        
        if username=="" or password=="" or to=="":
            notif.config(text="All fields required !! ",font=('Courier New',15,'bold'),fg="#fa6400")
            messagebox.showinfo('INCOMPLETE','    All fields required !!   ',icon = 'warning')
        else:
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            notif.config(text="EMAIL HAS BEEN SENT SUCCESSFULLY !!",font=('Courier New', 15,'bold'),fg="#0da300")
    except:
        notif.config(text="ERROR IN SENDING THE EMAIL !! ",font=('Courier New',15,'bold'),fg="#fa6400")
        MsgBox = tk.messagebox.askretrycancel("INVALID DETAILS","   Please Enter the details correctly !! ")
        if MsgBox ==0:
            exiting = tk.messagebox.askquestion('Exit Application','Are you sure you want to exit the application')
            if exiting =='yes':
                root.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        else:
            reset()
            return
          
def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")

#photos
photo1 = PhotoImage(file="attach_icon.png")
attach=photo1.subsample(4,4)

photo2=PhotoImage(file="reset_icon.png")
reset1=photo2.subsample(6,6)

photo3=PhotoImage(file="send_icon.png")
sending=photo3.subsample(4,4)

photo4=PhotoImage(file="error_icon.png")
error=photo4.subsample(15,15)

photo5 = PhotoImage(file="email_icon.png")
mail=photo5.subsample(16,16)
##262626  , #FFD966

title=Label(root,text='\tEMAIL APPLICATION',image=mail,font=("Goudy Old Style",35,'bold'),compound=LEFT,padx=20,bg='#222A35',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

a = tk.Button(root, text="Turn  On  Setting :  Less  Secure  App  Access  ( CLICK  HERE )  ",font=('times new roman',12,'bold'),bd=5,relief=GROOVE,fg="white",bg='darkgrey',cursor="hand2")
a.place(x=0,y=70,relwidth=1)
a.bind("<Button-1>", setup)

#Labels
#Label(root, text="Custom Email App", font=('Calibri',15)).grid(row=0, sticky=N)
#Label(root, text="Please use the form below to send an email", font=('Calibri',11)).grid(row=1, sticky=W, padx=5 ,pady=10)

frame1=tk.Frame(root,bg='white')
frame1.pack(padx=130,pady=110)

tk.Label(frame1, text=("FROM  * "), font=('times new roman',16,'bold'),bg='white').grid(row=2,column=0,sticky=W, padx=50)
tk.Label(frame1, text="PASSWORD  * ", font=('times new roman',16,'bold'),bg='white').grid(row=3,column=0,sticky=W, padx=50)
tk.Label(frame1, text="To  *", font=('times new roman',16,'bold'),bg='white').grid(row=4,column=0,sticky=W, padx=50)
tk.Label(frame1, text="SUBJECT", font=('times new roman',16,'bold'),bg='white').grid(row=5,column=0,sticky=W, padx=50)
tk.Label(frame1, text="BODY", font=('times new roman',16,'bold'),bg='white').grid(row=6,column=0,sticky=W, padx=50)
notif = tk.Label(frame1, text="", font=('Courier New', 13,'bold'),bg='white',fg="red")
notif.grid(row=7,sticky=S)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
bodyEntry     = StringVar()

#Entries
usernameEntry = tk.Entry(frame1, textvariable = temp_username,bg='powder blue',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,width=40,justify='center')
usernameEntry.grid(row=2,column=0,ipadx=30,ipady=2.5,padx=300,pady=15)
passwordEntry = tk.Entry(frame1, show="*", textvariable = temp_password,bg='powder blue',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,width=40,justify='center')
passwordEntry.grid(row=3,column=0,ipadx=30,ipady=2.5,padx=300,pady=15)
receiverEntry  = tk.Entry(frame1, textvariable = temp_receiver,bg='powder blue',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,width=40,justify='center')
receiverEntry.grid(row=4,column=0,ipadx=30,ipady=2.5,padx=300,pady=15)
subjectEntry  = tk.Entry(frame1, textvariable = temp_subject,bg='powder blue',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,width=40,justify='center')
subjectEntry.grid(row=5,column=0,ipadx=30,ipady=2.5,padx=300,pady=15)
bodyEntry     = tk.Text(frame1,bg='powder blue',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,width=40,height=6)
bodyEntry.grid(row=6,column=0,ipadx=30,ipady=2.5,padx=300,pady=15)


frame2=tk.Frame(root,bg='white')
frame2.place(x=190,y=600)

#Buttons
tk.Button(frame2, text = " SEND  ",font=('times new roman',13,'bold'),relief=GROOVE,bd=5,image = sending,compound = LEFT,command = send).grid(row=0,column=0,padx=30)
tk.Button(frame2, text = " RESET  ",font=('times new roman',13,'bold'),relief=GROOVE,bd=5,image = reset1,compound = LEFT,command = reset).grid(row=0,column=1,padx=30)
tk.Button(frame2, text = " ATTACHMENTS  ",font=('times new roman',13,'bold'),relief=GROOVE,bd=5,image = attach,compound = LEFT,command =attachFile).grid(row=0,column=2,padx=35)

#Mainloop
root.mainloop()