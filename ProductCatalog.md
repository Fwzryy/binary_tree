# 📦 Katalog Produk - Binary Tree (Non-BST)

Program Python ini adalah aplikasi terminal interaktif untuk mengelola data produk menggunakan struktur **Binary Tree (Non-BST : Binary Search Tree)**. Aplikasi ini memiliki fitur tambah, cari, hapus, tampilkan produk (pre-order traversal), cetak struktur hierarki, serta menyimpan dan memuat data dari file JSON.

**Program ini dibuat untuk memenuhi tugas project akhir mata kuliah Struktur Data**
---

## 🚀 Fitur Utama

- Tambah produk ke dalam Binary Tree
- Cari produk berdasarkan nama
- Hapus produk dari Binary Tree
- Tampilkan semua produk (pre-order traversal)
- Visualisasi hierarki struktur pohon
- Simpan dan muat data dari file `.json`

---

## 🧠 Struktur Program

### 1. Import Library
```python
import json
from collections import deque
from tabulate import tabulate
```
Digunakan untuk:
- Untuk menyimpan dan membaca data produk dari file `.json`
-  (`deque` dari `collections`) Struktur antrian yang efisien untuk menambahkan/menghapus dari kedua sisi: kiri dan kanan
- (`tabulate`) Untuk mencetak tabel dengan rapi di terminal. 

### 2. Kelas `NodeProduk`
```python
class NodeProduk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.left = None
        self.right = None
```
Mendefinisikan sebuah class bernama `NodeProduk`, Class ini digunakan untuk merepresentasikan satu produk dalam sistem katalog. Setiap node (produk) akan menyimpan nama, harga, dan sambungan ke produk lain (kiri dan kanan).  
`def __init__(self, nama, harga)` Ini adalah fungsi konstruktor. Fungsi ini akan otomatis dijalankan saat objek NodeProduk baru dibuat. Parameter: `self` Instance objek dari class NodeProduk (python mengisi otomatis), `nama`, `harga`   
`self.left = None` Menyiapkan sambungan ke sisi kiri dari node ini. di set ke None untuk nilai awal, begitu juga bagian kanan `self.right = None` 

### 3. Kelas `KatalogProduk`
#### a. Konstruktor
```python
self.root = None
```
Membuat pohon kosong.

#### b. Tambah Produk
```python
def tambah_produk(self, nama, harga):
```
Menambahkan produk menggunakan **Breadth-First Insertion** agar tree tetap seimbang dari kiri ke kanan.

#### c. Cari Produk
```python
def cari_produk(self, nama):
```
Mencari node dengan nama yang sesuai menggunakan traversal rekursif (DFS preorder).

#### d. Hapus Produk
```python
def hapus_produk(self, nama):
```
Menghapus node dengan menggantinya dengan node terakhir dan menghapus node terakhir dari pohon.

#### e. Tampilkan Produk
```python
def tampilkan_produk(self):
```
Menampilkan semua produk dalam format tabel dengan traversal **pre-order**.

#### f. Tampilkan Hierarki
```python
def tampilkan_hierarki(self):
```
Menampilkan struktur pohon dengan indentasi berdasarkan level dan arah cabang (`root`, `left`, `right`).

#### g. Simpan dan Muat File JSON
```python
def simpan_ke_file(self, nama_file):
def muat_dari_file(self, nama_file):
```
- Menyimpan struktur tree ke dalam file JSON
- Memuat dan membangun tree kembali dari file JSON

### 4. Fungsi `menu()`
```python
def menu():
```
Menampilkan menu pilihan interaktif ke pengguna:
- Tambah, cari, hapus produk
- Lihat daftar dan hierarki produk
- Simpan/muat ke/dari file JSON

### 5. Program Utama
```python
if __name__ == "__main__":
    menu()
```
Menjalankan fungsi `menu()` hanya jika file dijalankan langsung.

---

## 📂 Contoh Struktur Hierarki
```
[root] Laptop (Rp8.000.000,00)
    [left] Keyboard (Rp250.000,00)
        [left] Mouse (Rp150.000,00)
        [right] Flashdisk (Rp80.000,00)
    [right] Monitor (Rp2.000.000,00)
```

---

## 🧪 Cara Menjalankan
1. Pastikan Python 3 sudah terinstal.
2. Install library tabulate:
```bash
pip install tabulate
```
3. Jalankan file Python:
```bash
python katalog_produk.py
```

---

## 🧰 Dependencies
- Python 3.x
- `tabulate`

---

## 👥 Kontributor
- Muhammad Fawwaz Raihan
- Teman-teman Kelompok Struktur Data

---

## 📄 Lisensi
Proyek ini bebas digunakan untuk pembelajaran dan tugas akademik. Tidak untuk tujuan komersial.

---

Silakan fork, clone, dan kembangkan! 🚀

