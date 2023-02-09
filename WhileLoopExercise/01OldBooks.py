# OPTION 1

# fav_book = input()
#
# choice = None
# books_count = 0
#
# while True:
#     choice = input()
#     if choice != fav_book or choice != "No More Books":
#         books_count += 1
#     if choice == fav_book or choice == "No More Books":
#         break
#
# if choice == fav_book:
#     print(f"You checked {books_count - 1} books and found it.")
# if choice == "No More Books":
#     print(f"The book you search is not here! \nYou checked {books_count - 1} books.")

# OPTION 2

fav_book = input()

books_count = 0
is_book_found = False

choice = input()

while choice != "No More Books":
    if choice == fav_book:
        is_book_found = True
        print(f"You checked {books_count} books and found it.")
        break

    books_count += 1
    choice = input()

if not is_book_found:
    print(f"The book you search is not here! \nYou checked {books_count} books.")