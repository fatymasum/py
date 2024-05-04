# # task1

cavablar= []

for i in range(5):
    number = int(input("eded daxil et: "))
    cavablar.append(number)

cavablar.sort()
print(cavablar)


# task2


def alfabetik_duzulme():
    cumle="sabahin xeyir"
    cumle = cumle.lower()  
    kelimeler = cumle.split()  
    
    
    for i in range(len(kelimeler)):
        herfler=kelimeler[i].split()
        herfler.sort()
        print(herfler)
    print(kelimeler)
alfabetik_duzulme()        




# task3

n = 13
cehd_sayi = 0

while True:
    giris = int(input("eded daxil edin: "))
    cehd_sayi += 1
    
    if giris == n:
        print(f"Tebrikler! {cehd_sayi} cəhdə {n} rəqəmini tapdınız.")
        break
    
 
# task4


for sayi in range(2, 101):  # 1 bir asal sayı olmadığı için 2'den başlıyoruz
    asal_mi = True
    for bolen in range(2, int(sayi ** 0.5) + 1):  # Bir sayının asal olup olmadığını kontrol etmek için 2'den kareköküne kadar olan sayıları deniyoruz
        if sayi % bolen == 0:
            asal_mi = False
            break
    if asal_mi:
        print(sayi)