# kendisine gönderilen sayılardan sadece polindrom olanları toplayan diğerelini de bu toplamdan çıkaran ve geri gönderen fonksiyon.

def polinDRAM (*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam

print(toplam)