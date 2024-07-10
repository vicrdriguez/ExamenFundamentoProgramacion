import Funciones as Fn
import random

lista_trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

datos_trabajadores = {}
sueldo_liquido = {}
sueldo_Base = {}

while True:
    try:
        print("\n1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = int(input("Seleccione una opcion  porfavor: "))

        #Opcion 1 Asignar Sueldos aleatorios
        if opcion == 1:
            print("Datos generados con exito")
            datos_trabajadores,sueldo_liquido,sueldo_Base = Fn.Asignar_datosAleatorios(lista_trabajadores)
            print(sueldo_Base)
           

        if opcion == 2:
            if not sueldo_liquido:
                 print("No hay datos asignados")
            else:
                 Fn.Clasificar_datos(sueldo_liquido)
            

        if opcion == 3:
             
            if not sueldo_liquido:
                 print("No hay datos asignados")
            else:
                 Fn.Estadistica_datos(sueldo_liquido)

        if opcion == 4:
            if not sueldo_liquido:
                 print("No hay datos asignados")
            else:
                Fn.Mostrar_por_Consola(datos_trabajadores)
                Fn.Importar_plantilla(datos_trabajadores)
         
    
              

    except:
        print("Error, ingrese una opcion valida porfavor")
        

        
