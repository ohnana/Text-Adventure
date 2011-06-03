#!/usr/bin/python
# Text Adventure -- Made by Ohnana, #/g/sicp on Rizon IRC

a={'W':"What did you say?", 'r':"Excellent choice."}

import sys
import time

print "Welcome to the Text Adventure written by Ohnana. Your choices for each step are in all capitals. All words in capitals are valid choices. Type the choices in all caps. Do you understand? YES or NO?"

correct = 'YES'
wrong = 'NO'

while True:
    answer = raw_input().upper()
    if answer == correct:
        print "Then let\'s begin!"
        break
    elif answer == wrong:
        print "Apparently you do. Let\'s begin."
        break
    else:
        print 'What did you say? Maybe you should read the above again.'
        continue
print "You are in a room, oddly enough. The \'odd part\' is that it's not your room. You can EXPLORE, CRY, or LEAVE."

correct = 'EXPLORE'
derp = 'CRY'
wrong = 'LEAVE'

while True:
    answer = raw_input('You will ').upper()
    if answer == correct:
        a['r']
        break
    elif answer == wrong:
        print 'But you can\'t! Look around for a door, maybe?'
        continue
    elif answer == derp:
        print 'Stop that.'
        continue
    else:
        a['W']
        continue

print 'There are many things in this room, but no door. A book, a hat, and a computer to name a few. You can look at the BOOK, the HAT, or the COMPUTER.'

clue = 'BOOK'
correct = 'COMPUTER'
derp = 'HAT'

while True:
    answer = raw_input('You will look at the ').upper()
    if answer == correct:
        a['r']
        break
    elif answer == clue:
        print 'The book is titled \"The Top 10 Best Proprietary Licenses!\" It\'s a decidedly silly book, and you thumb through it briefly before putting it down.'
        continue
    elif answer == derp: 
        print "The hat is carnivorous. It clamps itself on your arm, releasing natural toxin into your body. After you pass out, it slowly digests your body. You are now dead. The adventure is over."
        time.sleep(20) #Is this too much time to read the above statement? Or too little?
        sys.exit()
    else:
        a['W']
        continue
print 'You turn on the computer, and it hums while booting. Maybe it could shed some light on this situation. A small Apple appears on the screen, along with a spinning wheel. It\'s a Macintosh. Interesting.'
print "The familiar chord plays, and a dialog box pops up. \"Please enter your name and SSN!\" it demands. You can SHUTDOWN the computer, FORGE your name, GIVE it the information, or MASTURBATE."

correct = 'GIVE'
wrong = 'SHUTDOWN'
clue = 'FORGE' 
derp = 'MASTURBATE'

while True: 
    answer = raw_input('You will ').upper()
    if answer == correct:
        a['r']
        break
    elif answer == wrong:
        print 'You shake your head in disbelief. Social Security? Really? You press the power button, but nothing happens. You try to press and hold, but the dialog box just blinks at you. It is very insistent.'
    elif answer == clue:
        print 'You type in a random name and series of numbers. The computer thinks for a minute, then the box changes: \"Under Stature 3.245 of the Trusted Computing Act, it is illegal to forge digital credentials. Failure to comply will result in immediate location and arrest. You have three (3) attempts left.\" Now you\'re in deep trouble.'
        continue
    elif answer == derp:
        print 'Hold the story for a second. You want to fap to Apple stuff? No. NO.'
        continue
    else:
        a['W']
        
print "You begrudgingly type in your name and social security number. This time, it accepts the information, and you are greeted by a gray and silver flag with the Macintosh logo on it. The Apple Corporation had a flag? Since when? The dock appears, with your picture as one of the dock icons. You click on it, and an entire profile comes up. It's scarily accurate, and almost completely true. The age field is horribly inaccurate, though. It shows the number 56, even though you know that you're not that old. You close the window and try a different program. It's a web browser, with only four buttons. \"Welcome!\" the screen says. \"This is a new experience in computing! The Computing of Trust!\" There was that word again. There are three buttons. One is named \"LEARN about Trusted Computing!\" One is named \"REPORT an offender against your security and safety!\" One is called \"USE the trusted web!\" The last is called \"BROWSE the unregulated web! If you do this, you could be hacked!\" Which button do you select?"

opt1 = 'LEARN'
opt2 = 'REPORT'
opt3 = 'BROWSE'
finalopt = "USE"
x = 0
#while True:
#    answer = raw_input('You choose the button marked ").upper()
#    if (answer == opt1 and x < 4):
#        print "A slideshow comes up with cheesy music. It talks about how wonderful and safe you are, because you'll always know who you're talking to online. \'Everyone prospers when we're safe and guarded,\' the final slide says. After the presentation (which really didn\'t contain much information for the number of slides it had), you are returned to the previous page."
#        x += 1
#        continue
#    if (answer == 'REPORT'
#THIS SECTION IS UNDER CONSTRUCTION

# while (selectedOpts[1] == false || selectedOpts[2] == false || selectedOpts[3] == false) { if (user picks opt1) {selectedOpts[1] = true} elseif (user picks opt2) {selectedOpts[2] = true} etc. }
#so, i have 3 options. I want the user to try all of them. Everytime the user selects one, increment a variable by 1. If the variable equals three, exit
#(08:31:49 PM) cocks: what if they pick the same option three times?
#(08:33:07 PM) ohnana: i guess i could write one big cluster fuck of a loop that covers all the permutations, subtracting an option each time
