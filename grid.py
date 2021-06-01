from tkinter import *
colourlist=["green","red","blue","orange","purple","yellow","grey","black","white"]
plus=0
plus2=0
plus3=0

plus4=0
plus5=0
plus6=0

plus7=0
plus8=0
plus9=0
def changecolour1(plus):
    button1=Button(root,relief="ridge",bg=colourlist[plus],fg="grey",height=5,width=10,command=lambda:changecolour1(plus)).grid(row=0,column=0)
    if plus>=8:
        plus=0
    plus+=1
def changecolour2(plus2):
    button2=Button(root,relief="ridge",bg=colourlist[plus2],fg="grey",height=5,width=10,command=lambda:changecolour2(plus2)).grid(row=0,column=1)
    if plus2>=8:
        plus2=0
    plus2+=1
def changecolour3(plus3):
    button3=Button(root,relief="ridge",bg=colourlist[plus3],fg="grey",height=5,width=10,command=lambda:changecolour3(plus3)).grid(row=0,column=2)
    if plus3>=8:
        plus3=0
    plus3+=1

def changecolour4(plus4):
    button4=Button(root,relief="ridge",bg=colourlist[plus4],fg="grey",height=5,width=10,command=lambda:changecolour4(plus4)).grid(row=1,column=0)
    if plus4>=8:
        plus4=0
    plus4+=1
def changecolour5(plus5):
    button5=Button(root,relief="ridge",bg=colourlist[plus5],fg="grey",height=5,width=10,command=lambda:changecolour5(plus5)).grid(row=1,column=1)
    if plus5>=8:
        plus5=0
    plus5+=1
def changecolour6(plus6):
    button6=Button(root,relief="ridge",bg=colourlist[plus6],fg="grey",height=5,width=10,command=lambda:changecolour6(plus6)).grid(row=1,column=2)
    if plus6>=8:
        plus6=0
    plus6+=1

def changecolour7(plus7):
    button7=Button(root,relief="ridge",bg=colourlist[plus7],fg="grey",height=5,width=10,command=lambda:changecolour7(plus7)).grid(row=2,column=0)
    if plus7>=8:
        plus7=0
    plus7+=1
def changecolour8(plus8):
    button8=Button(root,relief="ridge",bg=colourlist[plus8],fg="grey",height=5,width=10,command=lambda:changecolour8(plus8)).grid(row=2,column=1)
    if plus8>=8:
        plus8=0
    plus8+=1
def changecolour9(plus9):
    button9=Button(root,relief="ridge",bg=colourlist[plus9],fg="grey",height=5,width=10,command=lambda:changecolour9(plus9)).grid(row=2,column=2)
    if plus9>=8:
        plus9=0
    plus9+=1

root=Tk()
button1=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour1(plus)).grid(row=0,column=0)
button2=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour2(plus2)).grid(row=0,column=1)
button3=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour3(plus3)).grid(row=0,column=2)

button4=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour4(plus4)).grid(row=1,column=0)
button5=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour5(plus5)).grid(row=1,column=1)
button6=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour6(plus6)).grid(row=1,column=2)

button7=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour7(plus7)).grid(row=2,column=0)
button8=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour8(plus8)).grid(row=2,column=1)
button9=Button(root,relief="ridge",bg="white",fg="grey",height=5,width=10,command=lambda:changecolour9(plus9)).grid(row=2,column=2)

root.mainloop()