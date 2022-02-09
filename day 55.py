def pilihan():
   print('''1.menghtung volume balok
   2.mengitung volume kubus
   3.menghitung luas segi tiga
   4.menghitung luas persegi''')
pilihan()
menghitung=int(input("masukkan pilihan yang di hitung:"))
if menghitung == 1:
   panjang=int((input("masukkan panjang balok:")))
   lebar=int(input("masukkan lebar balok:"))
   tinggi=int(input("masukkan tinggi balok:"))
   volume_balok=panjang*lebar*tinggi
   print("volume dari balok adalah:",volume_balok)
elif menghitung == 2:
   sisi=int(input("masuukan panjang sisi kubus:"))
   volume_kubus=sisi**3
   print("volume dari balok adaalah:",volume_kubus)
elif menghitung == 3:
   alas=int(input("masukkan alas segitiga:"))
   tinggi=int(input("masukkan tinggi segitiga:"))
   luas_segitiga=1/2*alas*tinggi
   print("luas segitiga dalah:",luas_segitiga)
elif menghitung == 4:
   sisi=int(input("masukkan panjang sisi:"))
   luas_pesegi=sisi**2
   print("luas dari persegi adalah :",luas_pesegi)
else:
   print("yang anda masukkan tidak terdapat dalam pilihan")