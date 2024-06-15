GAJI_POKOK = {
    'A': 1500000,
    'B': 2000000,
    'C': 3000000
}

LEMBUR_PER_JAM = {
    'A': 25000,
    'B': 30000,
    'C': 35000
}
 
def hitung_gaji(golongan, hari_kerja, jam_lembur):
    gaji_pokok = GAJI_POKOK[golongan]
    tambahan_lembur = LEMBUR_PER_JAM[golongan] * jam_lembur
    total_gaji = gaji_pokok + tambahan_lembur
    return total_gaji
 
nama = input("Nama : ")
golongan = input("Masukkan golongan (A/B/C): ").strip().upper()
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan (minimal 20 hari): "))
jam_lembur = int(input("Masukkan jumlah jam lembur dalam sebulan: "))
 
if golongan not in GAJI_POKOK:
    print("Golongan tidak valid.")
elif hari_kerja < 20:
    print("jumlah minimal hari adalah 20")
else: 
    total_gaji = hitung_gaji(golongan, hari_kerja, jam_lembur)
    print(f"Total gaji untuk {nama} golongan {golongan} dengan {hari_kerja} hari kerja dan {jam_lembur} jam lembur adalah: Rp {total_gaji:,}")

