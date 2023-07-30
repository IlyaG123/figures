from tkinter import*
import time
def click():
    root["bg"]="yellow"
    btn.configure(bg="green")
def click2():
    root["bg"]="blue"
    btm.configure(bg="pink")
def click3():
    btn.destroy()
root=Tk()
root.title("window")
root.geometry("500x500")
root["bg"]="black"
btn=Button(root,bg="red",text="click",font=("Arial",20,"bold"),command=click3)
btn.pack()
btm=Button(root,text="s",font=("Arial",40,"bold"),command=click2)
btm.pack()

def click4():
    btm1.destroy()
root=Tk()
root.title("window")
root.geometry("500x500")
root["bg"]="black"
btn1=Button(root,bg="green",text="Да")
btn1.pack()
btm1=Button(root,bg="red",text="Нет",command=click4)
btm1.pack()
lbl=Label(root,bg="blue",text="Вы любите читать ?")
lbl.place(x=85,y=60,width=300,height=150)

root=Tk()
canvas=Canvas(bg="yellow",width=750,height=550)
canvas.pack()
canvas.create_line(0,0,750,550)
canvas.create_rectangle(250,100,345,150,fill="black",outline="red",width="4",activefill="white")
canvas.create_oval(50,500,150,540)
canvas.create_polygon(10,150,40,100,70,150)

root=Tk()
root.title("window")
root.geometry("500x500")
root["bg"]="black"
canvas=Canvas(bg="white",width=750,height=550)
canvas.pack()
canvas.create_oval(200,200,100,100)
canvas.create_oval(200,200,100,300)
canvas.create_oval(200,300,100,400)
canvas.create_oval(150,60,120,100,fill="black")
canvas.create_oval(110,110,90,90,fill="black")

root=Tk()
canvas=Canvas()
canvas.pack()
canvas.create_polygon(150,20,220,150,100,150,fill="green")
canvas.create_polygon(160,50,220,220,100,220,fill="green")
canvas.create_polygon(180,100,220,270,100,260,fill="green")
a=canvas.create_oval(170,80,150,100,fill="blue")
b=canvas.create_oval(190,100,170,120,fill="yellow")
c=canvas.create_oval(140,180,170,150,fill="pink")
d=canvas.create_oval(120,150,150,120,fill="red")
canvas.create_line(123,160,200,300,width=4,fill="yellow")
canvas.create_line(123,260,200,150,width=4,fill="yellow")
while True:
    for i in range(10):
        canvas.move(a,3,-2)
        canvas.update()
        canvas.move(b,3,-2)
        canvas.update()
        time.sleep(0.05)
        canvas.move(a, -3, 2)
        canvas.update()
        canvas.move(b, -3, 2)
        canvas.update()
        time.sleep(0.05)
        canvas.move(c, 3, -2)
        canvas.update()
        canvas.move(d, 3, -2)
        canvas.update()
        time.sleep(0.05)
        canvas.move(c, -3, 2)
        canvas.update()
        canvas.move(d, -3, 2)
        canvas.update()
        time.sleep(0.05)




root.mainloop()
#
# def f(x, i):
#     x = int(str(x), i)
#     return x
# print(max(int(str(38), 16), int(str(75), 8), int(str(110100), 2)))