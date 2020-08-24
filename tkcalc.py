from tkinter import *
calc=Tk()
calc.title("CALCULATOR")
calc.geometry("200x300")
# num=IntVar
tb=Entry(calc,width=30)
tb.grid(row=0,column=0,columnspan=4,padx=2,pady=15,ipady=8)
n=1
for i in range(1,4):
    for j in range(0,3):
        b=Button(calc,text=str(n))
        b.grid(row=i,column=j,ipadx=10,ipady=7,pady=5,padx=5)
        n+=1
b0=Button(calc,text=0)
b0.grid(row=4,column=0,ipadx=10,ipady=7,pady=5,padx=5)
bf=Button(calc,text=".")
bf.grid(row=4,column=1,ipadx=10,ipady=7,pady=5,padx=5)
# def equ():
#     print(num.get())
be=Button(calc,text="=")
be.grid(row=4,column=2,ipadx=10,ipady=7,pady=5,padx=5)
bp=Button(calc,text="+")
bp.grid(row=1,column=3,ipadx=10,ipady=7,pady=5,padx=5)
bs=Button(calc,text="-")
bs.grid(row=2,column=3,ipadx=10,ipady=7,pady=5,padx=5)
bm=Button(calc,text="*")
bm.grid(row=3,column=3,ipadx=10,ipady=7,pady=5,padx=5)
bd=Button(calc,text="/")
bd.grid(row=4,column=3,ipadx=10,ipady=7,pady=5,padx=5)
calc.mainloop()