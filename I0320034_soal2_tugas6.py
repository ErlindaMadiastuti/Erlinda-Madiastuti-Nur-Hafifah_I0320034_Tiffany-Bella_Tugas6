# Masukkan banyak nilai
banyak_nilai = int(input("Masukkan banyak nilai yang akan dihitung rata-ratanya : "))
nilai1 = []

# Masukkan nilai
for i in range(1, banyak_nilai+1):
    nilai2 = int(input("Masukan nilai %d : " % i))
    nilai1.append(nilai2)
    i += 1

# Menjumlahkan nilai
jumlah_nilai = sum(nilai1)

# Menghitung rata-rata
rata_rata = jumlah_nilai/banyak_nilai

print("Nilai rata-rata Anda adalah", rata_rata)
