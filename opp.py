class kucing:
    def __init__ (self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bersuara(self):
        print("Miawww!")

kucing1 = kucing("charles", "3 tahun")
kucing1.bersuara() 
