class Graf:
    def __init__(self, jumlah_simpul):
        self.jumlah_simpul = jumlah_simpul
        self.graf = {i: [] for i in range(jumlah_simpul)}

    def tambah_sisi(self, u, v):
        self.graf[u].append(v)

    def bpm(self, u, dikunjungi, pasangan):
        for v in self.graf[u]:
            if not dikunjungi[v]:
                dikunjungi[v] = True
                if pasangan[v] == -1 or self.bpm(pasangan[v], dikunjungi, pasangan):
                    pasangan[v] = u
                    return True
        return False

    def maksimum_bipartite_matching(self):
        pasangan = [-1] * self.jumlah_simpul
        hasil = 0
        for i in range(self.jumlah_simpul):
            dikunjungi = [False] * self.jumlah_simpul
            if self.bpm(i, dikunjungi, pasangan):
                hasil += 1
        return hasil

# Contoh penggunaan algoritma
g = Graf(4)
g.tambah_sisi(0, 1)
g.tambah_sisi(0, 2)
g.tambah_sisi(1, 2)
g.tambah_sisi(2, 0)
g.tambah_sisi(2, 3)
g.tambah_sisi(3, 3)

print("Jumlah maximum matching:", g.maksimum_bipartite_matching())
