import sqlite3
import tkinter as tk
import tkinter.messagebox
import time

class insert(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('insertbook')
        self.geometry('300x150')

        self.booknamelab=tk.Label(self,text="书名:")
        self.booknamelab.place(x=1,y=1,anchor='nw')
        self.authornamelab = tk.Label(self, text="著者名:")
        self.authornamelab.place(x=1, y=20, anchor='nw')
        self.pressnamelab = tk.Label(self, text="出版社:")
        self.pressnamelab.place(x=1, y=40, anchor='nw')
        self.bookname = tk.Entry(self)
        self.bookname.place(x=80, y=1, anchor='nw')
        self.authorname = tk.Entry(self)
        self.authorname.place(x=80, y=20, anchor='nw')
        self.pressname = tk.Entry(self)
        self.pressname.place(x=80, y=40, anchor='nw')
        self.insert = tk.Button(self, text="insert",relief='raised', command=self.insertbook)
        self.insert.place(x=80, y=70, anchor='nw')

    def insertbook(self):
        bookname = self.bookname.get() or None
        authorname = self.authorname.get() or None
        pressname = self.pressname.get() or None
        #localtime = time.asctime(time.localtime(time.time()))
        if bookname == None or authorname == None or pressname == None:
            return
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS FROM BOOKINFO ORDER BY ID ASC")
        id = 1
        for row in cursor:
            if row[0] != id:
                break
            id = id + 1
        c.execute("INSERT INTO BOOKINFO (ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,BORROWTIME,INSERTTIME) \
              VALUES (%d,'%s','%s','%s','可借',0,%f)" % (id, bookname, authorname, pressname, time.time()))
        tkinter.messagebox.showinfo('message', 'Success!')
        conn.commit()
        conn.close()
        self.destroy()
        return

#app=insert()
#app.mainloop()
