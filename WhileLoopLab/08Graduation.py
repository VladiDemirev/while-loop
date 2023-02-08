# student_name = input()
#
# current_class = 1
# average = 0
# fails = 0
#
# while True:
#     grade = float(input())
#
#     if grade < 4.00:
#         fails += 1
#         if fails >= 2:
#             break
#         continue
#
#     average += grade
#     current_class += 1
#
#     if current_class > 12:
#         break
#
# if fails >= 2:
#     print(f"{student_name} has been excluded at {current_class} grade")
# else:
#     print(f"{student_name} graduated. Average grade: {average / 12:.2f}")