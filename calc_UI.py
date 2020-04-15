#Proyecto Parte 1 - Calculadora con interfaz gráfica
#MIGUEL ANGEL CONDORI QUISPE
#tkinter
import tkinter as tk
from tkinter import*
root = tk.Tk()
sw = True
Operacion = tk.StringVar()
sen = ''
op = ""
vec_op = ('', '+', '-','*','/')
num = (0,1,2,3,4,5,6,7,8,9)
a = ''
i = 0
msj = tk.StringVar()

def clickbut(number):
     global op
     global sen
     global sw
     global a,i
     if number in num:
            op = op + str(number)
            msj.set(op)
     print(sw)
     if number == '+' and sw: #and not(op[len(op)-1] in vec_op):
            op = op + str(number)
            msj.set(op)
            sen = 's'
            i = int(len(op) - 1)
            a = int(op[0:i])
            sw = False
     elif number == '-' and sw: #and not(op[len(op)-1] in vec_op):
            op = op + str(number)
            msj.set(op)
            sen = 'r'
            i = int(len(op) - 1)
            a = int(op[0:i])
            sw = False
     elif number == '*' and sw: #and not(op[len(op)-1] in vec_op):
            op = op + str(number)
            msj.set(op)
            sen = 'm'
            i = int(len(op) - 1)
            a = int(op[0:i])
            sw = False
     elif number == '/' and sw: #and not(op[len(op)-1] in vec_op):
            op = op + str(number)
            msj.set(op)
            sen = 'd'
            i = int(len(op) - 1)
            a = int(op[0:i])
            sw = False
     if number == "AC":
        msj.set("")
        op = ""
        sw = True
     elif number == '=' and not(op[len(op)-1] in vec_op):
        if sen == 's':
            print("aqui")
            print(op)
            print("i",i)
            print(op[i+1:len(op)])
            print("Hola",type(op[i:len(op) - 1]))
            res = a + int(op[i+1:len(op)])
            ress = str(res)
        if sen == 'r':
            res = a - int(op[i+1:len(op)])
            ress = str(res)
        if sen == 'm':
            res = a * int(op[i+1:len(op)])
            ress = str(res)
        if sen == 'd':
            res = a / int(op[i+1:len(op)])
            ress = str(res)
        msj.set(ress)
        op = ress
        sw = True

root.geometry('320x400')
root.title('Calculadora')

root.configure(bg="#900C3F")
root.attributes('-alpha', 0.8)

tk.Label(root, text='Calculadora', bg="#900C3F", fg='white', font=('Courier', 24)).place(x=50, y=8)

tk.Label(root, textvariable=msj, bg="white", fg='black', font=('Courier', 24)).place(x=10, y=50)

#Números
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold')).place(x=10,y=100)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold')).place(x=10,y=170)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold')).place(x=10,y=240)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold')).place(x=75,y=100)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold')).place(x=75,y=170)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold')).place(x=75,y=240)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold')).place(x=140,y=100)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold')).place(x=140,y=170)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold')).place(x=140,y=240)
#operaciones
tk.Button(root,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold')).place(x=205,y=100)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold')).place(x=205,y=170)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold')).place(x=205,y=240)
tk.Button(root,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold')).place(x=205,y=310)
tk.Button(root,padx=46,pady=14,bd=4,bg='white',text="=",command=lambda:clickbut("="),font=("Courier New",16,'bold')).place(x=10,y=310)
#AC
tk.Button(root,padx=7,pady=14,bd=4,bg='white',text="AC",command=lambda:clickbut("AC"),font=("Courier New",16,'bold')).place(x=140,y=310)

root.mainloop()