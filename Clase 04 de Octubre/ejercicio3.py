class Persona:
    def __init__(self,nombre,edad,direccion):
        self.nombre = nombre
        self.direccion = direccion
        
    def burbuja(self,vector):
        n=len(vector)
        for i in range(n-1):
            for j in range(n-i-1):
                if vector[j]>vector[j+1]:
                    vector[j],vector[j+1]=vector[j+1],vector[j]
        return vector
    
    def dormir():
        print("la persona duerme")
        
    def corre():
        n=100
        return n
per=Persona("Messi" , "10" , "Upea")
vec=[21,5,6,9,74,58,1]
print("vector original",vec)
print ("vector ordenado",per.burbuja(vec))