import pandas as pd
from TurkishStemmer import TurkishStemmer
import nltk
from nltk.corpus import stopwords


file_name="ornek_duygu-analizi-verisi.xlsx"

#______FONKSIYONLAR _________________________________________________________________

def noktalama_temizle(str):
    nokt_isaret = [".",":",";", ",", "!", "?", "\"","\'","<",">","(",")"]
    for isaret in nokt_isaret:
        str = str.replace(isaret,"")
    return str.lower()


def baglaclari_cikar(cumledeki_kelimeler):
    baglaclar = nltk.corpus.stopwords.words('turkish')
    baglaclar = set(stopwords.words('turkish'))
    baglacsizCumle = []
    for i in range(len(cumledeki_kelimeler)):
        if cumledeki_kelimeler[i] not in baglaclar:
            baglacsizCumle.append(cumledeki_kelimeler[i])
        
    return baglacsizCumle
            
def cumledeki_kok_kelimeler(cumle):
    noktalamasiz_cumle = noktalama_temizle(cumle)
    cumledeki_kelimeler = noktalamasiz_cumle.split(" ")

    baglacsiz_cumle = baglaclari_cikar(cumledeki_kelimeler)
    
    #burada kokleri cikar.
    kokbul = TurkishStemmer()
    for i in range(len(baglacsiz_cumle)):
        baglacsiz_cumle[i] = kokbul.stem(baglacsiz_cumle[i])


    return baglacsiz_cumle


def Cumleyi_Analiz_Et(cumle,p_k,p_f,n_k,n_f):
    kelimeler = cumledeki_kok_kelimeler(cumle)

    pozitif_kelime_sayisi = 0
    pozitif_fiil_sayisi   = 0
    negatif_kelime_sayisi = 0
    negatif_fiil_sayisi   = 0

    for kelime in kelimeler:
        if(kelime in p_k):
            pozitif_kelime_sayisi+=1
        if(kelime in p_f):
            pozitif_fiil_sayisi+=1
        if(kelime in n_k):
            negatif_kelime_sayisi+=1
        if(kelime in n_f):
            negatif_fiil_sayisi+=1

 

    toplam =  pozitif_fiil_sayisi+pozitif_kelime_sayisi - negatif_fiil_sayisi-negatif_kelime_sayisi
    if toplam > 0:
        return "Pozitif"
    if toplam < 0:
        return "Negatif"
    return "Nötr"


    pass

#____________________________________________________________________________________


# _____ Analiz edilecek cumleleri okuyoruz _________________________________________
excel_sayfa1 = pd.read_excel(file_name, sheet_name="Sayfa1")
cumleler = excel_sayfa1.to_numpy()

# _____ Pozitif ve Negatif kelime ve fiilleri okuyoruz _____________________________

excel_sayfa2 = pd.read_excel(file_name, sheet_name="Sayfa2")
kelime_fiil_listesi = excel_sayfa2.to_numpy()
pozitif_kelimeler = kelime_fiil_listesi[:,0]
pozitif_fiiller   = kelime_fiil_listesi[:,1]
negatif_kelimeler = kelime_fiil_listesi[:,2]
negatif_fiiller   = kelime_fiil_listesi[:,3]

#____Kelime listesinin de koklerini ayiriyoruz ________________________

kokbul = TurkishStemmer()
for i in range(len(pozitif_kelimeler)):
    pozitif_kelimeler[i] = kokbul.stem(str(pozitif_kelimeler[i]))

for i in range(len(pozitif_fiiller)):
    pozitif_fiiller[i] = kokbul.stem(str(pozitif_fiiller[i]))

for i in range(len(negatif_kelimeler)):
    negatif_kelimeler[i] = kokbul.stem(str(negatif_kelimeler[i]))

for i in range(len(negatif_fiiller)):
    negatif_fiiller[i] = kokbul.stem(str(negatif_fiiller[i]))



#sonuc 0 dan buyukse pozitif, kucukse negatif, sifir ise hicbir eslesme bulunamadi
dogru_tahmin=0
yanlis_tahmin=0
for cumle in  cumleler:
    tahmin = Cumleyi_Analiz_Et(cumle[0], pozitif_kelimeler,pozitif_fiiller,negatif_kelimeler,negatif_fiiller)
    gercek = cumle[1]
   
    if tahmin.lower() == str(gercek).lower():
        dogru_tahmin+=1
    else:
        yanlis_tahmin+=1
   

print("Doğru tahmin sayisi: "+ str(dogru_tahmin))
print("Yanlış tahmin sayisi: " + str(yanlis_tahmin))

basari_orani = (dogru_tahmin/(dogru_tahmin+yanlis_tahmin))*100
print("Başarı oranı : "+ str(basari_orani))
    



