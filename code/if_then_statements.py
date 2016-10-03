# Created by: Hamza Salman
# Course: ICS3U
# Created: September 2016
# This program is used to learn if then statements

import ui

from numpy import random

number_to_guess = random.randint(1,10)
print number_to_guess

def check_touch_up_inside(sender):
    # check the number of students from constant
    global number_to_guess
    number_input = int(view['number_textfield'].text)
    if number_input == number_to_guess:
        view['output_label'].text = 'Thats the right number!'
    else:
    	view['output_label'].text = 'Thats the wrong number!'
    
view = ui.load_view()
view.present('full_screen')
