print("data dictionary")
print("cara membuat data dictionary")
# dapat menggunakan tanda kurung kurawal {}
data_diri={"nama":"nurul inayah","tgl lahir": "10/3/2002","tempat":"kelurahan tande", "universitas":"UNSULBAR","prodi":"informatika"}
# dan dapat menggunakan fungdi dict()
data_pribadi=dict(nama="awalluddin",tgl_lahir="8/4/2005",tempat="kelurahan tande",sekolah="SMKN 2 MAJENE",jurusan="multemedia")
print("cara mengagkses dat dictionary")
print("tanggal lahir",data_diri["tgl lahir"])#cara pertama
print("tanggal lahir",data_pribadi.get("tgl_lahir"))#cara ke dua
#keunggulan apa  ila kita menggunkan cara ke dua dalam mengecek elemen dari data dictionary kita dapat 
#mencamtumkan nialai dari keynya apa bila kita salah memakai keynya agar tidak eror 
print("tanggal lahir",data_pribadi.get("tgl_lair","8/4/2005"))
print("perulangan untuk dictionary")
kabupaten={1:"majene",2:"polewali",3:"mamuju",4:"makassar",5:"palu",6:"pinrang"}
print("memakai break")
for key in kabupaten:
    if key == 4:
        break
    print(key,'--->',kabupaten[key])   
print("memakai continue") 
for key in kabupaten:
    if key == 4:
        continue
    print(key,'--->',kabupaten[key])   
print("mengubah nilai item")
hari={1:"seinin",2:"selasa",3:"rabu",4:"kamis"}
hari[3]="sabtu"
print(hari)
print("menambah item")
hari1={1:"seinin",2:"selasa",3:"rabu",4:"kamis"}
hari1[5]="jumat"
print(hari1)
print("mengahups itme")
#cara pertama: menggunakan del<dict[key]>
hari2={1:"seinin",2:"selasa",3:"rabu",4:"kamis"}
del(hari2[4])
print(hari2)
#cara ke dua : menggunakan pop()
hari2={1:"seinin",2:"selasa",3:"rabu",4:"kamis"}
hari2.pop(3)
print(hari2)
print("mengecek keanggotaan")
#di dalam pengecekan keanggotaan yang kita pakai itu key nya bukan velue
print(1 in hari2)
print(9 in hari2)