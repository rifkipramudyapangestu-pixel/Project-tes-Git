class Dosen:
    def __init__(self, nama, nip, mata_kuliah):
        self.nama = nama
        self.nip = nip
        self.mata_kuliah = mata_kuliah
    
    def tampilkan_info(self):
        return f"Nama: {self.nama}, NIP: {self.nip}, Mata Kuliah: {self.mata_kuliah}"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek dosen
    dosen1 = Dosen("Dr. Siti", "987654", "Pemrograman Python")
    dosen2 = Dosen("Prof. Ahmad", "123987", "Struktur Data")
    
    # Menampilkan informasi
    print(dosen1.tampilkan_info())
    print(dosen2.tampilkan_info())
