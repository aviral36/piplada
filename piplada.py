import tkinter as tk
import turtle
from turtle import Screen
from PIL import Image, ImageTk
import webbrowser

#opens link from tk's label button
def callback(url):
    webbrowser.open_new(url)

#tkinter window
application = tk.Tk()
application.title("Piplada v1.0.2")

#position config
screen_width = application.winfo_screenwidth()
screen_height = application.winfo_screenheight()

dims = str(300)+"x"+str(screen_height)+"+"+str(int(screen_width/2)-400)+"+"+str(0)
print(dims, screen_width, screen_height)
application.geometry(dims)
application.configure(background="white")

#window items
banner_img = ImageTk.PhotoImage(Image.open("piplada_icon.PNG"))
top_banner = tk.Label(application, image = banner_img)
top_banner.pack(side = "top", fill = "both", expand = "no")
canvas_size_text = "Original canvas size " + str(int(screen_width/2 - 100)) + "x" + str(screen_height)
top_text = tk.Label(text=canvas_size_text, bg="white")
top_text.pack()
link1 = tk.Label(application, text="For Piplada documentation, click here", fg="blue", cursor="hand2", bg="white")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://aviral36.github.io"))


#turtle canvas
turtle.color("green","red")
board = Screen()
board.setup(width = int(screen_width/2 - 100), height = 1.0, startx = int(screen_width/2 - 100), starty = 0)
board.title("Piplada Canvas")
while True:
    turtle.forward(200) 
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.done()
application.mainloop()
