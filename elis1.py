# Data 10 Jenis Obat di Apotek
daftar_obat = [
    {"nama": "Paracetamol", "stok": 120, "harga": 10000, "kategori": "Bebas"},
    {"nama": "Amoxicillin", "stok": 8, "harga": 25000, "kategori": "Keras"},
    {"nama": "Ibuprofen", "stok": 45, "harga": 15000, "kategori": "Bebas Terbatas"},
    {"nama": "Cetirizine", "stok": 0, "harga": 12000, "kategori": "Bebas Terbatas"},
    {"nama": "Omeprazole", "stok": 30, "harga": 35000, "kategori": "Keras"},
    {"nama": "Metformin", "stok": 60, "harga": 20000, "kategori": "Keras"},
    {"nama": "Amlodipine", "stok": 15, "harga": 18000, "kategori": "Keras"},
    {"nama": "Salbutamol", "stok": 5, "harga": 40000, "kategori": "Keras"},
    {"nama": "Antasida Doen", "stok": 90, "harga": 8000, "kategori": "Bebas"},
    {"nama": "Vitamin C 500mg", "stok": 200, "harga": 30000, "kategori": "Bebas"}
]

print("=== PENGECEKAN STATUS OBAT APOTEK ===")
for obat in daftar_obat:
    # 1. Operator Pembanding (== dan <) untuk status stok
    if obat["stok"] == 0:
        status_stok = "HABIS (Segera Order!)"
    elif obat["stok"] < 10:
        status_stok = "MENIPIS (Sisa sedikit)"
    else:
        status_stok = "AMAN"

    # 2. Operator Pembanding (==) & Kondisional untuk syarat resep
    if obat["kategori"] == "Keras":
        aturan = "Wajib Resep Dokter"
    else:
        aturan = "Bisa Dibeli Bebas"

    # 3. Operator Pembanding (>=) untuk promo harga
    if obat["harga"] >= 30000:
        promo = "Gratis Konsultasi Apoteker"
    else:
        promo = "Tidak ada promo"

    print(f"- {obat['nama']}: Stok {status_stok} | {aturan} | {promo}")