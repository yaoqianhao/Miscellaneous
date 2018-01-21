import tkinter as tk
import sqlite3
import tkinter.messagebox
import better

class signup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x150')
        self.title('Sign up')

        self.accountlab = tk.Label(self, text="account:")
        self.accountlab.place(x=1, y=1, anchor='nw')
        self.passwordlab = tk.Label(self, text="password:")
        self.passwordlab.place(x=1, y=25, anchor='nw')
        self.confirm = tk.Label(self, text="confirm:")
        self.confirm.place(x=1, y=50, anchor='nw')
        self.account = tk.Entry(self)
        self.account.place(x=67, y=1, anchor='nw')
        self.password = tk.Entry(self, show='*')
        self.password.place(x=67, y=25, anchor='nw')
        self.confirm = tk.Entry(self, show='*')
        self.confirm.place(x=67, y=50, anchor='nw')
        self.sumbit = tk.Button(self, text="sumbit", command=self.check_signup)
        self.sumbit.place(x=100, y=75, anchor='nw')

    def check_signup(self):
        conn = sqlite3.connect("/home/nero/PycharmProjects/login.db")
        c = conn.cursor()
        account = self.account.get() or None
        password = self.password.get() or None
        confirm = self.confirm.get() or None
        cursor = c.execute("SELECT ACCOUNT,PASSWORD  FROM LOGIN WHERE ACCOUNT='%s'" % account)
        a = None
        for row in cursor:
            a = row[0]
        if account == None or password == None or confirm == None:
            conn.commit()
            conn.close()
            return
        elif password != confirm:
            tkinter.messagebox.showinfo('message', 'confirm failed!')
            conn.commit()
            conn.close()
            return
        elif a == None:
            tkinter.messagebox.showinfo('message', 'Success!')
            c.execute("INSERT INTO LOGIN (ACCOUNT,PASSWORD) \
                  VALUES ('%s','%s')" % (account, password));
            new = sqlite3.connect('/home/nero/PycharmProjects/userinfo/%s.db' % account)
            N = new.cursor()
            N.execute('''CREATE TABLE OWE
                  ( ID INT PRIMARY KEY     NOT NULL,
                    BOOKNAME     TEXT  NOT NULL,
                    AUTHORNAME    TEXT  NOT NULL,
                    PRESSNAME   TEXT  NOT NULL,
                    RETURNTIME   TEXT  NOT NULL,
                    STATUS        TEXT NOT NULL);''')
            new.commit()
            new.close()
            conn.commit()
            conn.close()
            self.destroy()
            app=better.window('%s'%account)
            app.mainloop()
            return
        else:
            tkinter.messagebox.showinfo('message', 'Account has already been used!')
            conn.commit()
            conn.close()
            return
        return

