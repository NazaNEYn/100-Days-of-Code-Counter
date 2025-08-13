# The main program imports the two counter classes you've created.
from count_up import CounterUp
from count_down import CounterDown

# This section of the code handles user input and initializes the program.
# It uses a while loop with a try-except block to ensure the user enters a valid number.
while True:
    try:
        user_max_day = int(input("How many days of code are you doing?\n"))
        break  # Exit the loop if a valid number is entered.
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Print an encouraging message using an f-string.
print(f"Awesome! You're committed to a {user_max_day}-day challenge.")

# Create a CounterUp object, starting its count from 0.
counter_up = CounterUp(0)

# Create a CounterDown object, starting its countdown from the user's max day.
counter_down = CounterDown(user_max_day)

# This is the main control loop for your program.
is_counting = True
while is_counting:
    # Get user input. We're checking for an empty string, so .lower() isn't needed.
    user_input = input("Press ENTER to count!\n")

    # Check if the user pressed Enter.
    if user_input == "":
        # Call both the count_up and count_down methods and store their return values.
        # This ensures both counters are updated on every step.
        up_result = counter_up.count_up(user_max_day)
        down_result = counter_down.count_down()

        # The loop continues only if BOTH return True. The 'and' operator
        # will evaluate to False if either one returns False, stopping the loop.
        is_counting = up_result and down_result

        # Print a decorative separator to make the output clear.
        print("-------------")
        print("#100DaysOfCode")
        print("-------------")
    else:
        # Inform the user if they entered something other than Enter.
        print("Invalid input. Try Again!")
