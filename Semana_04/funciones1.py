from colorama import Fore, Style


age = 0 
def readAge ():
    global age
    while True:
        try:
            age = int(input("Edad: "))
            break
        except ValueError:
            print(Fore.RED + "Ingrese un valor numerico." + Style.RESET_ALL)

            def evalAge():
                global age
                if age >= 18:
                    print("Mayor de edad")
                else:
                    print("Menor de edad")
            

            def show(): 
                global age 
                print ("Mayor de edad" if age >= 18 else "Menor de edad")

                readAge()
                show()