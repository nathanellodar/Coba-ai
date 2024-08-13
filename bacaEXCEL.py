import pandas as pd
import json
import os
from membacaFileJson import *
# menampilkan hasil dari excel yg udh di scan sebelumnya
def Mengambil_data_excel(nim):
    # fungsi untuk load json matkul c
    dict_cek_matkul_lulusC = {}
    dict_tidak_lulusC = {}
    list_lulusD = []
    sks_D = 0
    sks_lulus = 0
    with open ('matkul_minimal_c.json','r') as file:
        listMatkulLulusC = json.load(file)

    folder_path = 'hasil_filter/'+nim
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for indexData in range(len(files)):
        bacaExcel = pd.read_excel('hasil_filter/'+nim+'/'+files[indexData])
        # print(files[indexData])

        List_hasil_excel = []
        for i in bacaExcel.index:
            dataExcel = {
                bacaExcel['KODE_MATKUL'][i]:
                bacaExcel['NILAI_MATKUL'][i]
            }
            
            List_hasil_excel.append(dataExcel)
        # List_hasil_excel.pop()
        # print(List_hasil_excel)
        
        # bandingkan hasil sks dengan matkul yang c di json
        for key, item in listMatkulLulusC[0].items():
            for dataMatkul in List_hasil_excel:
                kodeMatkul = dataMatkul.keys()
                nilaiMatkul = dataMatkul.values()
                nilai = ''
                for nilai in nilaiMatkul:
                    nilai = nilai
                for k in kodeMatkul:
                    if k in item :
                        dict_cek_matkul_lulusC[key] = k
                        if nilai == 'D' or nilai == 'E':
                            dict_tidak_lulusC[key] = k
                            list_lulusD.append(k)
                        else:
                            sks_lulus +=3;
                    else:
                        if(Periksa_MatkulWajib(k) or Periksa_MatkulPilihan(k)):
                            dikatakanLulus = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D']
                            if nilai in dikatakanLulus:
                                if nilai == 'D':
                                    list_lulusD.append(k)
                                    if sks_D <= 15 and (AmbilSKS(k) + sks_D) <= 15:
                                        sks_D += AmbilSKS(k)
                                    else:
                                        list_lulusD.append(k)
                                elif k == 'E':
                                    list_lulusD.append(k)
                                else:
                                    sks_lulus+=AmbilSKS(k)
                            else:
                                list_lulusD.append(k)

    return {'jumlah_sks' : sks_lulus+sks_D , 'matkul_ulang' : list_lulusD, 'jumlah_semester' : len(files)} 
# print(Mengambil_data_excel('71220955'))