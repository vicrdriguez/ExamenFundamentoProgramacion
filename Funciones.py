import random,csv
from statistics import geometric_mean

lista_trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]


def Asignar_datosAleatorios(lista_trabajadores):


    datos_trabajadores = {}
    sueldo_liquido = {}
    sueldo_Base = {}
    
    for trabajador in lista_trabajadores: 

        SueldoBase = random.randint(300000,2500000)
        sueldo_Base[trabajador] = SueldoBase
        DescuentoAFP = round(SueldoBase * 0.12)
        DescuentoSalud = round(SueldoBase * 0.07)
        SueldoLiquido = SueldoBase - DescuentoAFP - DescuentoSalud
        sueldo_liquido[trabajador] = SueldoLiquido

        datos_trabajadores[trabajador] = {

            "Sueldo base" : SueldoBase,
            "Descuento AFP" : DescuentoAFP,
            "Descuento Salud" : DescuentoSalud,
            "Sueldo Liquido" : SueldoLiquido
        }
        
    
    
    return datos_trabajadores,sueldo_liquido,sueldo_Base


def Clasificar_datos(sueldo_Base):


    Sueldo_menor = {}
    Sueldo_Medio = {}
    Sueldo_mayor = {}


    for trabajador,SueldoLiquido in sueldo_Base.items():

        sueldos = SueldoLiquido
        
        if sueldos < 800000:
            Sueldo_menor[trabajador] = sueldos

        elif sueldos >= 800000 and sueldos <= 2000000:
            Sueldo_Medio[trabajador] = sueldos

        elif sueldos > 2000000:
            Sueldo_mayor[trabajador] = sueldos


    print("Estos son los sueldos menores , TOTAL =",len(Sueldo_menor))
    print("TRABAJADOR, SUELDO")
    print("------------------------------------------------------------")
    for trabajador, SueldoLiquido in Sueldo_menor.items():
        
        print(trabajador," = $",SueldoLiquido)


    print("Estos son los sueldos Entre $800.000 y $2.000.000 , TOTAL =",len(Sueldo_Medio))
    print("------------------------------------------------------------")
    print("TRABAJADOR, SUELDO")
    for trabajador, SueldoLiquido in Sueldo_Medio.items():
        print(trabajador," = $",SueldoLiquido)


    print("Estos son los sueldos Mayores , TOTAL =",len(Sueldo_mayor))
    print("------------------------------------------------------------")
    print("TRABAJADOR, SUELDO")
    for trabajador, SueldoLiquido in Sueldo_mayor.items():
        print(trabajador," = $",SueldoLiquido)




def  Estadistica_datos(sueldo_liquido):
  
    listaSueldos = list(sueldo_liquido.values())

    SueldoAlto = max(listaSueldos)
    SueldoBajo = min(listaSueldos)
    promedio = sum(listaSueldos) / len(listaSueldos)
    mediaGeo = round(geometric_mean(listaSueldos))

    print("\nEl sueldo mas alto es",(SueldoAlto))
    print("El sueldo mas bajo es",(SueldoBajo))
    print("El Promedio  es",(round(promedio)))
    print("La media es mediaGeo",(mediaGeo))

        
def Mostrar_por_Consola( datos_trabajadores):
    print("----------------------------------------------------------------------------------")
    print("Trabajador\t\tSueldo Base\tDescuento salud\tDescuento AFP\tSueldo Líquido")
    print("----------------------------------------------------------------------------------")

    for trabajador,dato in datos_trabajadores.items():
       print(f"{trabajador}\t\t{dato["Sueldo base"]}\t\t{dato["Descuento AFP"]}\t\t{dato["Descuento Salud"]}\t\t{dato["Sueldo Liquido"]}")


    
    



def Importar_plantilla(datos_trabajadores):

    with open('PlantillaCsv.csv',"w",newline='') as ArchivoCsv:
        escritor = csv.writer(ArchivoCsv,delimiter=',')
        escritor.writerow(["Trabajador,Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Liquido"])

        for trabajador, Dato in datos_trabajadores.items():
             
             sueldo = Dato["Sueldo base"]
             desucentafP = Dato["Descuento AFP"]
             descuentosalud = Dato["Descuento Salud"]
             sueldoL = Dato["Sueldo Liquido"]
             escritor.writerow([trabajador,sueldo,desucentafP,descuentosalud,sueldoL])

        



        

        
      


    





    

    
    

   

