import pymysql
import os
from fungsi_filter import *

connection = pymysql.connect(
    host="localhost",
    user="root@",
    password="",
    database="ta_ai"
)

def Menampilkan_data(nim):
    cursor = connection.cursor()
    sql = "SELECT * FROM mahasiswa WHERE NIM = %s"
    cursor.execute(sql, nim)
    data = cursor.fetchone()
    return data



def Membuat_folder(nim):
    parent_path = os.path.abspath("hasil_filter")
    new_folder = os.path.join(parent_path, nim)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
        print("Folder Created")
        Memproses_data(nim)
    else:
        print("Folder Already Exists")
        Memproses_data(nim)
    return True


def Memproses_data(nim):
    folder_path = Menampilkan_data(nim)[4]
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(files)
    for indexData in range(len(files)):
        if (Mengecek_File_Data_Transkrip(folder_path+files[indexData])):
            print("File Sudah Ada")
        else:
            nama_file_xlsx = files[indexData].split('.')[0]+'.xlsx'
            Membuat_File_Sortir_Data(folder_path+"/"+files[indexData], nama_file_xlsx, nim)