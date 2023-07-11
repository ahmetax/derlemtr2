# derlemtr2
DerlemTR Projesinin Devamı

- DerlemTr projesinin yeni sürümüne DerlemTr2 adı altında burada devam edeceğiz.
- Bu yeni sürümde geçerliliği test edilmiş bir derlem dosyası ile başlayacak, içeriği giderek geliştireceğiz.
- Hatalı ve geçersiz sözcükleri ayıkladığım, sadece denetimden geçmiş Türkçe sözcükleri içeren bir metin dosyasını öncelikle paylaşacağım.
- Bir başka dosyada ise frekansı düşük ve denetlenmemiş sözcükler yar alacak.
- Bu aşamada artık frekans takibi yapmayacağız, sadece denetlenmiş sözcüklerin sayısını arttıracağız.
- Kodlama dilimiz yine Python olacak
- Sözcük denetlemede Zemberek çalışmasından yararlanacağız.

## 2023-07-11 : zemberek_denetle.py betiği çalıştırıldı. hamveriler/tumkelimeler001.txt dosyasından 2 dosya elde edildi:
- derlem/derlemtr.txt  (zemberek denetiminden geçmiş sözcükler - 1,686,804 adet)
- hamveriler/denetimsiz.txt (zemberek denetimine takılmış sözcükler - 1,849125 adet)
   
- denetimsiz.txt dosyasının içerdiği sözcükler manuel olarak veya kalbur gibi araçlarla denetlenmeye devam edecek.
   Bu dosyadan kesin hatalı ve kesin geçerli sözcükler silinecek ve uzun vadede tamamen sıfırlanacaktır.
   Kesin geçerli sözcükler derlem/derlemtr.txt dosyasına eklenecektir.

