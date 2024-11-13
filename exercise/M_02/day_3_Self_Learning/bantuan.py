nilai_barang = {
    "pisau": 10,
    "peta": 15,
    "kompas": 8,
}


# bantuan.py

def count_items(inventory):
    total_nilai = 0
    for nilai in inventory.values():  # Mengambil semua nilai dari dictionary
        total_nilai += nilai  # Menjumlahkan nilai
    return total_nilai


# total_items = count_items(nilai_barang)

# print("Total: ", total_items)
