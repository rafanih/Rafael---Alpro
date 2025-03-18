# Daftar destinasi dan biaya dalam juta rupiah
destinations = [
    {"name": "Gunung Bromo", "total": 1.2},
    {"name": "Kawah Ijen", "total": 0.5},
    {"name": "Air Terjun Madakaripura", "total": 0.3},
]

# Anggaran yang harus dicapai (dalam juta rupiah)
budget = 2.0

# Fungsi backtracking untuk mencari kombinasi tepat 2 juta
def find_trip(destinations, budget, selected=None, index=0):
    if selected is None:
        selected = []
    
    total_cost = sum(d['total'] for d in selected)

    # Jika total biaya tepat 2 juta dan 3 destinasi terpilih, kembalikan hasilnya
    if total_cost == budget and len(selected) == 3:
        return selected  

    # Jika melebihi anggaran atau memilih lebih dari 3 destinasi, hentikan pencarian
    if total_cost > budget or len(selected) > 3:
        return None  

    for i in range(index, len(destinations)):
        selected.append(destinations[i])  # Tambahkan destinasi ke daftar
        result = find_trip(destinations, budget, selected, i + 1)  # Rekursif
        if result:
            return result  # Langsung kembalikan solusi pertama yang valid
        selected.pop()  # Kembali ke kondisi sebelumnya (backtrack)

    return None  # Jika tidak ada kombinasi yang valid

if __name__ == "__main__":
    # Menjalankan algoritma
    result = find_trip(destinations, budget)

    # Menampilkan hasil
    if result:
        print("\n✅ Rencana Liburan (Total harus 2 juta):")
        for d in result:
            print(f"- {d['name']} (Biaya: {d['total']} juta rupiah)")
        total_biaya = sum(d['total'] for d in result)
        print(f"\n💰 Total Biaya: {total_biaya} juta rupiah")
    else:
        print("❌ Tidak ada kombinasi yang tepat 2 juta rupiah.")
