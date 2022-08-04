from random import randint
from time import sleep
from tkinter import *
import pygame
game = Tk()
game.geometry('500x500')
game.title("Number Guessing Game")
game.config(bg='blue',height=500,width=500)
#craeting variables
def win():
    winning_number = randint(1,100)
    print(winning_number)
    return winning_number
input_number = IntVar()
count = 0

pygame.mixer.init()
wrong = pygame.mixer.Sound('wrong.wav')
right = pygame.mixer.Sound('right.wav')
button = pygame.mixer.Sound('button.wav')
#printing labels
def play():
    button.play()
    sleep(1)
    button.stop()
    play_button.place_forget()
    exit_button.place(x=200,y=400)
    winning_number = win()
    input_msg = Label(game, text='Guess A Number',fg='red',bg='blue',font=("Courier New", 30, 'bold','underline'))
    input_msg.place(x=85,y=70)
    low = Label(game, text='Too low guess high\n',fg='red',bg='blue',font=('Times New Roman', 25, 'bold'))
    high = Label(game, text='Too high guess low\n',fg='red',bg='blue',font=('Times New Roman', 25, 'bold'))
  # winning_msg = Label(game, text=f'You Won!!!\nYou guessed it on {countt} attempts', fg='#05fc05',bg='blue',font=('Times New Roman', 25, 'bold'))
#taking input
    get_number = Entry(game, width=3, textvariable=input_number, foreground='red', bg='#ffffff', font=('Times New Roman', 30, 'bold'))
    get_number.focus()
    get_number.place(x=210,y=140)
   # winning_msg=Label(game, text='You Won!!!\n')
    def replay():
        button.play()
        sleep(1)
        button.stop()
        global count
        count = 0
        replay_btn.after(0, lambda: replay_btn.destroy())
        input_number.initialize(1)
        msg1_hide = Label(game, text='                                                   ',bg='blue',font=('Times New Roman', 25, 'bold'))
        msg1_hide.place(x=155,y=260)
        msg2_hide = Label(game, text='                                                   ',bg='blue',font=('Times New Roman', 25, 'bold'))
        msg2_hide.place(x=50,y=300)
        play()
    replay_btn = Button(game, text='Replay', command=replay, font=('Times New Roman', 25, 'bold'))
    error = Label(game, text='Out Of Range', bg = 'blue', fg='red',font=('Times New Roman', 25, 'bold'))
#function for submit
    def check():
        button.play()
        sleep(1)
        button.stop()
        global count
        count= count +1
        winning_msg = Label(game, text='You Won!!!', fg='#05fc05',bg='blue',font=('Times New Roman', 25, 'bold'))
        winning_msg2 = Label(game, text=f'You guessed it on {count} attempts', fg='#05fc05',bg='blue',font=('Times New Roman', 25, 'bold'))
        game_over = False
        inputted_number = input_number.get()
        while not game_over:
            if winning_number == inputted_number:
                submit.place_forget()
                low.place_forget()
                high.place_forget()
                winning_msg.place(x=155,y=260)
                winning_msg2.place(x=50,y=300)
                get_number = Entry(game, width=3, textvariable=input_number, state='readonly', foreground='#12db12', font=('Times New Roman', 30, 'bold'))
                get_number.place(x=210,y=140)
                replay_btn.place(x=180,y=210)
                replay_btn.place_configure(bordermode='inside',height=40,width=120)
                right.play()
                sleep(1)
                right.stop()
                game_over = True
            elif inputted_number > 100:
                high.place_forget()
                low.place_forget()
                error.place(x=150,y=260)
                wrong.play()
                wrong.set_volume(0.4)
                sleep(1)
                wrong.stop()
                break
            elif winning_number > inputted_number:
                error.place_forget()
                high.place_forget()
                low.place(x=105,y=260)
                wrong.play()
                wrong.set_volume(0.4)
                sleep(1)
                wrong.stop()
                input_number.initialize(1)
                break
            elif winning_number < inputted_number:
                error.place_forget()
                low.place_forget()
                wrong.play()
                wrong.set_volume(0.4)
                sleep(1)
                wrong.stop()
                high.place(x=105,y=260)
                input_number.initialize(1)
                break
    #submit input
    submit = Button(game,text='ENTER', command=check,borderwidth=0,font=('Times New Roman', 25, 'bold'))
    submit.place(x=180,y=210)
    submit.place_configure(bordermode='inside',height=40,width=120)
##########################################################################
def exit():
    button.play()
    sleep(1)
    button.stop()
    game.destroy()
play_button = Button(game, text='Play',command=play, font=('Times New Roman',25,'bold'))
play_button.place(x=210,y=180)
play_button.place_configure(bordermode='inside',height=40,width=75)
exit_button = Button(game, text='Exit', command=exit, font=('Times New Roman',25,'bold'))
exit_button.place(x=210,y=230)
exit_button.place_configure(bordermode='inside',height=35,width=75)
game.mainloop()