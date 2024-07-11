#import random 
#aleatorio = random.randint(menor,mayor)
import time, csv, os, random, msvcrt
trabajadores_base = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
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

        opc = Validar_opc()
        
        if opc==1:
            Asignar_sueldos()
        elif opc==2:
            Clasificar_sueldos()
        elif opc==3:
            ver_estadisticas()
        elif opc==4:
            reporte_sueldos()
        elif opc==5:
            salir_programa()


def Asignar_sueldos():
    os.system('cls')
    print("ASIGNAR SUELDOS ALEATORIOS")
    
    for x in range(10):
        Sueldos_aleatorios = random.randint(300000,2500000)
        desc_salud = Sueldos_aleatorios * 0.07
        desc_afp = Sueldos_aleatorios * 0.12
        sueldo_liquido = Sueldos_aleatorios - (desc_afp + desc_salud)

        sueldo_trabajador= {"nombre":trabajadores_base[x],
                            "sueldo":Sueldos_aleatorios,
                            "descuento_salud":desc_salud,
                            "descuento_AFP":desc_afp,
                            "sueldo_liquido":sueldo_liquido}
        



        sueldos_trabajadores.append(sueldo_trabajador)
    print("Se han generado los sueldos...")
   

def Clasificar_sueldos():
    os.system('cls')
    if not sueldos_trabajadores:
        print("No se han generado los sueldos...")
    else:

        print("CLASIFICACION SUELDOS")
        print()
        print("Sueldos menores a $800.000") 
        print()
        print("Nombre empleado   Sueldo")

        total = 0
        for tra in sueldos_trabajadores:
            if tra["sueldo"]<800000: 
                total +=1
        print(f"TOTAL: {total}")
        print()

        for tra in sueldos_trabajadores:
            if tra["sueldo"]<800000: 
                print(f"{tra["nombre"]}       {tra["sueldo"]}")
        time.sleep(10)

        print()
        print("Sueldos entre $800.000 y $2.000.000") 
        print()
        print("Nombre empleado   Sueldo")

        total = 0
        for tra in sueldos_trabajadores:
            if tra["sueldo"]>800000 and tra["sueldo"]<2000000:
                total +=1
        print(f"TOTAL: {total}")
        print()


        for tra in sueldos_trabajadores:
            if tra["sueldo"]>800000 and tra["sueldo"]<2000000:
                print(f"{tra["nombre"]}       {tra["sueldo"]}")
        time.sleep(10)

        print()
        print("Sueldos superiores a $2.000.000") 
        print()
        print("Nombre empleado   Sueldo")

        total = 0
        for tra in sueldos_trabajadores:
            if tra["sueldo"]>2000000:
                total +=1
        print(f"TOTAL: {total}")
        print()


        for tra in sueldos_trabajadores:
            if tra["sueldo"]>2000000:
                print(f"{tra["nombre"]}       {tra["sueldo"]}")
        time.sleep(10)
        
def ver_estadisticas():
    if not sueldos_trabajadores:
        print("No se han generado los sueldos...")
    else:
        print("ESTADISTICAS SUELDOS")
        print()
        print()
        print()
        print()
        promedio = 0
        for pro in sueldos_trabajadores:
            promedio += pro["sueldo"]
            
        promedio_final = promedio/10
        print(f"El promedio de los sueldos es: {promedio_final}")
        print()
        acumulador = 0
        for mg in sueldos_trabajadores:
            
            acumulador = acumulador * mg["sueldo"]
        Media_geometrica = acumulador^(1/10)
        print(f"La media geometrica es: {Media_geometrica}")



def reporte_sueldos():
    if not sueldos_trabajadores:
        print("No se han generado los sueldos...")
    else:

        print("REPORTE DE SUELDOS")

        nombre_archivo = input("Ingrese nombre archivo: ")+".csv"
        with open(nombre_archivo,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo,["nombre","sueldo","descuento_salud","descuento_AFP","sueldo_liquido"])
            escritor.writerows(sueldos_trabajadores)

    
        
def salir_programa():
    print("Finalizando programa...")
    print("Desarrollado por ")
    print("RUT ")
    exit()

def Validar_opc():
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! Debe ingresar un número entre el 1 al 5!")
        except: 
                print("ERROR! Debe ingresar un número entero!")
    
     
       