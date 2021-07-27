import tkinter as tk

from tkinter import filedialog, Text
import os

root = tk.Tk()
apps=[]
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps= f.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename =filedialog.askopenfilename(initialdir="/", title="Select File",
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label= tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas=tk.Canvas(root, height=400, width=550, bg="yellow")


canvas.pack()

frame =tk.Frame(root, bg="white" )
frame.place(relwidth=0.8, relheight=0.6, relx=0.09,rely=0.09)
openFile=tk.Button(root, text= "Open File", padx=10, pady=5,
                   fg="white", bg="blue", command=addApp)
openFile.pack()
runFile=tk.Button(root, text= "Run File", padx=12, pady=5,
                  fg="white", bg="blue", command=runApps)
runFile.pack()

for app in apps:
    label=tk.Label(frame, text=app)
    label.pack()
root.mainloop()
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
