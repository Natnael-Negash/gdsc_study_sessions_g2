"""Develop a program that checks if a user-inputted word
 is a palindrome. A palindrome is a word that reads
   the same backward as forward (e.g., "radar").
word = input("please enter the word to check")
reverse_word = word[::-1]
if reverse_word == word:
    print("the word "  +  word  +  " is a palindrome.")
else:
    print("the word " + word + " is not palindore,", end="\n" "because " + reverse_word + " is not equal to " + word)"""

from scipy.optimize import fsolve
import numpy as np

# Given values
x = 60       # horizontal distance in feet
h_Q = 6.5    # height at which the quarterback releases the ball in feet
h_R = 7      # height at which the receiver catches the ball in feet
g = 32.2     # acceleration due to gravity in ft/s^2
v0 = 50      # initial velocity in ft/s

# Function representing the projectile motion equation
def fun(theta):
    return x * np.tan(theta) - (1/2) * (x**2 * g) / (v0**2 * np.cos(theta)**2) + h_Q

# Solve for the launch angle theta when y(theta) = h_R
theta_solution = fsolve(lambda theta: fun(theta) - h_R, 0)

# Display the result in degrees
theta_degrees = np.degrees(theta_solution[0])
print(f'The launch angle theta is approximately: {theta_degrees} degrees')
