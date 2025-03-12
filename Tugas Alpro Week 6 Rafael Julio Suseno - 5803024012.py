import sqlite3
import time
from datetime import datetime

def create_table():
    conn = sqlite3.connect("absensi.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS absensi (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama TEXT NOT NULL,
                        tanggal TEXT NOT NULL,
                        waktu_masuk TEXT NOT NULL,
                        waktu_keluar TEXT)''')
    conn.commit()
    conn.close()

# Algoritma O(n²): Pengecekan absensi menggunakan metode pencarian linear berulang

def absen_masuk_brute_force(nama):
    start_time = time.time()
    conn = sqlite3.connect("absensi.db")
    cursor = conn.cursor()
    tanggal = datetime.now().strftime("%Y-%m-%d")
    waktu_masuk = datetime.now().strftime("%H:%M:%S")
    cursor.execute("SELECT nama FROM absensi WHERE tanggal = ?", (tanggal,))
    data = cursor.fetchall()
    for row in data:
        if row[0] == nama:
            print(f"{nama} sudah absen hari ini!")
            conn.close()
            print(f"Waktu eksekusi: {time.time() - start_time:.6f} detik")
            return
    cursor.execute("INSERT INTO absensi (nama, tanggal, waktu_masuk) VALUES (?, ?, ?)", (nama, tanggal, waktu_masuk))
    conn.commit()
    conn.close()
    print(f"{nama} telah absen masuk pada {tanggal} pukul {waktu_masuk}")
    print(f"Waktu eksekusi: {time.time() - start_time:.6f} detik")

# Algoritma O(n log n): Menggunakan indeks pencarian binary search pada daftar nama yang telah disortir

def absen_masuk_optimized(nama):
    start_time = time.time()
    conn = sqlite3.connect("absensi.db")
    cursor = conn.cursor()
    tanggal = datetime.now().strftime("%Y-%m-%d")
    waktu_masuk = datetime.now().strftime("%H:%M:%S")
    cursor.execute("SELECT nama FROM absensi WHERE tanggal = ? ORDER BY nama", (tanggal,))
    data = [row[0] for row in cursor.fetchall()]
    
    # Implementasi Binary Search
    from bisect import bisect_left
    index = bisect_left(data, nama)
    if index < len(data) and data[index] == nama:
        print(f"{nama} sudah absen hari ini!")
        conn.close()
        print(f"Waktu eksekusi: {time.time() - start_time:.6f} detik")
        return
    cursor.execute("INSERT INTO absensi (nama, tanggal, waktu_masuk) VALUES (?, ?, ?)", (nama, tanggal, waktu_masuk))
    conn.commit()
    conn.close()
    print(f"{nama} telah absen masuk pada {tanggal} pukul {waktu_masuk}")
    print(f"Waktu eksekusi: {time.time() - start_time:.6f} detik")

def lihat_absensi():
    conn = sqlite3.connect("absensi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM absensi")
    data = cursor.fetchall()
    conn.close()
    print("\nData Absensi:")
    for row in data:
        print(row)

def main():
    create_table()
    while True:
        print("\nSistem Absensi Karyawan")
        print("1. Absen Masuk (O(n²))")
        print("2. Absen Masuk (O(n log n))")
        print("3. Lihat Data Absensi")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama: ")
            absen_masuk_brute_force(nama)
        elif pilihan == "2":
            nama = input("Masukkan nama: ")
            absen_masuk_optimized(nama)
        elif pilihan == "3":
            lihat_absensi()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
