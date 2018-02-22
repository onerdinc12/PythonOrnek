satir =0
sutun =0

satir = int(input("Satir sayınısı giriniz"))
sutun = int(input("Sutun sayısını giriniz"))
matriks = []
matriks2 = []
matriksToplam = []
for i in range(satir):
    matriks += [[satir] * sutun]


# 1. matriksi doldurma

for i in range(satir):
    for j in range(sutun):
        sayi = int(input("Matriksin %s satırının %s sutunun değerini giriniz" %(i+1,j+1)))
        matriks[i][j] = sayi

print("İkinci matriks için değerleri giriniz")

# ikinci matriks oluşturalım
for i in range(satir):
    matriks2 += [[satir] * sutun]


# 2. matriksi dolduralım
for i in range(satir):
    for j in range(sutun):
        sayi = int(input("2 . Matriksin %s satırının %s sutunun değerini giriniz" %(i+1,j+1)))
        matriks2[i][j] = sayi


for i in range(satir):
    matriksToplam += [[satir] * sutun]

for i in range(satir):
    print("\n")
    for j in range(sutun):
        matriksToplam[i][j] = matriks[i][j] + matriks2[i][j]


print("Sonuçları yazalım")

print(" Sonuç" ,matriksToplam)