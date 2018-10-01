import math
import random

# Menghitung fungsi yang diberikan
def fungsi( a,b ):
    f = -( abs ( math.sin(a) * math.cos(b) * math.exp( abs ( 1 - ( math.sqrt( a**2 + b**2 ) / math.pi )))))
    return f

# Insialisasi T (temperatur), c(derajat penurunan temperatur), n(iterasi)
T = 5000
c = 0.9
n = 1000

# Mencari titik awal dengan cara membangkitkan 2 nilai random yang kemudian dimasukkan ke fungsi
a = random.uniform(-10,10)
b = random.uniform(-10,10)
F1 = fungsi(a,b)
# print(a,b)
# print(F1)

# Mengecilkan batas atas dan bawah untuk titik kedua dan selanjutnya
def randomUni(x):
    atas = x+6
    bawah = x-6
    if bawah < -10:
        bawah = -10
        atas = 2
    elif atas > 10:
        atas = 10
        bawah = -2
    return random.uniform(bawah,atas)

# Menjadikan titik awal sebagai minimum
min = F1

# Iterasi berdasarkan nilai temperatur
while T > 0.001:
    # Iterasi berdasarkan nilai n
    for x in range(n):

        # Mencari titik berikutnya
        a = randomUni(a)
        b = randomUni(b)
        F2 = fungsi(a,b)
        # print(a,b)
        # print(F2)

        # Mencari selisih/delta dari kedua titik
        dF = F2 - F1

        # Jika delta negatif maka titik baru diterima, jika tidak maka diperiksa dengan menggunakan Metropolis Criterion
        if (dF < 0):
            F1 = F2
        else:
            r = random.random()
            P = math.exp(-dF/T)
            if ( r < P):
                F1 = F2
        
        # Jika titik yang paling baru diterima lebih kecil dari minimum, maka akan disimpan di variabel min
        if F1 < min:
            min = F1

    # Mengalikan temperatur dengan derajat penurunan untuk mengecilkan derajat temperatur
    T = T * c

print (min)