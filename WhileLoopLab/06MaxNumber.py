from sys import maxsize

max_num = - maxsize

while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num > max_num:
        max_num = num

print(max_num)



