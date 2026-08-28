#mostrar los numberos del o al 9
from colorama import fore, Style
for number in range(10):
    print(f"{number}")
    if number % 2 == 0:
        print(fore.GREEN + f"{number}" "es par" + Style.RESET_ALL)
    else:
        print(fore.RED + f"{number} es impar " + Style.RESET_ALL)
        