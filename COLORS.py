from tkinter import*
from tkinter.messagebox import *
import random
import pickle

colors = []
click_count = 0
d_leaders = [['','','']]
new_winner_ent = ''
new_winner_win = ''

def f_exit():
    if askyesno('EXIT', 'Do you want to\n        QUIT?'):
        root.destroy()

def f_about():
    showinfo('FIND the color of your DAY', 'Don\'t throw the slippers!!!\nGood luck!\n\nKonstiantyn Sh\nAugust_2019')

def exit_(event):
    f_exit()

def generator_colors():
    for i in range(10):
        r, g, b = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
        colors.append('#{:02x}{:02x}{:02x}'.format(r, g, b))

def stop_push():
    global d_leaders

    if btn_1['bg']==btn_2['bg']==btn_3['bg']==btn_4['bg']==btn_5['bg']==btn_6['bg']==btn_7['bg']==btn_8['bg']==btn_9['bg']:
        showinfo('!!! WINNER !!!', 'You are WINNER!!\nYour score is {}'.format(click_count))
        # adding to winner list
        if type(d_leaders[-1][1]) == str:
            if askyesno('WINNER', 'Do you want to left your name\n\
            in WINNER list?'):
                 f_new_winner()

            else:
                 f_askyesno()
        else:
            if click_count < d_leaders[-1][1]:
                if askyesno('WINNER', 'Do you want to left your name\n\
                in WINNER list?'):
                    f_new_winner()
                else:
                    f_askyesno()

def f_askyesno():
    if askyesno('Try again', 'Do you want to start new game?'):
        f_refresh()
    else:
        root.destroy()

def f_click_count():
    global click_count
    click_count += 1
    lab_click_count.config(text=click_count)
    stop_push()

# Window WINNERS (button = leaders)
def f_leaders_list(event):
    win = Toplevel(root, bg='lightblue', relief=RAISED)
    win.title('WINNERS')
    win.geometry('280x300')

    f_leaders_colors()
    global d_leaders


    lab_n_1_win_user  = Label(win, text=d_leaders[0][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_2_win_user  = Label(win, text=d_leaders[1][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_3_win_user  = Label(win, text=d_leaders[2][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_4_win_user  = Label(win, text=d_leaders[3][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_5_win_user  = Label(win, text=d_leaders[4][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_6_win_user  = Label(win, text=d_leaders[5][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_7_win_user  = Label(win, text=d_leaders[6][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_8_win_user  = Label(win, text=d_leaders[7][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_9_win_user  = Label(win, text=d_leaders[8][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)
    lab_n_10_win_user = Label(win, text=d_leaders[9][0], font='arial 12', width=12, bg='lightgreen', fg='red', height=1, bd=5, relief=RAISED)

    lab_1_win_user  = Label(win, text=d_leaders[0][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_2_win_user  = Label(win, text=d_leaders[1][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_3_win_user  = Label(win, text=d_leaders[2][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_4_win_user  = Label(win, text=d_leaders[3][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_5_win_user  = Label(win, text=d_leaders[4][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_6_win_user  = Label(win, text=d_leaders[5][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_7_win_user  = Label(win, text=d_leaders[6][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_8_win_user  = Label(win, text=d_leaders[7][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_9_win_user  = Label(win, text=d_leaders[8][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)
    lab_10_win_user = Label(win, text=d_leaders[9][1], font='arial 12', width=12, bg='pink', fg='black', height=1, bd=5, relief=SUNKEN)

    lab_n_1_win_user.grid (row=0, column=1)
    lab_n_2_win_user.grid (row=1, column=1)
    lab_n_3_win_user.grid (row=2, column=1)
    lab_n_4_win_user.grid (row=3, column=1)
    lab_n_5_win_user.grid (row=4, column=1)
    lab_n_6_win_user.grid (row=5, column=1)
    lab_n_7_win_user.grid (row=6, column=1)
    lab_n_8_win_user.grid (row=7, column=1)
    lab_n_9_win_user.grid (row=8, column=1)
    lab_n_10_win_user.grid(row=9, column=1)

    lab_1_win_user.grid (row=0, column=2)
    lab_2_win_user.grid (row=1, column=2)
    lab_3_win_user.grid (row=2, column=2)
    lab_4_win_user.grid (row=3, column=2)
    lab_5_win_user.grid (row=4, column=2)
    lab_6_win_user.grid (row=5, column=2)
    lab_7_win_user.grid (row=6, column=2)
    lab_8_win_user.grid (row=7, column=2)
    lab_9_win_user.grid (row=8, column=2)
    lab_10_win_user.grid(row=9, column=2)


    # New winner. Request for name.
def f_new_winner():
    global new_winner_ent, new_winner_win
    new_winner_win = Toplevel(root, bg='lightgreen', relief=RAISED)
    new_winner_win.title('YOU ARE NEW WINNER')
    new_winner_win.geometry('200x120')

    new_winner_lab = Label(new_winner_win, text='Enter your name', font='arial 12', bg='lightgreen', width=12, fg='black',\
                            relief=FLAT)
    new_winner_ent = Entry(new_winner_win, font='arial 12', width=20, bg='white', fg='black', bd=5, relief=SUNKEN)
    new_winner_btn = Button(new_winner_win, text='Add new\nWINNER', font='arial 12', width=12, bg='lightblue', fg='red', height=1,\
                            pady=5, bd=10, relief=RAISED)

    new_winner_lab.grid(row=1, column=0)
    new_winner_ent.grid(row=2, column=0)
    new_winner_btn.grid(row=3, column=0)

    new_winner_btn.bind('<Button-1>', f_add_new_winner)



def f_add_new_winner(event):
       global new_winner_ent, click_count, d_leaders, new_winner_win

       new_winner = new_winner_ent.get()
       f_leaders_colors()
       d_leaders.append([new_winner, click_count])
       with open ('LEADERS COLORS.pkl', 'wb') as file:
           d_leaders = f_sorting(d_leaders)
           pickle.dump(d_leaders, file)

       # close window for entering the name of winner
       new_winner_win.destroy()
       f_askyesno()


# Reading file winners list
def f_leaders_colors():
    global d_leaders

    with open('LEADERS COLORS.pkl', 'rb') as file:
        d_leaders = pickle.load(file)

# Sorting leaders on the board
def f_sorting(list):
    l = []
    for i in list:
        if i[0] != '':
            l.append(i)
    l.sort(key=lambda x: x[1])
    while len(l) < 11:
        l.append(['', ''])
    return l[:10]




def f_btn_1(event):
    btn_1.config(bg=random.choice(colors))
    f_click_count()

def f_btn_2(event):
    btn_2.config(bg=random.choice(colors))
    f_click_count()

def f_btn_3(event):
    btn_3.config(bg=random.choice(colors))
    f_click_count()

def f_btn_4(event):
    btn_4.config(bg=random.choice(colors))
    f_click_count()

def f_btn_5(event):
    btn_5.config(bg=random.choice(colors))
    f_click_count()

def f_btn_6(event):
    btn_6.config(bg=random.choice(colors))
    f_click_count()

def f_btn_7(event):
    f_click_count()
    btn_7.config(bg=random.choice(colors))

def f_btn_8(event):
    btn_8.config(bg=random.choice(colors))
    f_click_count()

def f_btn_9(event):
    btn_9.config(bg=random.choice(colors))
    f_click_count()

def f_refresh():
    global click_count
    generator_colors()
    btn_1.config(bg=random.choice(colors))
    btn_2.config(bg=random.choice(colors))
    btn_3.config(bg=random.choice(colors))
    btn_4.config(bg=random.choice(colors))
    btn_5.config(bg=random.choice(colors))
    btn_6.config(bg=random.choice(colors))
    btn_7.config(bg=random.choice(colors))
    btn_8.config(bg=random.choice(colors))
    btn_9.config(bg=random.choice(colors))
    click_count = 0
    lab_click_count.config(text=click_count)




root = Tk()
root.title('FIND the color of your DAY')
root.geometry('300x400')

m = Menu()
root.config(menu=m)

fm = Menu(m, fg='green', font='arial 12')
fm.add_command(label='Refresh', command=f_refresh)
fm.add_command(label='About', command=f_about)
fm.add_command(label='Exit', command=f_exit)

m.add_cascade(label='File', menu=fm)

lab_top = Label(root, text='chose your color', font='arial 16', fg='green')

btn_1 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_2 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_3 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_4 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_5 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_6 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_7 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_8 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)
btn_9 = Button(root, width=10, height=5, padx=5, pady=5, bd=5, relief=RAISED)



lab_click = Label(root, text='Clicks', font='arial 16', fg='green')
lab_click_count = Label(root, font='arial 16', fg='red', relief=RAISED)

btn_leaders = Button(root, text='Leaders', font='arial 16', fg='blue', relief=RAISED)

# function for start
f_refresh()

lab_top.grid(row=0, column=0, columnspan=3)
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)

# basement
lab_click.grid(row=4, column=0)
lab_click_count.grid(row=4, column=1)
btn_leaders.grid(row=4, column=2)

btn_1.bind('<Button-1>', f_btn_1)
btn_2.bind('<Button-1>', f_btn_2)
btn_3.bind('<Button-1>', f_btn_3)
btn_4.bind('<Button-1>', f_btn_4)
btn_5.bind('<Button-1>', f_btn_5)
btn_6.bind('<Button-1>', f_btn_6)
btn_7.bind('<Button-1>', f_btn_7)
btn_8.bind('<Button-1>', f_btn_8)
btn_9.bind('<Button-1>', f_btn_9)

btn_leaders.bind('<Button-1>', f_leaders_list)


root.bind('<Control-z>', exit_)
root.mainloop()