import tkinter as tk
import turtle
from turtle import Screen
from PIL import Image, ImageTk
import webbrowser

#global variables
commands = list() 
show_pointer = int()
speed = int()
pretty_sentences = list()

#opens link from tk's label button
def callback(url):
    webbrowser.open_new(url)

#add command entry
def add_command():
    lframe = tk.Frame()
    lframe.bind("<Add Input>", callback)
    lframe.grid(row = 0)

#add entry to motion command
def add_entry():
    l = [cmd_1.get(), val_str.get()]
    commands.append(l)
    pretty_text = str()

    if l[0] == "Move":
        pretty_text = l[0] + " pointer " + str(l[1]) + " pixels forward\n"
    else:
        pretty_text = l[0] + " pointer by " + str(l[1]) + " degrees\n"
    pretty_sentences.append(pretty_text)
    output_window.configure(state='normal')
    output_window.insert('end', pretty_text)
    output_window.configure(state='disabled')

#remove entry from motion command
def clear_entry():
    commands.pop()
    pretty_sentences.pop()
    output_window.configure(state='normal')
    output_window.delete(1.0, 'end')
    for sentence in pretty_sentences:
        output_window.insert('end', sentence)
    output_window.configure(state='disabled')

#clear all commands
def clear_all():
    global commands
    global pretty_sentences
    commands = list()
    pretty_sentences = list()
    output_window.configure(state='normal')
    output_window.delete(1.0, 'end')
    output_window.configure(state='disabled')

#pointer configuration
def ptr_config():
    global show_pointer
    output_window2.configure(state='normal')
    output_window2.delete(1.0, 'end')
    output_window2.configure(state='disabled')
    if var1.get() == 1:
        show_pointer = 1
        ptr_text = "pointer shown"
    else:
        show_pointer = 0
        ptr_text = "pointer hidden"
    output_window2.configure(state='normal')
    output_window2.insert('end', ptr_text)
    output_window2.configure(state='disabled')

#specify drawing speed
def speedometer():
    global speed
    s = cmd_2.get()
    if s == "Very Slow":
        speed = 1
    elif s == "Slow":
        speed = 4
    elif s == "Normal":
        speed = 6
    elif s == "Fast":
        speed = 8
    elif s == "Very Fast":
        speed = 10
    else:
        speed = 0

#generate fractal
def generate_fractal():
    #turtle canvas
    speedometer()
    command_list = commands
    board = Screen()
    turtle.speed(speed)
    turtle.color("green")
    board.setup(width = int(screen_width/2 - 100), height = 1.0, startx = int(screen_width/2 - 100), starty = 0)
    board.title("Piplada Canvas")
    if command_list == []:
        turtle.bye()
    if show_pointer == 1:
        turtle.showturtle()
    else:
        turtle.hideturtle()
    if command_list[0][0] == 'Move':
        #set pointer position midway of the first move
        d_ = int(command_list[0][1])/2
        centre = (-d_, 0)
        turtle.setpos(centre)
    while True:
        for cmd in command_list:
            if cmd[0] == "Move":
                turtle.forward(int(cmd[1]))
            else: 
                turtle.left(int(cmd[1]))
        if abs(turtle.pos() - centre) < 1:
            break
    turtle.done()
    application.mainloop()

#tkinter window
application = tk.Tk()
application.title("Piplada v1.1")
application.grid_columnconfigure((0, 1, 2), weight=1)

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
top_banner.grid(row = 1, columnspan = 3, sticky = "NESW")

canvas_size_text = "Original canvas size " + str(int(screen_width/2 - 100)) + "x" + str(screen_height)
top_text = tk.Label(text=canvas_size_text, bg="white")
top_text.grid(row=2, columnspan=3)

link1 = tk.Label(application, text="For Piplada documentation, click here", fg="blue", cursor="hand2", bg="white")
link1.grid(row=3, columnspan=3)
link1.bind("<Button-1>", lambda e: callback("https://github.com/aviral36/piplada/wiki"))

help_text = tk.Label(application, bg="white", text = "\nMovement is in a straight line in\n the direction it is facing, in pixels.\n Rotation is in degrees, anti-clockwise ")
help_text.grid(row=4, columnspan=3)
help_text2 = tk.Label(application, bg="white", text = "\nKeep fractal lengths within canvas dimensions.")
help_text2.grid(row=5, columnspan=3)

text_box1 = tk.Label(text = "\nInput fractal motion data:\n", bg = 'white')
text_box1.grid(row = 6, columnspan=3)

###Command row begins###
OptionList = ["Move" , "Rotate"]
cmd_1 = tk.StringVar(application)
cmd_1.set(OptionList[0])

opt = tk.OptionMenu(application, cmd_1, *OptionList)
opt.config(font=("system", 11), relief = "flat", bg = 'white', highlightcolor = 'white', fg = 'blue', width = 6)
opt.grid(row = 7, column = 0, sticky ='e', pady = 5)

l_box = tk.Label(application, text = "pointer", bg= 'white', fg = 'blue', font=("system", 11))
l_box.grid(row = 7, column = 1, pady = 5)

val_str = tk.StringVar(application, value='200')
l_entry = tk.Entry(application, textvariable = val_str, bg = "alice blue", fg = 'blue', font=("system", 11), width = 5)
l_entry.grid(row = 7, column = 2, sticky = 'w', pady = 5)
###Command row ends###

###fill config row begins###
var1 = tk.IntVar()
ptr_display = tk.Checkbutton(application, text = 'Show Pointer', bg = 'white', variable = var1, onvalue = 1, offvalue = 0, command = ptr_config)
ptr_display.grid(row = 8, column = 0)

SpeedList = ["Very Slow" , "Slow", "Normal", "Fast", "Very Fast", "Zoom!!!"]
cmd_2 = tk.StringVar(application)
cmd_2.set(SpeedList[2])

speed_label = tk.Label(application, text = "Speed:", bg = "white")
speed_label.grid(row = 8, column =1, sticky = 'e')

speed_menu = tk.OptionMenu(application, cmd_2, *SpeedList)
speed_menu.config(relief = "flat", bg = 'gray95', fg = 'black')
speed_menu.grid(row = 8, column = 2, sticky ='w')
###fill config row ends###

add_btn = tk.Button(application, text = "Add Entry", command = add_entry, bg = 'gainsboro')
add_btn.grid(row = 10, pady = 5, ipadx = 2, padx = 2, column = 0, sticky = 'nesw')

clear_btn = tk.Button(application, text = "Delete Entry", command = clear_entry, bg = 'gainsboro')
clear_btn.grid(row = 10, column = 1, pady = 5, padx = 2, sticky = 'nesw')

clearall_btn = tk.Button(application, text = "Clear All", command = clear_all, bg = 'gainsboro', fg = 'red4')
clearall_btn.grid(row = 10, column = 2, pady = 5, padx = 2, sticky = 'nesw')

output_window = tk.Text(application, state = 'disabled', bg = 'gray88', fg = 'gray40', exportselection = 0, height = 10)
output_window.grid(row = 12, columnspan = 3, padx = 10, pady = 10)

output_window2 = tk.Text(application, state = 'disabled', bg = 'gray88', fg = 'gray40', exportselection = 0, height = 1)
output_window2.grid(row = 13, columnspan = 3, padx = 10, pady = 2)

btn_draw = tk.Button(application, text = "Generate!", command = generate_fractal, bg= "green4", fg='white', width = 30)
btn_draw.grid(row=20, columnspan=3, padx = 10,pady = 10)

application.mainloop()