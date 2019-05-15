#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:54:42 2019

@author: jiaxinbu
"""
import tkinter as tk
import tkinter.messagebox
import pickle

class login_wind:

    def __init__(self,window):
        #set window
        self.sign = ''
        self.window = tk.Tk()
        self.window.title('Welcome to chat!')
        self.window.geometry('350x232')
           
        self.canvas = tk.Canvas(self.window, height = 300, width = 500)
        self.imagefile = tk.PhotoImage(file = 'xk.png')
        self.image = self.canvas.create_image(0,0,anchor = 'nw', image = self.imagefile) #????
        self.canvas.pack(side = 'top')
#username password
        tk.Label(self.window,text = 'Username:').place(x=40,y=72)
        tk.Label(self.window,text = 'Password:').place(x=40,y=114)
#enter place
        self.var_usn = tk.StringVar()
        self.entry_usn = tk.Entry(self.window, textvariable = self.var_usn)
        self.entry_usn.place(x=120,y=70)
        self.var_psw = tk.StringVar()
        self.entry_psw = tk.Entry(self.window, textvariable = self.var_psw)
        self.entry_psw.place(x=120,y=110)
# set canvas
   
        self.usn = ''
        self.psw = ''
        self.usr_info = {}
        
    def show_window(self):
        
        self.bt_login=tk.Button(self.window,text='log in',command=self.user_login)
        self.bt_login.place(x=50,y=170)
        self.bt_logup=tk.Button(self.window,text='register',command=self.user_signup)
        self.bt_logup.place(x=110,y=170)
        self.bt_logquit=tk.Button(self.window,text='log out',command=self.log_out)
        self.bt_logquit.place(x=190,y=170)
        self.window.mainloop()



        
        """self.window = tk.Tk()
        self.window.title('Welcome to chat!')
        self.window.geometry('350x232')
           
        self.canvas = tk.Canvas(self.window, height = 300, width = 500)
        self.imagefile = tk.PhotoImage(file = 'xk.png')
        self.image = self.canvas.create_image(0,0,anchor = 'nw', image = self.imagefile) #????
        self.canvas.pack(side = 'top')
#username password
        tk.Label(self.window,text = 'Username:').place(x=40,y=72)
        tk.Label(self.window,text = 'Password:').place(x=40,y=114)
#enter place
        self.var_usn = tk.StringVar()
        self.entry_usn = tk.Entry(self.window, textvariable = self.var_usn)
        self.entry_usn.place(x=120,y=70)
        self.var_psw = tk.StringVar()
        self.entry_psw = tk.Entry(self.window, textvariable = self.var_psw)
        self.entry_psw.place(x=120,y=110)"""

        
    def user_login(self):
        global usn
        self.usn = self.var_usn.get()
        self.psw = self.var_psw.get()
    #examine being or not being
        try:
            with open('usr_info.pickle','rb') as usr_file:
                self.usr_info = pickle.load(usr_file)
        except:
            with open('usr_info.pickle','wb') as usr_file:
                self.usr_info = {'admin':'admin'}#???
                pickle.dump(self.usr_info,usr_file)
    # match username and password
        if self.usn in self.usr_info:
            if self.psw == self.usr_info[self.usn]:
                tk.messagebox.showinfo(title = 'welcome', message = 'congratulation ' + self.usn)
                self.window.destroy()
                return 
            else:
                tk.messagebox.showerror(message = 'wrong password')
        elif self.usn == '' or self.psw =='':
            tk.messagebox.showerror(message = 'empty')

        else:
            self.signup = tk.messagebox.askyesno(title = 'oh new user', message = 'would you want to sign up now')
            if self.signup:
                self.user_signup()



    def user_signup(self):
    # create login window
        self.window_signup = tk.Toplevel(self.window)
        self.window_signup.title('Just for new user')
        self.window_signup.geometry('400x250')
        self.var_newname = tk.StringVar()
        tk.Label(self.window_signup,text = 'Username:').place(x=40,y=58)
        self.entry_newusn = tk.Entry(self.window_signup, textvariable = self.var_newname)
        self.entry_newusn.place(x=120,y=58)
        self.var_newpsw = tk.StringVar()
        tk.Label(self.window_signup,text = 'Password:').place(x=40,y=97)
        self.entry_newpsw = tk.Entry(self.window_signup, textvariable = self.var_newpsw)
        self.entry_newpsw.place(x=120,y=97)
        self.var_cfnewpsw = tk.StringVar()
        tk.Label(self.window_signup,text = 'Confirm Password:').place(x=40,y=136)
        self.entry_cfnewpsw = tk.Entry(self.window_signup, textvariable = self.var_cfnewpsw)
        self.entry_cfnewpsw.place(x=170,y=136)
        
        bt_enter=tk.Button(self.window_signup,text="Let's Start",command=self.signinfo)
        bt_enter.place(x=150,y=170)


        
    # get new user's info
    def signinfo(self):
        self.newname = self.var_newname.get()
        self.newpw = self.var_newpsw.get()
        self.newpw_cf = self.var_cfnewpsw.get()
            
        try:
            with open('usr_info.pickle','rb') as usr_file:
                self.exist_usr_info = pickle.load(usr_file)
        except:
            self.exist_usr_info = {}
                            
    # examine whether the username exists or passwords are same
        if self.newname in self.exist_usr_info:
            tk.messagebox.showerror(title = 'Mistake', message = self.newname + 'has already existed')
        elif self.newname == '' or self.newpw == '' or self.newpw_cf == '':
            tk.messagebox.showerror(title = 'Mistake', message = 'empty')
        elif self.newpw != self.newpw_cf:
            tk.messagebox.showerror(title = 'Mistake', message = 'reenter the password')
        else:
            self.exist_usr_info[self.newname] = self.newpw
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(self.exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome','Successful sign up!!!')
            self.window_signup.destroy()


    def log_out(self):
        self.window.destroy()

    
