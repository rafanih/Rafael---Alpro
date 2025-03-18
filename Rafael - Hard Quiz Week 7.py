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

def main():
    # Menjalankan algoritma
    result = find_trip(destinations, budget)

    # Menampilkan hasil
    if result:
        print("\n✅ Rencana Liburan (Total harus 2 juta):")
        for d in result:
            print(f"- {d['name']} (Biaya: {d['total']} juta rupiah)")
        total_biaya = sum(d['total'] for d in result)
        print(f"\n💰 Total Biaya: {total_biaya} juta rupiah")
        
        # Menampilkan penjelasan logika backtracking (Jawaban Nomor 3)
        print("\n🔍 Penjelasan Logika Backtracking:")
        print("1. Program menggunakan rekursi untuk mencoba berbagai kombinasi destinasi.")
        print("2. Setiap kali destinasi ditambahkan, program mengecek total biaya.")
        print("3. Jika biaya mencapai 2 juta dan terdiri dari 3 destinasi, kombinasi disimpan sebagai solusi.")
        print("4. Jika melebihi 2 juta atau lebih dari 3 destinasi, kombinasi tersebut diabaikan (backtrack).")
        print("5. Program terus mencoba berbagai kemungkinan hingga menemukan kombinasi yang valid.")

        # Menampilkan kelebihan dan kekurangan backtracking (Jawaban Nomor 4)
        print("\n📊 Analisis Backtracking:")
        
        print("\n✅ Kelebihan:")
        print("- Backtracking efektif untuk mencari solusi dalam jumlah pilihan yang tidak terlalu besar.")
        print("- Dapat digunakan untuk berbagai permasalahan kombinatorial seperti subset sum dan traveling salesman.")
        print("- Memastikan solusi optimal ditemukan dengan mencoba berbagai kemungkinan.")
        
        print("\n❌ Kekurangan:")
        print("- Jika jumlah destinasi sangat banyak, prosesnya bisa menjadi lambat karena mencoba semua kemungkinan.")
        print("- Memori yang digunakan bertambah seiring dengan kedalaman rekursi, berisiko mengalami stack overflow.")
        print("- Tidak efisien dibanding metode lain seperti dynamic programming untuk skala data yang lebih besar.")

    else:
        print("❌ Tidak ada kombinasi yang tepat 2 juta rupiah.")

if __name__ == "__main__":
    main()
