import platform

def get_information_about_system():

    try:

        System = platform.system()
        Version = platform.release()
        Data = platform.version()
        print("\nSystem: {}\nVersion: {}\nData: {}".format(System,Version,Data))
        
    except Exception as error:

        pritn("Error: {}".format(error))

