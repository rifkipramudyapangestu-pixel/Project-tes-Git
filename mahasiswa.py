class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_info(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek mahasiswa
    mahasiswa1 = Mahasiswa("Ahmad", "123456", "Informatika")
    mahasiswa2 = Mahasiswa("Budi", "654321", "Teknik Elektro")
    mahasiswa3 = Mahasiswa("cindy", "098765", "Teknik Mesin")
    Mahasiswa4 = Mahasiswa("Dewi", "567890", "Sistem Informasi")
    # Menampilkan informasi
    print(mahasiswa1.tampilkan_info())
    print(mahasiswa2.tampilkan_info())
    print(mahasiswa3.tampilkan_info())
    print(Mahasiswa4.tampilkan_info())