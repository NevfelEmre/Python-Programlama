class sinif:
    a = 0
    b = "ads"
    c = [1, 3, 5]

    def __init__(self, a):
        self.metin = a

    def __del__(self):
        print("beni siliyorlar")
        
    def yazdir(self):
        d = 100
        print(d, self.a)
    def yazdir2(self, t): #self yazmak zorundaymışız
        print(self)
    def __str__(self):
        return "Nesne gibi nesne"





nesne = sinif("Meitn")
print(nesne.a) #0
nesne.a = 32
print(nesne.a) #32

nesne.yazdir() #(100 32)
nesne.yazdir2("sfsdf")

print(nesne.metin)
del nesneS