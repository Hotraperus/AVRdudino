import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import re


pcbs = ["-patmega328", "-pm328p","-patmega2560"]
pcbstr = ""

pathstr = ""
portstr = ""

AVRdudinopath = str(re.sub(r'AVRdudino.py', '', str(os.path.abspath(__file__))))


def setpcb():
   global pcbstr
   selection = var.get()
   pcbstr = pcbs[selection]
   #print(pcb)

def opendialog():
   global pathstr
   pathstr=tk.filedialog.askopenfilename(defaultextension=".hex",filetypes =[("hex files","*.hex")])
   

def loadbuttonhandler():
   global pathstr
   global portentry
   setpcb()
   allgood = True
   if pathstr == "": allgood = False
   if pcbstr == "": allgood = False
   portstr = portentry.get()
   portnum = -1
   if portstr != "": portnum = int(portstr)
   if portnum <0 or portnum >100: allgood = False
   if allgood:
      portstr = "-PCOM" + str(portnum)
      execstr ="avrdudinocmd.bat" + " " + '''"''' + pathstr + '''"''' + " " + pcbstr + " " + portstr
      print(execstr)
      os.system(execstr)
root = tk.Tk()
root.iconbitmap('AVRdudino.ico')
#statusbar = ttk.Label(root, text="", relief=tk.SUNKEN, anchor=tk.W)
#statusbar.pack(side = tk.BOTTOM, fill=tk.X)

menubar = tk.Menu(root)
root.config(menu=menubar)

#statusbar.pack(side = tk.BOTTOM, fill=tk.X)
menubar.add_command(label="Open hex", command=opendialog)

loadbutton = tk.Button(root, width = 40, height = 3 , text="Load",command=loadbuttonhandler)
loadbutton.pack(side = tk.BOTTOM)



var = tk.IntVar()

ArduinoUNOr3 = tk.Radiobutton(root, text="Arduino UNO r3", variable=var, value=0, command=setpcb)
ArduinoUNOr3.pack( anchor = tk.W )

ArduinoNano = tk.Radiobutton(root, text="Arduino Nano", variable=var, value=1, command=setpcb)
ArduinoNano.pack( anchor = tk.W )

ArduinoMEGA2560 = tk.Radiobutton(root, text="Arduino MEGA 2560", variable=var, value=2, command=setpcb)
ArduinoMEGA2560.pack( anchor = tk.W )

portpromptlabel = tk.Label(root, text="Write the serial port number:")
portpromptlabel.pack(side = tk.LEFT)
portentry = tk.Entry(root)
portentry.pack(side = tk.LEFT)


root.title("AVRdudino")
root.geometry("300x150")
root.resizable(False, False)
#root.resizable(True, True)
root.mainloop()

