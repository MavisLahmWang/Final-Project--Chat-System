#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:54:42 2019

@author: jiaxinbu
"""
import tkinter as tk
import tkinter.messagebox
import pickle

#set window
window = tk.Tk()
window.title('Welcome to chat!')
window.geometry('350x232')
           
# set canvas

"""canvas = tk.Canvas(window, width=500,height=350,bd=0, highlightthickness=0)
img = Image.open('xk.png')
photo = ImageTk.PhotoImage(img)
 
canvas.create_image(350, 233, image=photo)
canvas.pack()
entry=tk.Entry(root,insertbackground='blue', highlightthickness =2)
entry.pack()
 
canvas.create_window(100, 50, width=100, height=20,
                                       window=entry)"""

canvas = tk.Canvas(window, height = 300, width = 500)
imagefile = tk.PhotoImage(file = 'xk.png')
image = canvas.create_image(0,0,anchor = 'nw', image = imagefile) #????
canvas.pack(side = 'top')
#username password
tk.Label(window,text = 'Username:').place(x=40,y=72)
tk.Label(window,text = 'Password:').place(x=40,y=114)
#enter place
var_usn = tk.StringVar()
entry_usn = tk.Entry(window, textvariable = var_usn)
entry_usn.place(x=120,y=70)
var_psw = tk.StringVar()
entry_psw = tk.Entry(window, textvariable = var_psw)
entry_psw.place(x=120,y=110)

def user_login():
    usn = var_usn.get()
    psw = var_psw.get()
    #examine being or not being
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usr_info = pickle.load(usr_file)
    except:
         with open('usr_info.pickle','wb') as usr_file:
            usr_info = {'admin':'admin'}#???
            pickle.dump(usr_info,usr_file)
    # match username and password
    if usn in usr_info:
        if psw == usr_info[usn]:
            tk.messagebox.showinfo(title = 'welcome', message = 'congratulation' + usn)
        else:
            tk.messagebox.showerror(message = 'wrong password')
    elif usn == '' or psw =='':
        tk.messagebox.showerror(message = 'empty')
    else:
        signup = tk.messagebox.askyesno(title = 'oh new user', message = 'would you want to sign up now')
        if signup:
            user_signup()

def user_signup():
    # create login window
    window_signup = tk.Toplevel(window)
    window_signup.title('Just for new user')
    window_signup.geometry('400x250')
    var_newname = tk.StringVar()
    tk.Label(window_signup,text = 'Username:').place(x=40,y=58)
    entry_newusn = tk.Entry(window_signup, textvariable = var_newname)
    entry_newusn.place(x=120,y=58)
    var_newpsw = tk.StringVar()
    tk.Label(window_signup,text = 'Password:').place(x=40,y=97)
    entry_newpsw = tk.Entry(window_signup, textvariable = var_newpsw)
    entry_newpsw.place(x=120,y=97)
    var_cfnewpsw = tk.StringVar()
    tk.Label(window_signup,text = 'Confirm Password:').place(x=40,y=136)
    entry_cfnewpsw = tk.Entry(window_signup, textvariable = var_cfnewpsw)
    entry_cfnewpsw.place(x=170,y=136)

    # get new user's info
    def signinfo():
        newname = var_newname.get()
        newpw = var_newpsw.get()
        newpw_cf = var_cfnewpsw.get()
        
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except:
            exist_usr_info = {}
            
    # examine whether the username exists or passwords are same
        if newname in exist_usr_info:
            tk.messagebox.showerror(title = 'Mistake', message = newname + 'has already existed')
        elif newname == '' or newpw == '' or newpw_cf == '':
            tk.messagebox.showerror(title = 'Mistake', message = 'empty')
        elif newpw != newpw_cf:
            tk.messagebox.showerror(title = 'Mistake', message = 'reenter the password')
        else:
            exist_usr_info[newname] = newpw
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome','Successful sign up!!!')
            window_signup.destroy()
    bt_enter=tk.Button(window_signup,text="Let's Start",command=signinfo)
    bt_enter.place(x=150,y=170)

def log_out():
    window.destroy()

bt_login=tk.Button(window,text='log in',command=user_login)
bt_login.place(x=50,y=170)
bt_logup=tk.Button(window,text='register',command=user_signup)
bt_logup.place(x=110,y=170)
bt_logquit=tk.Button(window,text='log out',command=log_out)
bt_logquit.place(x=190,y=170)


window.mainloop()