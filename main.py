from fungsi_validasi import *
from fungsi_filter import *
from bacaEXCEL import *
import streamlit as st
from topdf import *

def Persentase_Lulus(jumlahSKS, ICE, pointSAC):
    persentaseSks = (jumlahSKS/144)*0.6
    persentaseICE = (ICE/3)*0.2
    persentaseSAC = (pointSAC/120)*0.2
    KeseluruhanPersentase = (persentaseSks + persentaseICE + persentaseSAC)*100
    print(KeseluruhanPersentase)
    return round(KeseluruhanPersentase, 2)

def PerkiraanSemesterTempuh(jumlahSKS, jumlah_semester):
    #diperhitungkan berdasarkan kualitas belajar selama berapa semester yang sudah ditempuh sebelumnya
    rata_rata_kualitas_belajar = ((jumlahSKS/144)*10)/jumlah_semester
    Jumlah_semester_tempuh = (((144-jumlahSKS)/144)*10)/rata_rata_kualitas_belajar
    return round(Jumlah_semester_tempuh)

st.markdown(
    f"""
    <style>
    header {{
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# st.write("Hello, World!")
st.header("Generate :blue[Persentase] Kelulusan", divider="rainbow")

# Judul aplikasi
st.markdown('### Masukan Data Diri Anda')

# Input NIM dan Nama
nim = st.text_input('Masukan NIM Anda:')
if(nim != '' and len(nim) == 8):
    if(Membuat_folder(nim) == True):
        jumlah_sks_lulus = Mengambil_data_excel(nim)['jumlah_sks']
        matkul_tidak_lulus = Mengambil_data_excel(nim)['matkul_ulang']
        jumlah_point_sac = Menampilkan_data(nim)[2]
        nama_lengkap = Menampilkan_data(nim)[1]
        ice_lulus = int(Menampilkan_data(nim)[3].split(" ")[1])
        jumlah_semester = Mengambil_data_excel(nim)['jumlah_semester']
        perkiraan_semester_tempuh = PerkiraanSemesterTempuh(jumlah_sks_lulus, jumlah_semester)
        # print(jumlah_sks_lulus)
        persentase_kelulusan = Persentase_Lulus(jumlah_sks_lulus, ice_lulus, jumlah_point_sac)
        CreatePDF(matkul_tidak_lulus, jumlah_sks_lulus, nim, perkiraan_semester_tempuh, persentase_kelulusan, jumlah_point_sac, ice_lulus, nama_lengkap)

# name = st.text_input('Masukan Nama Anda:')

# Tombol untuk menghasilkan PDF
if st.button('Generate Kelulusan Anda'):
    if nim:
        pdf_file = "hasil_pdf/" + nim +'.pdf'
        with open(pdf_file, "rb") as file:
            btn = st.download_button(
                label="Download PDF",
                data=file,
                file_name=pdf_file,
                mime="application/octet-stream"
            )
    else:
        st.error('Please enter both NIM and Name')

