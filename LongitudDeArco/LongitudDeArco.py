from math import *

# Andrés Eduardo Arciniega Arellano
#Programa que calcula la longitud de arco

#Se reutiliza la derivada
def deri(coeficientes):
    derivada = []
    k = 1
    if((len(coeficientes)) == 1):
        derivada.append(0)
    else:
        while(len(coeficientes) > k):
            derivada.append(coeficientes[k]*k)
            k = k+1

    return derivada


#Se reutiliza horner y con eso evaluamos los polinomios
def horner(grdo, coeficientes, x):
    polinomio = 0

    for k in range(grdo):
        polinomio = polinomio + (coeficientes[k] * pow(x,k))

    polinomio = sqrt(1 + pow(polinomio,2))
    return polinomio


#Algoritmo que utiliza el metodo del trapecio para obtener la longitud de arco

def MetodoDelTrapecio(a, b, n, Tolerancia, anteriorValue,derivada):

    suma = resultado = 0
    deltaX = (b-a)/n

    # Hacemos las sumas de riemann
    for i in range(1, n):  # inicia en 1 y termina en n
        suma += horner(grdo, derivada, (a+(i*deltaX)))

    # formula de la regla del trapecio
    resultado = ((b-a)/(2*n))*(horner(grdo, derivada, a) + 2*suma + horner(grdo, derivada, b))
    error = ((resultado - anteriorValue)/resultado)*100
    print("Aproximacion: "+str(resultado) + " \ncon n = "+str(n)+". \tError: "+str(error))

    if(abs(error) >= Tolerancia):
        n += 10
        anteriorValue = resultado
        return MetodoDelTrapecio(a, b, n, Tolerancia, anteriorValue, derivada)
    print()
    print("Longitud de Arco: "+str(resultado)+"\t Numero de Particiones \t"+str(n))


#Método que utiliza Simpson para la obtencion de la longitud de arco
def AlgoritmoSimpson(a, b, n, tol, anteriorValue,derivada):
    
    deltaX = (b-a)/n
    SumaIMPAR = SumaPAR = resultado = 0  

    #Se separa el método en dos, las sumas pares y las sumas impares
    for i in range(1, n):  
        if i % 2 == 0:
            SumaPAR += horner(grdo, derivada,(a+(i*deltaX)))

        else:
            SumaIMPAR += horner(grdo, derivada,(a+(i*deltaX)))

    #Metodo de Simpson pero utilizamos las sumas para la aplicacion de una formula general 
    resultado = (deltaX/3)*(horner(grdo, derivada, a) + 4 *SumaIMPAR + 2*SumaPAR + horner(grdo, derivada, b))
    error = ((resultado - anteriorValue)/resultado)*100
    print("Aproximacion: "+str(resultado) + " \ncon n = "+str(n)+". \tError: "+str(error))

    if(abs(error) >= tol):
        n += 10
        anteriorValue = resultado
        return AlgoritmoSimpson(a, b, n, tol, anteriorValue,derivada)
    print()
    print("Longitud de Arco: "+str(resultado)+"\t Numero de Particiones \t"+str(n))

#Metodo que calcula la longitu de arco
def longitudArco():
    derivada = deri(coeficientes)
    if Opcion == 1:
            MetodoDelTrapecio(a, b, n, Tolerancia, anterior, derivada)
    elif Opcion == 2:
        AlgoritmoSimpson(a, b, n, Tolerancia, anterior, derivada)
    else:
        print("Numero no valido")



#***************************************************************PROGRAMA PRINCIPAL*******************************************************************
grdo = 0
grdo = int(input("Grado del polinomio (n > 1): "))

#Método de comprobación de indicación previa
if grdo > 1:

    coeficientes = []
    x = []

    #Se pide ingresar el polinomio a trabajar
    aux = grdo
    for i in range(grdo+1):
        coefi = float(input("\nIngresa el coeficiente x^"+str(aux) +": "))
        aux -= 1
        coeficientes.append(coefi)
    coeficientes.reverse()

    a = b = 0

    #Se ingresan los Limites superiores e inferiores
    a = float(input("\n Limite inferior: "))
    b = float(input(" Limite superior: "))

    #Se ingresa el valor de n
    n = int(input(" Valor de n (valor entero): "))

    #Comprobacion de que el area bajo la curva existe 
    if a != b:

        #Se ingresan cifras significativas
        CifrasSig = int(input("\n Cifras significativas: "))
        Tolerancia = 0.5*(10**(2-CifrasSig))
        anterior = 0

        # Hacemos un menu para elegir dos metodos de integracion numerica
        print("Metodo a implementar: ")
        print("\n1.-Metodo Trapecios \n2.- Metodo Simpson")
        Opcion = int(input("Opcion (1/2): "))

        print("\nLa Tolerancia: "+str(Tolerancia) + " de "+str(CifrasSig)+" cifras significativas.\n")

        longitudArco()

    else:
        print("El area debe existir, a y b no pueden ser iguales")
else:
    print("Polinomio mayor a grado 1")
#*********************************************************************************************************************************************