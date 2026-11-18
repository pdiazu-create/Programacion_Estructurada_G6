#un ages =[], def addage, get max age, get min age, showsize, show ages, while, true, try: age = int(input("Ingrese la edad: ")) if age > 3 else debe ser un numero mayor a 3, answer ingresa otro s-n, if answer.upper != "S" break, except valuererror: print("Debe ingresar um entero")
ages = []
def addAge(age):
    ages.append(age)    

    def getMaxAge():
        MaxAge = ages[0]
        for age in ages:
            if age > MaxAge:
                MaxAge = age
                return MaxAge

    def getMinAge():
        MinAge = ages[0]
        for age in ages:
            if age < MinAge:
                MinAge = age
                return MinAge

            def showSize():
                return ages.count

            def showAges():
                return ages

            while True:
                try:
                    age = int(input("Ingrese la edad: "))
                    if age > 3:
                        addAge(age)
                    else:
                        print("Debe ser un numero mayor a 3")
                    answer = input("Ingresa otra edad? (S/N): ")
                    if answer.upper() != "S":
                        break
                except ValueError:
                    print("Debe ingresar un entero")