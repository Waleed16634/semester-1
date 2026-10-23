"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Waleed Khan 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
state_time = 0

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

while systime < maxtime:
    systime = systime + 1
    state_time = state_time + 1

    if state_time == states[state]:
        state_time = 0

        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        else:
            state = "red"

    print(f"Time {systime:03} State {state}")
