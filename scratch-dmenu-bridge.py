from scratra3 import *
import dmenu

@start
def whenstart(scratch):
    scratch.choices = []

@broadcast("send-choices")
def sendChoices(scratch):
    scratch.choices = []

@update("choice")
def addChoice(scratch, value):
    try:
        scratch.choices.append(str(value))
    except AttributeError:
        scratch.choices = [str(value)]

@broadcast("choices-sent")
def makeChoice(scratch):
    print(scratch.choices)
    choice = dmenu.show(scratch.choices)
    scratch.sensor.__setitem__("text-response",str(choice))
    scratch.broadcast("process-choice")

run()
