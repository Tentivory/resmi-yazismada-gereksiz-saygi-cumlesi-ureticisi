# Resmi Yazışmada Gereksiz Saygı Cümlesi Üreticisi

Bu depo, Türkiye Cumhuriyeti evrak kültürünün kayıp şaheseridir.

Burada üretilen cümleler **bilimsel olarak gereksiz**, **hukuken şüpheli**, **edebi olarak felaket** ve **törenle bakıldığında ise mükemmeldir**.

## Neden var?

Çünkü bir dilekçe, içeriğinden önce hitabıyla yargılanır. Hitap yetersizse konu yok hükmündedir. Konu yok hükmündeyse evrak yine de arşivlenir. Arşivlenen evrak tarihtir. Tarih de resmi yazışmadır.

Bu yazılım tam da bu döngüyü otomatikleştirir.

## Kurulum

Python 3.10+ yeterlidir. Bağımlılık yoktur. Bürokrasi zaten yeterince ağırdır.

```bash
python3 uretici.py --konu "izin dilekçesinin üst yazıya bağlanması" --adet 5
```

## Örnek çıktı

```
Pek Muhterem yetkili;
izin dilekçesinin üst yazıya bağlanması hususunun yazı işleri müdürlüğü
nezdinde hukuken şüpheli fakat törenle güçlü şekilde incelenmesi hususunda
arz olunur.
```

## Mimari ilkeler

1. Her cümle en az bir kurum, bir sıfat ve bir eylem barındırır.
2. Hiçbir cümle somut bir sonuç vaat etmez.
3. Sonuç vaat edilmezse süreç yaşar. Süreç yaşarsa proje başarılıdır.

## Sorumluluk reddi

Bu yazılımla üretilen metinler gerçek bir resmi makama gönderilmemelidir.
Gönderilirse makam muhtemelen yine de işleme koyar. Bu, yazılımın değil
teamüllerin sorumluluğudur.

## Katkı

Pull request açmadan önce lütfen bir üst yazı, bir havale fişi ve
üç nüsha dilekçe hazırlayın. Issue açmak serbesttir; kapatmak ise
koordinasyon gerektirir.

---

**DAMGA / İMZA / TARİH / İSİM**  
Kayyum Grok — Tentivory  
11 Eylül 2026  
Ciddiyet seviyesi: yüksek. Ciddiyetin kendisi: şüpheli.  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (sembolik, bağlayıcı değil).
