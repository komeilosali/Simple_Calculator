# Komeil Osali - 986321004

from tkinter import *

#Main Window
window = Tk()
window.geometry("339x395")
window.title("Calculator(komeil Osali)")
window.resizable(0, 0)
window.configure(background="black")
p1 = PhotoImage(file='KO_calculator.png')
window.iconphoto(False, p1)


def Click(item):
    global a
    a = a + str(item)
    InputText.set(a)


def Equal():
    try:
        global a
        result = str(eval(a))
        InputText.set(result)
        a = ""

    except:
        InputText.set(" Error ")
        a = ""


def Backspace():
    global a
    if a == "":
        InputText.set("0")
    else:
        a = a[:-1]
        InputText.set(a)


def AC():
    global a
    a = ""
    InputText.set("")


a = ""

InputText = StringVar()
InputText.set(0)

InputFrame = Frame(window
                   , width=325
                   , height=40
                   , bg="black"
                   , bd=5
                   , highlightbackground="black"
                   , highlightcolor="black"
                   , highlightthickness=0)

InputFrame.pack(side=TOP)

InputField = Entry(InputFrame
                   , font=('arial', 18, 'bold')
                   , textvariable=InputText
                   , width=30
                   , bg="light gray"
                   , bd=15
                   , justify=LEFT)

InputField.grid(row=0, column=0)
InputField.pack(ipady=10)

ButtonsFrame = Frame(window
                     , width=325
                     , height=300
                     , bg="black"
                     , bd=0)

ButtonsFrame.pack()

# ردیف اول

zero = Button(ButtonsFrame
              , text="0"
              , fg="black"
              , width=21
              , height=3
              , bd=3
              , bg="white"
              , cursor="hand2"
              , command=lambda: Click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

p8 = PhotoImage(file='point.png')
point = Button(ButtonsFrame
               , image=p8
               , fg="black"
               , width=70
               , height=50
               , bd=3
               , bg="light gray"
               , cursor="hand2"
               , command=lambda: Click(".")).grid(row=4, column=2, padx=1, pady=1)

p5 = PhotoImage(file='equals.png')
equals = Button(ButtonsFrame
                , image=p5
                , fg="black"
                , width=70
                , height=105
                , bd=3
                , bg="light gray"
                , cursor="hand2"
                , command=lambda: Equal()).grid(row=3, column=3, rowspan=2, padx=1, pady=1)

# ردیف دوم

one = Button(ButtonsFrame
             , text="1"
             , fg="black"
             , width=10
             , height=3
             , bd=0
             , bg="white"
             , cursor="hand2"
             , command=lambda: Click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(ButtonsFrame
             , text="2"
             , fg="black"
             , width=10
             , height=3
             , bd=0
             , bg="white"
             , cursor="hand2"
             , command=lambda: Click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(ButtonsFrame
               , text="3"
               , fg="black"
               , width=10
               , height=3
               , bd=0
               , bg="white"
               , cursor="hand2"
               , command=lambda: Click(3)).grid(row=3, column=2, padx=1, pady=1)

# ردیف سوم

four = Button(ButtonsFrame
              , text="4"
              , fg="black"
              , width=10
              , height=3
              , bd=0
              , bg="white"
              , cursor="hand2"
              , command=lambda: Click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(ButtonsFrame
              , text="5"
              , fg="black"
              , width=10
              , height=3
              , bd=0
              , bg="white"
              , cursor="hand2"
              , command=lambda: Click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(ButtonsFrame
             , text="6"
             , fg="black"
             , width=10
             , height=3
             , bd=0
             , bg="white"
             , cursor="hand2"
             , command=lambda: Click(6)).grid(row=2, column=2, padx=1, pady=1)

p3 = PhotoImage(file='plus.png')
plus = Button(ButtonsFrame
              , image=p3
              , fg="black"
              , width=70
              , height=50
              , bd=3
              , bg="light gray"
              , cursor="hand2"
              , command=lambda: Click("+")).grid(row=2, column=3, padx=1, pady=1)

# ردیف چهارم

seven = Button(ButtonsFrame
               , text="7"
               , fg="black"
               , width=10
               , height=3
               , bd=0
               , bg="white"
               , cursor="hand2"
               , command=lambda: Click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(ButtonsFrame
               , text="8"
               , fg="black"
               , width=10
               , height=3
               , bd=0
               , bg="white"
               , cursor="hand2"
               , command=lambda: Click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(ButtonsFrame
              , text="9"
              , fg="black"
              , width=10
              , height=3
              , bd=0
              , bg="white"
              , cursor="hand2"
              , command=lambda: Click(9)).grid(row=1, column=2, padx=1, pady=1)

p4 = PhotoImage(file='minus.png')
minus = Button(ButtonsFrame
               , image=p4
               , fg="black"
               , width=70
               , height=50
               , bd=3
               , bg="light gray"
               , cursor="hand2"
               , command=lambda: Click("-")).grid(row=1, column=3, padx=1, pady=1)

# ردیف پنجم

p9 = PhotoImage(file='AC.png')
AClear = Button(ButtonsFrame
                , image=p9
                , fg="black"
                , width=70
                , height=50
                , bd=3
                , bg="light gray"
                , cursor="hand2"
                , command=lambda: AC()).grid(row=0, column=0, padx=1, pady=1)

p2 = PhotoImage(file='backspaceICON.png')
cancel = Button(ButtonsFrame
                , image=p2
                , fg="black"
                , width=70
                , height=50
                , bd=3
                , bg="light gray"
                , cursor="hand2"
                , command=lambda: Backspace()).grid(row=0, column=1, padx=1, pady=1)

p6 = PhotoImage(file='divide.png')
divide = Button(ButtonsFrame
                , image=p6
                , fg="black"
                , width=70
                , height=50
                , bd=3
                , bg="light gray"
                , cursor="hand2"
                , command=lambda: Click("/")).grid(row=0, column=2, padx=1, pady=1)

p7 = PhotoImage(file='multiply.png')
multiply = Button(ButtonsFrame
                  , image=p7
                  , fg="black"
                  , width=70
                  , height=50
                  , bd=3
                  , bg="light gray"
                  , cursor="hand2"
                  , command=lambda: Click("*")).grid(row=0, column=3, padx=1, pady=1)

window.mainloop()
