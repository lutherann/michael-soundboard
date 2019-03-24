from tkinter import *
import pygame

root = Tk()
root.resizable(False, False)
root.title("Michael Soundboard")


pygame.mixer.init()

def play(arg):
    pygame.mixer.music.load(arg)
    pygame.mixer.music.play()

canthearyouoversilverstypewriter = Button(text="Can't hear you over silver's typewriter", command = lambda: play("canthearyouoversilverstypewriter.mp3"))
canthearyouoversilverstypewriter.grid(row = 0, column = 0, padx = (10, 10), pady = (0, 10))

accordingtothewelsconstitution = Button(text="According to the WELS Constitution...", command = lambda: play ("accordingtothewelsconstitution.mp3"))
accordingtothewelsconstitution.grid(row = 0, column = 1, padx = (0, 10), pady = (0, 10))

letmesmokethisfagrealquick = Button(text="Let Me Smoke This Fag Real Quick", command = lambda: play("letmesmokethisfagrealquick.mp3"))
letmesmokethisfagrealquick.grid(row = 0, column = 2, padx = (0, 10), pady = (0, 10))

imgoingtosaythenword = Button(text="I'm Going to Say the N Word", command = lambda: play("imgoingtosaythenword.mp3"))
imgoingtosaythenword.grid(row = 0, column = 3, padx = (0, 10), pady = (0, 10))

thisiswhyyoureincel = Button(text="This is Why You're Incel", command = lambda: play("thisiswhyyoureincel.mp3"))
thisiswhyyoureincel.grid(row = 1, column = 0, padx = (10, 10))

letsgetthisbread = Button(text="Let's Get This Bread", command = lambda: play("letsgetthisbread.mp3"))
letsgetthisbread.grid(row = 1, column = 1, padx = (0, 10))

thisgameissobad = Button(text="This Game is so Bad", command = lambda: play("thisgameissobad.mp3"))
thisgameissobad.grid(row = 1, column = 2, padx = (0, 10))

dontdothistome = Button(text="Don't do This to me", command = lambda: play("dontdothistome.mp3"))
dontdothistome.grid(row = 1, column = 3, padx = (0, 10))

weirdflexbutok = Button(text="Weird Flex, but ok", command = lambda: play("weirdflexbutok.mp3"))
weirdflexbutok.grid(row = 2, column = 0, padx = (0, 10), pady = (10, 0))

iwishiwasdead = Button(text="I Wish I Was Dead", command = lambda: play("iwishiwasdead.mp3"))
iwishiwasdead.grid(row = 2, column = 1, padx = (0, 10), pady = (10, 0))

gamersriseup = Button(text="Gamers Rise Up", command = lambda: play("gamersriseup.mp3"))
gamersriseup.grid(row = 2, column = 2, padx = (0, 10), pady = (10, 0))

itsoverfor = Button(text="It's Over For...", command = lambda: play("itsoverfor.mp3"))
itsoverfor.grid(row = 2, column = 3, padx = (0, 10), pady = (10, 0))

oksweaty = Button(text="Ok, Sweaty", command = lambda: play("oksweaty.mp3"))
oksweaty.grid(row = 3, column = 1, padx = (0, 10), pady = (10, 0))

whohurtyou = Button(text="Who Hurt You?", command = lambda: play("whohurtyou.mp3"))
whohurtyou.grid(row = 3, column = 2, padx = (0, 10), pady = (10, 0))

#start this abomination
mainloop()
