from gettext import install
from pkgutil import get_data
from tkinter import * 
import tkinter as tk
import os
import time 
from tkinter.font import BOLD
#from PIL import Image,ImageTk
from functools import partial
from tkinter.ttk import Progressbar
from pytube import YouTube


window=tk.Tk()

window.geometry('1080x720')

window.resizable(True,True)

window.title("YouTubeVideoDownloader")

window.configure(bg="black")


img=PhotoImage(file=r"yt.png")
icon=PhotoImage(file=r"yt.png")

window.iconphoto(False,icon)

clicked =StringVar()
click=StringVar()

label_img=Label(image=img).place(x=225,y=90,height=120,width=125)


heading = tk.Label(window,text='YOUTUBE VIDEO DOWNLOADER',font='simsun 40 bold',fg="#f00",bg="black").place(x = 400,y =120)

font_style=("Comic Sans Ms",15,'bold')


label_paste = tk.Label(window ,text="Paste URL Here: ",font = font_style,bg ="black",fg="#fff").place(x=550,y=250)

user_password_entry_area = tk.Entry(window,width = 60,textvariable=click,fg="navy",font='tahoma 11').place(x = 420,y =325,height=40)
                                                   

# def common():
#     resolution()
#     progress() 

def resolution():
    
    qua=clicked.get()
    link = click.get()

    try:

      video=YouTube(link)

      size =video.length
      print(size)

      label_link_1.config(text=video.title)

      label_status.config(fg ="#0f0")

      label_finish.config(fg ="#0f0")

      finish.set("Downloading")

      video.streams.filter(progressive ="True",file_extension='mp4',res=qua).first().download()

      progress()

    except:
        label_finish.config(fg ="#f00")
        finish.set("Invalid Link")
        status.set(" ")
        label_link_1.config(text="ERROR OCCURED IN DOWNLOAD")
        bar["value"] = 0
      

    

def progress():

    task =10
    x =0
    
    while(x<task):

        time.sleep(2)
        bar['value'] += 10 
    
        x+=1
        
        status.set(str(bar['value']) + "%")
        if(bar['value']==100):
            finish.set("Download Completed")
        
        window.update_idletasks()


    #stream=video.streams.get_highest_resolution()

    #stream.download()
    

options = [
    "144p",
    "240p",
    "360p",
    "480p",
    "720p",
    "1080p",
    "1440p"
]

finish=StringVar()

status=StringVar()

clicked.set("720p")

drop_down = OptionMenu(window, clicked , *options)
drop_down.place(x=950,y=330,width ="120")

 

label_link=tk.Label(window ,text ="Downloaded File Name  :",bg="black",fg ="#f00",font="arial 14 bold")
label_link.place(x=250,y=620)

label_link_1=tk.Label(window ,text ="",bg="#000",fg ="#fff",font ='simsun 12')
label_link_1.place(x=490,y=620)

label_status=tk.Label(window ,textvariable=status,bg="black",fg="#fff")
label_status.place(x=550,y=400)

label_finish=tk.Label(window ,textvariable=finish,bg="black",fg="#fff")
label_finish.place(x=610,y=400)

bar = Progressbar(window,orient=HORIZONTAL,length =250)
bar.place(x=545,y=430)

button =tk.Button( window , text = "DOWNLOAD",fg="#000",bg="red",bd =0,font='arial 12',command = resolution).place(x =625,y =500)
window.mainloop()


