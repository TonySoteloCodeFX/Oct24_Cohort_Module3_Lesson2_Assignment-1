library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    print("-" * 50)
    new_title = input("Enter Book Title:  ")
    new_author = input("Enter Author: ")
    formatted_tuple = new_title, new_author
    if formatted_tuple in library:
        print("-" * 50)
        print("That book is already in your library.")
    else:
        library.append(formatted_tuple)

def display_all():
    for index, book in enumerate(library):
        print("-" * 50)
        title = book[0]
        author = book[1]
        print(f"Book {index + 1}: '{title}' by {author}")

keep_running = True
while keep_running:
    try:
        print("-" * 50)
        print("Menu")
        print("1. Add A Book")
        print("2. Display All Books")
        print("3. Quit")
        print("-" * 50)
        option = int(input("Enter Option: "))
        if option == 1:
            add_book()
        elif option == 2:
            display_all()
        elif option == 3:
            print("-" * 50)
            print("Goodbye!")
            keep_running = False
        else:
            print("-" *50)
            print("That is not an option. Try again.")
    except ValueError:
        print("-" * 50)
        print("That is not an option. Please try again.")