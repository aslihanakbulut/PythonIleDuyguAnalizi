# PythonIleDuyguAnalizi
# Projenin Amacı
Projede Türkçe metinlerde duygu analizi yaparak  verilen cümlenin belirttiği duyguya göre  ‘Pozitif’, ‘Negatif’ ya da  ‘Nötr’ olarak sınıflandırılması amaçlanmaktadır.

# Projenin Yapılışı
1-	Gerekli kütüphanelerin import edilmesi (pandas, nltk)

2-	Veri setindeki cümlelerin ve kelimelerin okunması, 

3-	Okunan cümleden “noktalama_temizle” fonksiyonu ile noktalama işaretlerinin çıkarılması ve cümledeki harflerin lower() fonksiyonu ile küçük harfe çevrilmesi

4-	“noktalama_temizle” fonksiyonundan alınan noktalamasiz_cumle’ nin; split(“ “) ile kelimelerine ayrılması 

5-	Kelimelerine ayrılmış cümlede “baglaclari_cikar” fonksiyonu içinde nltk.corpus.stopwords.words('turkish') kullanılarak cümlenin polaritesine etki etmeyecek kelimelerin (ve, ile, en, değil, daha vb.) çıkarılması 

6-	Nokatalama işareti ve bağlaçların bulunmadığı cümlede kelimelerin köklerine ayrılması 

          kokbul = TurkishStemmer()
          baglacsiz_cumle[i] = kokbul.stem(baglacsiz_cumle[i])

7-	Kelime listesinden okunan kelimelerin köklerine ayrılması ve olumlu–olumsuz  kelime-fiil olma durumuna göre ayrı listelere eklenmesi

          kokbul = TurkishStemmer()
          for i in range(len(pozitif_kelimeler)):
   			            pozitif_kelimeler[i] = kokbul.stem(str(pozitif_kelimeler[i]))
          for i in range(len(pozitif_fiiller)):
    			         pozitif_fiiller[i] = kokbul.stem(str(pozitif_fiiller[i]))
          for i in range(len(negatif_kelimeler)):
    			         negatif_kelimeler[i] = kokbul.stem(str(negatif_kelimeler[i]))
          for i in range(len(negatif_fiiller)):
    			         negatif_fiiller[i] = kokbul.stem(str(negatif_fiiller[i]))
 
8-	Cumleyi_Analiz_Et fonksiyonu ile köklerine ayrılmış cümlede kelimelerin kelime listesinde bulunduğu sınıfa göre olumlu-olumsuz olma durumunun kontrol edilmesi ve buna bağlı olarak gerekli değişkenlerin güncellenmesi

                 for kelime in kelimeler:
        		 if(kelime in p_k):
            		pozitif_kelime_sayisi+=1
       		 if(kelime in p_f):
            		pozitif_fiil_sayisi+=1
      		 if(kelime in n_k):
          			negatif_kelime_sayisi+=1
        		 if(kelime in n_f):
            		negatif_fiil_sayisi+=1

9-	Hesaplanan toplam değerine göre cümlenin ‘Pozitif’, ‘Negatif’ ya da  ‘Nötr’ olarak sınıflandırılması

            toplam= pozitif_fiil_sayisi+pozitif_kelime_sayisi - negatif_fiil_sayisi-negatif_kelime_sayisi
            if toplam > 0:
               return "Pozitif"
            if toplam < 0:
               return "Negatif"
            return "Nötr"

10-	Cumleyi_Analiz_Et fonksiyonundan alınan sonucun “tahmin” değişkenine, cümlenin sınıf etiketinin “gerçek” değişkenine atanması ve bu değişkenlerin karşılaştırılması buna göre doğru ya da yanlış tahmin sayısının güncellenmesi

            dogru_tahmin=0
            yanlis_tahmin=0
            for cumle in  cumleler:
                tahmin = Cumleyi_Analiz_Et(cumle[0], pozitif_kelimeler,pozitif_fiiller,negatif_kelimeler,negatif_fiiller)
                gercek = cumle[1]
                if tahmin.lower() == str(gercek).lower():
                    dogru_tahmin+=1
                else:
                    yanlis_tahmin+=1

11-	Doğru ve yanlış tahmin sayıları ile hesaplanan başarı oranının ekrana yazdırılması

            print("Doğru tahmin sayisi: "+ str(dogru_tahmin))
            print("Yanlış tahmin sayisi: " + str(yanlis_tahmin))
            basari_orani = (dogru_tahmin/(dogru_tahmin+yanlis_tahmin))*100
            print("Başarı oranı : "+ str(basari_orani))
            
# Sonuc
Örnek veri setinde bulunan 1200 cümlede 637 cümle doğru sınıflandırılmış, %53,083 başarı oranı elde edilmiştir. 

