
import pyguiauto
import time
import tkinter as tk


def screenshot():
    time.sleep(5)
    name = time.time()
    name = "C:/Users/LENOVO/Desktop/DevOps/Python_projects/{}.png".format(name)
    img = pyguiauto.screenshot()
    img.save(name)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Take Screenshot", command=screenshot())
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="quit", command=quit())
close.pack(side=tk.LEFT)

root.mainloop()
