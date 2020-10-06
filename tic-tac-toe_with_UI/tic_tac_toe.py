from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.title("TIC TAC TOE")


def btnClick(btn):
    global count, clicked
    if btn['text'] == " " and clicked:
        btn['text'] = "X"
        clicked = False
        count += 1
        check_win()
    elif btn['text'] == " " and not clicked:
        btn['text'] = "O"
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror("TIC TAC TOE", "Already Filled!")

count = 0
clicked = True
winner = False
def disable_buttons():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)

def check_win():
    global winner, count
    if (b1['text'] + b2['text'] + b3['text'] == 'XXX' or
        b4['text'] + b5['text'] + b6['text'] == 'XXX' or
        b7['text'] + b8['text'] + b9['text'] == 'XXX' or
        b1['text'] + b5['text'] + b9['text'] == 'XXX' or
        b3['text'] + b5['text'] + b7['text'] == 'XXX' or
        b1['text'] + b4['text'] + b7['text'] == 'XXX' or
        b2['text'] + b5['text'] + b8['text'] == 'XXX' or
        b3['text'] + b6['text'] + b9['text'] == 'XXX'):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Hurray!!  Winner is X")
        disable_buttons()

    elif (b1['text'] + b2['text'] + b3['text'] == 'OOO' or
          b4['text'] + b5['text'] + b6['text'] == 'OOO' or
          b7['text'] + b8['text'] + b9['text'] == 'OOO' or
          b1['text'] + b5['text'] + b9['text'] == 'OOO' or
          b3['text'] + b5['text'] + b7['text'] == 'OOO' or
          b1['text'] + b4['text'] + b7['text'] == 'OOO' or
          b2['text'] + b5['text'] + b8['text'] == 'OOO' or
          b3['text'] + b6['text'] + b9['text'] == 'OOO'):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Hurray!!  Winner is O")
        disable_buttons()
    elif count == 9 and not winner:
        disable_buttons()
        messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

def reset_all():
    global count, clicked
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    count = 0
    clicked = True
    b1 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", activebackground="red",command=lambda: btnClick(b1))
    b1.grid(row=0, column=0)
    b2 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b2))
    b2.grid(row=0, column=1)
    b3 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b3))
    b3.grid(row=0, column=2)
    b4 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b4))
    b4.grid(row=1, column=0)
    b5 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b5))
    b5.grid(row=1, column=1)
    b6 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b6))
    b6.grid(row=1, column=2)
    b7 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b7))
    b7.grid(row=2, column=0)
    b8 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b8))
    b8.grid(row=2, column=1)
    b9 = Button(tk, text=" ", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: btnClick(b9))
    b9.grid(row=2, column=2)

reset = Button(tk, text="Reset", font=("Times New Roman", 20),height=3, width=6, bg="#ecf0f1", command=lambda: reset_all())
reset.grid(row=3, column=1)
reset_all()
tk.mainloop()
