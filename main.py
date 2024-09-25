import turtle
import pandas as pd
from stateswriter import Stateswriter

IMAGE = 'blank_states_img.gif'
CSV_FILE = '50_states.csv'
MISSED_STATES_FILE_NAME = 'missed_states.csv'

# Set up screen
screen = turtle.Screen()
screen.title('Guessing Game\n United States')
screen.addshape(IMAGE)
us_image = turtle.Turtle(shape=IMAGE)


writer = Stateswriter()



# Create a pandas DataFrame from CSV_FILE
df = pd.read_csv(CSV_FILE)

# Store all the states names
all_states = df['state'].to_list()

# This variable will store all the states the user missed to write
all_states_remaining = all_states

# Store all correct answers
guessed_states = []



while len(guessed_states) <= 50:

    #  Pop a prompt and store the user answer
    user_answer = screen.textinput(title=f'{len(guessed_states)}/50 Correct States', prompt='Guess a state name').title()
    
    
    if user_answer == 'Exit':
    # Stop the game
        break

    if user_answer in all_states_remaining:

        # Remove the state guessed by user from all_states_remaining
        all_states_remaining.remove(user_answer)      
        guessed_states.append(user_answer)


        # Get coordinates of the states stored in CSV_FILE
        state_x = df[df.state == user_answer].x.item()     # 'item()' method gets the first value of a specified column row ( x in this case ) ignoring the index
        state_y = df[df.state == user_answer].y.item()
        state_coords = (state_x, state_y) # Set x and y into a tuple variable

        # writer object draws the state name at its coordinates on the screen
        writer.draw_state_name(state_name=user_answer, coords=state_coords) 
        
    else:
        print('Wrong guess')
    


# Store the missing states into a file named 'missed_states.csv'
pd.DataFrame(all_states_remaining).to_csv(MISSED_STATES_FILE_NAME) # pandas also can send lists to csv file, not only dicts
