class Postres:
    def __init__(self):
        self.recetario = {}

    def insertar_recetario(self, postre, ingredientes):
        if postre not in self.recetario:
            self.recetario[postre] = [] 
        self.recetario[postre].append(ingredientes)  
        print(f"Postre ({postre}) añadido con ingredientes ({', '.join(ingredientes)})")

    def insertar_nuevosING_recetario(self, postre, nuevos_ingredientes):

        if postre in self.recetario:
            self.recetario[postre][-1].extend(nuevos_ingredientes) 
            print(f"Nuevos ingredientes añadidos a {postre}: {', '.join(nuevos_ingredientes)}")
        else:
            print(f"El postre {postre} no existe")

    def eliminar_ingrediente(self, postre, ingrediente):
        if postre in self.recetario:
            removed = False
            for ingredientes in self.recetario[postre]:
                if ingrediente in ingredientes:
                    ingredientes.remove(ingrediente)
                    removed = True
                    print(f"El ingrediente {ingrediente} se eliminó del postre {postre}")
            if not removed:
                print(f"El ingrediente {ingrediente} no está en el postre")
        else:
            print(f"El postre {postre} no existe")

    def baja_postre(self, postre):
        if postre in self.recetario:
            del self.recetario[postre]
            print(f"El postre {postre} se eliminó")
        else:
            print(f"El postre {postre} no existe")

    def imprimir_ingredientes(self, postre):
        if postre in self.recetario:
            print(f"Los ingredientes del postre {postre} son:")
            for ingredientes in self.recetario[postre]:
                todos_los_ingredientes = ', '.join(ingredientes)
                print(f"- {todos_los_ingredientes}")
        else:
            print(f"El postre {postre} no existe")

    def imprimir_recetario(self):
        if not self.recetario:
            print("El recetario está vacío.")
        else:
            print("El recetario completo es:")
            for postre, listas_ingredientes in self.recetario.items():
                for ingredientes in listas_ingredientes:
                    todos_los_ingredientes = ', '.join(ingredientes)  
                    print(f"{postre}: {todos_los_ingredientes}")

    def eliminar_duplicados(self):
        nuevos_recetarios = {}
        for postre, listas_ingredientes in self.recetario.items():
            if postre not in nuevos_recetarios:
                nuevos_recetarios[postre] = [listas_ingredientes[0]]  

        self.recetario = nuevos_recetarios
        print("Duplicados eliminados del recetario")

def sistema():
    todo_recetario = Postres()

    while True:
        print("\nOpciones disponibles:")
        print("1. Insertar un nuevo postre")
        print("2. Insertar nuevos ingredientes en un postre")
        print("3. Eliminar un ingrediente de un postre")
        print("4. Imprimir los ingredientes de un postre")
        print("5. Dar de baja un postre")
        print("6. Imprimir el recetario")
        print("7. Eliminar duplicados del recetario")
        print("salir")

        opcion = input("Seleccione una opción o 'salir': ")

        if opcion == "1":
            postre = input("Ingrese el nombre del postre: ")
            ingredientes = input("Ingrese los ingredientes separados por comas: ").split(", ")
            todo_recetario.insertar_recetario(postre, ingredientes)

        elif opcion == "2":
            postre = input("Ingrese el nombre del postre: ")
            nuevos_ingredientes = input("Ingrese los nuevos ingredientes separados por comas: ").split(", ")
            todo_recetario.insertar_nuevosING_recetario(postre, nuevos_ingredientes)

        elif opcion == "3":
            postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a eliminar: ")
            todo_recetario.eliminar_ingrediente(postre, ingrediente)

        elif opcion == "4":
            postre = input("Ingrese el nombre del postre: ")
            todo_recetario.imprimir_ingredientes(postre)

        elif opcion == "5":
            postre = input("Ingrese el nombre del postre a eliminar: ")
            todo_recetario.baja_postre(postre)

        elif opcion == "6":
            todo_recetario.imprimir_recetario()

        elif opcion == "7":
            todo_recetario.eliminar_duplicados()

        elif opcion == "salir":
            print("Terminando")
            break

        else:
            print("Opción inválida")

sistema()


