print("Nguyễn Xuân Dịu")
print("235752021610078")
# Import the modules
import tkinter
import random

# List of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# The game time left, initially 120 seconds
timeleft = 120

# Function that will start the game
def startGame(event):
    global timeleft
    if timeleft == 120:
        # Start the countdown timer
        countdown()
    # Run the function to choose the next colour
    nextColour()

# Function to choose and display the next colour
def nextColour():
    global score
    global timeleft

    # If a game is currently in play
    if timeleft > 0:
        # Make the text entry box active
        e.focus_set()

        # If the colour typed is equal to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 2  # Increase score by 2 for correct answer
        else:
            score -= 1  # Decrease score by 1 for wrong answer

        # Clear the text entry box
        e.delete(0, tkinter.END)

        # Shuffle the colours list
        random.shuffle(colours)

        # Change the colour to type by changing the text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # Update the score
        scoreLabel.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft

    # If a game is in play
    if timeleft > 0:
        # Decrement the timer
        timeleft -= 1

        # Update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))

        # Run the function again after 1 second
        timeLabel.after(1000, countdown)

# Driver Code

# Create a GUI window
root = tkinter.Tk()

# Set the title
root.title("COLORGAME")

# Set the size
root.geometry("375x200")

# Add an instructions label
instructions = tkinter.Label(root, text="Type in the colour of the words, not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

# Add a time left label
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

# Add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Add a text entry box for typing in colours
e = tkinter.Entry(root)

# Run the 'startGame' function when the Enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# Set focus on the entry box
e.focus_set()

# Start the GUI
root.mainloop()
