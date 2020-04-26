import time
import numpy as np
import sys

# Define constants
time_step = 0.1  # In seconds. Default value

if len(sys.argv) > 1:
    time_step = float(sys.argv[1])

time_old = time.time()
time_new = time_old
sleeptime = 0

n_turtles = 4
n_lines = 5 + n_turtles

creatures = ["🐢", "🐌", "🐊", "🐇"]  # len >= n_turtles

# Initialize scores and flags
turtle_win = ["❌"]*n_turtles
turtle_score = [0]*n_turtles
turtle_victories = [0]*n_turtles
equation_solved = True
victoryflag = False
running = True

print("\n"*n_lines)  # Clear empty lines for printing

while running is True:
    turtle_win = ["❌"]*n_turtles
    time_old = time_new + sleeptime

    if equation_solved is True:
        # Generate new random numbers if solved flag is true
        equation = np.random.randint(1, 10, 2)
        solution = np.sum(equation)
        equation_solved = False

    turtle_number = np.random.randint(1, 20, n_turtles)

    for i in range(n_turtles):
        # Check if turtle has won
        if turtle_number[i] == solution:
            turtle_win[i] = "✅"
            equation_solved = True
            turtle_score[i] += 1
            if turtle_score[i] == 20:
                turtle_victories[i] += 1
                victoryflag = True

    # print the interface.
    print("\r\033[A"*n_lines, end="")  # Go back up n_lines
    print("             Turtle Game")
    print(" Race to the finish - Place your bets ")
    print("")
    print(f" Problem: {equation[0]} + {equation[1]} = ?")
    print("")
    for i in range(n_turtles):
        # Print line without turtle, then add turtle on top to override flag on
        # victory.
        print(f"{' '*21}🏁{turtle_number[i]:3}{turtle_win[i]} "
              f"{turtle_victories[i]:5} 🏆", end="\r")
        print(f"{'='*turtle_score[i] + creatures[i]}")

    # Time to sleep in order to add up to time_step.
    time_new = time.time()
    sleeptime = time_step - (time_new - time_old)
    if sleeptime > 0:
        time.sleep(sleeptime)

    if victoryflag is True:
        time.sleep(5*time_step)
        turtle_score = [0]*n_turtles
        time_old = time.time()
        time_new = time_old
        victoryflag = False
