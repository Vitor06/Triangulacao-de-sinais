
import math
import numpy as np

p_0 = {'1':-26,'2':-33.8,'3':-29.8,'4':-31.2,'5':-33.0}
Ft = {'1':2.1,'2':1.8,'3':1.3,'4':1.4,'5':1.5}
posicao_k = {'1':(1.55,17.63,1.35),'2':(-4.02,0,1.35),'3':(-4.40,9.60,1.35),'4':(9.27,4.64,1.35),'5':(9.15,12,1.35)}
pk_caso1 = {'1':-48.4,'2':-50.6,'3':-32.2,'4':-47.4,'5':-46.3}
pk_caso2 = {'1':-46.9,'2':-46.4,'3':-41.2,'4':-45.8,'5':-48.7}



def distancia_radial(k,p):
    k = str(k)
    Dk =pow(10, ((p_0[k]-p[k]) / (10*Ft[k]))  )
    return Dk

def matrizA():
    Ma = np.empty([5,2])
    k = 1;
    #2*(Xn-Xk)
    for i in range(len(Ma)):
            Ma[i][0] = 2*(posicao_k['5'][0] - posicao_k[str(k)][0])
            k+=1
    k = 1
     #2*(Yn-Yk)
    for i in range(len(Ma)):
            Ma[i][1] = 2*(posicao_k['5'][1] - posicao_k[str(k)][1])
            k+=1
    return Ma

def matrizB(d0):
    Mb = np.empty([5,1])
    k = 1;

    for i in range(len(Mb)-1):
            #Wk - Wn
            Mb[i][0] = ( (pow(d0[str(k)],2) -  pow(posicao_k[str(k)][0],2) -  pow(posicao_k[str(k)][1],2)) )- (pow(d0['5'],2) -  pow(posicao_k['5'][0],2) -  pow(posicao_k['5'][1],2))
            k+=1
    return Mb

def d0():
    distancia = dict({str(k):distancia_radial(k,pk_caso1) for k  in range(1,6)})
    return distancia

D0 = d0()
Ma = matrizA()
Mb = matrizB  (D0)
MaT = Ma.transpose()
MaT_X_Ma = np.matmul( MaT,Ma)
MaT_X_Ma_inv =  np.linalg.inv(MaT_X_Ma)
Mx =  np.matmul( np.matmul(MaT_X_Ma_inv,MaT) ,Mb)

print(Mx)
