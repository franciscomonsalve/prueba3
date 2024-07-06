import csv 
lista_de_alumnos =[]

def procesar_lista_estudiantes ():
    
 with open ("ListaCurso5B.csv","r") as archivocurso_csv:
        lecturalista = csv.DictWriter(archivocurso_csv)
        for i in lecturalista :
            lista_de_alumnos.append({
                "rut": i ["rut"],
                "nombre":i ["nombre"],
                "nota 1":i ["nota 1"],
                "nota 2":i ["nota 2"],
            })    
        print(lista_de_alumnos)
        

def regitro_estudiante ():
    with open ("ListaCurso5B.csv","w") as archivocurso_csv:
        lista_curso = csv.writer(archivocurso_csv)
        lista_curso.append( {
            "rut": input("Ingresar rut"),
            "nombre":input("Ingresar nombre "), 
            "nota 1":input("Ingresar nota 1"),
            "nota 2":input("Ingresar nota 2")
        })
def modificar_nota ():
    
    monbre_alumno = input("Ingresar nombre de alumno a promediar")
    for i in lista_de_alumnos:
        if i ["nombre"] == nombre_alumno :
            cambiar_nota = input("Ingresar nueva nota")
            i ["nota 1"] = cambiar_nota 
        
        
            

def eliminar_estudiante ():
    pass 


def generar_promedio_nota ():
    monbre_alumno_para_nota = input("Ingresar nombre de alumno a promediar")
    
    for i in  lista_de_alumnos :
            if ["nombre"] == nombre_alumno_para_nota :

                nota_promedio = (i["nota 1"]+i["nota 2"])/2   
                print(f"El alumno:" [nombre_alumno_para_nota])
                print(nota_promedio)         
def generar_acta_de_cierre_curso ():
    pass

def salir ():
    pass
while True :
    try :
        def menu ():
            opcion = int(input("Ingresar una opcion \n1 Procesar lista estudiantes \n2 Registrar estudiantes \n3 Modificar nota \n4 Eliminar estudiante \n5 Generar promedio de notas \n6 Generar acta de cierre de curso \n7 Salir "))
            if   opcion == 1 :
                procesar_lista_estudiantes()
            elif opcion == 2 :
                regitro_estudiante()
            elif opcion == 3 :
                modificar_nota()
            elif opcion == 4 :
                 eliminar_estudiante()
            elif opcion == 5 :
                generar_promedio_nota()
            elif opcion == 6 :
                generar_acta_de_cierre_curso()
            elif opcion == 7 :
                salir()
            else:
                print("Opcion invalida ")
    except:("Ingresar una opcion valida ")

menu()