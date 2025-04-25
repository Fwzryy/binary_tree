import json
from collections import deque
from tabulate import tabulate

class NodeProduk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.left = None
        self.right = None

class KatalogProduk:
    def __init__(self):
        self.root = None

    def tambah_produk(self, nama, harga):
        node_baru = NodeProduk(nama, harga)
        if not self.root:
            self.root = node_baru
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = node_baru
                return
            elif not current.right:
                current.right = node_baru
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def cari_produk(self, nama):
        return self._cari(self.root, nama)

    def _cari(self, node, nama):
        if not node:
            return None
        if node.nama.lower() == nama.lower():
            return node
        ditemukan = self._cari(node.left, nama)
        if ditemukan:
            return ditemukan
        return self._cari(node.right, nama)

    def hapus_produk(self, nama):
        if not self.root:
            return None

        queue = deque()
        queue.append(self.root)

        target = None
        node_terakhir = None

        while queue:
            node_terakhir = queue.popleft()
            if node_terakhir.nama.lower() == nama.lower():
                target = node_terakhir
            if node_terakhir.left:
                queue.append(node_terakhir.left)
            if node_terakhir.right:
                queue.append(node_terakhir.right)

        if not target:
            return None

        target.nama = node_terakhir.nama
        target.harga = node_terakhir.harga

        queue.clear()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            if current.left:
                if current.left == node_terakhir:
                    current.left = None
                    return node_terakhir
                queue.append(current.left)
            if current.right:
                if current.right == node_terakhir:
                    current.right = None
                    return node_terakhir
                queue.append(current.right)
        return node_terakhir

    def tampilkan_produk(self):
        print("\n KATALOG PRODUK - BINARY TREE")
        produk_list = self._preorder(self.root)
        print(tabulate(produk_list, headers=["Nama Produk", "Harga"], tablefmt="fancy_grid"))

    def _preorder(self, node):
        produk_list = []
        if node:
            produk_list.append([node.nama, f"Rp{node.harga:,.2f}"])
            produk_list.extend(self._preorder(node.left))
            produk_list.extend(self._preorder(node.right))
        return produk_list

    def tampilkan_hierarki(self):
        if not self.root:
            print("Katalog kosong.")
            return

        def _cetak(node, level=0, sisi="root"):
            if node:
                print("    " * level + f"[{sisi}] {node.nama} (Rp{node.harga:,.2f})")
                _cetak(node.left, level + 1, "left")
                _cetak(node.right, level + 1, "right")

        print("\n=== STRUKTUR HIERARKI PRODUK ===")
        _cetak(self.root)
        print("===============================\n")

    def simpan_ke_file(self, nama_file):
        data = []
        queue = deque()
        if self.root:
            queue.append(self.root)

        while queue:
            node = queue.popleft()
            data.append({'nama': node.nama, 'harga': node.harga})
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        with open(nama_file, 'w') as f:
            json.dump(data, f)
        print(f"Katalog berhasil disimpan ke '{nama_file}'.")

    def muat_dari_file(self, nama_file):
        try:
            with open(nama_file, 'r') as f:
                data = json.load(f)
            self.root = None  # reset
            for item in data:
                self.tambah_produk(item['nama'], item['harga'])
            print(f"Katalog berhasil dimuat dari '{nama_file}'.")
        except FileNotFoundError:
            print(f"File '{nama_file}' tidak ditemukan.")
        except Exception as e:
            print("Terjadi kesalahan saat memuat file:", str(e))


def menu():
    katalog = KatalogProduk()

    while True:
        print("MENU KATALOG PRODUK")
        menu = [
            ["1.", "Tambah Produk"],
            ["2.", "Cari Produk"],
            ["3.", "Hapus Produk"],
            ["4.", "Tampilkan Semua Produk"],
            ["5.", "Tampilkan Struktur Hierarki"],
            ["6.", "Simpan ke File"],
            ["7.", "Muat dari File"],
            ["8.", "Keluar"]
        ]
        print(tabulate(menu, headers=["No.", "Menu"], tablefmt="fancy_grid"))

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            nama = input("Masukkan nama produk: ").strip()
            try:
                harga = float(input("Masukkan harga produk: "))
                katalog.tambah_produk(nama, harga)
                print(f"Produk '{nama}' berhasil ditambahkan.")
            except ValueError:
                print("Harga tidak valid. Masukkan angka.")

        elif pilihan == '2':
            nama = input("Masukkan nama produk yang dicari: ").strip()
            hasil = katalog.cari_produk(nama)
            if hasil:
                print(f"Ditemukan: {hasil.nama} | Harga: Rp{hasil.harga:,.2f}")
            else:
                print("Produk tidak ditemukan.")

        elif pilihan == '3':
            nama = input("Masukkan nama produk yang ingin dihapus: ").strip()
            dihapus = katalog.hapus_produk(nama)
            if dihapus:
                print(f"Produk '{nama}' berhasil dihapus.")
            else:
                print("Produk tidak ditemukan.")

        elif pilihan == '4':
            katalog.tampilkan_produk()

        elif pilihan == '5':
            katalog.tampilkan_hierarki()

        elif pilihan == '6':
            nama_file = input("Masukkan nama file untuk menyimpan (contoh: katalog.json): ")
            katalog.simpan_ke_file(nama_file)

        elif pilihan == '7':
            nama_file = input("Masukkan nama file untuk dimuat (contoh: katalog.json): ")
            katalog.muat_dari_file(nama_file)

        elif pilihan == '8':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()