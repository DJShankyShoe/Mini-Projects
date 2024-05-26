from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import os
import sys
import threading
dirpath = os.getcwd()
sys.path.append(dirpath.replace("\\", "\\\\") + "\\\\Data")
from Encrypt import*
import Encryption_Code_Duplicator
def option():
    def remove1(event):
        win.withdraw()
        encryptor()
    def remove2(event):
        win.withdraw()
        viewer()       
    win = Tk()
    win.title("")
    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.geometry('{}x{}'.format(190, 63))
    Label(win, text = "Would you like to....").grid(row = 0, columnspan = 2, pady = 2)
    Label(win, text = "\n\n").grid(row = 1)
    view = Button(win, text = "View Passwords")
    view.bind("<Button-1>", remove2)
    view.grid(row = 1)
    encryption = Button(win, text = "Store Passwords")
    encryption.bind("<Button-1>", remove1)
    encryption.grid(row = 1, column = 1)
    win.mainloop()
def checkpassword(event):
    temp = []
    dirpath = os.getcwd()
    data = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r")
    key = data.readline().split("@4tBp:>s#&^")[-1][::-1].split("\n", 1)[-1][::-1]
    data.close()
    if encrypt(passw.get()) != key:
        tkinter.messagebox.showerror("Warning", "Incorrect Password, Access Denied")
        passw.delete(0,END)
    else:
        win.destroy()
        option()
def viewer():
    class MultipleScrollingListbox(Tk):
        def closing(self,event):
            self.withdraw()
            option()         
        def deloption(self,event):
            self.withdraw()          
            class MultipleScrollingListbox(Tk):
                def reboot(self): 
                    self.withdraw()
                    viewer()
                def direct(self):                        
                    self.withdraw()
                    def end(event):
                        win.withdraw()
                        viewer()
                    def delete(event):
                        lines = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r").readlines()
                        open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r").close()
                        temp = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "w")
                        temp.close()
                        temp = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "a")
                        for run in lines:
                            if run != delmsg:
                                temp.write(run)
                        temp.close()
                        win.destroy()
                        viewer()
                    win = Tk()
                    windowWidth = win.winfo_reqwidth()
                    windowHeight = win.winfo_reqheight()
                    positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
                    positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
                    win.geometry("+{}+{}".format(positionRight - 225, positionDown))   
                    dirpath = os.getcwd()    
                    data = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r")
                    data = data.readlines()[1:]
                    global line_num
                    line_num = 0
                    i = 1
                    for line in data:
                        if i == new_num:
                            global delmsg
                            delmsg = line
                            text = line.split("~")
                            line_num += 1
                            lists = []
                            for run in text[-1]:
                                lists.append(run)
                            lists.remove("\n")
                            lists = "".join(lists)
                            text[-1] = lists
                            msg1 = decrypt(text[0])
                            msg2 = decrypt(text[1])
                        i += 1
                    Label(win, text = "Are you sure you want to delete the following:",fg = "red").grid(row = 1, columnspan = 2, pady = 2)
                    Label(win, text = msg1 + " --> " + msg2, font = ("ariel", 11)).grid(row = 2, columnspan = 2, padx = 70, sticky = W)
                    cancel = Button(win, text = "cancel", width = 15)
                    cancel.bind("<Button-1>", end)
                    cancel.grid(row = 3, column = 0, padx = 2, pady = 5, sticky = E)  
                    proceed = Button(win, text = "proceed>", width = 15)
                    proceed.bind("<Button-1>", delete)
                    proceed.grid(row = 3, column = 1, padx = 2, pady = 5, sticky = W)  
                def __init__(self):
                    Tk.__init__(self)
                    self.title("Passwords") 
                    def reboot2(event):
                        win.withdraw()
                        self.reboot()  
                    def checklist(event):                        
                        try:
                            if int(option.get()) > 0 and int(option.get()) <= line_num:
                                global new_num
                                new_num = int(option.get())
                                win.withdraw()
                                self.direct() 
                            else:
                                tkinter.messagebox.showerror("Warning", "Invalid row number!")
                                win.withdraw()
                                self.reboot()                                 
                        except ValueError:
                            tkinter.messagebox.showerror("Warning", "Must be Integer!")
                            win.withdraw()
                            self.reboot()                             
                    windowWidth = self.winfo_reqwidth()
                    windowHeight = self.winfo_reqheight()
                    positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
                    positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)
                    self.geometry("+{}+{}".format(positionRight, positionDown))
                    Label(self, text = "      Description     ", fg = "red", font = ("ariel", 12)).grid(row = 0, sticky = W, pady = 8)
                    Label(self, text = "    Password          ", fg = "red", font = ("ariel", 12)).grid(row = 0, column = 1, sticky = W)       
                    self.scrollbar = Scrollbar(self, orient='vertical')
                    self.list1 = Listbox(self, width = 40, height = 10, yscrollcommand = self.yscroll1)
                    self.list1.grid(row = 2, sticky = W)
                    self.list2 = Listbox(self, width = 40, height = 10, yscrollcommand = self.yscroll1)
                    self.list2.grid(row = 2, column = 1, sticky = E)
                    self.scrollbar.config(command=self.yview)
                    self.scrollbar.grid(row = 2, column = 2, sticky = "nsw")
                    self.bind_all("<MouseWheel>", self.mousewheel)
                    dirpath = os.getcwd()    
                    data = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r")
                    data = data.readlines()[1:]
                    line_num = 0
                    for line in data:
                        text = line.split("~")
                        line_num += 1
                        lists = []
                        for run in text[-1]:
                            lists.append(run)
                        lists.remove("\n")
                        lists = "".join(lists)
                        text[-1] = lists
                        msg1 = decrypt(text[0])
                        msg2 = decrypt(text[1])
                    
                        self.list1.insert(END, "    " + str(line_num) + ") " + msg1 + "  " + "-"*100)
                        self.list2.insert(END, "--->  " + msg2)
                        self.list1.insert(END, "")
                        self.list2.insert(END, "") 
                    win = Tk()
                    win.title("")
                    windowWidth = win.winfo_reqwidth()
                    windowHeight = win.winfo_reqheight()
                    positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
                    positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
                    win.geometry("+{}+{}".format(positionRight - 225, positionDown))
                    Label(win, text = "Delete Password",fg = "red", font = ("ariel", 12)).grid(row = 1, columnspan = 3, pady = 2)
                    Label(win, text = "Choose row number").grid(row = 2, column = 0, sticky = W)
                    option = Entry(win, width = 7)
                    option.grid(row = 2, column = 2, padx = 5, pady = 3, sticky = W)
                    cancel = Button(win, text = "cancel", width = 12)
                    cancel.bind("<Button-1>", reboot2)
                    cancel.grid(row = 3, sticky = E)     
                    delete = Button(win, text = "Delete Row", width = 12, bg = "red")
                    delete.bind("<Button-1>", checklist)
                    delete.grid(row = 3, column = 2, pady = 5 , padx = 8, sticky = W)                    
                def mousewheel(self, event):
                    self.list1.yview_scroll(-1 * int(event.delta / 120), "units")
                    self.list2.yview_scroll(-1 * int(event.delta / 120), "units")         
                def yscroll1(self, *args):
                    if self.list2.yview() != self.list1.yview():
                        self.list2.yview_moveto(args[0])
                    self.scrollbar.set(*args)
                def yscroll2(self, *args):
                    if self.list1.yview() != self.list2.yview():
                        self.list1.yview_moveto(args[0])
                    self.scrollbar.set(*args)
                def yview(self, *args):
                    self.list1.yview(*args)
                    self.list2.yview(*args)
            if __name__ == "__main__":
                root = MultipleScrollingListbox()
                root.mainloop()   
        def __init__(self):
            Tk.__init__(self)
            self.title("Passwords")
            windowWidth = self.winfo_reqwidth()
            windowHeight = self.winfo_reqheight()
            positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
            positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)
            self.geometry("+{}+{}".format(positionRight, positionDown))
            Label(self, text = "      Description     ", fg = "red", font = ("ariel", 12)).grid(row = 0, sticky = W, pady = 8)
            Label(self, text = "    Password          ", fg = "red", font = ("ariel", 12)).grid(row = 0, column = 1, sticky = W)       
            self.scrollbar = Scrollbar(self, orient='vertical')
            self.list1 = Listbox(self, width = 40, height = 10, yscrollcommand = self.yscroll1)
            self.list1.grid(row = 2, sticky = W)
            self.list2 = Listbox(self, width = 40, height = 10, yscrollcommand = self.yscroll1)
            self.list2.grid(row = 2, column = 1, sticky = E)
            self.scrollbar.config(command=self.yview)
            self.scrollbar.grid(row = 2, column = 2, sticky = "nsw")
            self.bind_all("<MouseWheel>", self.mousewheel)
            dirpath = os.getcwd()    
            data = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r")
            data = data.readlines()[1:]
            line_num = 0
            for line in data:
                text = line.split("~")
                line_num += 1
                lists = []
                for run in text[-1]:
                    lists.append(run)
                lists.remove("\n")
                lists = "".join(lists)
                text[-1] = lists
                msg1 = decrypt(text[0])
                msg2 = decrypt(text[1])
                self.list1.insert(END, "    " + str(line_num) + ") " + msg1 + "  " + "-"*100)
                self.list2.insert(END, "--->  " + msg2)
                self.list1.insert(END, "")
                self.list2.insert(END, "")   
            back = Button(self, text = "<Back", width = 8)
            back.bind("<Button-1>", self.closing)
            back.grid(columnspan = 2, pady = 5)     
            if line_num > 0:
                delete = Button(self, text = "Delete Pass", width = 8, bg = "red")
                delete.bind("<Button-1>", self.deloption)
                delete.grid(row = 3, padx = 4, sticky = W)
        def mousewheel(self, event):
            self.list1.yview_scroll(-1 * int(event.delta / 120), "units")
            self.list2.yview_scroll(-1 * int(event.delta / 120), "units")         
        def yscroll1(self, *args):
            if self.list2.yview() != self.list1.yview():
                self.list2.yview_moveto(args[0])
            self.scrollbar.set(*args)
        def yscroll2(self, *args):
            if self.list1.yview() != self.list2.yview():
                self.list1.yview_moveto(args[0])
            self.scrollbar.set(*args)
        def yview(self, *args):
            self.list1.yview(*args)
            self.list2.yview(*args)
    if __name__ == "__main__":
        root = MultipleScrollingListbox()
        root.mainloop()
def encryptor():
    def backspace(event):
        Label(win, text = " "*60).grid(row = 2, column =1, sticky = W)        
    def clearing(event):
        win.withdraw()
        encryptor()
    def checks():
        threading.Timer(0.1, checks).start()
        Label(win, text = passw.get(), borderwidth=2, relief="groove").grid(row = 2, column =1, sticky = W)
    def remove1(event):
        win.withdraw()
        option()
    def remove2(event):
        encryption()
    def encryption():
        if dec.get() == "" or passw.get() == "":
            tkinter.messagebox.showerror("Error", "Description and Password entry boxes needed to be filled")
        else:
            dirpath = os.getcwd()           
            data = open("data.txt", "a")
            datad = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "a")
            total = encrypt(dec.get())
            data.write(total + "~")
            datad.write(total + "~")
            total = encrypt(passw.get())
            data.write(total + "\n") 
            datad.write(total + "\n") 
            data.close()
            datad.close()
            tkinter.messagebox.showinfo("Successful", "Your password has been encryted and stored")
            clearing("")
    win = Tk()
    win.title("")
    win.geometry("+{}+{}".format(positionRight, positionDown))
    Label(win, text = "Description").grid(row = 0, sticky = E)
    Label(win, text = "Password: ").grid(row = 1, sticky = E, pady = 4)
    Label(win, text = "").grid(row = 2)
    check = Button(win, text = "Show Password", command = checks)
    check.grid(row = 1, column = 2, padx = 6, sticky = W)
    passw = Entry(win, show = "*", width = 30)
    passw.bind("<BackSpace>", backspace)
    passw.grid(row = 1, column = 1, sticky = W)
    dec = Entry(win, width = 30)
    dec.grid(row = 0, column = 1, sticky = W)    
    clear = Button(win, text = "Clear", width = 6)
    clear.bind("<Button-1>", clearing)
    clear.grid(row = 3, column = 1, sticky = E)
    enter = Button(win, text = "Enter", width = 10)
    enter.bind("<Button-1>", remove2)
    enter.grid(row = 3, column = 2, padx = 4, sticky = W)
    back = Button(win, text = "<Back", width = 7)
    back.bind("<Button-1>", remove1)
    back.grid(row = 3, padx = 4, sticky = W)
    win.mainloop()
def match(event):
    def choice():
        def closing(event):
            dirpath = os.getcwd()
            os.remove(dirpath.replace("\\", "/").replace("C:", "") + "/data.txt") 
            os.remove(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt")
            data = open("data.txt", "a")  
            datad = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "a")
            data.write("@4tBp:>s#&^" + encrypt(added) + "\n")
            datad.write("@4tBp:>s#&^" + encrypt(added) + "\n")
            data.close()
            datad.close()
            win.destroy()
            option()
        def update(event): 
            dirpath = os.getcwd()
            os.remove(dirpath.replace("\\", "/").replace("C:", "") + "/data.txt")
            os.remove(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt")
            data = open("data.txt", "a")
            datad = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "a")
            data.write("@4tBp:>s#&^" + encrypt(added) + "\n")
            datad.write("@4tBp:>s#&^" + encrypt(added) + "\n")
            total = encrypt("this program")   
            data.write(total + "~")
            datad.write(total + "~")  
            total = encrypt(added)            
            data.write(total + "\n")
            datad.write(total + "\n") 
            data.close()
            datad.close()
            win.destroy()
            option()
        win = Tk()
        win.geometry("+{}+{}".format(positionRight, positionDown))
        Label(win, text = "Would you like to securely store the login password in the program").grid(row = 0, pady = 5)
        yes = Button(win, text = "yes", width = 6)
        yes.bind("<Button-1>", update)
        yes.grid(row = 1, sticky = W, padx = 125, pady = 10)
        no = Button(win, text = "no", width = 6)
        no.bind("<Button-1>", closing)
        no.grid(row = 1, sticky = E, padx = 125)
        win.mainloop()    
    if passw1.get() == "" or passw2.get() == "":
        print(passw1.get())
        tkinter.messagebox.showerror("Error", "Both entry boxes neeeded to be filled")
        passw1.delete('0', END)
        passw2.delete('0', END)
    elif passw1.get() != passw2.get():
        tkinter.messagebox.showerror("Error", "Passwords don't match!!!")
        passw1.delete('0', END)
        passw2.delete('0', END)    
    else:
        added = passw1.get()
        win.withdraw()
        choice()
win = Tk()
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()
positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
win.geometry("+{}+{}".format(positionRight, positionDown))
verify = 0
words = []
code = ("@ 4 t B p : > s # & ^")
code = code.split(" ")
dirpath = os.getcwd()
data = open(dirpath.replace("\\", "/").replace("C:", "") + "/Data/data.txt", "r")
for word in data.readline():
    if word != "\n":
        words.append(word)
data.close()
try:
    for run in range(len(code)):
        if words[run] == code[run]:
            verify += 1
except:
    verfiy = 0
        
if verify == len("@4tBp:>s#&^"):
    win.title("Password Storage")
    Label(win, text = "   Enter password to have access to the program   ", fg = "red").grid(row = 0, columnspan = 2, pady = 2)
    Label(win, text = "Password:").grid(row = 2, sticky = E, pady = 6)
    passw = Entry(win, show = "*")
    passw.grid(row = 2, column = 1, sticky = W)
    equal = Button(win, text = "Submit", width = 10, bg = "red")
    equal.bind("<Button-1>", checkpassword)
    equal.grid(row = 3,column = 1, sticky = W)
else:
    Encryption_Code_Duplicator.cipher()
    Encryption_Code_Duplicator.decipher()
    Encryption_Code_Duplicator.hexa_rehexa()    
    win.geometry("+{}+{}".format(positionRight, positionDown))
    win.title("Setup")
    Label(win, text = "Looks like you are a new user", fg = "red", font = ("ariel", 12)).grid(row = 0)
    Label(win, text = "Create a password below so that you can use the program successfully everytime you login").grid(row = 1, pady = 15)
    Label(win, text = " New Password").grid(row = 2, padx = 20, sticky = W)
    passw1 = Entry(win, width = 40, show = "*")
    passw1.grid(row = 2, padx = 110, sticky = W)
    Label(win, text = " Confirm Password").grid(row = 3, sticky = W)
    passw2 = Entry(win, width = 40, show = "*")
    passw2.grid(row = 3, pady = 5, padx = 110, sticky = W) 
    proceed = Button(win, text = "Proceed>", width = 10)
    proceed.bind("<Button-1>", match)
    proceed.grid(row = 4, pady = 10)
win.mainloop()