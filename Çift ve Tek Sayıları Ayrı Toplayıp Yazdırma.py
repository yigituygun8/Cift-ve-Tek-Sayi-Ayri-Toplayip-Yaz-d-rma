# Klavyeden girilecek n tane sayının (kullanıcı belirleyecek) tek olanlarını ayrı çift olanlarını ayrı toplayıp sonuçları ekrana yazdır

tek = []
cift = []
n = int(input("Kaç Sayı Girmek İstiyorsunuz?: "))

for k in range(n):
    sayi = int(input("Sayı Giriniz: "))
    if sayi % 2 == 0:
        cift.append(sayi)
    else:
        tek.append(sayi)
print("-"*30)
print("Tek Sayılar:", tek)
print("Çift Sayılar:",cift)
print("-"*30)
print("Girilen Tek Sayıların Toplamı:",sum(tek))
print("Giirilen Çift Sayıların Toplamı:",sum(cift))