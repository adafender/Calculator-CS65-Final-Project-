''' Final Project: Simple Calculator - Ada Fender
    
    External source: https://www.brianheinold.net/python/python_book.html#chapter_GUI1

        I used this source to learn more about GUIs and also used their certain way (syntax)
        of coding with GUIs which differs from what we went over in class. '''


from tkinter import *
#define what buttons on calculator will be (except clear all (AC), because of placement)
calc_buttons = '789/456*123-0=+'

#calculator function
def calculator(button_pressed):
    '''
    This function is called when any of the buttons on the calculator are pressed, and gives
    the appropriate output. '=' will evaluate the entry, 'AC' will clear the entry, and any other
    button will add to the entry. 'error' will output if you try to divide by 0.
    The parameter button_pressed refers to whichever button was pressed on the calculator.
    '''
    #use cget to get the current state of the entry widget
    current_entry = entry.cget('text')
    if button_pressed == '=':
        if '/0' in str(current_entry):
            entry.configure(text='error')    
        else:
            result = eval(current_entry)
            entry.configure(text=result)
    elif button_pressed == 'AC':
        entry.configure(text='')
    else:
        entry.configure(text=str(current_entry)+str(button_pressed))

#create GUI window and title it
root = Tk()
root.title("Calculator")

#create label where user input goes
entry = Label(font=('Helvetica', 32))
entry.grid(row=0, column=0, columnspan=3)

#create button list
buttons = [0]*15
#place buttons in window
clear = Button(text='AC',
               command = lambda: calculator('AC'), font=('Helvetica', 32))
clear.grid(row=0, column=3)
count=-1
for i in range(0,4):
    count+=1
    buttons[i] = Button(text=calc_buttons[i],
                        command = lambda x=calc_buttons[i]: calculator(x), font=('Helvetica', 32))
    buttons[i].grid(row=1, column=count)
count=-1
for i in range(4,8):
    count+=1
    buttons[i] = Button(text=calc_buttons[i],
                        command = lambda x=calc_buttons[i]: calculator(x), font=('Helvetica', 32))
    buttons[i].grid(row=2, column=count)
count=-1
for i in range(8,12):
    count+=1
    buttons[i] = Button(text=calc_buttons[i],
                        command = lambda x=calc_buttons[i]: calculator(x), font=('Helvetica', 32))
    buttons[i].grid(row=3, column=count)
count=0
for i in range(12,15):
    count+=1
    buttons[i] = Button(text=calc_buttons[i],
                        command = lambda x=calc_buttons[i]: calculator(x), font=('Helvetica', 32))
    buttons[i].grid(row=4, column=count)
    
mainloop()