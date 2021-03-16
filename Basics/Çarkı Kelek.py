# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:26:53 2020

@author: Ahmet Kasım Erbay
"""
import time,random

while True:
    print("\n****Çıkmak için 'q' ya basarsın...*****")
    a = input("Canın mı sıkıldı?\n\nEvet için 1'i tuşla\nHayır için 2'yi tuşla\n")
    if(a=="q"):
        print("Oyundan Çıkılıyor...")
        for i in range(5):
            print(".")
            time.sleep(1)
        print("Yine bekleriz...")
        break
    elif(a == "1"):
        b=input("Oyun mu istiyorsun?\n\nEvet için 1'i tuşla\nHayır için 2'yi tuşla\n")
        if(b=="1"):
            c=input("Refiklerini mi özledin?\n\nEvet için 1'i tuşla\nHayır için 2'yi tuşla\n")
            if(c=="1"):
                print("\nSen kaşındın ;)\n")
                time.sleep(2)
                print("Geliyor oyun biraz bekle...\n")
                time.sleep(2)
                print("---------------------------HOŞGELDİN----------------------------------")
                time.sleep(2.5)
                print("""
                    *     *    *******   ****    *
                    * *   *    *         *   *   
                    *  *  *    *         * * *   * 
                    *   * *    ******    *   *   *
                    *    **    *         *    *  *
                    *     *    *******   * * *   *
                """)
                print(""" 
                      
      Bu oyun bir sayı tahmin oyunudur. Nebi Resul Kardeşim için özel olarak tasarlanmıştır.
      
      Dikkat Program Atar Yapar...
                
                """)
                z = input("Kuralları öğrenmek için lütfen ekrana 'Kurallar' yazınız.\n")
                if(z.lower()=="kurallar"):
                    print("Geliyoooor biraz daha sabır")
                    for i in range(5):
                        print(".")
                        time.sleep(1)
                    print("""                       ---- 0-100 arasında random atanan sayıyı bulacaksın.----
                          
                    Dikkat program atar yapabilir...
                          
                          Sakın korkma devam et oynamaya...
                          
                          Kaç defada tahmin edebileceğini sorup devam edeceğiz. Yazdığın sayı kadar deneme hakkına sahip olacaksın dikkatli seç.
                          
                          Maximum 100 puana sahip olacaksın. Yanlış kullandığın her deneme hakkı için puan kaybedeceksin.
                          
                          *****100 puan alır ve bana SS atarsan adresine özel ödüller yolluyoruz...*****
                                     
                                      ***** Tabi ünlü İNSTA hesabında bizi de paylaşırsan*****
                          
                          DİKKAT!!!
                          Ne kadar risk alırsan o kadar fazla kazanırsın...
                          """)
                    a = random.randint(1,100)
                    b = int(input("Sence bu oyunu kaç deneme hakkında kazanırsın?\n--->"))
                    turn = 0
                    print("(Lütfen1-100 arası bir sayı ver)\n")
                    print("\n****Çıkmak için 'q' ya basarsın...*****")
                    while turn<b:
                        turn+=1
                        guess=int(input("Tahmin alalım:\n--->"))
                        if(guess=="q"):
                            print("Oyundan Çıkılıyor...")
                            for i in range(5):
                                print(".")
                                time.sleep(1)
                                print("Yine bekleriz...")
                                break
                        elif(guess==a):
                            print("\n****Helal bea kazandın!!! ;) {}. defada bildin. Puanın: {}".format(turn,100-turn*(100/b)))
                            print("\n****Kasımovic Production Gururla Sundu...\nYine bekleriz")
                            print("\nÇıkmak için 'q' ya basarsın...")
                            break
                        elif(guess>a):
                            print("Fazla Salladın biraz in!\nKalan hakkın:{}\n".format(b-turn))
                        elif(guess<a):
                            print("Ufak at da civcivler aç kalmasın!\nÇık biraz!\nKalan hakkın:{}\n".format(b-turn))
                        if(b==0):
                            print (f"Kazanamadın kardeşim!\nBulamadığın sayı:{a}")
                            print("\n")
                            print("Olsun yine de denemeye devam edeceğiz...")
                            break
                        elif(b-turn==0):
                            print (f"Kazanamadın kardeşim!\nBulamadığın sayı:{a}")
                            print("\n")
                            print("Olsun yine de denemeye devam edeceğiz...")
                else:
                    print("Kuralları öğrenmeden oynayamazsın.\nBaştan başlayalım")
                    break
                
            else:
                d = input("Nasıl özlemezsin özlemişsindir kesin!!\nO zaman lütfen ekrana 'ÖZLEDİM' yazar mısın canım kardeşim...?")
                if(d.lower()=="özledim"):
                    print("Sana ceza... Bizi özlemediğin için programı baştan başlatacaksın:)")
                    break
        else:
            print("Nasıl oyun istemezsin birader !!! :|\n Cuma günü demedin mi 'İçinde bulunduğumuz zorunlu asosyallik beni bitirdi' diye")
            e = input("Dediysen 1'e demediysen 2' ye bas")
            if(e=="1"):
                print("Lütfen programı baştan başlatıp doru seçeneği seç deli etme bizi...")
                break
            else:
                print("Dememiş olabilirsin ama oyun yazdık o kadar bizi kırma\nLütfen baştan başlat şu programı")
                break
    else:
        print("Canının sıkılmamamsı imkan dahilinde olmadığından mütevellit sanan bu çılgın oyunu hazırladım.\nEmeğe saygı...\n")
        print("LÜTFEN OYUNU ORİJİNAL SİTEDEN OYNAYIN...\nBOŞ YAPANLARA İTİBAR ETMEYİNİZ...")
        print("Oynamak İçin Tekrar başlat...")
        break