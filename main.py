from count_up import CounterUp
from count_down import CounterDown
from progressbar_art import create_progress_bar

while True:
    try:
        user_max_day = int(input("How many days of code are you doing?\n"))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")


print(f"Awesome! You're committed to a {user_max_day}-day challenge.")
print("----------------------------------------")
print("\n")

counter_up = CounterUp(0)

counter_down = CounterDown(user_max_day)

is_counting = True
while is_counting:
    user_input = input("Press ENTER to count!\n")

    if user_input == "":
        up_result = counter_up.count_up(user_max_day)
        down_result = counter_down.count_down()

        is_counting = up_result and down_result

        print(create_progress_bar(counter_up.num_up, user_max_day))
        print(f"#{user_max_day}DaysOfCode")
    else:
        print("Invalid input. Try Again!")
