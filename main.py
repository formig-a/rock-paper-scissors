from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

whiteColor = "#FFFFFF"  # white / branca
blackColor = "#333333"  # black / preta
orangeColor = "#fcc058"  # orange / laranja
yellowCollor = "#fff873"  # yellow / amarela
greenColor = "#34eb3d"   # green / verde
redColor = "#e85151"   # red / vermelha

background = "#3b3b3b"

# set the window

window = Tk()
window.title('Rock Paper Scissor')
window.geometry('260x280')
window.configure(bg=background)

global player
global bot
global rounds
global playerPoints
global botPoints
global playerInterfacePoints

playerPoints = 0
botPoints = 0
rounds = 3

def play(playerOption):
    global rounds
    global playerPoints
    global botPoints

    print(rounds)
    options = ['Rock', 'Paper', 'Scissor']
    botOption = random.choice(options)
    botPlay['text'] = translate(botOption)
    botPlay['fg'] = blackColor

    if playerOption == botOption:
        draw()
    elif playerOption == 'Paper' and botOption == 'Rock':
        victory()
    elif playerOption == 'Rock' and botOption == 'Paper':
        defeat()
    elif playerOption == 'Paper' and botOption == 'Scissor':
        defeat()
    elif playerOption == 'Scissor' and botOption == 'Paper':
        victory()
    elif playerOption == 'Rock' and botOption == 'Scissor':
        victory()
    elif playerOption == 'Scissor' and botOption == 'Rock':
        defeat()
    else:
        print('Não catalogado!', playerOption, botOption)

    if rounds == 0:
        playerInterfacePoints['text'] = playerPoints
        botInterfacePoints['text'] = botPoints
        finishGame()

def finishGame():
    global rounds
    global playerPoints
    global botPoints

    rockBtn.destroy()
    paperBtn.destroy()
    scissorsBtn.destroy()

    print(playerPoints, botPoints)
    if playerPoints > botPoints:
        winner = Label(bottomFrame, text = 'Parabéns! Você venceu.', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = whiteColor, fg = greenColor)
        winner.place(x = 5, y = 60)
    elif botPoints > playerPoints:
        winner = Label(bottomFrame, text = 'Infelizmente, você perdeu.', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = whiteColor, fg = redColor)
        winner.place(x = 5, y = 60)

    playerPoints = 0
    botPoints = 0
    rounds = 3

    def restart():
        playAgainBtn.destroy()
        winner.destroy()
        startGame()
        playerInterfacePoints['text'] = '0'
        botInterfacePoints['text'] = '0'

    playAgainBtn = Button(bottomFrame, width = 30, command = restart, text = 'Jogar novamente', bg = background, fg = whiteColor, font = ('Ivy 10 bold'), anchor = 'center', relief = RAISED, overrelief = RIDGE)
    playAgainBtn.place(x = 5, y = 150)

def draw():
    print('Empate!')
    botLine['bg'] = whiteColor
    playerLine['bg'] = whiteColor
    app_line['bg'] = yellowCollor

def victory():
    global rounds
    global playerPoints
    global botPoints

    print('Vitória!')
    botLine['bg'] = whiteColor
    playerLine['bg'] = greenColor
    app_line['bg'] = whiteColor
    playerPoints += 1
    playerInterfacePoints['text'] = playerPoints
    rounds -= 1

def defeat():
    global rounds
    global playerPoints
    global botPoints

    print('Derrota!')
    botLine['bg'] = greenColor
    playerLine['bg'] = whiteColor
    app_line['bg'] = whiteColor
    botPoints += 1
    botInterfacePoints['text'] = botPoints
    rounds -= 1

def translate(value):
    if value == 'Rock': return 'Pedra'
    if value == 'Paper': return 'Papel'
    if value == 'Scissor': return 'Tesoura'

# splitting the window

topFrame = Frame(window, width = 260, height = 100, bg = blackColor, relief = 'raised')
topFrame.grid(row = 0, column = 0, sticky = NW)
bottomFrame = Frame(window, width = 260, height = 300, bg = whiteColor, relief = 'flat')
bottomFrame.grid(row = 1, column = 0, sticky = NW)

style = ttk.Style(window)
style.theme_use('clam')

# player

player = Label(topFrame, text='Usuário', height = 1, anchor='center', font = ('Ivy 10 bold'), bg = blackColor, fg = whiteColor)
player.place(x = 25, y = 70)
playerLine = Label(topFrame, text = '', height = 10, anchor='center', font = ('Ivy 10 bold'), bg = whiteColor, fg = whiteColor)
playerLine.place(x = 0, y = 0)
playerInterfacePoints = Label(topFrame, text = '0', height = 1, anchor='center', font = ('Ivy 30 bold'), bg = blackColor, fg = whiteColor)
playerInterfacePoints.place(x = 50, y = 20)

# middle

app_ = Label(topFrame, text=':' ,height = 1, anchor='center', font = ('Ivy 30 bold'), bg = blackColor, fg = whiteColor)
app_.place(x = 125, y = 20)
app_line = Label(topFrame, text = '', width = 255, anchor = 'center', font = ('Ivy 1 bold'), bg = whiteColor, fg = whiteColor)
app_line.place(x = 0, y = 95)

# bot

bot = Label(topFrame, text = 'Bot', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = blackColor, fg = whiteColor)
bot.place(x = 205, y = 70)
botLine = Label(topFrame, text = '', height = 10, anchor = 'center', font = ('Ivy 10 bold'), bg = whiteColor, fg = whiteColor)
botLine.place(x = 255, y = 0)
botInterfacePoints = Label(topFrame, text = '0', height = 1, anchor = 'center', font = ('Ivy 30 bold'), bg = blackColor, fg = whiteColor)
botInterfacePoints.place(x = 170, y = 20)

botPlay = Label(bottomFrame, text = '', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = whiteColor, fg = blackColor)
botPlay.place(x = 190, y = 10)

# bottom frame

def startGame():
    global rock
    global paper
    global scissors
    global rockBtn
    global paperBtn
    global scissorsBtn

    startBtn.destroy()

    rock = Image.open('images/rock.png')
    rock = rock.resize((50, 50))
    rock = ImageTk.PhotoImage(rock)
    rockBtn = Button(bottomFrame, command = lambda: play('Rock'), width = 50, image = rock, compound = 'center', bg = whiteColor, fg = whiteColor, font = ('Ivy 10 bold'), anchor = 'center', relief = FLAT)
    rockBtn.place(x = 15, y = 60)

    paper = Image.open('images/paper.png')
    paper = paper.resize((50, 50))
    paper = ImageTk.PhotoImage(paper)
    paperBtn = Button(bottomFrame, command = lambda: play('Paper'), width = 50, image = paper, compound = 'center', bg = whiteColor, fg = whiteColor, font = ('Ivy 10 bold'), anchor = 'center', relief = FLAT)
    paperBtn.place(x = 95, y = 60)

    scissors = Image.open('images/scissors.png')
    scissors = scissors.resize((50, 50))
    scissors = ImageTk.PhotoImage(scissors)
    scissorsBtn = Button(bottomFrame, command = lambda: play('Scissor'), width = 50, image = scissors, compound = 'center', bg = whiteColor, fg = whiteColor, font = ('Ivy 10 bold'), anchor = 'center', relief = FLAT)
    scissorsBtn.place(x = 170, y = 60)

startBtn = Button(bottomFrame, width = 30, command = startGame, text = 'Jogar', bg = background, fg = whiteColor, font = ('Ivy 10 bold'), anchor = 'center', relief = RAISED, overrelief = RIDGE)
startBtn.place(x = 5, y = 150)

window.mainloop()