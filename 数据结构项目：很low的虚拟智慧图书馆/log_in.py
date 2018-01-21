import tkinter as tk
import sqlite3
import tkinter.messagebox
import better


class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x100')
        self.title('Log in')
        self.accountlab = tk.Label(self, text="account:")
        self.accountlab.place(x=1, y=1, anchor='nw')
        self.passwordlab = tk.Label(self, text="password:")
        self.passwordlab.place(x=1, y=25, anchor='nw')
        self.account = tk.Entry(self)
        self.account.place(x=67, y=1, anchor='nw')
        self.password = tk.Entry(self, show='*')
        self.password.place(x=67, y=25, anchor='nw')
        self.sumbit = tk.Button(self, text="login", command=self.check_login)
        self.sumbit.place(x=100, y=50, anchor='nw')

    def check_login(self):
        account = self.account.get() or ''
        password = self.password.get() or ''
        if account =='' or password=='':
            return
        conn = sqlite3.connect("/home/nero/PycharmProjects/login.db")
        c = conn.cursor()
        a = None
        b = None
        cursor = c.execute("SELECT ACCOUNT,PASSWORD  FROM LOGIN WHERE ACCOUNT='%s'" % account)
        for row in cursor:
            a = row[0]
            b = row[1]
        if a == account and b == password:
            tkinter.messagebox.showinfo('message', 'Success!')
            conn.close()
            self.destroy()
            app=better.window('%s'%account)
            app.mainloop()
            return
        elif a==None:
            tkinter.messagebox.showinfo('message', 'No such account!')
        else:
            tkinter.messagebox.showinfo('message', 'Password error!')
        conn.close()
        return

