import tkinter
from tkinter import*

c=Tk()
c.title('calculator')
c.geometry('340x415')
c.configure(bg="midnight blue")

equation=""
def show(value):
    global equation
    equation+=value
    lab_result.config(text=equation)

def clear():
    global equation
    equation=""
    lab_result.config(text=equation)

def calculate():
    global equation
    result= ""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    lab_result.config(text=result)

    

lab_result=Label(c,width=14,height=2,text="",font=('arial',30),fg='white',bg='MediumOrchid4')
lab_result.place(x=0,y=0)

b1=Button(c,text='C',width=5,height=1,font=('arial,32'),bd=5,fg="white",bg='green3',command=lambda:clear())
b1.place(x=10,y=100)

b2=Button(c,text='()',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show('()'))
b2.place(x=90,y=100)

b3=Button(c,text='%',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show('%'))
b3.place(x=170,y=100)

b4=Button(c,text='/',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show('/'))
b4.place(x=250,y=100)

b5=Button(c,text='7',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("7"))
b5.place(x=10,y=160)

b6=Button(c,text='8',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("8"))
b6.place(x=90,y=160)

b7=Button(c,text='9',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("9"))
b7.place(x=170,y=160)

b8=Button(c,text='*',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show("*"))
b8.place(x=250,y=160)

b9=Button(c,text='4',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("4"))
b9.place(x=10,y=220)

b10=Button(c,text='5',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("5"))
b10.place(x=90,y=220)

b11=Button(c,text='6',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("6"))
b11.place(x=170,y=220)

b12=Button(c,text='-',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show("-"))
b12.place(x=250,y=220)

b13=Button(c,text='1',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("1"))
b13.place(x=10,y=280)

b14=Button(c,text='2',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("2"))
b14.place(x=90,y=280)

b15=Button(c,text='3',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("3"))
b15.place(x=170,y=280)

b16=Button(c,text='+',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show("+"))


b16.place(x=250,y=280)
b17=Button(c,text='0',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='steel blue',command=lambda:show("0"))
b17.place(x=10,y=340)

b18=Button(c,text="()",width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:clear("()"))
b18.place(x=90,y=340)

b19=Button(c,text='.',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='light sea green',command=lambda:show("."))
b19.place(x=170,y=340)

b1=Button(c,text='=',width=5,height=1,font=('arial,30'),bd=5,fg="white",bg='forest green',command=lambda:calculate())
b1.place(x=250,y=340)


c.mainloop()