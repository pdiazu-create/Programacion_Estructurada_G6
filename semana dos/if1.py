# Leer la nota de un estudiante y decir si aprobo o su aprendizaje es inicial.
grade = int(input("Ingresa la nota del estudiante: "))
if grade >= 60:
    print(Fore.GREEN + "El estudiante aprobo.") # type: ignore
else:
    print(Fore.RED + "El estudiante tiene un aprendizaje inicial.") # type: ignore
    Style.RESET_ALL # type: ignore
