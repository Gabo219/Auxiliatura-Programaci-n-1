def burbuja(vector):
    n=len(vector)
    for i in range(n-1):
        for j in range(n-i-1):
            if vector[j]>vector[j+1]:
                vector[j],vector[j+1]=vector[j+1],vector[j]
    return vector
v=[5,8,2,1,66,5,9,45,1]
print ("vector original" ,v)
ordenado=burbuja(v)
print ("vector ordenado" ,ordenado)