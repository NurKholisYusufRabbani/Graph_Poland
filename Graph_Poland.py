class Peta:
    def __init__(self):
        # Inisialisasi dictionary untuk menyimpan daftar kota dan jalannya
        self.jalur_kota = {}
    
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
        
    def tambahkanJalan(self,kota1,kota2):
        #menambahkan jalan antar dua kota
        if kota1 in self.jalur_kota and kota2 in self.jalur_kota:
        #tambahkan kota2 ke daftar kota1 dan sebaliknya 
            self.jalur_kota[kota1].append(kota2)
            self.jalur_kota[kota2].append(kota1)
            return True
        return False
        
    def hapusJalan(self,kota1,kota2):
        #menghapus jalan antara dua kota
        if kota1 in self.jalur_kota and kota2 in self.jalur_kota:
            #hapus kota2 dari daftar kota1 dan sebaliknya 
            if kota2 in self.jalur_kota[kota1]:
                self.jalur_kota[kota1].remove(kota2)
            if kota1 in self.jalur_kota[kota2]:
                self.jalur_kota[kota2].remove(kota1)
            return True 
        return False

peta = Peta()

peta.tambahkanKota("Bytow")
peta.tambahkanJalan("Bytow", "Koscierzyna")
peta.tambahkanJalan("Bytow", "Czersk")
peta.tambahkanKota("Koscierzyna")
peta.tambahkanJalan("Koscierzyna", "Bytow")
peta.tambahkanJalan("Koscierzyna", "Czersk")
peta.tambahkanJalan("Koscierzyna", "Sopot")
peta.tambahkanJalan("Koscierzyna", "Gdansk")
peta.tambahkanKota("Sopot")
peta.tambahkanJalan("Sopot", "Koscierzyna")
peta.tambahkanJalan("Sopot", "Gdansk")
peta.tambahkanKota("Gdansk")
peta.tambahkanJalan("Gdansk", "Sopot")
peta.tambahkanJalan("Gdansk", "Koscierzyna")
peta.tambahkanJalan("Gdansk", "Tczew")
peta.tambahkanJalan("Gdansk", "Nowy Dwor Gdanski")
peta.tambahkanJalan("Gdansk", "Starogard Gdanski")
peta.tambahkanKota("Czersk")
peta.tambahkanJalan("Czersk", "Bytow")
peta.tambahkanJalan("Czersk", "Koscierzyna")
peta.tambahkanJalan("Czersk", "Starogard Gdanski")
peta.tambahkanKota("Starogard Gdanski")
peta.tambahkanJalan("Starogard Gdanski", "Gdansk")
peta.tambahkanJalan("Starogard Gdanski", "Czersk")
peta.tambahkanJalan("Starogard Gdanski", "Tczew")
peta.tambahkanKota("Tczew")
peta.tambahkanJalan("Tczew", "Starogard Gdanski")
peta.tambahkanJalan("Tczew", "Gdansk")
peta.tambahkanJalan("Tczew", "Nowy Dwor Gdanski")
peta.tambahkanJalan("Tczew", "Malbork")
peta.tambahkanKota("Nowy Dwor Gdanski")
peta.tambahkanJalan("Nowy Dwor Gdanski", "Tczew")
peta.tambahkanJalan("Nowy Dwor Gdanski", "Gdansk")
peta.tambahkanJalan("Nowy Dwor Gdanski", "Krynica Morska")
peta.tambahkanJalan("Nowy Dwor Gdanski", "Elblag")
peta.tambahkanKota("Elblag")
peta.tambahkanJalan("Elblag", "Malbork")
peta.tambahkanJalan("Elblag", "Nowy Dwor Gdanski")
peta.tambahkanKota("Malbork")
peta.tambahkanJalan("Malbork", "Tczew")
peta.tambahkanJalan("Malbork", "Elblag")
peta.tambahkanJalan("Malbork", "Sztum")
peta.tambahkanKota("Sztum")
peta.tambahkanJalan("Sztum", "Malbork")
peta.tambahkanKota("Krynica Morska")
peta.tambahkanJalan("Krynica Morska", "Nowy Dwor Gdanski")

peta.printPeta()
