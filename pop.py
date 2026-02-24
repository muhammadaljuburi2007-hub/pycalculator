#!/bin/bash python3
import tkinter as tk 

##---------------OUTER DEFS --------##
def delete(seq,index) :
    end=''
    for i in seq :
        if i != seq[index] :
            end= end + i
    return end

#----main screen -----#cc



root = tk.Tk()
root.title("#--Calculator--#")
root.geometry("300x400")
#------- Label -------#
label = tk.Label(root,text ="0",) 
label.grid(row=0,column=1,padx=5,pady=15)

m1=0
m2=0
x=0

m="0"
#--------- Button -----#

def n1b():
    global m
    m = str(m) + '1'
    label.config(text= m ) 


def n2b():
    global m
    
    m = str(m) + '2'
    label.config(text= m )

def n3b():
    global m
    m = str(m) + '3'
    label.config(text= m )

def n4b():
    global m
    m = str(m) + '4'
    label.config(text= m )

def n5b():
    global m
    m = str(m) + '5'
    label.config(text= m )

def n6b():
    global m
    m = str(m) + '6'
    label.config(text=m)

def n7b():
    global m
    m = str(m) + '7'
    label.config(text= m )

def n8b():
    global m
    m = str(m) + '8'
    label.config(text= m )

def n9b():
    global m
    m = str(m) + '9'
    label.config(text= m )

def n0b():
    global m
    m = str(m) + '0'
    label.config(text= m )

def plusb() :
    global m
    global m1
    global x
    m1 = 0
    
    m = float(m)
    m1 = m1 + m
    m = ""
    label.config(text=m1)
    x=1

def minusb() :
    global m
    global m1
    global x
    m1 = 0
    m = float(m)
    m1 = m1 - m
    m = ""
    label.config(text=m1)
    x=2

def equb() :
    global m
    global m1
    global m2
    global x
    m = float(m)
    m2 = m
    if x == 1 :
        r = m1 + m2 
    elif x == 2 :
        r = m1 - m2
    elif x == 3 :
        r = m1 * m2
    elif x == 4 :
        r = m1 / m2
    else :
        r = m2
    r = str(r)
    label.config(text= r )

def multib() :
    global m
    global m1
    global x
    m = float(m)
    m1 = 1
    m1 = m1 * m
    m = ""
    label.config(text=m1)
    x=3

def dividb() :
    global m
    global m1
    global x
    m1 =1
    m = float(m)
    m1 =  m1 / m
    m = ""
    label.config(text=m1)
    x=4

def delb() :
    global m
    m = str(m)
    m = delete(m,-1)
    label.config(text=m)

def cb():
    global m
    m=""
    label.config(text = m)

def pointb():
    global m
    m = str(m) + '.'
    label.config(text=m)



n1 = tk.Button(root,text="1",command=n1b)
n2 = tk.Button(root,text="2",command=n2b)
n3 = tk.Button(root,text="3",command=n3b)
n4 = tk.Button(root,text="4",command=n4b)
n5 = tk.Button(root,text="5",command=n5b)
n6 = tk.Button(root,text="6",command=n6b)
n7 = tk.Button(root,text="7",command=n7b)
n8 = tk.Button(root,text="8",command=n8b)
n9 = tk.Button(root,text="9",command=n9b)
n0 = tk.Button(root,text="0",command=n0b)
plus = tk.Button(root,text="+",command=plusb)
minus=tk.Button(root,text="-",command=minusb)
equ = tk.Button(root,text="=",command=equb)
multi = tk.Button(root,text="x",command=multib)
divid=tk.Button(root,text="/",command=dividb)
_del = tk.Button(root,text="del",command=delb)
c = tk.Button(root,text="C",command=cb)
point=tk.Button(root,text=".",command=pointb)

label.bind("<1>",n1b)
label.bind("<2>",n2b)



n1.grid(row=1,column=0,padx=5,pady=5)
n2.grid(row=1,column=1,padx=5,pady=5)
n3.grid(row=1,column=2,padx=5,pady=5)
n4.grid(row=2,column=0,padx=5,pady=5)
n5.grid(row=2,column=1,padx=5,pady=5)
n6.grid(row=2,column=2,padx=5,pady=5)
n7.grid(row=3,column=0,padx=5,pady=5)
n8.grid(row=3,column=1,padx=5,pady=5)
n9.grid(row=3,column=2,padx=5,pady=5)
n0.grid(row=4,column=1,padx=5,pady=5)
c.grid(row=1,column=3,padx=5,pady=5)
_del.grid(row=2,column=3,padx=5,pady=5)
plus.grid(row=3,column=3,padx=5,pady=5)
multi.grid(row=1,column=4,padx=5,pady=5)
divid.grid(row=2,column=4,padx=5,pady=5)
point.grid(row=4,column=0,padx=5,pady=5)
equ.grid(row=4,column=2,padx=5,pady=5)
minus.grid(row=3,column=4,padx=5,pady=5)

#------- mainloop -------#
root.mainloop()
