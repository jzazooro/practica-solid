class Matriz():
    def __init__(self, elementos):
        self.elementos=elementos
    
class Transpuesta(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)

    def transpuesta(self):
        return Matriz([[fila[i]for fila in self.elementos]for i in range(len(self.elementos[0]))])

class Imprimir(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

class Lanzador():
    def __init__(self):
        self.elementos=[]
        self.cantidad_filas=int(input("Ingrese la cantidad de filas: "))
        self.cantidad_columnas=int(input("Ingrese la cantidad de columnas: "))
        self.create_matrix()
        self.matriz=Matriz(self.elementos)
        self.transpuesta=Transpuesta(self.elementos)
        self.imprimir=Imprimir(self.elementos)   
    
    def create_matrix(self):
        for i in range(self.cantidad_filas):
            fila=[]
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Ingrese el elemento {i+1} de la fila {j+1}: ")))
            self.elementos.append(fila)
    
    def lanzar(self):
        print("Matriz original: ")
        self.imprimir.imprimir()
        print("Matri transpuesta: ")
        transpuesta_result=self.transpuesta.transpuesta()
        imprimir_transpuesta=Imprimir(transpuesta_result.elementos)
        imprimir_transpuesta.imprimir()

if __name__=="__main__":
    lanzador=Lanzador()
    lanzador.lanzar()