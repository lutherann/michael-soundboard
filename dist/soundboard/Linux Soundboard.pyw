from tkinter import *
import pygame

root = Tk()
root.resizable(False, False)
root.title("Michael Soundboard")
root.iconbitmap('favicon.ico')

pygame.mixer.init()


def play1():
    pygame.mixer.music.load("whohurtyou.mp3")
    pygame.mixer.music.play()

def play2():
    pygame.mixer.music.load("dontdothistome.mp3")
    pygame.mixer.music.play()

def play3():
    pygame.mixer.music.load("letsgetthisbread.mp3")
    pygame.mixer.music.play()

def play4():
    pygame.mixer.music.load("thisiswhyyoureincel.mp3")
    pygame.mixer.music.play()
    
def play5():
    pygame.mixer.music.load("oksweaty.mp3")
    pygame.mixer.music.play()


def play6():
    pygame.mixer.music.load("itsoverfor.mp3")
    pygame.mixer.music.play()

def play7():
    pygame.mixer.music.load("weirdflexbutok.mp3")
    pygame.mixer.music.play()

def play8():
    pygame.mixer.music.load("thisgameissobad.mp3")
    pygame.mixer.music.play()

def play9():
    pygame.mixer.music.load("imgoingtosaythenword.mp3")
    pygame.mixer.music.play()

def play10():
    pygame.mixer.music.load("iwishiwasdead.mp3")
    pygame.mixer.music.play()

def play11():
    pygame.mixer.music.load("accordingtothewelsconstitution.mp3")
    pygame.mixer.music.play()

def play12():
    pygame.mixer.music.load("gamersriseup.mp3")
    pygame.mixer.music.play()

def play13():
    pygame.mixer.music.load("letmesmokethisfagrealquick.mp3")
    pygame.mixer.music.play()

def play14():
    pygame.mixer.music.load("canthearyouoversilverstypewriter.mp3")
    pygame.mixer.music.play()


canthearyouoversilverstypewriter = Button(text="Can't hear you over silver's typewriter", command = play14)
canthearyouoversilverstypewriter.grid(row = 0, column = 0, padx = (10, 10), pady = (0, 10))

accordingtothewelsconstitution = Button(text="According to the WELS Constitution...", command = play11)
accordingtothewelsconstitution.grid(row = 0, column = 1, padx = (0, 10), pady = (0, 10))

letmesmokethisfagrealquick = Button(text="Let Me Smoke This Fag Real Quick", command = play13)
letmesmokethisfagrealquick.grid(row = 0, column = 2, padx = (0, 10), pady = (0, 10))

imgoingtosaythenword = Button(text="I'm Going to Say the N Word", command = play9)
imgoingtosaythenword.grid(row = 0, column = 3, padx = (0, 10), pady = (0, 10))

thisiswhyyoureincel = Button(text="This is Why You're Incel", command = play4)
thisiswhyyoureincel.grid(row = 1, column = 0, padx = (10, 10))

letsgetthisbread = Button(text="Let's Get This Bread", command = play3)
letsgetthisbread.grid(row = 1, column = 1, padx = (0, 10))

thisgameissobad = Button(text="This Game is so Bad", command = play8)
thisgameissobad.grid(row = 1, column = 2, padx = (0, 10))

dontdothistome = Button(text="Don't do This to me", command = play2)
dontdothistome.grid(row = 1, column = 3, padx = (0, 10))

weirdflexbutok = Button(text="Weird Flex, but ok", command = play7)
weirdflexbutok.grid(row = 2, column = 0, padx = (0, 10), pady = (10, 0))

iwishiwasdead = Button(text="I Wish I Was Dead", command = play10)
iwishiwasdead.grid(row = 2, column = 1, padx = (0, 10), pady = (10, 0))

gamersriseup = Button(text="Gamers Rise Up", command = play12)
gamersriseup.grid(row = 2, column = 2, padx = (0, 10), pady = (10, 0))

itsoverfor = Button(text="It's Over For...", command = play6)
itsoverfor.grid(row = 2, column = 3, padx = (0, 10), pady = (10, 0))

oksweaty = Button(text="Ok, Sweaty", command = play5)
oksweaty.grid(row = 3, column = 1, padx = (0, 10), pady = (10, 0))

whohurtyou = Button(text="Who Hurt You?", command = play1)
whohurtyou.grid(row = 3, column = 2, padx = (0, 10), pady = (10, 0))

#start this abomination
mainloop()
