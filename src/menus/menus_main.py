from os import system
from src.submenus import submenus

def menu_main():
    
    try:

        print("""
                1) Install tools of pentest
                2) Red dragon Tools
                3) System management 
                0) BACK
                -1) EXIT
                    
        """)

        option_main = int(input("Your option: "))

        if option_main == 1:
            ...
        elif option_main == 2:
            ...
        elif option_main == 3:
            ...
        elif option_main == 0:
            ...
        elif option_main == -1:
            ...
        else:
            system("clear")
            print("Invalid option. Try again.")
            menu_main()
                
    except Exception as error:

        print("Error: {}".format(error))
    

