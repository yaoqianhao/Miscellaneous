import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import sqlite3
import time
import random
from xpinyin import Pinyin
import tkinter.messagebox
import log_in
import sign_up
import _insert

p=Pinyin()

def partition2(a, l, r, num):
    #print(num)
    #print(a[l][0])
    x = p.get_pinyin(str(a[l][num]), '')
    j = l
    for i in range(l + 1, r + 1):
        if p.get_pinyin(str(a[i][num]), '') <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r, num):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r, num)
    randomized_quick_sort(a, l, m - 1, num)
    randomized_quick_sort(a, m + 1, r, num)

class window(tk.Tk):
    def __init__(self,account):
        super().__init__()
        self.tran = {}
        self.tran['书名'] = 'BOOKNAME'
        self.tran['著者名'] = 'AUTHORNAME'
        self.tran['出版社'] = 'PRESSNAME'
        self.account = account
        self.sw=0
        self.geometry('950x500')
        self.title('智能图书管理系统%s'%self.account)

        image = Image.open("/home/nero/PycharmProjects/lib4.jpg")
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self,image=photo)
        self.label.image = photo  # keep a reference!
        self.label.pack()


        self.searchname = tk.Entry(self)
        self.searchname.place(x=30, y=35, anchor='nw')
        self.method = tk.StringVar()
        self.selectmethod = ttk.Combobox(self, textvariable=self.method)
        self.selectmethod['values'] = ('书名', '著者名', '出版社')
        self.selectmethod.place(x=180, y=35, anchor='nw')
        self.selectmethod.current(0)
        self.searchbutton = tk.Button(self, text="搜索",width=21,height=5,background='white',command=self.search_book)
        self.searchbutton.place(x=70, y=70, anchor='nw')

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.place(x=880,y=35,relheight =0.85,anchor='nw')

        self.listbox = tk.Listbox(self,width=75,height=22,yscrollcommand=self.scrollbar.set)
        self.listbox.place(x=350,y=35,anchor='nw')
        self.scrollbar.config(command=self.listbox.yview)

        self.menubar = tk.Menu(self,background='white')
        self.menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='选择', menu=self.menu)
        self.menu.add_command(label='登录', command=self.login)
        self.menu.add_command(label='注册', command=self.signup)
        self.config(menu=self.menubar)

        self.swid=tk.Button(self,text="ID",width=2,height=1,background='white',command=self.setswid)
        self.swid.place(x=350,y=5,anchor='nw')
        self.swbookname = tk.Button(self, text="书名", width=2, height=1, background='white', command=self.setswbookname)
        self.swbookname.place(x=430, y=5, anchor='nw')
        self.swauthorname = tk.Button(self, text="著者名", width=2, height=1, background='white', command=self.setswauthorname)
        self.swauthorname.place(x=510, y=5, anchor='nw')
        self.swpressname = tk.Button(self, text="出版社", width=2, height=1, background='white', command=self.setswpressname)
        self.swpressname.place(x=590, y=5, anchor='nw')
        self.swhot = tk.Button(self, text="借阅次数", width=3, height=1, background='white',
                                command=self.setswhot)
        self.swhot.place(x=670, y=5, anchor='nw')

        if self.account=='ADMIN':
            self.inbook=tk.Button(self,text="入库",width=3,height=3,background='white',command=self.in_book)
            self.inbook.place(x=100,y=225,anchor='nw')
            self.outbook=tk.Button(self,text="出库",width=3,height=3,background='white',command=self.out_book)
            self.outbook.place(x=140, y=325, anchor='nw')
            self.infromfile=tk.Button(self,text="从文件",width=3,height=3,background='white',
                                      command=self.in_fromfile)
            self.infromfile.place(x=190,y=225,anchor='nw')
            self.outfromfile = tk.Button(self, text="从文件", width=3, height=3, background='white',
                                        command=self.out_fromfile)
            self.outfromfile.place(x=230, y=325, anchor='nw')
            self.swtime = tk.Button(self, text="入库时间", width=3, height=1, background='white',
                                         command=self.setswtime)
            self.swtime.place(x=770, y=5, anchor='nw')

        elif self.account!='':
            self.owesb = tk.Scrollbar(self)
            self.owesb.place(x=30, y=458, relheight=0.026,relwidth=0.3, anchor='nw')
            self.owelb = tk.Listbox(self, width=40, height=11,xscrollcommand=self.owesb.set)
            self.owelb.place(x=30, y=245, anchor='nw')
            self.owesb.config(orient='horizontal',command=self.owelb.xview)
            self.showowe()
            self.borrowbutton=tk.Button(self,text="借",width=1,height=1,background='white',command=self.borrowbook)
            self.borrowbutton.place(x=70,y=190,anchor='nw')
            self.returnbutton = tk.Button(self, text="还",width=1,height=1,background='white',command=self.returnbook)
            self.returnbutton.place(x=140, y=190, anchor='nw')
            self.renewbutton = tk.Button(self, text="续借", width=1,height=1,background='white',command=self.renewbook)
            self.renewbutton.place(x=210, y=190, anchor='nw')
            self.getcnt()

    def setswid(self):
        self.sw=0
        self.search_book()

    def setswbookname(self):
        self.sw=1
        self.search_book()

    def setswauthorname(self):
        self.sw=2
        self.search_book()

    def setswpressname(self):
        self.sw=3
        self.search_book()

    def setswhot(self):
        self.sw=5
        self.search_book()

    def setswtime(self):
        self.sw=6
        self.search_book()

    def login(self):
        self.destroy()
        app=log_in.login()
        app.mainloop()
        return

    def signup(self):
        self.destroy()
        app=sign_up.signup()
        app.mainloop()
        return

    def in_book(self):
        app=_insert.insert()
        app.mainloop()
        return

    def in_fromfile(self):
        f = open('/home/nero/PycharmProjects/inbook.txt', 'r')
        lines = f.readlines()
        f.close()
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        for i in lines:
            l=i.split()
            id=1
            cursor = c.execute("SELECT ID FROM BOOKINFO")
            for row in cursor:
                if row[0] != id:
                    break
                id = id + 1
            #print(id)
            #localtime = time.asctime(time.localtime(time.time()))
            c.execute("INSERT INTO BOOKINFO (ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,BORROWTIME,INSERTTIME) \
                          VALUES (%d,'%s','%s','%s','可借',0,%f)" % (id, l[0], l[1], l[2], time.time()))
        conn.commit()
        conn.close()
        self.search_book()
        tkinter.messagebox.showinfo('message', 'Success!')

    def out_book(self):
        fail=()
        if self.listbox.curselection()==fail:
            return
        value = self.listbox.get(self.listbox.curselection())
        id = 0
        i = 0
        while value[i] != ' ':
            id = id * 10 + int(value[i])
            i = i + 1
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        cursor = c.execute("SELECT STATUS FROM BOOKINFO WHERE ID = %d" % id)
        status = None
        for row in cursor:
            status = row[0]
        if status=='可借':
            c.execute("DELETE FROM BOOKINFO WHERE ID=%d"%id)
            conn.commit()
            conn.close()
            self.search_book()
            tkinter.messagebox.showinfo('message', 'Success!')
        else:
            conn.close()
            tkinter.messagebox.showinfo('message', 'The book is rent!')

    def out_fromfile(self):
        f = open('/home/nero/PycharmProjects/inbook.txt', 'r')
        lines = f.readlines()
        f.close()
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        for i in lines:
            l = i.split()
            c.execute("DELETE FROM BOOKINFO WHERE BOOKNAME = '%s' AND AUTHORNAME = '%s' AND PRESSNAME='%s'"%(l[0],l[1],l[2]))
        conn.commit()
        conn.close()
        self.search_book()
        tkinter.messagebox.showinfo('message', 'Success!')

    def search_book(self):
        searchname = self.searchname.get() or None
        if searchname == None:
            if self.account=='ADMIN':
                conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
                c = conn.cursor()
                if self.sw!=5:
                    cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,BORROWTIME,INSERTTIME FROM BOOKINFO ORDER BY ID ASC")
                else:
                    cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,BORROWTIME,INSERTTIME FROM BOOKINFO ORDER BY BORROWTIME DESC")
                output=[]
                for row in cursor:
                    output.append(row)
                conn.close()
                # print(output)
                if self.sw!=0 and self.sw!=5:
                    self.mysort(output)
                self.listbox.delete('0', 'end')
                for item in output:
                    self.listbox.insert('end', str(item[0])+' '+item[1]+' '+item[2]+' '+item[3]+' '+item[4]+' '+str(item[5])+' '+time.asctime(time.localtime(item[6])))
            return
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        # print("SELECT BOOKNAME,AUTHORNAME,PRESSNAME,STATUS  from BOOKINFO WHERE %s LIKE '%%%s%%'"%(str.upper(method.get()),searchname))
        cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,BORROWTIME,INSERTTIME FROM BOOKINFO WHERE %s LIKE '%%%s%%' ORDER BY ID ASC" % (self.tran[self.method.get()], searchname))
        output = []
        for row in cursor:
            output.append(row)
        conn.close()
        # print(output)
        if self.sw!=0:
            self.mysort(output)
        self.listbox.delete('0','end')
        for item in output:
            if self.account=='ADMIN':
                self.listbox.insert('end', str(item[0])+' '+item[1]+' '+item[2]+' '+item[3]+' '+item[4]+' '+str(item[5])+' '+time.asctime(time.localtime(item[6])))
            else:
                self.listbox.insert('end', str(item[0]) + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + ' ' + item[4]+' '+str(item[5]))

    def showowe(self):
        conn = sqlite3.connect("/home/nero/PycharmProjects/userinfo/%s.db" % self.account)
        c = conn.cursor()
        cursor = c.execute("SELECT ID,BOOKNAME,AUTHORNAME,PRESSNAME,RETURNTIME,STATUS FROM OWE ORDER BY ID ASC")
        owe = []
        for row in cursor:
            owe.append('%d %s %s %s %s %s' % (
            row[0], row[1], row[2], row[3], time.asctime(time.localtime(float(row[4]))), row[5]))
        conn.close()
        self.owelb.delete('0', 'end')
        for item in owe:
            self.owelb.insert('end', item)

    def borrowbook(self):
        fail = ()
        if self.listbox.curselection() == fail:
            return
        self.getcnt()
        if self.cnt==10:
            tkinter.messagebox.showinfo('message', '不能再借了!')
            return
        value = self.listbox.get(self.listbox.curselection())
        id=0
        i=0
        while value[i]!=' ':
            id = id*10+int(value[i])
            i=i+1
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        cursor = c.execute("SELECT BOOKNAME,AUTHORNAME,PRESSNAME,STATUS,BORROWTIME FROM BOOKINFO WHERE ID=%d" % id)
        needstatus = None
        needbookname = None
        needauthorname = None
        needpressname = None
        borrowtime=None
        for row in cursor:
            needbookname = row[0]
            needauthorname = row[1]
            needpressname = row[2]
            needstatus = row[3]
            borrowtime=row[4]
        if needstatus == '可借':
            c.execute("UPDATE BOOKINFO SET STATUS = '不可借',BORROWTIME=%d WHERE ID=%d" % (borrowtime+1,id))
            conn.commit()
            conn.close()
            timel = time.time()
            timel = timel + 60 * 60 * 24 * 30  # 30days
            conn = sqlite3.connect("/home/nero/PycharmProjects/userinfo/%s.db" % self.account)
            c = conn.cursor()
            c.execute("INSERT INTO OWE (ID,BOOKNAME,AUTHORNAME,PRESSNAME,RETURNTIME,STATUS) \
                                      VALUES (%d,'%s','%s','%s','%s','%s')" % (
            id, needbookname, needauthorname, needpressname, str(timel), '可续借'))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo('message', 'Success!')
            self.search_book()
            self.showowe()
        else:
            conn.close()
            tkinter.messagebox.showinfo('message', '这本书已经被借走了!')
        return

    def returnbook(self):
        fail = ()
        if self.owelb.curselection() == fail:
            return
        value = self.owelb.get(self.owelb.curselection())
        id = 0
        i = 0
        while value[i] != ' ':
            id = id * 10 + int(value[i])
            i = i + 1
        conn = sqlite3.connect("/home/nero/PycharmProjects/userinfo/%s.db" % self.account)
        c = conn.cursor()
        c.execute("DELETE FROM OWE WHERE ID=%d" % id)
        conn.commit()
        conn.close()
        conn = sqlite3.connect("/home/nero/PycharmProjects/book.db")
        c = conn.cursor()
        c.execute("UPDATE BOOKINFO SET STATUS = '可借' where ID=%d" % id)
        conn.commit()
        tkinter.messagebox.showinfo('message', 'Success!')
        self.search_book()
        self.showowe()

    def renewbook(self):
        fail = ()
        if self.owelb.curselection() == fail:
            return
        value = self.owelb.get(self.owelb.curselection())
        id = 0
        i = 0
        while value[i] != ' ':
            id = id * 10 + int(value[i])
            i = i + 1
        print(id)
        conn = sqlite3.connect("/home/nero/PycharmProjects/userinfo/%s.db" % self.account)
        c = conn.cursor()
        cursor = c.execute("SELECT ID,RETURNTIME,STATUS FROM OWE WHERE ID = %d"%id)
        for row in cursor:
            print(row)
            if row[2] == '可续借':
                c.execute("UPDATE OWE SET RETURNTIME='%s',STATUS = '不可续借' WHERE ID = %d" % (
                str(float(row[1]) + 60 * 60 * 24 * 30), id))
                tkinter.messagebox.showinfo('message', 'Success!')
            else:
                tkinter.messagebox.showinfo('message', '不能再续了!')

        conn.commit()
        conn.close()
        self.search_book()
        self.showowe()

    def mysort(self,a):
       randomized_quick_sort(a,0,len(a)-1,self.sw)

    def getcnt(self):
        conn = sqlite3.connect("/home/nero/PycharmProjects/userinfo/%s.db" % self.account)
        c = conn.cursor()
        cursor = c.execute("SELECT ID FROM OWE ")
        self.cnt=0
        for row in cursor:
            self.cnt=self.cnt+1
        conn.commit()
        conn.close()
        return




