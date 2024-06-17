Lista=[]
Lista_Plan=[]

def promedio(a):
    'a=0'
    X1=PPE
    X2=a
    X3=a*PPE

def promedio_alto(z):
    

def PPE(y):
    if y>=0 and y<=100:
        print("Porcentaje Guardado")
    else: 
        print("Porcentaje No Aceptado")

def PCI(x):
    if x>=0 and x<=25:
        print("Chiste")
    elif x>=26 and x<=50:
        print("Anecdota")
    elif x>=51 and 75:
        print("Peligro")
    elif x>=76 and x<=99:
        print("Atencion")
    elif x>=100:
        print("ESCLAVITUD")


while (True):
    print("- Menu -")
    print("1. Agregar Plan")
    print("2. Listar Planes")
    print("3. Eliminar Plan por ID")
    print("4. Generar BBDD/CSV")
    print("5. Cargar BBDD/CSV")
    print("6. Generar Estadisticas")
    print("0. Cerrar Programa")
    OP=int(input("Coloque su Opcion : "))
    
    if OP==1:
        print(" - Agregar Plan -")
        print("")
        PID=int(input("Coloque ID (SOLO NUMEROS): "))
        PNom=input("Coloque Nombre : ")
        PPE=input("Coloque Porcentaje (SOLO NUMERO ENTERO): ")
        PCI=input("Coloque Categoria : ")
                
        Lista_Plan=['PID','PNom','PPE','PCI']
        
        print("Datos guardados...")
    elif OP==2:
        print(" - Listar Plan/es")
        print("")
        for x in Lista_Plan:
            print(f'ID : {x[0]}, Nombre : {x[1]}, Porcentaje Efectividad : {x[2]}, Categoria Interna : {x[3]}')
        print("\n")
    elif OP==3:
        Encontrado=False
        Eliminado=False
        print(" - Eliminar Plan/es -")
        print("")
        x=int(input("Coloque el ID del Plan"))
        if x['PID']==Lista_Plan:
            print("Plan encontrado, procediendo")
            Encontrado=True
            print(f'ID : {x[0]}, Nombre : {x[1]}, Porcentaje Efectividad : {x[2]}, Categoria Interna : {x[3]}')
            print("Esta seguro de borrar este plan?")
            OPB=int(input(" Opciones: "
                          "1. Yes"
                          "2. No "))
            if OP==1:
                Lista_Plan.remove(x)
                print("Plan eliminado")
                Eliminado=True
            if OP==2:
                print("Plan no eliminado")
        elif Encontrado==False:
            print("Plan no encontrado...")
    elif OP==4:
        print(" - Generar BBDD -")
        print("")
        print("Generando archivo... espere...")
        with open ('LP_csv','w',newline=' ') as LP_csv:
            escritor_csv = csv.writer(LP_csv) 
            escritor_csv.writerow('PID','PNom','PPE','PCI')
            escritor_csv.writerows(Lista_Plan)
            print("Archivo creado y guardado corerectamente...")
    elif OP==5:
        print(" - Mostrando BBDD -")
        print("")
        print("Mostrando archivo... espere...")
        with open ('LP_csv','r',newline=' ') as LP_csv:
            lector_csv=csv.reader(LP_csv)
            for fila in lector_csv:
                if cont==0:
                    cont==cont+1
                PID=int(fila[0])
                PNom=int(fila[1])
                PPE=int(fila[2])
                PCI=int(fila[3])
    elif OP==6:
        print(" - Generar Estadisticas -")
        promedio(Lista_Plan)
        promedio_alto(Lista_Plan)
        print("")
    elif OP==0:
        print("Esta seguro/a de cerrar el programa?")
        OP=int(input(" Opciones:" 
              "1. Yes"
              "2. No "))
        if OP==1:
            print("Cerrando programa... Goodbye")
            break
        elif OP==2:
            print("Entendible, redirigiendo al menu")
    else:
        print("El programa ha detectado una opcion invalida...")
        print("Por favor, coloque una opcion valida : ")