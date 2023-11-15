from Class import Person

class Siswa(Person):
    def __init__(self,nama,alamat,nim):
        super().__init__(nama,alamat)
        self.nim = nim

    def tampil(self):
     print("Nama = ",self.nama,"Alamat =",self.alamat,"NIM =",self.nim)