# OPTION 1

needed_money = float(input())
available_money = float(input())

num_days = 0
num_days_spending = 0

can_save = True

while needed_money > available_money:
    action = input()
    saved_or_spent_money = float(input())
    num_days += 1
    if action == "spend":
        available_money -= saved_or_spent_money
        num_days_spending += 1
        if available_money < 0:
            available_money = 0
        if num_days_spending == 5:
            can_save = False
            break
    elif action == "save":
        available_money += saved_or_spent_money
        num_days_spending = 0
    # if available_money < 0:
    #     available_money = 0

if not can_save:
    print(f"You can't save the money.\n{num_days}")
else:
    print(f"You saved the money for {num_days} days.")

# OPTION 2

# needed_money = float(input())
# available_money = float(input())
#
# num_days = 0
# num_days_spending = 0
#
# while available_money < needed_money and num_days_spending < 5:
#     action = input()
#     saved_or_spent_money = float(input())
#     num_days += 1
#     if action == "spend":
#         available_money -= saved_or_spent_money
#         num_days_spending += 1
#         if available_money < 0:
#             available_money = 0
#     elif action == "save":
#         available_money += saved_or_spent_money
#         num_days_spending = 0
#
# if num_days_spending == 5:
#     print(f"You can't save the money.\n{num_days}")
# if available_money >= needed_money:
#     print(f"You saved the money for {num_days} days.")