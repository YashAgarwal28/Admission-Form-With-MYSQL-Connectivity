
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def show():
    name=fname.get()

    father=ffather.get()

    mother=fmother.get()

    dob=fdob.get()

    gender=var.get()
    if(gender==1):
        gender= "Male"

    if(gender==2):
        gender= "Female"

    rel1=var1.get()
    rel2=var2.get()
    rel3=var3.get()
    rel4=var4.get()

    if(rel1==0 and rel2==0 and rel3==0 and rel4==0):
        religion=" "
    if(rel1==1 and rel2==0 and rel3==0 and rel4==0):
        religion=" HINDU "
    if(rel1==0 and rel2==1 and rel3==0 and rel4==0):
        religion=" CHRISTIAN "
    if(rel1==0 and rel2==0 and rel3==1 and rel4==0):
        religion=" MUSLIM "
    if(rel1==0 and rel2==0 and rel3==0 and rel4==1):
            religion=" PUNJABI "


    cas1=var5.get()
    cas2=var6.get()
    cas3=var7.get()
    cas4=var8.get()

    if(cas1==0 and cas2==0 and cas3==0 and cas4==0):
       caste=" "
    if(cas1==1 and cas2==0 and cas3==0 and cas4==0):
        caste=" SC "
    if(cas1==0 and cas2==1 and cas3==0 and cas4==0):
        caste=" ST "
    if(cas1==0 and cas2==0 and cas3==1 and cas4==0):
        caste=" OBC "
    if(cas1==0 and cas2==0 and cas3==0 and cas4==1):
        caste=" GEN "



    address=faddr.get()
    localguardian=flg.get()
    home=fhome.get()
    own=fown.get()
    nat=fnation.get()


    gr1=var9.get()
    gr2=var10.get()
    gr3=var11.get()
    if(gr1==0 and gr2==0 and gr3==0):
       subject=" "
    if(gr1==1 and gr2==0 and gr3==0):
        subject=" SCIENCE "
    if(gr1==0 and gr2==1 and gr3==0):
        subject=" ARTS "
    if(gr1==0 and gr2==0 and gr3==1):
        subject=" COMMERCE "

    con = mysql.connector.connect(
        host=" localhost ", user="root", password="", database="admission_form")
    cursor=con.cursor()

    sql="insert into candidate(Name_Of_Candidate , Father_Name , Mother_Name , Date_Of_Birth, Gender , Religion , Caste , Address , Local_Guardian , Home_No , Own_No , Nationality , Subject)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    info=[name,father,mother,dob,gender,religion,caste,address,localguardian,home,own,nat,subject]

    cursor.execute(sql,info)
    con.commit()

    messagebox.showinfo("Message","Registered Successfully \n Thank You")

    con.close()



frame=Tk()

ladd=Label(text="ADMISSION FORM",font=("Verdana Bold",20))
ladd.place(x=550,y=10)


ldate=Label(text="Date________________",font=("Bold",10))
ldate.place(x=5,y=10)

lform=Label(text="Form No_____________",font=("Bold",10))
lform.place(x=5,y=40)

laddm=Label(text="Admission No_________________",font=("Bold",10))
laddm.place(x=5,y=70)

lstud=Label(text="STUDENT'S PROFILE:",font=("Verdana Bold",15))
lstud.place(x=5,y=120)

lname=Label(text="Name of Candidate(In Capital Letters)",font=("Bold",12))
lname.place(x=5,y=155)
fname=Entry(width=80,font=("verdana bold",10))
fname.place(x=275,y=155)

lfather=Label(text="Father's Name(In Capital Letters)",font=("Bold",12))
lfather.place(x=5,y=190)
ffather=Entry(width=80,font=("verdana bold",10))
ffather.place(x=275,y=190)

lmother=Label(text="Mother's Name(In Capital Letters)",font=("Bold",12))
lmother.place(x=5,y=225)
fmother=Entry(width=80,font=("verdana bold",10))
fmother.place(x=275,y=225)

ldob=Label(text="Date Of Birth(DD-MM-YYY)",font=("Bold",12))
ldob.place(x=5,y=260)
fdob=Entry(width=80,font=("verdana bold",10))
fdob.place(x=275,y=260)

lgender=Label(text="Gender",font=("Bold",12))
lgender.place(x=5,y=295)

var=IntVar()

bmale=Radiobutton(text="Male",font=("georgia Bold Italic",12),value=1,variable=var,)
bfemale=Radiobutton(text="Female",font=("georgia Bold Italic",12),value=2,variable=var)
bmale.place(x=275,y=295)
bfemale.place(x=375,y=295)



lreligion=Label(text="Religion",font=("Bold",12))
lreligion.place(x=5,y=330)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

bhindu=Checkbutton(text="Hindu",font=("calibri Bold",13),variable=var1)

bchristian=Checkbutton(text="Christian",font=("calibri Bold",13),variable=var2)

bmuslim=Checkbutton(text="Muslim",font=("calibri Bold",13),variable=var3)

bpunjabi=Checkbutton(text="Punjabi",font=("calibri Bold",13),variable=var4)


l=Label(text="(Put Tick Mark Only One)",fg="red",font=("verdana Bold",11))
l.place(x=795,y=330)

bhindu.place(x=275,y=330)
bchristian.place(x=395,y=330)
bmuslim.place(x=540,y=330)
bpunjabi.place(x=685,y=330)


lcaste=Label(text="Caste",font=("Bold",12))
lcaste.place(x=5,y=365)

var5=IntVar()
bsc=Checkbutton(text="SC",font=("calibri Bold",13),variable=var5)
bsc.place(x=275,y=365)

var6=IntVar()
bst=Checkbutton(text="ST",font=("calibri Bold",13),variable=var6)
bst.place(x=395,y=365)

var7=IntVar()
bobc=Checkbutton(text="OBC",font=("calibri Bold",13),variable=var7)
bobc.place(x=540,y=365)

var8=IntVar()
bgen=Checkbutton(text="GEN",font=("calibri Bold",13),variable=var8)
bgen.place(x=685,y=365)


l=Label(text="(Put Tick Mark Only One)",fg="red",font=("verdana Bold",11))
l.place(x=795,y=365)

laddr=Label(text="Address",font=("Bold",12))
laddr.place(x=5,y=400)
faddr=Entry(width=150,font=("verdana bold",10))
faddr.place(x=275,y=400)


llg=Label(text="Local Guardian",font=("Bold",12))
llg.place(x=5,y=435)
flg=Entry(width=110,font=("verdana bold",10))
flg.place(x=275,y=435)

lmobile=Label(text="Mobile Number",font=("Bold",12))
lmobile.place(x=5,y=470)

lhome=Label(text="Home:",font=("Bold",12))
lhome.place(x=215,y=470)
fhome=Entry(font=("verdana bold",10))
fhome.place(x=275,y=470)

lown=Label(text="Own:",font=("Bold",12))
lown.place(x=428,y=470)
fown=Entry(font=("verdana bold",10))
fown.place(x=475,y=470)

lnation=Label(text="Nationality",font=("Bold",12))
lnation.place(x=5,y=505)
fnation=Entry(width=110,font=("verdana bold",10))
fnation.place(x=275,y=505)

lsubject=Label(text="Subject",font=("Bold",12))
lsubject.place(x=5,y=540)


var9=IntVar()
var10=IntVar()
var11=IntVar()

bscience=Checkbutton(text="Science",font=("calibri Bold",13),variable=var9)
bart=Checkbutton(text="Arts",font=("calibri Bold",13),variable=var10)
bbuss=Checkbutton(text="Commerce",font=("calibri Bold",13),variable=var11)

l=Label(text="(Put Tick Mark Only One)",fg="red",font=("verdana Bold",11))
l.place(x=695,y=540)

bscience.place(x=275,y=540)
bart.place(x=395,y=540)
bbuss.place(x=475,y=540)



l=Label(text="Signature Of Student:",font=("verdana Bold",12),fg="dark green")
l.place(x=5,y=600)
l=Label(text="____________________",font=("verdana Bold",12))
l.place(x=5,y=655)

l=Label(text="Signature Of Office Assistant:",font=("verdana bold",12),fg="dark green")
l.place(x=525,y=600)
l=Label(text="____________________",font=("verdana Bold",12))
l.place(x=525,y=655)

l=Label(text="Signature Of Headmaster:",font=("verdana Bold",12),fg="dark green")
l.place(x=1050,y=600)
l=Label(text="____________________",font=("verdana Bold",12))
l.place(x=1050,y=655)

bsub=Button(text="SUBMIT FORM",font=("verdana Bold",20),bg="White",fg="dark green",command=show)
bsub.place(x=1000,y=80)
lclick=Label(text="Click Here^",fg="red",font=("verdana bold",9))
lclick.place(x=1080,y=139)

scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)


frame.geometry("1250x550")
frame.title("www.admissionform.com")
frame.configure(bg="white")
frame.mainloop()
