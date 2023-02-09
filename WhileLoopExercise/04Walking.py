# OPTION 1

GOAL_STEPS = 10000
completed_steps = 0
user_input = input()
goal_is_completed = False

while completed_steps < GOAL_STEPS:
    if user_input != "Going home":
        user_input = int(user_input)
        completed_steps += user_input
    if user_input == "Going home":
        user_input = int(input())
        completed_steps += user_input
        if completed_steps >= GOAL_STEPS:
            goal_is_completed = True
            break
        else:
            break
    if completed_steps >= GOAL_STEPS:
        goal_is_completed = True
        break
    user_input = input()

if goal_is_completed:
    print(f"Goal reached! Good job!")
    print(f"{abs(completed_steps - GOAL_STEPS)} steps over the goal!")
else:
    print(f"{abs(completed_steps - GOAL_STEPS)} more steps to reach goal.")

# OPTION 2

# GOAL_STEPS = 10000
# completed_steps = 0
#
# while completed_steps < GOAL_STEPS:
#     user_input = input()
#     if user_input != "Going home":
#         completed_steps += int(user_input)
#     else:
#         completed_steps += int(input())
#         break
#
# if completed_steps >= GOAL_STEPS:
#     print(f"Goal reached! Good job!")
#     print(f"{abs(completed_steps - GOAL_STEPS)} steps over the goal!")
# else:
#     print(f"{abs(completed_steps - GOAL_STEPS)} more steps to reach goal.")