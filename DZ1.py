import math
metan = 0.891434
etan = 0.039068
propan = 0.018336
u_butan = 0.002386
h_butan = 0.002606
neo_pentan = 0
u_peptan = 0
h_pentan = 0.000619
neo_gecsan = 0
h_gecsan = 0.000681
geptan = 0
azot = 0.044545
uglecisliy = 0.00013
geliy = 0.000177
vodorod = 0

davlenie = 20 #МПа
tempC = -1 #C

ri = [metan, etan, propan, u_butan, h_butan, neo_pentan, u_peptan, h_pentan, neo_gecsan, h_gecsan, geptan, azot, uglecisliy, geliy, vodorod]
smes = []
Ki = [0.4619255, 0.5279209, 0.583749, 0.6406937, 0.6341423,0.6738577, 0.6738577, 0.6798307, 0.7175118, 0.7175118,0.7175118, 0.4479153, 0.4557489, 0.3589888, 0.3514916]
Kij = [[1, 1, 1.007619, 1, 0.997596, 1, 1, 1.002529, 1, 0.982962, 0.982962, 1.00363, 0.995933, 1, 1.02326],[1, 1, 0.986893, 1, 1, 1, 1, 1, 1, 1, 1, 1.00796, 1.00851, 1, 1.02034],[1.007619, 0.986893, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0.997596, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1.002529, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0.982962, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.910183, 1, 1],[0.982962, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1.00363, 1.00796, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982361, 0.982361, 1.03227],[0.995933, 1.00851, 1, 1, 1, 1, 1, 1, 1, 0.910183, 1, 0.982361, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982361, 1, 1, 1],[1.02326, 1.02034, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.03227, 1, 1, 1]]
a = [0.1538326, 1.341953, -2.998583, -0.04831228, 0.3757965, -1.589575, -0.05358847, 0.88659463, -0.71023704, -1.471722, 1.32185035, -0.78665925, 0.00000000229129, 0.1576724, -0.4363864, -0.04408159, -0.003433888, 0.03205905, 0.02487355, 0.07332279, -0.001600573, 0.6424706, -0.4162601, -0.06689957, 0.2791795, -0.6966051, -0.002860589, -0.008098836, 3.150547, 0.007224479, -0.7057529, 0.5349792, -0.07931491, -1.418465, -5.99905*10**(-17), 0.1058402, 0.03431729, -0.007022847, 0.02495587, 0.04296818, 0.7465453, -0.2919613, 7.294616, -9.936757, -0.005399808, -0.2432567, 0.04987016, 0.003733797, 1.874951, 0.002168144, -0.6587164, 0.000205518, 0.009776195, -0.02048708, 0.01557322, 0.006862415, -0.001226752, 0.002850908]
b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
u = [0, 0.5, 1, 3.5, -0.5, 4.5, 0.5, 7.5, 9.5, 6, 12, 12.5, -6, 2, 3, 2, 2, 11, -0.5, 0.5, 0, 4, 6, 21, 23, 22, -1, -0.5, 7, -1, 6, 4, 1, 9, -13, 21, 8, -0.5, 0, 2, 7, 9, 22, 23, 1, 9, 3, 8, 23, 1.5, 5, -0.5, 4, 7, 3, 0, 1, 0]
k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 4, 4, 0, 0, 2, 2, 2, 4, 4, 4, 4, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 0, 0, 2, 2, 2, 4, 4, 0, 2, 2, 4, 4, 0, 2, 0, 2, 1, 2, 2, 2, 2]
g = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
q = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]
f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Gi = [0, 0.0793, 0.141239, 0.256692, 0.281835, 0.332267, 0.332267, 0.366911,0.289731, 0.289731, 0.289731, 0.027815, 0.189065, 0, 0.034369]
Gij = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.807653, 1, 1.95731],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.370296, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982746, 1, 1],[0.807653, 0.370296, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982746, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1.95731, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Qi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0]
Fi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
Ei = [151.3183, 244.1667, 298.1183, 324.0689, 337.6389, 365.5999, 365.5999, 370.6823,402.636293, 402.636293, 402.636293, 99.73778, 241.9606, 2.610111, 26.95794]
Eij = [[1, 1, 0.994635, 1.01953, 0.989844, 1, 1.00235, 0.999268, 1, 1.107274, 1.107274, 0.97164, 0.960644, 1, 1.17052],[1, 1, 1.02256, 1, 1.01306, 1, 1, 1.00532, 1, 1, 1, 0.97012, 0.925053, 1, 1.16446],[0.994635, 1.02256, 1, 1, 1.0049, 1, 1, 1, 1, 1, 1, 0.945939, 0.960237, 1, 1.034787],[1.01953, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.946914, 0.906849, 1, 1.3],[0.989844, 1.01306, 1.0049, 1, 1, 1, 1, 1, 1, 1, 1, 0.973384, 0.897362, 1, 1.3],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1.00235, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.95934, 0.726255, 1, 1],[0.999268, 1.00532, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.94552, 0.859764, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1.107274, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.855134, 1, 1],[1.107274, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.855134, 1, 1],[0.97164, 0.97012, 0.945939, 0.946914, 0.973384, 1, 0.95934, 0.94552, 1, 1, 1, 1, 1.02274, 1, 1.08632],[0.960644, 0.925053, 0.960237, 0.906849, 0.897362, 1, 0.726255, 0.859764, 1, 0.855134, 0.855134, 1.02274, 1, 1, 1.28179],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1.17052, 1.16446, 1.034787, 1.3, 1.3, 1, 1, 1, 1, 1, 1, 1.08632, 1.28179, 1, 1]]
Vij = [[1, 1, 0.990877, 1, 0.992291, 1, 1, 1.00367, 1, 1.302576, 1.302576, 0.886106, 0.963827, 1, 1.15639],[1, 1, 1.065173, 1.25, 1.25, 1, 1.25, 1.25, 1, 1, 1, 0.816431, 0.96987, 1, 1.61666],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.915502, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.993556, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.066638, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.066638, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.835058, 1, 0.408838],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Si = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Wi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B0i = [4.00088, 4.00263, 4.02939, 4.06714, 4.33944, 4, 4, 4, 4, 4, 4, 3.50031, 3.50002, 2.50, 2.47906]
C0i = [0.76315, 4.33939, 6.60569, 8.97575, 9.44893, 11.7618, 11.7618, 8.95043, 11.6977, 11.6977, 11.6977, 0.13732, 2.04452, 0.00, 0.95806]
D0i = [820.659, 559.314, 479.856, 438.27, 468.27, 292.503, 292.503, 178.67, 182.326, 182.326, 182.326, 662.738, 919.306, 0.00, 228.734]
E0i = [0.0046, 1.23722, 3.197, 5.25156, 6.89406, 20.1101, 20.1101, 21.836, 26.8142, 26.8142, 26.8142, -0.1466, -1.06044, 0.00, 0.45444]
F0i = [178.41, 223.284, 200.893, 198.018, 183.636, 910.237, 910.237, 840.538, 859.207, 859.207, 859.207, 680.562, 865.07, 0.00, 326.843]
G0i = [8.74432, 13.1974, 19.1921, 25.1423, 24.4618, 33.1688, 33.1688, 33.4032, 38.6164, 38.6164, 38.6164, 0.90066, 2.03366, 0.00, 1.56039]
H0i = [1062.82, 1031.38, 955.312, 1905.02, 1914.1, 1919.37, 1919.37, 1774.25, 1826.59, 1826.59, 1826.59, 1740.06, 483.553, 0.00, 1651.71]
I0i = [-4.46921, -6.01989, -8.37267, 16.1388, 14.7824, 0, 0, 0, 0, 0, 0, 0, 0.01393, 0.00, -1.3756]
J0i = [1090.53, 1071.29, 1027.29, 893.765, 903.185, 0, 0, 0, 0, 0, 0, 0, 341.109, 0.00, 1671.69]
zci = [0.9981, 0.992, 0.9834, 0.971, 0.9682, 0.953, 0.953, 0.945, 0.919, 0.919, 0.919, 0.9997, 0.9947, 1.0005, 1.0006]

Srizci = 0
for i in range(len(ri)):
    Srizci += (ri[i]/zci[i])

for i in range(len(ri)):
    smes.append((ri[i]/zci[i])/Srizci)

tempK = tempC + 273.15

SxiKi = 0
for i in range(len(smes)):
    SxiKi += smes[i]*((Ki[i])**(5/2))
SxiKi = SxiKi**2

Sxixj = 0
for i in range(len(smes)-1):
    for j in range(i+1,len(smes)):
        Sxixj += smes[i]*smes[j]*(Kij[i][j]**5-1)*((Ki[i]*Ki[j])**(5/2))

Kx = (SxiKi + 2*Sxixj)**(1/5)

p0m = 10**(-3)*(Kx**(-3))*8.31451
pi = davlenie/p0m
t = tempK/1

Q = 0
for i in range(len(smes)):
    Q += smes[i]*Qi[i]

F = 0
for i in range(len(smes)):
    F += (smes[i]**2)*Fi[i]

G1 = 0
for i in range(len(smes)):
    G1 += smes[i]*Gi[i]
G2 = 0
for i in range(len(smes)-1):
    for j in range(i+1,len(smes)):
        G2 += smes[i]*smes[j]*(Gij[i][j] - 1)*(Gi[i] + Gi[j])
G = G1 + G2

V1 = 0
for i in range(len(smes)):
    V1 += smes[i]*(Ei[i]**(5/2))
V1 = V1**2

V2 = 0
for i in range(len(smes)-1):
    for j in range(i+1,len(smes)):
        V2 += smes[i]*smes[j]*(Vij[i][j]**5-1)*((Ei[i]*Ei[j])**(5/2))
V = (V1 + 2*V2)**(1/5)

U = []
for n in range(12):
    U.append(0)
    
def Cn(n):
    global G,g,Q,q,F,f,V,u
    return ((G+1-g[n])**g[n])*((Q**2+1-q[n])**q[n])*((F+1-f[n])**f[n])*(V**u[n])

for n in range(12,58):
    U.append(Cn(n))
    
def Bn(n):
    B = 0
    global smes,u,Ei,Eij,Ki
    for i in range(len(smes)):
        for j in range(len(smes)):
            B += smes[i]*smes[j]*Bnij(n,i,j)*Eijn(i,j)**u[n]*((Ki[i]*Ki[j])**(3/2))
    return B

def Eijn(i,j):
    global Eij,Ei
    return Eij[i][j]*math.sqrt(Ei[i]*Ei[j])
          
def Bnij(n,i,j):
    global Gij,g,Qi,q,Fi,f,Si,s,Wi,w
    return ((Gijn(i,j)+1-g[n])**g[n])*((Qi[i]*Qi[j]+1-q[n])**q[n])*((math.sqrt(Fi[i]*Fi[j])+1-f[n])**f[n])*((Si[i]*Si[j]+1-s[n])**s[n])*((Wi[i]*Wi[j]+1-w[n])**w[n])

def Gijn(i,j):
    global Gij,Gi
    return ((Gij[i][j])*(Gi[i]+Gi[j]))/2

D = []
for n in range(12):
    D.append(Bn(n)*(Kx**(-3)))
for n in range(12,18):
    D.append(Bn(n)*(Kx**(-3))-Cn(n))
for n in range(18,58):
    D.append(0)

def A0(plotnost):
    global a,b,t,u,D,c,k,U
    A0 = 0
    for n in range(58):
        A0 += a[n]*plotnost**b[n]*t**(-u[n])*(b[n]*D[n]+(b[n]-c[n]*k[n]*plotnost**k[n])*U[n]*math.exp(-c[n]*plotnost**k[n]))
    return A0
def A1(plotnost):
    global a,b,t,u,D,c,k,U
    A1 = 0
    for n in range(58):
        A1 += a[n]*plotnost**b[n]*t**(-u[n])*((b[n]+1)*b[n]*D[n]+((b[n]-c[n]*k[n]*plotnost**k[n])*(b[n]-c[n]*k[n]*plotnost**k[n]+1)-c[n]*k[n]**2*plotnost**k[n])*U[n]*math.exp(-c[n]*plotnost**k[n]))
    return A1

plotnost0 = (10**3*davlenie*Kx**3)/(8.31451*tempK) #плотность на 0 шаге - приведенная плотность 

def pirash(plotnost):
    global t
    return plotnost*t*(1+A0(plotnost))

while abs((pirash(plotnost0)-pi)/pi) > 10**(-6):
    plotnost0 += ((pi/t) - (1 + A0(plotnost0))*plotnost0)/(1+A1(plotnost0))

def A2(plotnost):
    global a,b,t,u,D,c,k,U
    A2 = 0
    for n in range(58):
        A2 += a[n]*plotnost**b[n]*t**(-u[n])*(1-u[n])*(b[n]*D[n]+(b[n]-c[n]*k[n]*plotnost**k[n])*U[n]*math.exp(-c[n]*plotnost**k[n]))
    return A2

def A3(plotnost):
    global a,b,t,u,D,c,k,U
    A3 = 0
    for n in range(58):
        A3 += a[n]*plotnost**b[n]*t**(-u[n])*u[n]*(1-u[n])*(D[n]+U[n]*math.exp(-c[n]*plotnost**k[n]))
    return A3

A0 = A0(plotnost0)
A1 = A1(plotnost0)
A2 = A2(plotnost0)
A3 = A3(plotnost0)

z = 1 + A0
cp0r = 0

def cp0ri(i):
    global B0i,C0i,D0i,E0i,F0i,G0i,H0i,I0i,J0i,t
    det = t**(-1)
    cp0ri = B0i[i] + C0i[i]*((D0i[i]*det)/math.sinh(D0i[i]*det))**2+E0i[i]*((F0i[i]*det)/math.cosh(F0i[i]*det))**2+G0i[i]*((H0i[i]*det)/math.sinh(H0i[i]*det))**2+I0i[i]*((J0i[i]*det)/math.cosh(J0i[i]*det))**2
    return cp0ri
for i in range(9):
    cp0r += smes[i]*cp0ri(i)
for i in range(10,13):
    cp0r += smes[i]*cp0ri(i)
cp0r += smes[14]*cp0ri(14)
det = t**(-1)
cp0r += smes[9]*(B0i[9] + E0i[9]*((F0i[9]*det)/math.cosh(F0i[9]*det))**2+I0i[9]*((J0i[9]*det)/math.cosh(J0i[9]*det))**2)
cp0r += smes[13]*(B0i[13] + E0i[13]*((F0i[13]*det)/math.cosh(F0i[13]*det))**2+I0i[13]*((J0i[13]*det)/math.cosh(J0i[13]*det))**2)
kadiabat = (1 + A1 + (((1 + A2)**2)/(cp0r - 1 + A3)))/z
print('Показатель адиабаты равен k = ', kadiabat)