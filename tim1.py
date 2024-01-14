import time
from playsound import playsound
from tkinter import *
root = Tk()
root.geometry('400x600+400+150')
root.config(bg='#000000')
root.title('timer')
image1 = PhotoImage(file='brush.png')
image2 = PhotoImage(file='eggs.png')
image3 = PhotoImage(file='face.png')
image4 = PhotoImage(file='picture.png')
image5 = PhotoImage(file='stop.png')

qwerty = Label(root, text='TIMER!', font='Arial 30 bold', bg='#000000', fg='#ea3548')
qwerty.pack(pady=10)
CURRENTtime = Label(root, font="Arial 15 bold", text='current time:', bg='papaya whip', fg='#000000')
CURRENTtime.place(x=65, y=70)
stop_flg = True


def clock():
    clock_time = time.strftime('%H:%M:%S')
    current.config(text=clock_time)
    current.after(ms=1000, func=clock)


def timer():
    times = int(hrs.get())*3600 + int(mns.get())*60 + int(scs.get())*1
    while times > -1:
        min, sec = (times//60, times % 60)
        hour = 0
        if min > 60:
            hour, min = (min//60, min % 60)
        if len(str(hour)) == 1:
            hour = '0' + str(hour)
        if len(str(min)) == 1:
            min = '0' + str(min)
        if len(str(sec)) == 1:
            sec = '0' + str(sec)

        scs.set(sec)
        mns.set(min)
        hrs.set(hour)
        root.update()
        time.sleep(1)
        if stop_flg == True:
            pass
            start.config(image=image4)
        elif stop_flg == False:
            times = -1
            start.config(image=image5)
            if times == 0:
                playsound('music.wav')
                scs.set('00')
                mns.set('00')
                hrs.set('00')


def eggs():
    hrs.set('00')
    mns.set('10')
    scs.set('00')


def face():
    hrs.set('00')
    mns.set('15')
    scs.set('00')


def teeth():
    hrs.set('00')
    mns.set('02')
    scs.set('00')


current = Label(root, font='Arial 15 bold', text='', bg='#ffffff', fg='#000000')
current.place(x=190, y=70)
clock()

hrs = StringVar()
mns = StringVar()
scs = StringVar()
Entry(root, textvariable=hrs, width=2, font='Arial 50', bg='#000000', fg='#ffffff', bd=0).place(x=30, y=155)
Entry(root, textvariable=mns, width=2, font='Arial 50', bg='#000000', fg='#ffffff', bd=0).place(x=150, y=155)
Entry(root, textvariable=scs, width=2, font='Arial 50', bg='#000000', fg='#ffffff', bd=0).place(x=270, y=155)
hrs.set('00')
mns.set('00')
scs.set('00')

start = Button(root, image=image4, bg='#000000', bd=0, command=timer)

eggs = Button(root, image=image2, bg='#000000', bd=0, command=eggs)
start.place(x=100, y=500)
eggs.place(x=30, y=300)
root.mainloop()
