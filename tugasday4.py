import math

class BangunDatar:
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 3.14 * self.jari_jari ** 2

class Trapesium(BangunDatar):
    def __init__(self, alas1, alas2, tinggi):
        self.alas1 = alas1
        self.alas2 = alas2
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * (self.alas1 + self.alas2) * self.tinggi

# Main program
def main():
    n = int(input("Masukkan jumlah bangun datar yang akan dihitung luasnya: "))
    bangun_datar_list = []

    for i in range(n):
        jenis = input(f"Bangun datar ke-{i+1} (persegi/persegi panjang/segitiga/lingkaran/trapesium): ").lower()

        if jenis == "persegi":
            sisi = float(input("Masukkan panjang sisi: "))
            bangun_datar = Persegi(sisi)
        elif jenis == "persegi panjang":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            bangun_datar = PersegiPanjang(panjang, lebar)
        elif jenis == "segitiga":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            bangun_datar = Segitiga(alas, tinggi)
        elif jenis == "lingkaran":
            jari_jari = float(input("Masukkan jari-jari: "))
            bangun_datar = Lingkaran(jari_jari)
        elif jenis == "trapesium":
            alas1 = float(input("Masukkan panjang alas atas: "))
            alas2 = float(input("Masukkan panjang alas bawah: "))
            tinggi = float(input("Masukkan tinggi: "))
            bangun_datar = Trapesium(alas1, alas2, tinggi)
        else:
            print("Jenis bangun datar tidak valid.")
            continue

        bangun_datar_list.append(bangun_datar)

    # Hitung luas masing-masing bangun datar
    luas_bangun_datar = [bangun_datar.hitung_luas() for bangun_datar in bangun_datar_list]

    # Urutkan luas bangun datar dari terkecil hingga terbesar
    luas_bangun_datar.sort()

    # Hitung total luas bangun datar
    total_luas = sum(luas_bangun_datar)

    # Tampilkan hasil
    print("Luas Bangun Datar:")
    for i, luas in enumerate(luas_bangun_datar):
        print(f"Bangun datar ke-{i+1}: {luas}")
    print(f"Total Luas: {total_luas}")

if __name__ == "__main__":
    main()
