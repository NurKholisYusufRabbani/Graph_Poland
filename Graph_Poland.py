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
        
    def tambahkanjalan(self,kota1,kota2):
        #menambahkan jalan antar dua kota
        if kota1 in self.jalur_kota and kota2 in self.jalur_kota:
        #tambahkan kota2 ke daftar kota1 dan sebaliknya 
            self.jalur_kota[kota1].append(kota2)
            self.jalur_kota[kota2].append(kota1)
            return True
        return False
        
    def hapusjalan(self,kota1,kota2):
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

#Data kota dan jalur-jalurnya
data_kota = {
    "Bytow": ["Koscierzyna", "Czersk"],
    "Koscierzyna": ["Bytow", "Czersk", "Sopot", "Gdansk"],
    "Sopot": ["Koscierzyna", "Gdansk"],
    "Gdansk": ["Sopot", "Koscierzyna", "Tczew", "Nowy Dwor Gdanski", "Starogard Gdanski"],
    "Czersk": ["Bytow", "Koscierzyna", "Starogard Gdanski"],
    "Starogard Gdanski": ["Gdansk", "Czersk", "Tczew"],
    "Tczew": ["Starogard Gdanski", "Gdansk", "Nowy Dwor Gdanski", "Malbork"],
    "Nowy Dwor Gdanski": ["Tczew", "Gdansk", "Krynica Morska", "Elblag"],
    "Elblag": ["Malbork", "Nowy Dwor Gdanski"],
    "Malbork": ["Tczew", "Elblag", "Sztum"],
    "Sztum": ["Malbork"],
    "Krynica Morska": ["Nowy Dwor Gdanski"]
}

#Menambahkan kota dan jalur-jalurnya ke dalam peta
for kota, jalur in data_kota.items():
    peta.tambahkanKotaDanJalur(kota, jalur)

peta.printPeta()
