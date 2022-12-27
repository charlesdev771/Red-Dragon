from os import system
from time import sleep
from src.submenus.submenus import submenu_one, submenu_two, submenu_three

def menu_main():
    
    try:

        print("""
                1) Install tools of pentest
                2) Red dragon Tools
                3) System management 
                -1) EXIT
                    
        """)

        option_main = int(input("Your option: "))

        if option_main == 1:
            
            submenu_one()

        elif option_main == 2:
            
            submenu_two()

        elif option_main == 3:
            
            submenu_three()

        elif option_main == -1:

            print("Goodbye...")
            sleep(1)
            system("clear")

        else:
            system("clear")
            print("Invalid option. Try again.")
            menu_main()
                
    except Exception as error:

        print("Error: {}".format(error))
    

