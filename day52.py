print("perbedaan dari mendasar dari data list, data tuple, data set ")
print("perbedaan secara pengertian")
def perbedaan_secara_pengertian():
    print("1.dapat di akses via indeks")
    print("2.bisa di ubah via indeks")
    print("3.bisa di tambah anggota baru atau di hapus")
    print("4.semua nggota harus unik")
perbedaan_secara_pengertian()
sifat=int(input("masukkan macam sifat:"))
if sifat == 1:
    print("data list dan data tuple")
elif sifat == 2:
    print("data list")
elif sifat == 3:
    print("data list data set")
elif sifat == 4:
    print("hanya dat set")

print("perbedaan sintaks dari 3 data tersebut")
data_list=[1,2,3,4,5]
data_tuple=(1,2,3,4)
data_set={1,2,3,4,5}
print(data_list)
print("menggunakan yang tanda kurung siku")
print(data_tuple)
print("menggunakan tanda  kurung")
print(data_set)
print("menggunakan tanda kurung kurawal")

        