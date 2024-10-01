import time
from adafruit_circuitplayground import cp

# Set up the Circuit Playground LEDs
cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

def set_color(color):
    for i in range(10):
        cp.pixels[i] = color
    cp.pixels.show()

while True:
    #  options for user to select the function
    print("Choose an option:")
    print("1: Red color")
    print("2: Green color")
    print("3: Blue color")
    print("Press 'q' to quit")

    # input section for user
    user_input = input("Enter your choice: ")

    if user_input.lower() == 'q':
        print("Exiting the program.")
        break

    # invalid inputs
    try:
        choice = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3, or 'q' to quit.")
        continue

    # if function to to select choices mention colors like red,green,blue
    if choice ==1:
        set_color((255,0,0))  # Red
    elif choice ==2:
        set_color((0, 255, 0))  # Green
    elif choice == 3:
        set_color((0, 0, 255))  # Blue
    else: # else function for invalid input
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Wait a bit before asking for input again
    time.sleep(0.5)
