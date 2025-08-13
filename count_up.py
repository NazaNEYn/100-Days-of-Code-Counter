class CounterUp:
    """
    A simple class to handle counting up from a starting number to a maximum number.

    This class keeps track of the current day and provides a method to
    increment the count and check if the goal has been reached.
    """

    def __init__(self, num_up):
        """
        Initializes the CounterUp object with a starting number.

        Args:
            num_up (int): The number to start the count from, usually 0.
        """
        # The num_up variable stores the current day number.
        self.num_up = num_up

    def count_up(self, user_max_day):
        """
        Increments the counter by one and checks if the maximum day is reached.

        Args:
            user_max_day (int): The target day number for the challenge.

        Returns:
            bool: False if the counter has reached the max day, otherwise True.
        """
        # Add 1 to the current day count.
        self.num_up += 1

        # Print the current day count using an f-string.

        if self.num_up == 1:
            print(f"{self.num_up} day down")
        else:
            print(f"{self.num_up} days down")

        # Check if the current day has reached the user's max day.
        if self.num_up == user_max_day:
            # If so, print a congratulatory message and return False to stop the main loop.
            print("You've reached your maximum day! Great job! 🎉")
            return False
        else:
            # If not, return True to keep the main loop running.
            return True
