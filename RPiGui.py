from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

## our LED hardware ##
red = LED(4)
blue = LED(17)
green = LED(18)

## LEDs toggle function ##
def redToggle():
    if blue.is_lit:
        blue.off()
    if green.is_lit:
        green.off()
    if red.is_lit:
        red.off()
        ledRadBut1["text"] = "On"
    else:
        red.on()
        ledRadBut1["text"] = "Off"
        ledRadBut2["text"] = "Blue"
        ledRadBut3["text"] = "Green"
def blueToggle():
    if red.is_lit:
        red.off()
    if green.is_lit:
        green.off()
    if blue.is_lit:
        blue.off()
        ledRadBut2["text"] = "On"
    else:
        blue.on()
        ledRadBut2["text"] = "Off"
        ledRadBut1["text"] = "Red"
        ledRadBut3["text"] = "Green"

def greenToggle():
    if red.is_lit:
        red.off()
    if blue.is_lit:
        blue.off()
    if green.is_lit:
        green.off()
        ledRadBut3["text"] = "On"
    else:
        green.on()
        ledRadBut3["text"] = "Off"
        ledRadBut2["text"] = "Blue"
        ledRadBut1["text"] = "Red"
## GUI DESIGN ##
window = Tk()
window.geometry("430x25")
window.title("Led Radio Toggle")
guiFont = tkinter.font.Font(family = 'Helvetica',
                            size = 12, weight = "bold")
### BUTTONS ###
ledRadBut1 = Radiobutton(window, text = 'Red', font = guiFont,
                    command = redToggle, bg = 'bisque',height = 1,
                    width = 12)
ledRadBut2 = Radiobutton(window, text = 'Blue', font = guiFont,
                    command = blueToggle, bg = 'bisque',height = 1,
                    width = 12)
ledRadBut3 = Radiobutton(window, text = 'Green', font = guiFont,
                    command = greenToggle, bg = 'bisque',height = 1,
                    width = 12)
ledRadBut1.grid(row = 0, column = 1)
ledRadBut2.grid(row = 0, column = 2)
ledRadBut3.grid(row = 0, column = 3)

