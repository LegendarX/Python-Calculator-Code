print("Hesap Makinesi")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("\nToplama işlemi için 1'e \nÇıkarma işlemi için 2'ye \nÇarpma işlemi için 3'e \nBölme işlemi için 4'e basınız:")

islem = int(input())

if islem == 1:
    print("\nSonuç:" + str(sayi1 + sayi2))
elif islem == 2:
    print("\nSonuç:" + str(sayi1 - sayi2))
elif islem == 3:
    print("\nSonuç:" + str(sayi1 * sayi2))
elif islem == 4:
    print("\nSonuç:" + str(sayi1 / sayi2))
else:
    print("Geçersiz işlem")