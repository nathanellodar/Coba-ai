import os
import tabula
import pandas as pd

# preprocessing
def Mengecek_File_Data_Transkrip(file_path):
    if(os.path.exists("hasil_filter/"+file_path)):
        return True
    else:
        return False
def Membuat_File_Sortir_Data(file_pdf, nama_file_excel, nim):
    table = tabula.read_pdf(file_pdf, pages="all");
    print(pd.DataFrame(table[0].head(10)))
    Data_Kode_Matkul = pd.DataFrame(table[0].head(10)['Unnamed: 0'])
    Data_Nama_Matkul = pd.DataFrame(table[0].head(10)['Unnamed: 1'])
    Data_Nilai_Matkul = pd.DataFrame(table[0].head(10)['Unnamed: 4'])
    # mengambil data kode matkul
    for key, data in Data_Kode_Matkul.to_dict().items():
        Penampung_Data = []
        data_pertama = True
        for key, Kode_Matkul in data.items():
            if(data_pertama):
                data_pertama = False
            else:
                Penampung_Data.append(Kode_Matkul)
    # mengubah format dan membuat dictionary kode matkul
    Data_Utuh_Kode_Matkul = {'KODE_MATKUL' : Penampung_Data}

    # menambah nama matkul dan nilai
    for key, data in Data_Nama_Matkul.to_dict().items():
        Penampung_Data = []
        data_pertama = True
        for key, Nama_Matkul in data.items():
            if(data_pertama):
                data_pertama = False
            else:
                Penampung_Data.append(Nama_Matkul)
    Data_Utuh_Nama_Matkul = {'NAMA_MATKUL' : Penampung_Data}

    for key, data in Data_Nilai_Matkul.to_dict().items():
        Penampung_Data = []
        data_pertama = True
        for key, Nilai_Matkul in data.items():
            if(data_pertama):
                data_pertama = False
            else:
                Penampung_Data.append(Nilai_Matkul)
    Data_Utuh_Nilai_Matkul = {'NILAI_MATKUL' : Penampung_Data}
    # dibuat dalam satu frame
    Data_Keseluruhan = {list(Data_Utuh_Kode_Matkul.keys())[0] : Data_Utuh_Kode_Matkul[list(Data_Utuh_Kode_Matkul.keys())[0]], list(Data_Utuh_Nama_Matkul.keys())[0] : Data_Utuh_Nama_Matkul[list(Data_Utuh_Nama_Matkul.keys())[0]], list(Data_Utuh_Nilai_Matkul.keys())[0] : Data_Utuh_Nilai_Matkul[list(Data_Utuh_Nilai_Matkul.keys())[0]]}
    Frame_Data_Keseluruhan = pd.DataFrame(Data_Keseluruhan)
    # menyimpan hasil yang dibuat
    Frame_Data_Keseluruhan.to_excel('hasil_filter/'+nim+'/'+nama_file_excel, index=False)

    # print(list(Data_Utuh_Nilai_Matkul.keys())[0])
    # print(Data_Utuh_Nilai_Matkul[list(Data_Utuh_Nilai_Matkul.keys())[0]])




# processing 
def Memproses_Data_Sortir():
    pass

