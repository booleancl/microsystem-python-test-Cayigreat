import random
options = ["rojo","blanco","azul","verde","naranja","morado"]
import time

print("Bienvenido a tu horóscopo")
print("############################")
user_input = ""
user_option = random.choice(options)


def read_file(file_name):
    file = open("signs/" + file_name,"r", encoding="UTF-8")
    for line in file:
        print(line)

def print_menu():
    print("Selecciona el número correspondiente a tu signo")
    print("1 Acuario")
    print("2 Aries")
    print("3 Cáncer")
    print("4 Capricornio")
    print("5 Géminis")
    print("6 Leo")
    print("7 Libra")
    print("8 Piscis")
    print("9 Sagitario")
    print("10 Escorpión")
    print("11 Tauro")
    print("12 Virgo")
    print("13 Color de la suerte")
    print("0 Salir")
    print("############################")
    
while user_input != 0:
    print_menu()
    user_input = input()

    if user_input == "1":
        read_file("aquarius.txt")
    elif user_input == "2":
        read_file("aries.txt")
    elif user_input == "3":
        read_file("cancer.txt")
    elif user_input == "4":
        read_file("capricornus.txt")        
    elif user_input == "5":
        read_file("gemini.txt")        
    elif user_input == "6":
        read_file("leo.txt")    
    elif user_input == "7":
        read_file("libra.txt")    
    elif user_input == "8":
        read_file("pisces.txt")    
    elif user_input == "9":
        read_file("sagittarius.txt")    
    elif user_input == "10":
        read_file("scorpio.txt")    
    elif user_input == "11":
        read_file("taurus.txt")    
    elif user_input == "12":
        read_file("virgo.txt")    
    elif user_input == "13":
        print("Tu color de la suerte es:")
        input(user_option) 
        time.sleep (0.3)  
    elif user_input == "0":
        print("Adiós")  
        exit()
    else:
        print("opción inválida")        
       


 
