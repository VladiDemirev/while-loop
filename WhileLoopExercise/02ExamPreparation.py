# OPTION 1

bad_grades = int(input())

bad_grades_counter = 0
text_counter = 0

sum_grades = 0
num_grades = 0

text = input()
last_assignment = None

while text != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades:
            print(f"You need a break, {bad_grades_counter} poor grades.")
            break

    sum_grades += grade
    num_grades += 1
    text_counter += 1
    text = input()
    if text != "Enough":
        last_assignment = text

if text == "Enough":
    print(f"Average score: {sum_grades / num_grades:.2f}")
    print(f"Number of problems: {text_counter}")
    print(f"Last problem: {last_assignment}")

# OPTION 2

bad_grades = int(input())

has_failed = False
num_problems = 0
sum_grades = 0
num_grades = 0
num_bad_grades = 0
last_problem = None

while num_bad_grades < bad_grades:
    problem = input()
    if problem == "Enough":
        break
    grade = int(input())
    if grade <= 4:
        num_bad_grades += 1
        if num_bad_grades == bad_grades:
            has_failed = True
            break
    sum_grades += grade
    num_problems += 1
    num_grades += 1
    last_problem = problem

if not has_failed:
    print(f"Average score: {sum_grades / num_grades:.2f}")
    print(f"Number of problems: {num_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {num_bad_grades} poor grades.")


