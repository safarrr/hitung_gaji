import os
import pandas as pd
from datetime import datetime
def get_format():
    data = {
    'Nama': [],
    'hari': [],
    'golongan gaji pokok': [],
    'lembur dalam Jam': [],
}
    df = pd.DataFrame(data)
    df.to_excel('format_gaji.xlsx', index=False)
def clearConsol():
    if os.name == 'nt':
        # For Windows
        os.system('cls')
    else:
        # For Unix-like systems (Linux, macOS, etc.)
        os.system('clear')

def hitung_gaji(golonganGaji, nama, lembur,hari):
    if hari < 20:
        print(f"{nama} belom 20 hari tidak di masukan ke data atau tidak di tampilkan")
        return {}
    
    gapok = 0
    hasil_lembur = 0 
    match golonganGaji.upper():
        case "A":
            gapok = 1_500_000 
        case "B":
            gapok = 2_000_000 
        case "C":
            gapok = 3_000_000 
        case _ :
            print(F"golongan gaji pokok tidak ada tolong masukan ulang")
            exit()

    match golonganGaji.upper():
        case "A":
            hasil_lembur = 25_000 
        case "B":
            hasil_lembur =  30_000 
        case "C":
            hasil_lembur = 35_000 
        case _ :
            print(F"golongan gaji pokok tidak ada tolong masukan ulang")
            exit()
            
    total_gaji = gapok + (lembur * hasil_lembur)
    data = {"nama":nama,"golongan":golonganGaji, "total_gaji":total_gaji,"jam_lembur": lembur, "total_lembur":lembur * hasil_lembur,"gaji_format": f"Rp {total_gaji:,.0f}".replace(',', '.') }
    return data

def saveElsx(data):
    date_now = datetime.now()
    df = pd.DataFrame(data)
    filename = f'{date_now.strftime("%H_%M_%S")}_data_gaji.xlsx'
    df.to_excel(filename, index=False)
    print(f"""
====================================================
DATA TERSIMPAN DALAM {filename}
====================================================
              """)

def readXlsx(fileName):
    df = pd.read_excel(f'./{fileName}') 
    data = []
    for index, row in df.iterrows():
        data.append({"nama":row['Nama'],"hari": row['hari'], "gapok": row['golongan gaji pokok'],"lembur":row["lembur dalam Jam"]}) 
    return data;

def menu2():
    data = []
    data_xlsx = {
                'Nama': [],
                'golongan': [], 
                'jam lembur': [], 
                'total lembur': [], 
                'gaji': [], 
                }
    print("nama file tidak boleh memiliki spasi dan harus sesuai format di menu no 1")
    filename = input("nama file : ")
    clearConsol()
    error = False
    get_data_xlsx =readXlsx(filename)
    for item in get_data_xlsx:
        item_data = hitung_gaji(nama=item["nama"], golonganGaji=item["gapok"],lembur=item["lembur"],hari=item["hari"] )
        if len(item_data) == 0:
            error = True
            break
        data.append(item_data)
        data_xlsx["Nama"].append(item_data["nama"])
        data_xlsx["golongan"].append(item_data["golongan"])
        data_xlsx["gaji"].append(item_data["total_gaji"])
        data_xlsx["total lembur"].append(item_data["total_lembur"])
        data_xlsx["jam lembur"].append(item_data["jam_lembur"])

    if error:
        return 
    saveElsx(data_xlsx) 
    print("""
====================================================
                HSIL PERHITUGAN
====================================================
              """)
    for d in data:
        print("====================================================")
        print("Nama         :",d["nama"])
        print("Golongan     :",d["golongan"])
        print("jam lembur   :",d["jam_lembur"])
        print("total lembur :",d["total_lembur"])
        print("total gaji   :",d["gaji_format"])
        print("====================================================")

    print("""
====================================================
    PERHITUGAN SELESAIN DI ALIHKAN KE MENU UTAMA
====================================================
              """)
    __main__()

# def input_manual():
   

def menu_manual():
    clearConsol()
    total_data = int(input("masukan total data: "))
    data = []
    data_xlsx = {
                'Nama': [],
                'golongan': [], 
                'jam lembur': [], 
                'total lembur': [], 
                'gaji': [], 
                }
    
    for i in range(0, total_data):
        print(f"data {i+1}")
        nama = input("masukan nama : ")
        golongan = input("masukan golongan gaji pokok : ")
        hari = int(input("masukan total hari : "))
        lembur = int(input("lembur dalam Jam : "))
        data_hitung =hitung_gaji(golonganGaji=golongan,nama=nama,hari=hari,lembur=lembur)
        if len(data_hitung) == 0:
            error = True
            break
        error = False
        data_xlsx["Nama"].append(data_hitung["nama"])
        data_xlsx["golongan"].append(data_hitung["golongan"])
        data_xlsx["gaji"].append(data_hitung["total_gaji"])
        data_xlsx["total lembur"].append(data_hitung["total_lembur"])
        data_xlsx["jam lembur"].append(data_hitung["jam_lembur"])
        data.append(data_hitung)

    if error: 
         return
    saveElsx(data_xlsx) 
    print("""
====================================================
                HSIL PERHITUGAN
====================================================
              """)
    for d in data:
        print("====================================================")
        print("Nama         :",d["nama"])
        print("Golongan     :",d["golongan"])
        print("jam lembur   :",d["jam_lembur"])
        print("total lembur :",d["total_lembur"])
        print("total gaji   :",d["gaji_format"])
        print("====================================================")

    print("""
====================================================
    PERHITUGAN SELESAIN DI ALIHKAN KE MENU UTAMA
====================================================
              """)
    __main__()
 



def __main__():
    print("""  
====================================================
                    PILIH MENU
====================================================
1, dapatkan Format excel
2, Input excel
3, input Manual
q, untuk keluar
====================================================
""")
    try: 
        menu = input(("pilih menu: "))  
        if menu == "q" or menu =="Q":
            print(f"""
====================================================
                  KELUAR  
====================================================
              """)
            quit()
            
        match int(menu):
            case 1:
                get_format()
            case 2:
                menu2()
            case 3:
                menu_manual()
               
            case _:
                print("menu tidak ada")

    except ValueError: 
        print("terjadi masalah") 


__main__()