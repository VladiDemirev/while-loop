cake_width = int(input())
cake_length = int(input())

cake_area = cake_width * cake_length

while cake_area > 0:
    user_input = input()
    if user_input != "STOP":
        cake_area -= int(user_input)
    else:
        break

if cake_area > 0:
    print(f"{cake_area} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_area)} pieces more.")
