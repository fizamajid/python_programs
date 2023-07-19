

def display_phone_book(names, phone_numbers):
    pass


def search_phone_book(names, phone_numbers):
    pass

def delete_phone_entry(names, phone_numbers):
    pass

def add_phone_entry(names, phone_numbers):
    pass

def display_menu():
    print('1. Display phone book')
    print('2. Search phone book')
    


def main():
    names = ['neenu','ammu','pachi','thabu']
    phone_numbers = ['9746555182','7907784236','0524514507','0565801213']

    display_menu()
    choice = int(input('Choice: '))
    while choice != 5:
        
        if choice == 1:
            display_phone_book(names, phone_numbers)
        elif choice == 2:
            pass
        elif choice == 3:
            pass


        display_menu()
        choice = int(input('Choice: '))



    


main()



