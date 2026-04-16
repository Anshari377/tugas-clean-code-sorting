def urutkan_berdasarkan_tahun(daftar):
    total_data = len(daftar)
    for pass_indeks in range(total_data):
        sudah_terurut = True
        for indeks in range(0, total_data - pass_indeks - 1):
            if daftar[indeks]['tahun'] > daftar[indeks + 1]['tahun']:
                daftar[indeks], daftar[indeks + 1] = daftar[indeks + 1], daftar[indeks]
                sudah_terurut = False
        
        if sudah_terurut:
            break
    return daftar

def tampilkan_koleksi(daftar, pesan):
    print(f"\n--- {pesan} ---")
    for item in daftar:
        print(f"{item['judul']} ({item['tahun']})")

def main():
    koleksi_komik = [
        {"judul": "One Piece", "tahun": 1997},
        {"judul": "Ruri Dragon", "tahun": 2022},
        {"judul": "Naruto", "tahun": 1999}
    ]

    tampilkan_koleksi(koleksi_komik, "SEBELUM DIURUTKAN")
    
    komik_terurut = urutkan_berdasarkan_tahun(koleksi_komik)
    
    tampilkan_koleksi(komik_terurut, "SETELAH DIURUTKAN (KRONOLOGIS)")

if __name__ == "__main__":
    main()