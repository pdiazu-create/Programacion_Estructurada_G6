#crear una suma con def get_sum number 1 , number2, despues show_result,despuesprint dame un numero y despues pide otro y el argumento es el valor que se le envia a la funcion cuando se llama con un sum = get_sum al final y print show_result(lasuma es: sum)
def get_sum(number1, number2):    
    return number1 + number2
def show_result(message, result):
    return f"{message} {result}"

print("Dame un numero: ")
num1 = float(input())

print("Dame otro numero: ")
num2 = float(input())

sum = get_sum(num1, num2)
print(show_result("La suma es: ", sum))

