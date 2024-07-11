#import random 
#aleatorio = random.randint(menor,mayor)
import time, csv, os, random, msvcrt
trabajadores_base = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_trabajadores =[]

def menu():
    while True:
        os.system('cls')
        print("Menú")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opc =int(input("Ingrese una opción: "))
        
        if opc==1:
            Asignar_sueldos()
        elif opc==2:
            Clasificar_sueldos()
        elif opc==3:
            ver_estadisticas()
        elif opc==4:
            pass
        elif opc==5:
            salir_programa()


def Asignar_sueldos():
    os.system('cls')
    print("ASIGNAR SUELDOS ALEATORIOS")
    for x in range(10):
        Sueldos_aleatorios = random.randint(300000,2500000)
        sueldo_trabajador= {"nombre":trabajadores_base[x],
                            "sueldo":Sueldos_aleatorios}
        



        sueldos_trabajadores.append(sueldo_trabajador)
    print("Se an generado los sueldos...")
    time.sleep(3)

def Clasificar_sueldos():
    print("CLASIFICACION SUELDOS")
    print()
    print("Sueldos menores a $800.000") 
    print("Nombre empleado   Sueldo")
    for tra in sueldos_trabajadores:
        if tra["sueldo"]<800000: 
           print(f"{tra["nombre"]}       {tra["sueldo"]}")
    time.sleep(10)

    print()
    print("Sueldos entre $800.000 y $2.000.000") 
    print("Nombre empleado   Sueldo")

    for tra in sueldos_trabajadores:
        if tra["sueldo"]>800000 and tra["sueldo"]<2000000:
           print(f"{tra["nombre"]}       {tra["sueldo"]}")
    time.sleep(10)

    print()
    print("Sueldos superiores a $2.000.000") 
    print("Nombre empleado   Sueldo")

    for tra in sueldos_trabajadores:
        if tra["sueldo"]>2000000:
           print(f"{tra["nombre"]}       {tra["sueldo"]}")
    time.sleep(10)
    
def ver_estadisticas():
    print("ESTADISTICAS SUELDOS")
    print()






def salir_programa():
    
     
       