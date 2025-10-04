def dimension():
    n=int(input("digite el tamaño del vector"))
    return n

def crear(tamaño):
    v=[0]*tamaño
    return v

def leer(v,t):
    for i in range(0,t):
        v[i]=int(input(f"digite el elemento {i} del vector"))
        
def burbuja(vector,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if vector[j]>vector[j+1]:
                vector[j],vector[j+1]=vector[j+1],vector[j]
    return vector

num=dimension()
vec=crear(num)
leer(vec,num)
print ("vector original" ,vec)
vectorOrdenado=burbuja(vec,num)
print ("vector odenado" ,vectorOrdenado)
