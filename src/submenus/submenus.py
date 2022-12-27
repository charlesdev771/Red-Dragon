
from os import system
from src.scripts.get_information_about_system import get_information_about_system
from time import sleep

def submenu_one():

    try:

        print("""
            
            1) Install arpspoof

            2) Install crunch
            
            3) Install dig
            
            4) Install dnsenum
            
            5) Install dnsrecon
            
            6) Install dnsmap
            
            7) Install dnsspoof
            
            8) Install ettercap
            
            9) Install fierce
            
            10) Install hydra
            
            11) Install iptables
            
            12) Install maltego
            
            13) Install medusa
            
            14) Install metasploit
            
            
            15) Install mitmf
            
            16) Install netcat
            
            17) Install netdiscover
            
            18) Install nmap
            
            19) Install netcat
            
            20) Install sslsplit
            
            21) Install sslsplit
            
            22) Install tcpdump
            
            23) Install zenmap
            
            0) BACK
            
           -1) EXIT 
            
            """)

        secundary_option = int(input("Your option: "))

        if secundary_option == 1:

            system("sudo apt install arpspoof")

        elif secundary_option == 2:

            system("sudo apt upgrade crunch")

        elif secundary_option == 3:

            system("sudo apt install dig")

        elif secundary_option == 4:

            system("sudo apt install dnsenum")

        elif secundary_option == 5:

            system("sudo apt install dnsrecon")

        if secundary_option == 6:

            system("sudo apt install dnsmap")

        elif secundary_option == 7:

            system("sudo apt upgrade dnsspoof")

        elif secundary_option == 8:

            system("sudo apt install ettercap")

        elif secundary_option == 9:

            system("sudo apt install fierce ")

        elif secundary_option == 10:

            system("sudo apt install hydra")

        elif secundary_option == 11:

            system("sudo apt install iptables")

        elif secundary_option == 12:

            system("sudo apt upgrade maltego")

        elif secundary_option == 13:

            system("sudo apt install medusa")

        elif secundary_option == 14:

            system("sudo apt install metasploit-framework")

        elif secundary_option == 15:

            system("sudo apt install mitmf")

        elif secundary_option == 16:

            system("sudo apt install netcat")

        elif secundary_option == 17:

            system("sudo apt upgrade netdiscover")

        elif secundary_option == 18:

            system("sudo apt install nmap")

        elif secundary_option == 19:

            system("sudo apt install netcat")

        elif secundary_option == 20:

            system("sudo apt install sslsplit")

        elif secundary_option == 21:

            system("sudo apt install sslsplit")

        elif secundary_option == 22:

            system("sudo apt upgrade tcpdump")

        elif secundary_option == 23:

            system("sudo apt install zenmap")

        elif secundary_option == 0:

            menu_main()                

        elif secundary_option == -1:
            system("clear")
            exit()

        else:

            system("clear")
            submenu_one()

        submenu_one()

    except Exception as error:

        print("Error: {}".format(error))
        submenu_one()        



def submenu_two():

    try:
        
        print(""" 
        
            1) Get Information about system
            0) back
           -1) Exit
            
        
        """)

        secundary_option = int(input("your option: "))
        
        if secundary_option == 1:
            
            get_information_about_system()
            submenu_two()

        elif secundary_option == 0:

            menu_main()

        elif secundary_option == -1:

            system("clear")
            exit()

        else:

            print("option invalid. Try again")
            sleep(1)
            submenu_two()


            



    except Exception as error:

        print("Error: {}".format(error))    

def submenu_three():
    print('ccc')
