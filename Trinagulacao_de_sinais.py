
import math
import numpy as np
import matplotlib.pyplot as plt

p_0 = {'1':-26,'2':-33.8,'3':-29.8,'4':-31.2,'5':-33.0}
Ft = {'1':2.1,'2':1.8,'3':1.3,'4':1.4,'5':1.5}
posicao_k = {'1':(1.55,17.63,1.35),'2':(-4.02,0,1.35),'3':(-4.40,9.60,1.35),'4':(9.27,4.64,1.35),'5':(9.15,12,1.35)}
pk_caso1 = {'1':-48.4,'2':-50.6,'3':-32.2,'4':-47.4,'5':-46.3}
pk_caso2 = {'1':-46.9,'2':-46.4,'3':-41.2,'4':-45.8,'5':-48.7}
ponto_real_caso1 = (0,9)
ponto_real_caso2 = (3,3)
plt.axis([-30, 30, -30, 30])

n = 5 #equação que será eleiminada  -> k - n
def desenhar_ponto(ponto,color):
    plt.plot(ponto[0], ponto[1], marker="o", markersize=5, markeredgecolor=color, markerfacecolor=color)#Posicao real
def desenhar_circulos(d0):

    for i in range(1,len(posicao_k)+1):
        x = posicao_k[str(i)][0]
        y = posicao_k[str(i)][1]
        c=plt.Circle((x, y), d0[str(i)],fill= False)
        plt.gca().add_artist(c)

def distancia_radial(k,p):
    k = str(k)
    Dk =pow(10, ((p_0[k]-p[k]) / (10*Ft[k]))  )
    return Dk

def matrizA():
    M = len(posicao_k)-1
    N = 2
    Ma = np.empty([M,N])
    k = 1;
    #2*(Xn-Xk)
    for i in range(len(Ma)):
        if(k==n):k+=1
        if(k<=len(posicao_k)):
            # print('2*' + '(' + 'X'+str(n)+'-' + 'X'+str(k) + ')' )#Somente para vizualizacao
            Ma[i][0] = 2*(posicao_k[str(n)][0] - posicao_k[str(k)][0])
            k+=1
    k = 1

    #2*(Yn-Yk)
    for i in range(len(Ma)):
        if(k==n):k+=1
        if(k<=len(posicao_k)):
            #print( '2*' + '(' + 'Y'+str(n)+'-' + 'Y'+str(k) + ')' )#Somente para vizualizacao
            Ma[i][1] = 2*(posicao_k[str(n)][1] - posicao_k[str(k)][1])
            k+=1
    return Ma

def matrizB(d0):
    M = len(posicao_k)-1
    N = 1
    Mb = np.empty([M,N])
    k = 1;

    for i in range(len(Mb)):
        #Wk - Wn
        if(k==n):k+=1
        if(k<=len(posicao_k)):
            #Wk = Rk^2 -Xk^2 -Yk^2
            wk = ( pow(d0[str(k)],2) -  pow(posicao_k[str(k)][0],2) - pow(posicao_k[str(k)][1],2) )
            #n = Rn^2 -Xn^2 -Yn^2
            wn = ( pow(d0[str(n)],2) -  pow(posicao_k[str(n)][0],2) -  pow(posicao_k[str(n)][1],2) )
            Mb[i][0] =  wk - wn
            k+=1

    return Mb

def d0(pk_caso):
    distancia = dict({str(k):distancia_radial(k,pk_caso) for k  in range(1,6)})
    return distancia

def main():
    D0 = d0(pk_caso1)
    Ma = matrizA()
    Mb = matrizB  (D0)
    MaT = Ma.transpose()
    MaT_X_Ma = np.matmul( MaT,Ma)
    MaT_X_Ma_inv =  np.linalg.inv(MaT_X_Ma)
    Mx =  np.matmul( np.matmul(MaT_X_Ma_inv,MaT) ,Mb)
    print(Mx)
    desenhar_circulos(D0)
    desenhar_ponto(ponto_real_caso1,"red")#Real
    desenhar_ponto((Mx[0],Mx[1]),"green")#Estimado
    plt.show()


main()
