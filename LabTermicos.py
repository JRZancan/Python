# Calculo de MMQ #
import matplotlib.pyplot as plt
from math import sqrt

x=[-23.8,-21,-15.5,-13.5,-10,-6,0,4]                       #Adicionar os Valores identificados para X#
y=[-0.65,-0.545,-0.46,-0.375,-0.260,-0.145,0,0.125]   #Adicionar os Valores Identificados para Y#
z=[]
yerr=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
Sx=Sy=Sx2=Sy2=Sxy=Mx=Mx2=My=Spxy=Sqx=Sqy=Sxx=Syy=r=r2=0     # Variaveis : Sx -> Somatorio de X / Sx2 -> Somatorio de x² / Mx -> Media de x / Mx2 -> Media de X ao Quadrado #
                                                            #             Sy -> Somatorio de Y / Sy2 -> Somatorio de y² / My -> Media de y / Sxy -> Somatorio de x*y #

n = len(x)
for i in range(n):       # Calculo das Variaveis
    Sx = Sx + x[i]
    Sxx = Sx*Sx
    Sy = Sy + y[i]
    Syy = Sy*Sy
    Mx = Sx / n
    Mx2 = Mx * Mx
    My = Sy / n
    Sx2 = Sx2 + (x[i]*x[i])
    Sy2 = Sy2 + (y[i]*y[i])
    Sxy = Sxy + (x[i]*y[i])
    Spxy= Sxy - ((Sx*Sy)/n)
    Sqx= Sx2 - (Sxx/n)
    Sqy= Sy2 - (Syy/n)
    r=Spxy/sqrt(Sqx*Sqy)
    r2=r*r


# print(x, Sx, Sx2, Mx, Mx2) -> Teste
# print(y, Sy, Sy2, My)
# print(Sxy)

b= (Sxy-(n*Mx*My))/(Sx2-(n*Mx2))   #Calculo de a e b.
a= My-(b*Mx)

# print(b,a) -> Teste

for i in x:                     #Calculo da reta para os valores de A e B.
    aux= a + b*i
    z.append(aux)

a = round(a,3)                  # Arredondamento
b = round(b,3)                  #       ---
Sx = round(Sx,3)                #       ---
Mx = round(Mx,3)                #       ---
Mx2 = round(Mx2,3)              #       ---
Sx2 = round(Sx2,3)              #       ---
Sy = round(Sy,3)                #       ---
My = round(My,3)                #       ---
Sy2 = round(Sy2,3)              #       ---
r2 = round(r2,3)                #       ---
Sxy = round(Sxy,3)              #  Arredontamento

def table():        # Criacao da Tabela com os valores calculados
    row_labels = ['Σx', 'Xbar', 'Xbar²', 'Σx²','Σy','Ybarr','Σy²','Σxy','b','a','R²']
    table_vals = [[Sx], [Mx], [Mx2], [Sx2], [Sy], [My], [Sy2], [Sxy], [a], [b], [r2]]

    plt.table(cellText=table_vals,
                colWidths=[0.1279],
                rowLabels=row_labels,
                loc='center right',
                bbox=[0.793, 0.01, 0.2, 0.56]) #-> Mudar a localização da tabela. OBS: Valores menores que 1 !

plt.errorbar(x=x, y=y,yerr=yerr,fmt='o')
plt.plot(x,z)                                                   # Regressao Linear
plt.xlabel("Variação de Temperatura (°C)")                      # Titulo do Eixo X
plt.ylabel("Variação de Altura (cm)")                           # Titulo do Eixo Y
plt.title("Dilatação do Alcool - t0=26°C")                      # Titulo Principal
table()                                                         # Chamando função tabela para gera-la
plt.show()