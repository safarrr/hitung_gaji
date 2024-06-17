# import locale

# locale.setlocale(locale.LC_ALL, 'id_ID')
def format_currency_id(amount):
    return f'Rp {amount:,.2f}'  # Assumes amount is a float with 2 decimal places

print("       Progam Hitung Gaji Karyawan      ")
print("      -----------------------------     ")

# Data tunjangan jabatan 
gajipokok = {
    "A" : 1500000,    
    "B" : 2000000,
    "C" : 3000000
}

# Honor lembur per jam
honorlembur= {
    "A" :25000,
    "B" :30000,
    "C" :35000
}

def hitung_gaji(golongan,harikerja,jamlembur):
    if golongan in gajipokok and golongan in honorlembur:
        gaji= gajipokok[golongan]
        tunjangan= 30000 * harikerja
        honorperjamlembur= honorlembur[golongan]
        honorlemburtotal= jamlembur * honorperjamlembur
        gajibersih= gaji+tunjangan+ honorlemburtotal
        return gajibersih
    else:
        return"Golongan tidak valid"
    
#Input nama,golongan,harikerja,jamlembur
total_data = int(input("masukan total data : "))
data = []
for i in range(total_data):
    print("data ke ", i+1 )
    nama= input("Nama Karyawan: ")
    golongan= input("Masukan golongan (A/B/C): ").upper()
    harikerja= int(input("Masukkan jumlah hari kerja: "))
    jamlembur= int(input("Masukkan jumlah jam lembur: "))
    gajitotal= hitung_gaji(golongan,harikerja,jamlembur)
    data.append({
        "nama": nama,
        "golongan": golongan,
        "harikerja": harikerja,
        "jamlembur": jamlembur,
        "gajitotal": gajitotal,
    })
 
for d in data:
    print("="*20)
    print("nama                 : ",d["nama"])
    print("golongan             : ",d["golongan"])
    print("jumlah hari kerja    : ",d["harikerja"])
    print("jumlah lembur        : ",d["jamlembur"])
    print("total gajih          : ",format_currency_id(d["gajitotal"]))

print("="*20)

#Panggil Fungsi Hitunggaji

#Cetak Hasil

# if isinstance(gajitotal,int):
#     print(f"Total gaji bersih untuk golongan {golongan}: {format_currency_id(gajitotal)}")
# else:
#     print(gajitotal)