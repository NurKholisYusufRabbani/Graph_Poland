class Peta:
    def __init__(self):
        # Inisialisasi dictionary untuk menyimpan daftar kota dan jalannya
        self.jalur_kota = {}

    def tambahkanKotaDanJalur(self, nama_kota, jalur):
        if nama_kota not in self.jalur_kota:
            self.jalur_kota[nama_kota] = jalur
            #Tambahkan kota ini ke jalur-jalur kota lain
            for kota in jalur:
                if kota in self.jalur_kota:
                    self.jalur_kota[kota].append(nama_kota)
                else:
                    self.jalur_kota[kota] = [nama_kota]
            return True
        return False
    
    def printPeta(self):
        # Mencetak daftar kota beserta jalannya
        for kota in self.jalur_kota:
            print(kota, ":", self.jalur_kota[kota])
        
    def tambahkanKota(self, nama_kota):
        # Menambahkan kota baru ke dalam peta jika belum ada
        if nama_kota not in self.jalur_kota:
            self.jalur_kota[nama_kota] = []
            return True
        return False
    
    def hapusKota(self, nama_kota_dihapus):
        # Menghapus kota dari peta berserta semua jalannya
        if nama_kota_dihapus in self.jalur_kota:
            # Hapus koneksi ke nama_kota_dihapus dari setiap kota lainnya
            for kota_lain in self.jalur_kota:
                if nama_kota_dihapus in self.jalur_kota[kota_lain]:
                    self.jalur_kota[kota_lain].remove(nama_kota_dihapus)
            # Hapus nama_kota_dihapus dari daftar kota
            del self.jalur_kota[nama_kota_dihapus]
            return True
        return False
        