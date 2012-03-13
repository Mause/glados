#this is a test GLaDOS promt
#the following variables define the ratio for the perimeters
# of the actual text
text_area=4/5

from threading import Thread
from Tkinter import *
import time
import os
import sys

#fh=open('aperture_logo.txt', 'rb')
#aperture_logo = fh.read()
#fh.close()

root=Tk()
# make it cover the entire screen
fullscreen=False
if fullscreen:
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: root.destroy())
root.title(string='admin@GLaDOS$')
# create the canvas, size in pixels
if fullscreen:
    canvas = Canvas(root, width = w, height = h)
else:
    canvas = Canvas(root, width = 1280, height = 720)
    
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)

def giffer(canvas):
    imagelist = os.listdir(os.getcwd()+'\\background')
    # create a list of image objects
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=(os.getcwd()+'\\background\\')+imagefile)
        giflist.append(photo)
    # loop through the gif image objects for a while
    lastimage=None
    for k in range(0, 1000):
        for gif in giflist:
            try:
                if lastimage != None: canvas.delete(lastimage)
            except TclError:
                pass
            if fullscreen:
                lastimage=canvas.create_image((1280/2), (720/2), image = gif)
            else:
                lastimage=canvas.create_image((1280/2), (720/2), image = gif)
            canvas.tag_lower(lastimage)
            canvas.update()
            time.sleep(0.05)


def write_text(canvas, text, y_in=0):
    text_colour = '#FAFA64'
    text_colour_active = '#FAFA32'
    position_x=60
    position_y=50
    for letter in text:
#        print letter,
        if str(letter) != '*':
            if str(letter) != '/':
                printed=canvas.create_text(position_x, position_y+y_in, text=letter, activefill=text_colour_active, fill=text_colour, font=("Terminus", 15, "bold"), width=12) #anchor='NW', offset="0,0", #, )
            else:
                time.sleep(0.09)
        position_x += 15
        #print position_x,':',position_y+y_in
        print letter,
        if str(letter) != '/' and str(letter) != '*':
            canvas.tag_raise(printed)
            canvas.update()
        if str(letter) != ' ' and str(letter) != '*' and str(letter) != '/':
            if str(letter) == '\n':
                for x in range(3):
                    underline=canvas.create_text(position_x-30, position_y+y_in, text='_', activefill=text_colour_active, fill=text_colour, font=("Terminus", 15, "bold"))
                    time.sleep(0.1)
                    canvas.delete(underline)
            else:
                underline=canvas.create_text(position_x, position_y+y_in, text='_', activefill=text_colour_active, fill=text_colour, font=("Terminus", 15, "bold"))
                time.sleep(0.09)
                canvas.delete(underline)
        if str(letter) == '*':
            print 'reseting canvas'
            position_x=60
            position_y=50
            canvas.delete(ALL)
            return 'reset'


def wait_and_exec(canvas):
    print 'started'
    time.sleep(1)
    lines_fh = open('lines.txt', 'rb')
    lines=lines_fh.readlines()
    y_in=0
    for line in lines:
        returned=write_text(canvas, line, y_in=y_in)
        y_in +=22
        time.sleep(0.5)
        if str(returned) == 'reset':
            y_in=0
    print '\nfinished'



giffery=Thread(target=giffer, args=(canvas,))
giffery.start()

print 'ready to start'

wait_and_exec(canvas)


root.mainloop()


