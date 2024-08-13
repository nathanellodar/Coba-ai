import json

# Load the JSON file
with open('percobaanDataiList.json') as f:
    data = json.load(f)

# Access the data for semester 7
kodeMatkul = "TI9383"
matkul_wajib = list()
def Periksa_MatkulWajib(KodeMatkul):
    keberapa = int()
    hasilKode = ''
    for i in range(1, 9):
        keberapa+=1
        semester = 'semester ' + str(keberapa)
        semester_7_data = data['syarat']['jumlah sks']['jenis matkul']['wajib'][semester]
        # print(semester_7_data)
        for key, item in semester_7_data.items():
            if KodeMatkul == key:
                hasilKode = key
                return True
            else:
                continue
    if hasilKode == '':
        return False
def Periksa_MatkulPilihan(kodeMatkul):
    hasilKode = ''
    matakuliah_pilihan_wajib_profil = data['syarat']['jumlah sks']['jenis matkul']['pilihan']['matkul_pilihan']['Matkul_WajibProdi']
    matakuliah_pilihan_bebas_profil = data['syarat']['jumlah sks']['jenis matkul']['pilihan']['matkul_pilihan']['MatkulPilihan_BebasProdi']
    for key, item in matakuliah_pilihan_wajib_profil.items():
        if kodeMatkul == key:
            return True
        else:
            for key, item in matakuliah_pilihan_bebas_profil.items():
                if kodeMatkul == key:
                    hasilKode = key
                    return True
                else:
                    continue
    if hasilKode =='':
        return False

def AmbilSKS(kodeMatkul):
    if Periksa_MatkulWajib(kodeMatkul):
        keberapa = int()
        for i in range(1, 9):
            keberapa+=1
            semester = 'semester ' + str(keberapa)
            semester_7_data = data['syarat']['jumlah sks']['jenis matkul']['wajib'][semester]
            # print(semester_7_data)
            for key, item in semester_7_data.items():
                if kodeMatkul == key:
                    return item
                else:
                    continue
    else:
        matakuliah_pilihan_wajib_profil = data['syarat']['jumlah sks']['jenis matkul']['pilihan']['matkul_pilihan']['Matkul_WajibProdi']
        matakuliah_pilihan_bebas_profil = data['syarat']['jumlah sks']['jenis matkul']['pilihan']['matkul_pilihan']['MatkulPilihan_BebasProdi']
        for key, item in matakuliah_pilihan_wajib_profil.items():
            if kodeMatkul == key:
                return item
            else:
                for key, item in matakuliah_pilihan_bebas_profil.items():
                    if kodeMatkul == key:
                        return item
                    else:
                        continue

# print(AmbilSKS(kodeMatkul))

   

# Print the data
# print(semester_7_data)
# for key, value in semester_7_data.items():
#     print(f"kode Matkul: {key}\nsks: {value}\n")