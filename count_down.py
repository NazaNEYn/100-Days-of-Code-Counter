class CounterDown:
    """
    A simple class to handle a countdown from a given number to zero.

    This class keeps track of the current count and provides a method to
    decrement the number and check if the countdown is finished.
    """

    def __init__(self, num_down):
        """
        Initializes the CounterDown object with a starting number.

        Args:
            num_down (int): The starting number for the countdown.
        """
        # The num_down variable stores the current number in the countdown.
        self.num_down = num_down

    def count_down(self):
        """
        Decrements the counter by one and checks if the countdown is complete.

        Returns:
            bool: False if the counter has reached 0, otherwise True.
        """
        # Subtract 1 from the current count.
        self.num_down -= 1

        # Print the updated count using an f-string.
        print(f"{self.num_down} more to go!")

        # Check if the count has reached zero.
        if self.num_down == 0:
            # If the count is zero, return False to stop the main loop.
            return False
        else:
            # If the count is not zero, return True to continue the main loop.
            return True
