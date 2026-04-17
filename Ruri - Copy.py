def bubble_sort_komik(daftar_komik):
    n = len(daftar_komik)
    for i in range(n):
       
        swapped = False
        for j in range(0, n - i - 1):
            if daftar_komik[j]['tahun'] > daftar_komik[j+1]['tahun']:
                # Proses penukaran posisi (Swap)
                daftar_komik[j], daftar_komik[j+1] = daftar_komik[j+1], daftar_komik[j]
                swapped = True
    
        if not swapped:
            break
    return daftar_komik

koleksi_komik = [
    {"judul": "One Piece", "tahun": 1997},
    {"judul": "Ruri Dragon", "tahun": 2022},
    {"judul": "Naruto", "tahun": 1999}
]

print("--- SEBELUM DIURUTKAN ---")
for k in koleksi_komik:
    print(f"{k['judul']} ({k['tahun']})")

komik_terurut = bubble_sort_komik(koleksi_komik)

print("\n--- SETELAH DIURUTKAN (KRONOLOGIS) ---")
for k in komik_terurut:
    print(f"{k['judul']} ({k['tahun']})")