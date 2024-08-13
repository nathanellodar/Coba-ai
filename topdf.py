import pymysql
from fpdf import FPDF

def CreatePDF(matkulTidakLulus, jumlahSksLulus, nim, jumlahSemester, persentaseKelulusan, jumlahSAC, levelICE, namaLengkap):
    header_id = nim
    header_id2 = namaLengkap
    class PDF(FPDF):
        def __init__(self, header_id, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.header_id = header_id

        def header(self):
            self.set_font('Arial', 'B', 18)
            self.cell(0, 10,'Persentase Kelulusan', 0, 1, 'C')

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        def chapter_titleCenter(self, title):
            self.set_font('Arial', 'I', 12)
            self.cell(0, 10, title, 0, 1, 'C')
            self.ln(10)

        def chapter_titleLeft(self, title):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 3, title, 0, 1, 'L')
            self.ln(10)

        def chapter_body(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 4, body)
            self.ln()

    pdf = PDF(header_id)
    pdf.add_page()
    pdf.chapter_titleCenter(f'{header_id} | {header_id2}')
    pdf.chapter_titleLeft(f'Jumlah SKS Lulus : {jumlahSksLulus}')
    pdf.chapter_titleLeft(f'Jumlah Point SAC : {jumlahSAC}')
    pdf.chapter_titleLeft(f'Status ICE : Level {levelICE}')
    pdf.chapter_titleLeft('Mata Kuliah yang disarankan untuk diulang: ')
    for subject in matkulTidakLulus:
        pdf.chapter_body(subject)
    pdf.chapter_titleLeft('')
    pdf.chapter_titleLeft(f'Persentase Kelulusan Anda : {persentaseKelulusan} %')
    pdf.chapter_titleLeft(f'Jumalah Semester yang akan di Tempuh : {jumlahSemester} Semester')
    pdf.output('hasil_pdf/'+nim+'.pdf')