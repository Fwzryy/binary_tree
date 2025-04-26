# 📦 Katalog Produk - Binary Tree (Non-BST)

Program Python ini adalah aplikasi terminal interaktif untuk mengelola data produk menggunakan struktur **Binary Tree (Non-BST : Binary Search Tree)**. Aplikasi ini memiliki fitur tambah, cari, hapus, tampilkan produk (pre-order traversal), cetak struktur hierarki, serta menyimpan dan memuat data dari file JSON.

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
-  (`deque` dari `collections`) Struktur antrian yang efisien untuk menambahkan/menghapus dari anak kiri dan anak kanan
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
`self.left = None` Menyiapkan sambungan ke anak kiri dari node ini. di set ke None untuk nilai awal, begitu juga bagian kanan

### 3. Kelas `KatalogProduk`
```python
class KatalogProduk:
    def __init__(self):
        self.root = None
```
Membuat objek katalog dengan akar (root) yang awalnya kosong.

#### a. Tambah Produk
```python
def tambah_produk(self, nama, harga):
    node_baru = NodeProduk(nama, harga)
    if not self.root:
        self.root = node_baru
        return
```
Fungsi `tambah_produk` berguna untuk menambahkan produk baru ke dalam pohon. Pertama, dibuat node baru yang berisi nama dan harga produk menggunakan `NodeProduk(nama, harga)`. Lalu, dicek apakah `self.root` masih kosong; jika kosong, node baru langsung dijadikan akar pohon. Ini penting karena node pertama akan menjadi dasar untuk menambahkan produk-produk berikutnya di pohon.

```python
    queue = deque() #membuat antrian kosong
    queue.append(self.root) #memasukkan akar pohon(root) ke dalam antrian

    while queue: #selama antrian masih ada isinya, proses akan terus berjalan
        current = queue.popleft() #mengambil node paling depan dari antrian untuk diperiksa
        if not current.left: #jika node yang sedang diperiksa belum punya anak kiri? 
            current.left = node_baru #maka node baru langsung ditempatkan di kiri.
            return
        elif not current.right: #jika anak kiri sudah ada, tapi anak kanan belum?
            current.right = node_baru #maka node baru ditempatkan di kanan
            return
        else: #kalau kiri dan kanan sudah terisi, anak-anaknya dimasukkan ke antrian supaya nanti diperiksa juga ↓
            queue.append(current.left)
            queue.append(current.right)
```

#### b. Cari Produk
```python
def cari_produk(self, nama): #fungsi untuk mencari produk berdasarkan nama
    return self._cari(self.root, nama) #memanggil fungsi bantu _cari untuk melakukan pencarian secara rekursif mulai dari root.
    ''' Mencari secara rekursif:
    - Mulai cari dari root(paling atas), 
    - kalau tidak ketemu di root, fungsi _cari memanggil dirinya sendiri untuk lanjut cari ke anak kiri, 
    - kalau belum ketemu juga di kiri, fungsi _cari memanggil dirinya sendiri untuk lanjut cari ke anak kanan
    Begitu seterusnya sampai ketemu dan semua cabang habis diperiksa✅
    '''
def _cari(self, node, nama): #ini dia fungsi rekursif yang akan menelusuri node 1 per 1
    if not node: #kalau node yang diperiksa kosong(None)?
        return None #berarti produk tidak ditemukan -> return None
    if node.nama.lower() == nama.lower(): #jika nama produk di node sekarang sama dengan nama yang dicari(tidak peduli huruf besar-kecil)
        return node #maka return node itu
    ditemukan = self._cari(node.left, nama) #kalau belum ketemu, cari di anak kiri terlebih dahulu, simpan ke variable ditemukan
    if ditemukan: #jika sudah ketemu hasilnya di anak kiri?
        return ditemukan #return hasilnya
    return self._cari(node.right, nama) #kalau belum ketemu di kiri, panggil lagi fungsi _cari untuk menelusuri anak kanan.

```

#### c. Hapus Produk


#### e. Tampilkan Produk


#### f. Tampilkan Hierarki


#### g. Simpan dan Muat File JSON


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
python product_catalog.py
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
(DD/MM/YYYY)
---

Silakan fork, clone, dan kembangkan! 🚀

