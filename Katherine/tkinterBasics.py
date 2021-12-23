from tkinter import*


def handleClick():
    label1 = Label(frame1, text="I'm Alex", font=("Arial", 20, "bold"))
    label1.pack()


window = Tk()
window.title("Practice")
window.geometry("500x500+400+50")

frame3 = LabelFrame(window, text="frame3", width=50, height=50)
frame3.pack()

frame1 = LabelFrame(frame3, text="frame1", width=200, height=200)
frame1.pack()

frame2 = LabelFrame(frame3, text="frame2", width=50, height=50)
frame2.pack()


button1 = Button(frame1, text="Click Me", command=handleClick, fg="green", bg="yellow",
                 padx=20, pady=10, relief=GROOVE)
button1.pack()

button2 = Button(frame2, text="Enter", command=handleClick, fg="blue", bg="orange",
                 padx=20, pady=10, relief=GROOVE)
button2.grid(row=0, column=0)
button3 = Button(frame2, text="Enter", command=handleClick, fg="purple", bg="teal",
                 padx=20, pady=10, relief=GROOVE)
button3.grid(row=0, column=1)


window.mainloop()