import tkinter

button_values= [
    ["AC","+/-","%","/"],
    ["7","8","9","x"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","√","="]
]

right_symbols = ["/","x","-","+","="]
top_symbols = ["AC","+/-","%"]

row_count =len(button_values)
column_count=len(button_values[0])

color_light_gray ="#D4D4D2"
color_black="#1C1C1C"
color_dark_gray="#505050"
colour_yellow="#FF9500"
color_white="white"

#window setup
window= tkinter.Tk() #creates the window
window.title("calculator")
window.resizable(False,False)

frame= tkinter.Frame(window)
label= tkinter.Label(frame, text="0", font=("arial",45),background=color_black,foreground=color_white,anchor="e",width=column_count)

label.grid(row=0,column=0,columnspan=column_count,sticky="We")

for row in range(row_count):
    for column in range(column_count):
        values= button_values[row][column]
        button= tkinter.Button(frame,text=values, font=("arial",30),width=column_count-1,height=1,command=lambda value= values: button_clicked(value))

        if values in top_symbols:
            button.config(foreground=color_black,background=color_light_gray)
        elif values in right_symbols:
            button.config(foreground=color_white, background= colour_yellow)
        else:
            button.config(background=color_dark_gray,foreground=color_white)

        button.grid(row=row+1,column=column)
frame.pack()
def remove_zero(num):
    if num %1 ==0:
        num= int(num)
    return str(num)

A="0"
operator = None
B= None

def button_clicked(value):
    global right_symbols,top_symbols,label,A,B,operator

    if value in right_symbols:
        if value=="=":
            if A is not None and operator is not None:
                B=label["text"]
                numA=float(A)
                numB=float(B)
                if operator=="+":
                    label["text"]=remove_zero(numA+numB)
                elif operator=="-":
                    label["text"]=remove_zero(numA-numB)
                elif operator=="/":
                    label["text"]=remove_zero(numA/numB)
                elif operator=="x":
                    label["text"]=remove_zero(numA*numB)



        elif value in ["+","/","-","x"]:
            if operator is None:
                A = label["text"]
                label["text"]="0"
                B="0"
            operator=value
           



    elif value in top_symbols:
        if value=="AC":
           label["text"]="0"
           A="0"
           operator=None
           B= None
        elif value=="+/-":
            result= float(label["text"])*-1
            label["text"]=remove_zero(result)
        elif value=="%":
            result= float(label["text"])/100
            label["text"]=remove_zero(result)
       
    else: 
        if value ==".":
            if value not in label["text"]:
                label["text"]+=value

        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value




#center the window
window.update() #update window with the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()

