
import os
def display_phone_book(names, phone_numbers):


    print('names:phone numbers')
    i = 0
    while i < len(names):
        print(i + 1, names[i], ':' , phone_numbers[i])
        i += 1



def search_phone_book(names, phone_numbers):
    search_name = input('Enter the number you want to search:')
    for n in search_name:
        if n == names[0]:
            print(phone_numbers[0])
            break
        elif n == names[1]:
            print(phone_numbers[1])
            break
        elif n == names[2]:
            print(phone_numbers[2])
            break
        else:
            print(phone_numbers[3])
            break

def delete_phone_entry(names, phone_numbers):
    name = print('Enter the name you want to delete:')
    i = names.index(name)
    del names[i]
    del phone_numbers[i]
    

def add_phone_entry(names, phone_numbers):
    new_name = input('Enter the name you wanted to add:')
    new_num = input('Enter the number: ')
    names.append(new_name)
    phone_numbers.append(new_num)   

def display_menu():
    os.system('clear')
    print('*' * 40)
    print('Main Menu')
    print('*' * 40)
    print('1. Display phone book')
    print('2. Search phone book')
    print('3. delete_phone_entry')
    print('4. add_phone_entry')
    print('*' * 40)
    


def main():
    names = ['neenu','ammu','pachi','thabu']
    loop_continue = 'y'
    phone_numbers = ['9746555182','7907784236','0524514507','0565801213']
    
 
    
    while  loop_continue == 'y':

        display_menu()
        choice = int(input('Choice:1/2/3/4:'))
        
        if choice == 1:
            display_phone_book(names, phone_numbers)
        elif choice == 2:
            search_phone_book(names, phone_numbers)
        elif choice == 3:
            delete_phone_entry(names, phone_numbers)
        elif choice == 4:
            add_phone_entry(names, phone_numbers)
        else:
            break

        
        loop_continue = input('Do you want to continue(y/n):')


        
       



    


main()



