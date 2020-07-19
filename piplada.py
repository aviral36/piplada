import tkinter as tk
import turtle
from turtle import Screen
from PIL import Image, ImageTk
import webbrowser
from turtle import TurtleScreen
import os
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

    
#global variables
commands = list() 
show_pointer = int()
speed = int()
str_speed = str()
pretty_sentences = list()
bg_color = "white"
fg_color = "black"
bg_colours = [["black", "navy", "red4", "dark green", "dark goldenrod"], ["gray30", "blue", "red3", "forest green", "goldenrod"], ["gray50", "RoyalBlue1", "red", "green2", "gold"], ["gray80", "light sky blue", "dark orange", "lawn green", "navajo white"], ["white", "light cyan", "orange", "SeaGreen1", "bisque"]]
fg_hex = str()
bg_hex = str()

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
        ptr_text = "pointer: shown"
    else:
        show_pointer = 0
        ptr_text = "pointer: hidden"
    output_window2.configure(state='normal')
    output_window2.insert('end', ptr_text)
    output_window2.configure(state='disabled')

#specify drawing speed
def speedometer():
    global speed
    global str_speed
    s = cmd_2.get()
    str_speed = s
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

######color functions#####

#bg colors
def bg_clr_00():
    global bg_color
    bg_color = bg_colours[0][0]

def bg_clr_01():
    global bg_color
    bg_color = bg_colours[0][1]

def bg_clr_02():
    global bg_color
    bg_color = bg_colours[0][2]

def bg_clr_03():
    global bg_color
    bg_color = bg_colours[0][3]

def bg_clr_04():
    global bg_color
    bg_color = bg_colours[0][4]

def bg_clr_10():
    global bg_color
    bg_color = bg_colours[1][0]

def bg_clr_11():
    global bg_color
    bg_color = bg_colours[1][1]

def bg_clr_12():
    global bg_color
    bg_color = bg_colours[1][2]

def bg_clr_13():
    global bg_color
    bg_color = bg_colours[1][3]

def bg_clr_14():
    global bg_color
    bg_color = bg_colours[1][4]

def bg_clr_20():
    global bg_color
    bg_color = bg_colours[2][0]

def bg_clr_21():
    global bg_color
    bg_color = bg_colours[2][1]

def bg_clr_22():
    global bg_color
    bg_color = bg_colours[2][2]

def bg_clr_23():
    global bg_color
    bg_color = bg_colours[2][3]

def bg_clr_24():
    global bg_color
    bg_color = bg_colours[2][4]

def bg_clr_30():
    global bg_color
    bg_color = bg_colours[3][0]

def bg_clr_31():
    global bg_color
    bg_color = bg_colours[3][1]

def bg_clr_32():
    global bg_color
    bg_color = bg_colours[3][2]

def bg_clr_33():
    global bg_color
    bg_color = bg_colours[3][3]

def bg_clr_34():
    global bg_color
    bg_color = bg_colours[3][4]

def bg_clr_40():
    global bg_color
    bg_color = bg_colours[4][0]

def bg_clr_41():
    global bg_color
    bg_color = bg_colours[4][1]

def bg_clr_42():
    global bg_color
    bg_color = bg_colours[4][2]

def bg_clr_43():
    global bg_color
    bg_color = bg_colours[4][3]

def bg_clr_44():
    global bg_color
    bg_color = bg_colours[4][4]

#fg colors
def fg_clr_00():
    global fg_color
    fg_color = bg_colours[0][0]

def fg_clr_01():
    global fg_color
    fg_color = bg_colours[0][1]

def fg_clr_02():
    global fg_color
    fg_color = bg_colours[0][2]

def fg_clr_03():
    global fg_color
    fg_color = bg_colours[0][3]

def fg_clr_04():
    global fg_color
    fg_color = bg_colours[0][4]

def fg_clr_10():
    global fg_color
    fg_color = bg_colours[1][0]

def fg_clr_11():
    global fg_color
    fg_color = bg_colours[1][1]

def fg_clr_12():
    global fg_color
    fg_color = bg_colours[1][2]

def fg_clr_13():
    global fg_color
    fg_color = bg_colours[1][3]

def fg_clr_14():
    global fg_color
    fg_color = bg_colours[1][4]

def fg_clr_20():
    global fg_color
    fg_color = bg_colours[2][0]

def fg_clr_21():
    global fg_color
    fg_color = bg_colours[2][1]

def fg_clr_22():
    global fg_color
    fg_color = bg_colours[2][2]

def fg_clr_23():
    global fg_color
    fg_color = bg_colours[2][3]

def fg_clr_24():
    global fg_color
    fg_color = bg_colours[2][4]

def fg_clr_30():
    global fg_color
    fg_color = bg_colours[3][0]

def fg_clr_31():
    global fg_color
    fg_color = bg_colours[3][1]

def fg_clr_32():
    global fg_color
    fg_color = bg_colours[3][2]

def fg_clr_33():
    global fg_color
    fg_color = bg_colours[3][3]

def fg_clr_34():
    global fg_color
    fg_color = bg_colours[3][4]

def fg_clr_40():
    global fg_color
    fg_color = bg_colours[4][0]

def fg_clr_41():
    global fg_color
    fg_color = bg_colours[4][1]

def fg_clr_42():
    global fg_color
    fg_color = bg_colours[4][2]

def fg_clr_43():
    global fg_color
    fg_color = bg_colours[4][3]

def fg_clr_44():
    global fg_color
    fg_color = bg_colours[4][4]

#####color functions end#####

#background color setter
def bg_color_setter():
    
    bg_window = tk.Toplevel(application)
    
    global bg_color
    global bg_colours
    global fg_color

    #closes bg_window
    def close_bg_window():    
        bg_window.destroy()
        ow3_text = "bg: "+ bg_color + " | line: " + fg_color
        output_window3.configure(state = 'normal')
        output_window3.delete(1.0, 'end')
        output_window3.insert('end', ow3_text)
        output_window3.configure(state='disabled')
    
    bg_window.title("Colour Picker")
    bg_window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
    s_width = application.winfo_screenwidth()
    s_height = application.winfo_screenheight()

    s_dims = str(300)+"x"+str(int(s_height/2.5))+"+"+str(int(s_width/2)-400)+"+"+str(150)
    bg_window.geometry(s_dims)
    bg_window.configure(background="white")

    picker_banner_img = ImageTk.PhotoImage(Image.open("colour_picker_icon.PNG"))
    picker_top_banner = tk.Label(bg_window, image = picker_banner_img)
    picker_top_banner.grid(row = 1, columnspan = 5, ipadx = 2, padx = 2, pady = 5, sticky = "nesw")

    label1 = tk.Label(bg_window, text = "Choose Canvas Colour:", bg = 'white')
    label1.grid(row = 2, columnspan = 5, pady = 15)

    #colours start here

    c0_0 = tk.Button(bg_window, width = 7, bg = bg_colours[0][0], command = bg_clr_00)
    c0_0.grid(row = 3, column = 0)

    c0_1 = tk.Button(bg_window, width = 7, bg = bg_colours[0][1], command = bg_clr_01)
    c0_1.grid(row = 3, column = 1)

    c0_2 = tk.Button(bg_window, width = 7, bg = bg_colours[0][2], command = bg_clr_02)
    c0_2.grid(row = 3, column = 2)

    c0_3 = tk.Button(bg_window, width = 7, bg = bg_colours[0][3], command = bg_clr_03)
    c0_3.grid(row = 3, column = 3)

    c0_4 = tk.Button(bg_window, width = 7, bg = bg_colours[0][4], command = bg_clr_04)
    c0_4.grid(row = 3, column = 4)

    c1_0 = tk.Button(bg_window, width = 7, bg = bg_colours[1][0], command = bg_clr_10)
    c1_0.grid(row = 4, column = 0)

    c1_1 = tk.Button(bg_window, width = 7, bg = bg_colours[1][1], command = bg_clr_11)
    c1_1.grid(row = 4, column = 1)

    c1_2 = tk.Button(bg_window, width = 7, bg = bg_colours[1][2], command = bg_clr_12)
    c1_2.grid(row = 4, column = 2)

    c1_3 = tk.Button(bg_window, width = 7, bg = bg_colours[1][3], command = bg_clr_13)
    c1_3.grid(row = 4, column = 3)

    c1_4 = tk.Button(bg_window, width = 7, bg = bg_colours[1][4], command = bg_clr_14)
    c1_4.grid(row = 4, column = 4)

    c2_0 = tk.Button(bg_window, width = 7, bg = bg_colours[2][0], command = bg_clr_20)
    c2_0.grid(row = 5, column = 0)

    c2_1 = tk.Button(bg_window, width = 7, bg = bg_colours[2][1], command = bg_clr_21)
    c2_1.grid(row = 5, column = 1)

    c2_2 = tk.Button(bg_window, width = 7, bg = bg_colours[2][2], command = bg_clr_22)
    c2_2.grid(row = 5, column = 2)

    c2_3 = tk.Button(bg_window, width = 7, bg = bg_colours[2][3], command = bg_clr_23)
    c2_3.grid(row = 5, column = 3)

    c2_4 = tk.Button(bg_window, width = 7, bg = bg_colours[2][4], command = bg_clr_24)
    c2_4.grid(row = 5, column = 4)

    c3_0 = tk.Button(bg_window, width = 7, bg = bg_colours[3][0], command = bg_clr_30)
    c3_0.grid(row = 6, column = 0)

    c3_1 = tk.Button(bg_window, width = 7, bg = bg_colours[3][1], command = bg_clr_31)
    c3_1.grid(row = 6, column = 1)

    c3_2 = tk.Button(bg_window, width = 7, bg = bg_colours[3][2], command = bg_clr_32)
    c3_2.grid(row = 6, column = 2)

    c3_3 = tk.Button(bg_window, width = 7, bg = bg_colours[3][3], command = bg_clr_33)
    c3_3.grid(row = 6, column = 3)

    c3_4 = tk.Button(bg_window, width = 7, bg = bg_colours[3][4], command = bg_clr_34)
    c3_4.grid(row = 6, column = 4)

    c4_0 = tk.Button(bg_window, width = 7, bg = bg_colours[4][0], command = bg_clr_40)
    c4_0.grid(row = 7, column = 0)

    c4_1 = tk.Button(bg_window, width = 7, bg = bg_colours[4][1], command = bg_clr_41)
    c4_1.grid(row = 7, column = 1)

    c4_2 = tk.Button(bg_window, width = 7, bg = bg_colours[4][2], command = bg_clr_42)
    c4_2.grid(row = 7, column = 2)

    c4_3 = tk.Button(bg_window, width = 7, bg = bg_colours[4][3], command = bg_clr_43)
    c4_3.grid(row = 7, column = 3)

    c4_4 = tk.Button(bg_window, width = 7, bg = bg_colours[4][4], command = bg_clr_44)
    c4_4.grid(row = 7, column = 4)

    text_2 = tk.Label(bg_window, text = "OR", bg = "white")
    text_2.grid(row = 8, columnspan = 5, pady = 5)

    text_b = tk.Label(bg_window, text = "Enter Hex:", bg = "white",  width = 7)
    text_b.grid(row = 9, column = 1, sticky='w')

    box_b = tk.Entry(bg_window, textvariable = bg_hex, width = 10)
    box_b.grid(row = 9, column = 2, columnspan = 2, sticky = 'nesw', padx = 3)
    
    done_btn = tk.Button(bg_window, text = "Done", command = close_bg_window, bg = "gray88")
    done_btn.grid(row = 8, columnspan = 5, padx = 10, pady = 20, sticky = 'nesw')


    bg_window.wait_window(bg_window)
    

#line color setter
def fg_color_setter():
    
    fg_window = tk.Toplevel(application)
    
    global bg_color
    global bg_colours
    global fg_color

    #closes fg_window
    def close_fg_window():    
        fg_window.destroy()
        ow3_text = "bg: "+ bg_color + " | line: " + fg_color
        output_window3.configure(state = 'normal')
        output_window3.delete(1.0, 'end')
        output_window3.insert('end', ow3_text)
        output_window3.configure(state='disabled')
    
    fg_window.title("Colour Picker")
    fg_window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
    s_width = application.winfo_screenwidth()
    s_height = application.winfo_screenheight()

    s_dims = str(300)+"x"+str(int(s_height/2.15))+"+"+str(int(s_width/2)-400)+"+"+str(150)
    fg_window.geometry(s_dims)
    fg_window.configure(background="white")

    picker_banner_img = ImageTk.PhotoImage(Image.open("colour_picker_icon.PNG"))
    picker_top_banner = tk.Label(fg_window, image = picker_banner_img)
    picker_top_banner.grid(row = 1, columnspan = 5, ipadx = 2, padx = 2, pady = 5, sticky = "nesw")

    label1 = tk.Label(fg_window, text = "Choose Line Colour:", bg = 'white')
    label1.grid(row = 2, columnspan = 5, pady = 15)

    #colours start here

    c0_0 = tk.Button(fg_window, width = 7, bg = bg_colours[0][0], command = fg_clr_00)
    c0_0.grid(row = 3, column = 0)

    c0_1 = tk.Button(fg_window, width = 7, bg = bg_colours[0][1], command = fg_clr_01)
    c0_1.grid(row = 3, column = 1)

    c0_2 = tk.Button(fg_window, width = 7, bg = bg_colours[0][2], command = fg_clr_02)
    c0_2.grid(row = 3, column = 2)

    c0_3 = tk.Button(fg_window, width = 7, bg = bg_colours[0][3], command = fg_clr_03)
    c0_3.grid(row = 3, column = 3)

    c0_4 = tk.Button(fg_window, width = 7, bg = bg_colours[0][4], command = fg_clr_04)
    c0_4.grid(row = 3, column = 4)

    c1_0 = tk.Button(fg_window, width = 7, bg = bg_colours[1][0], command = fg_clr_10)
    c1_0.grid(row = 4, column = 0)

    c1_1 = tk.Button(fg_window, width = 7, bg = bg_colours[1][1], command = fg_clr_11)
    c1_1.grid(row = 4, column = 1)

    c1_2 = tk.Button(fg_window, width = 7, bg = bg_colours[1][2], command = fg_clr_12)
    c1_2.grid(row = 4, column = 2)

    c1_3 = tk.Button(fg_window, width = 7, bg = bg_colours[1][3], command = fg_clr_13)
    c1_3.grid(row = 4, column = 3)

    c1_4 = tk.Button(fg_window, width = 7, bg = bg_colours[1][4], command = fg_clr_14)
    c1_4.grid(row = 4, column = 4)

    c2_0 = tk.Button(fg_window, width = 7, bg = bg_colours[2][0], command = fg_clr_20)
    c2_0.grid(row = 5, column = 0)

    c2_1 = tk.Button(fg_window, width = 7, bg = bg_colours[2][1], command = fg_clr_21)
    c2_1.grid(row = 5, column = 1)

    c2_2 = tk.Button(fg_window, width = 7, bg = bg_colours[2][2], command = fg_clr_22)
    c2_2.grid(row = 5, column = 2)

    c2_3 = tk.Button(fg_window, width = 7, bg = bg_colours[2][3], command = fg_clr_23)
    c2_3.grid(row = 5, column = 3)

    c2_4 = tk.Button(fg_window, width = 7, bg = bg_colours[2][4], command = fg_clr_24)
    c2_4.grid(row = 5, column = 4)

    c3_0 = tk.Button(fg_window, width = 7, bg = bg_colours[3][0], command = fg_clr_30)
    c3_0.grid(row = 6, column = 0)

    c3_1 = tk.Button(fg_window, width = 7, bg = bg_colours[3][1], command = fg_clr_31)
    c3_1.grid(row = 6, column = 1)

    c3_2 = tk.Button(fg_window, width = 7, bg = bg_colours[3][2], command = fg_clr_32)
    c3_2.grid(row = 6, column = 2)

    c3_3 = tk.Button(fg_window, width = 7, bg = bg_colours[3][3], command = fg_clr_33)
    c3_3.grid(row = 6, column = 3)

    c3_4 = tk.Button(fg_window, width = 7, bg = bg_colours[3][4], command = fg_clr_34)
    c3_4.grid(row = 6, column = 4)

    c4_0 = tk.Button(fg_window, width = 7, bg = bg_colours[4][0], command = fg_clr_40)
    c4_0.grid(row = 7, column = 0)

    c4_1 = tk.Button(fg_window, width = 7, bg = bg_colours[4][1], command = fg_clr_41)
    c4_1.grid(row = 7, column = 1)

    c4_2 = tk.Button(fg_window, width = 7, bg = bg_colours[4][2], command = fg_clr_42)
    c4_2.grid(row = 7, column = 2)

    c4_3 = tk.Button(fg_window, width = 7, bg = bg_colours[4][3], command = fg_clr_43)
    c4_3.grid(row = 7, column = 3)

    c4_4 = tk.Button(fg_window, width = 7, bg = bg_colours[4][4], command = fg_clr_44)
    c4_4.grid(row = 7, column = 4)

    text_1 = tk.Label(fg_window, text = "OR", bg = "white")
    text_1.grid(row = 8, columnspan = 5, pady = 5)

    text_a = tk.Label(fg_window, text = "Enter Hex:", bg = "white",  width = 7)
    text_a.grid(row = 9, column = 1, sticky='w')

    box_a = tk.Entry(fg_window, textvariable = fg_hex, width = 10)
    box_a.grid(row = 9, column = 2, columnspan = 2, sticky = 'nesw', padx = 3)

    done_btn = tk.Button(fg_window, text = "Done", command = close_fg_window, bg = "gray88")
    done_btn.grid(row = 10, columnspan = 5, padx = 10, pady = 20, sticky = 'nesw')


    fg_window.wait_window(fg_window)


def generate_fractal():
    #turtle canvas
    TurtleScreen._RUNNING = True
    speedometer()
    global bg_color
    global fg_color
    command_list = commands
    board = Screen()
    turtle.speed(speed)
    turtle.bgcolor(bg_color)
    turtle.color(fg_color)
    board.setup(width = int(screen_width/2 - 100), height = 1.0, startx = int(screen_width/2 - 100), starty = 0)
    board.title("Piplada Canvas")
    if command_list == []:
        turtle.bye()
    if show_pointer == 1:
        turtle.showturtle()
    else:
        turtle.hideturtle()
    time.sleep(1)
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

#tkinter window
application = tk.Tk()
application.title("Piplada v1.1")
application.grid_columnconfigure((0, 1, 2), weight=1)

#position config
screen_width = application.winfo_screenwidth()
screen_height = application.winfo_screenheight()

dims = str(300)+"x"+str(screen_height)+"+"+str(int(screen_width/2)-400)+"+"+str(0)
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
help_text2 = tk.Label(application, bg="white", text = "Keep fractal lengths within canvas dimensions.")
help_text2.grid(row=5, columnspan=3, pady = 10)

text_box1 = tk.Label(text = "Input fractal motion data:\n", bg = 'white')
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
l_entry.grid(row = 7, column = 2, sticky = 'we', pady = 5, padx = 25)
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
speed_menu.grid(row = 8, column = 2)

color_label = tk.Label(application, text = "Pick Colour:", bg = "white")
color_label.grid(row = 9, column = 0)

bg_color_btn = tk.Button(application, text = "Background", command = bg_color_setter, bg = "white")
bg_color_btn.grid(row = 9, column = 1, pady = 5, ipadx = 2, padx = 2, sticky = 'nesw')

fg_color_btn = tk.Button(application, text = "Line", command = fg_color_setter, bg = "white")
fg_color_btn.grid(row = 9, column = 2, pady = 5, ipadx = 2, padx = 2, sticky = 'nesw')
###fill config row ends###

add_btn = tk.Button(application, text = "Add Entry", command = add_entry, bg = 'gainsboro')
add_btn.grid(row = 10, pady = 5, ipadx = 2, padx = 2, column = 0, sticky = 'nesw')

clear_btn = tk.Button(application, text = "Delete Entry", command = clear_entry, bg = 'gainsboro')
clear_btn.grid(row = 10, column = 1, pady = 5, padx = 2, sticky = 'nesw')

clearall_btn = tk.Button(application, text = "Clear All", command = clear_all, bg = 'gainsboro', fg = 'red4')
clearall_btn.grid(row = 10, column = 2, pady = 5, padx = 2, sticky = 'nesw')

output_window = tk.Text(application, state = 'disabled', bg = 'gray88', fg = 'gray40', exportselection = 0, height = 10)
output_window.grid(row = 12, columnspan = 3, padx = 10, pady = 10)

output_window2 = tk.Text(application, state = 'normal', bg = 'gray88', fg = 'gray40', exportselection = 0, height = 1)
output_window2.grid(row = 13, columnspan = 3, padx = 10, pady = 2)
output_window2.insert('end', "pointer: hidden")
output_window2.configure(state = 'disabled')

output_window3 = tk.Text(application, state = 'normal', bg = 'gray88', fg = 'gray40', exportselection = 0, height = 1)
output_window3.grid(row = 14, columnspan = 3, padx = 10, pady = 2)
ow_text3 = "bg: "+ bg_color + " | line: " + fg_color
output_window3.insert('end', ow_text3)
output_window3.configure(state='disabled')

btn_draw = tk.Button(application, text = "Generate!", command = generate_fractal, bg= "green4", fg='white', width = 30)
btn_draw.grid(row=20, columnspan=3, padx = 10,pady = 10)

application.mainloop()