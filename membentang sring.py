#untuk menangani kasus seperti ini,setiap kolom harus dibentang dengan nilai 
# tertentu menggunakan metode ljust(),rjust(),atau center() yang terdpat di dalam kelas str.

nilai='python'.ljust(10)
print(nilai)

nilai='python'.ljust(10,"#")
print(nilai)
# metode ljust() di dalam kelas str berguna untuk membentang teks dan meluruska teks kiri kirinya.

nilai1="hello world!".rjust(20,"*")
print(nilai1)
# jika yang ingin diluruskan sisi kananya, makan anda perlu menggunakan metode rjust()r()

nilai2="selamat datang".center(25,"*")
print(nilai2)
#jika kita ingin rata tengah kita dapat menggunakan metode center()