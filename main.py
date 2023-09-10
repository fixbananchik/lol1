from main_menu import main_menu_print
from facts_menu import print_facts_menu
from request1 import response1
from request2 import response2
from response3 import response3
from response4 import response4

while True:
    main_menu_print()
    a = int(input("Введите цифру"))
    if a == 1:
        print_facts_menu()
        c = int(input("Введите цифру"))
        if c == 1:
            print(response1())
        elif c == 2:
            print(response2())
            
    elif a==2:
        b = str(input("Введите число"))
        print_facts_menu()
        c = int(input("Введите цифру"))
        if c == 1:
            print(response3(b))
        elif c == 2:
            print(response4(b))
            
    else:
        break
