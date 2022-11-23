import dataModel
import os
from getpass import getpass
from tabulate import tabulate


class management_perpustakaan:
    def __init__(self) -> None:
        self.dataBase = dataModel.dataModel()
        self.whoiam = None

    def main_menu(self):
        """Show main menu for petugas"""
        os.system("cls")
        print("Login berhasil.")
        prined = """
Main Menu/>

Silakan pilih (angka) menu yang anda inginkan
    [1]: Input ke Data Base (Rak dan Buku)
    [2]: Input Peminjaman
    [3]: Input Pengembalian
    [4]: Pendaftaran Anggota Baru
    [5]: Edit Buku
    [9]: Keluar Aplikasi
"""
        print(prined)
        trial = 0
        while trial < 5:
            menu = input("Masukkan (angka) menu yang dipilih: ")
            try:
                menu = int(menu)
                trial += 5
            except:
                print("masukkan angka saja")
                trial += 1

        if menu == 1:
            # run Input menu data base
            self.input_data_base()
        elif menu == 2:
            # run Input peminjaman
            self.input_data_peminjaman()
        elif menu == 3:
            # run Input Pengembalian
            self.input_data_pengembalian()
        elif menu == 4:
            self.input_anggota_baru()
        elif menu == 5:
            self.edit_buku()
        elif menu == 9:
            print("Keluar Aplikasi ...")
            exit()
        else:
            exit()

    def input_data_base(self):
        """Input Data to Data Base"""
        os.system("cls")
        pil_block = """
Main Menu/Input Data/>

Silakan pilih (angka) menu yang anda inginkan:
    [1]: Input Data Rak
    [2]: Input Data Buku
    [8]: Kembali (Menu Utama)
    [9]: Keluar Aplikasi.
"""
        print(pil_block)
        trial = 0
        while trial < 5:
            menu = input("Masukkan (angka) menu yang dipilih: ")
            try:
                menu = int(menu)
                trial += 5
            except:
                print("Masukkan hanya angka saja")

        if menu == 1:
            # run Input Data Rak
            self.input_data_rak_buku()
        elif menu == 2:
            self.input_data_buku()
            # run Input data buku
        elif menu == 8:
            self.main_menu()
        elif menu == 9:
            print("\nKeluar Aplikasi...")
            exit()
        else:
            self.main_menu()

#     def _input_data_block_rak_buku(self):
#         block = ("Block A", "Block B", "Block C", "Block D", "Block E")
#         pil_block = """
# Main Menu/Input Data/Rak Buku/>

# Silakan masukkan data:

# Pilih (angka) Lokasi Rak Buku:
#     [1]: Block A
#     [2]: Block B
#     [3]: Block C
#     [4]: Block D
#     [5]: Block E
#         """
#         print(pil_block)
#         trial = 4

#         idx_rak_buku = input("Masukkan (angka) Lokasi yang dipilih: ")
#         # print(idx_rak_buku)
#         try:
#             for i in range(trial):
#                 idx_rak_buku = int(idx_rak_buku)
#                 lokasi_rak_buku = block[idx_rak_buku - 1]
#                 i += 5
#                 # print(lokasi_rak_buku)
#                 return lokasi_rak_buku
#         except:
#             i += 1
#             print(
#                 "Masukkan hanya angka saja. / (percobaan ke -{} dari 4".format(
#                     i
#                 )
#             )

#     def _input_data_nama_rak(self, block_name):
#         list_nama_rak = {
#             "Block A": {"a": "A116", "b": "A216", "c": "A316"},
#             "Block B": {"a": "B412", "b": "B512", "c": "B612"},
#             "Block C": {"a": "C721", "b": "C821", "c": "C921"},
#             "Block D": {"a": "D942", "b": "D842", "c": "D742"},
#             "Block E": {"a": "E651", "b": "E551", "c": "E451"},
#         }
#         # print(list_nama_rak[block_name])
#         pil_nama_rak = """
# Pilih nama Block berikut:
#     [1]: %(a)s
#     [2]: %(b)s
#     [3]: %(c)s
#         """
#         # pilih nama rak buku
#         forma = list_nama_rak[block_name]
#         # print(forma)
#         print(pil_nama_rak % forma)
#         idx_nama_rak = None
#         jj = 0
#         while jj < 5:
#             idx_nama_rak = input("Masukkan (angka) nama rak yang dipilih")
#             try:
#                 idx_nama_rak = int(idx_nama_rak)
#                 jj += 5
#             except:
#                 jj += 1
#                 print(
#                     "Masukkan hanya angka saja. / (percobaan ke -{} dari 4".format(
#                         jj
#                     )
#                 )
#         if idx_nama_rak is not None:
#             nama_rak = list_nama_rak[block_name]
#             if idx_nama_rak == 1:
#                 nama_rak = nama_rak["a"]
#             elif idx_nama_rak == 2:
#                 nama_rak = nama_rak["b"]
#             elif idx_nama_rak == 3:
#                 nama_rak = nama_rak["c"]
#         return nama_rak

    def input_data_rak_buku(self):
        """Input data rak buku baru"""
        os.system("cls")
        print("Main menu/Input Data/Input Data Rak Buku/>\n")
        cancel_ = " [c]->cancel> "
        # lokasi_rak_buku = self._input_data_block_rak_buku()
        # # print(lokasi_rak_buku)
        # nama_rak_buku = self._input_data_nama_rak(lokasi_rak_buku)
        nama_rak_buku = input("Masukkan Nama Rak Buku" + cancel_)
        if (nama_rak_buku == "c") or (nama_rak_buku == "C"):
            self.main_menu()

        lokasi_rak_buku = input("Masukkan Lokasi Rak Buku" + cancel_)
        if (lokasi_rak_buku == "c") or (lokasi_rak_buku == "C"):
            self.main_menu()

        # input ke data base
        try:
            self.dataBase.add_rak_buku(nama_rak_buku, lokasi_rak_buku)
            cmd = (
                "Apakah anda ingin menambah data rak buku? [Y (default)]/[n]?: "
            )
            command = input(cmd) or 'y'
            if (command == "n") or (command == "N"):
                self.main_menu()
            else:
                self.input_data_rak_buku()
        except:
            print("input_rak_buku_error: ")
            self.main_menu()

    def input_data_buku(self):
        """Input data buku baru"""
        os.system("cls")
        print("Main menu/Input Data/Input Data Buku/>\n")
        cancel_ = " [c]->cancel> "

        kode_buku = input("Masukkan Kode Buku" + cancel_)
        if (kode_buku == "c") or (kode_buku == "C"):
            self.main_menu()

        judul_buku = input("Masukkan judul buku" + cancel_)
        if (judul_buku == "c") or (judul_buku == "C"):
            self.main_menu()

        pengarang_buku = input("Masukkan pengarang buku" + cancel_)
        if (pengarang_buku == "c") or (pengarang_buku == "C"):
            self.main_menu()

        penerbit_buku = input("Masukkan Penerbit Buku" + cancel_)
        if (penerbit_buku == "c") or (penerbit_buku == "C"):
            self.main_menu()

        tahun_terbit_buku = input("Masukkan Tahun terbit buku" + cancel_)
        if (tahun_terbit_buku == "c") or (tahun_terbit_buku == "C"):
            self.main_menu()

        stock_buku = int(input("Masukkan jumlah stock buku [0]->cancel> "))
        if stock_buku == 0:
            self.main_menu()

        all_rak = self.dataBase.get_all_nama_rak_buku()  # get all nama rak buku
        print("Data nama rak buku: ", all_rak)
        nama_rak_buku = input("masukkan nama rak buku" + cancel_)
        if (nama_rak_buku == "c") or (nama_rak_buku == "C"):
            self.main_menu()

        self.dataBase.add_buku(
            kode_buku,
            judul_buku,
            pengarang_buku,
            penerbit_buku,
            tahun_terbit_buku,
            stock_buku,
            nama_rak_buku,
        )

        cmd = "Apakah anda ingin menambah data buku? [Y (default)]/[n]?: "
        command = input(cmd) or 'y'
        if (command == "n") or (command == "N"):
            self.main_menu()
        else:
            self.input_data_buku()

    def input_data_peminjaman(self):
        """Input data Peminjaman"""
        os.system("cls")
        print("Main Menu/Input Data Peminjaman/> \n")
        cancel_ = " [c]->cancel> "

        kode_buku = input("Masukkan kode buku" + cancel_)
        if (kode_buku == "c") or (kode_buku == "C"):
            self.main_menu()

        nama_peminjam = input("Masukkan nama Peminjam" + cancel_)
        if (nama_peminjam == "c") or (nama_peminjam == "C"):
            self.main_menu()

        self.dataBase.add_peminjaman(kode_buku, nama_peminjam, self.whoiam)

        cmd = "\nApakah anda ingin menambah data peminjam? [Y (default)]/[n]?: "
        command = input(cmd)  or 'y'
        if (command == "n") or (command == "N"):
            self.main_menu()
        else:
            self.input_data_peminjaman()
        # data.add_peminjaman('fisdas1', 'yusuf', 'zami')

    def input_data_pengembalian(self):
        """Add data pengembalian buku"""
        os.system("cls")
        print("Main Menu/Input Pengembalian Buku/> \n")
        cancel_ = " [c]->cancel> "

        kode_buku = input("Masukkan kode buku" + cancel_)
        if (kode_buku == "c") or (kode_buku == "C"):
            self.main_menu()

        nama_peminjam = input("Masukkan nama Peminjam" + cancel_) 
        if (nama_peminjam == "c") or (nama_peminjam == "C"):
            self.main_menu()

        self.dataBase.add_pengembalian(kode_buku, nama_peminjam, self.whoiam)

        cmd = "\nApakah anda ingin menambah data pengembalian? [Y (default)]/[n]?: "
        command = input(cmd)  or 'y'
        if (command == "n") or (command == "N"):
            self.main_menu()
        else:
            self.input_data_pengembalian()
    
    def input_anggota_baru(self):
        """Menambahkan anggota baru"""
        os.system('cls')
        print("Main Menu/Input Pendaftaran Anggota Baru/> \n")
        cancel_ = " [c]->cancel> "

        nama_anggota = input("Nama Anggota" + cancel_)
        if (nama_anggota == "c") or (nama_anggota == "C"):
            self.main_menu()

        kelas_anggota = int(input("Kelas Anggota (1 s/d 12): [0]->cancel:> "))
        if kelas_anggota in range(1, 13):
            kelas_anggota = kelas_anggota
        elif kelas_anggota == 0:
            self.main_menu()
        else:
            print("Kelas harus dari 1 s/d 12")
            self.input_anggota_baru()
        
        no_telp_anggota = input("Nomor Telephon" + cancel_)
        if (no_telp_anggota == "c") or (no_telp_anggota == "C"):
            self.main_menu()
        
        alamat_anggota = input("Alamat Anggota" + cancel_)
        if (alamat_anggota == "c") or (alamat_anggota == "C"):
            self.main_menu()

        self.dataBase.add_anggota(nama_anggota, kelas_anggota, no_telp_anggota, alamat_anggota)

        cmd = "\nApakah anda ingin menambah data anggota baru? [Y (default)]/[n]?: "
        command = input(cmd) or 'y'
        if (command == "n") or (command == "N"):
            self.main_menu()
        else:
            self.input_anggota_baru()
    
    def edit_buku(self):
        """Edit table buku"""
        os.system('cls')
        print("Main Menu/Edit Buku/>\n")
        all_data_buku = self.dataBase._get_all_data_from_table('buku')
        print("Silakan pilih id_buku")
        headers = ['Id Buku', 'Kode Buku', 'Judul Buku', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Stock', 'Id Rak']

        print(tabulate(all_data_buku, headers, tablefmt='orgtbl'))
        print('\n')

        id_buku_terpilih = input("Pilih Id Buku: [c]->cancel :> ")
        if (id_buku_terpilih == 'c') or (id_buku_terpilih == 'C'):
            self.main_menu()
        else:
            id_buku_terpilih = int(id_buku_terpilih)

        val = self.dataBase._get_data_table_where('buku', ("id_buku", id_buku_terpilih))
        # print(val)
        print("Pilih (Nomor) yang mau diedit")

        tampil = []
        for i in range(1, len(val)-1):
            tampil.append([i, headers[i], val[i]])
        
        print(tabulate(tampil, ["No", "kunci", "Nilai yang diganti"], tablefmt='orgtbl'))
        print('\n')
        idx = int(input("Pilih (No) yang akan diganti:> "))
        pengganti = input(f"{val[idx]} Diganti dengan:> ")

        key = ('id_buku', 'kode_buku', 'judul_buku', 'penulis_buku', 'penerbit_buku', 'tahun_terbit_buku', 'stock_buku', 'id_rak')

        resp = self.dataBase._update_data_table_where('buku', (key[idx], pengganti), (key[0], id_buku_terpilih))
        if resp:
            print("\nBerhasil mengganti!")
            print(f"{val[idx]} diganti dengan {pengganti}")
            cmd = "\nGanti tabel buku lagi? [Y (default)]/[n]?: "
            command = input(cmd) or 'y'
            if (command == "n") or (command == "N"):
                self.main_menu()
            else:
                self.edit_buku()
        else:
            print("Edit Buku Error.\nkembali ke Main Menu\n")
            self.main_menu()

    def login(self):
        """Login petugas perpustakaan"""
        # print('\n\n\n\n')
        print("===Silakan login ke akun petugas anda===\n")

        ntrials = 0
        while (self.whoiam is None) & (ntrials < 3):
            # username = input("Enter username: ")
            # password = getpass("Enter password: ")
            username = "zami"
            password = "zami123"
            if (username == "zami") & (password == "zami123"):
                self.whoiam = "zami"
                ntrials += 3
                print("Logged in...")
                return self.whoiam
            else:
                ntrials += 1
                if ntrials > 2:
                    print(f"percobaan ke-{ntrials} dari 3")
                    exit()
                else:
                    print(f"Please enter the corect username and password!")
                    print(f"percobaan ke-{ntrials} dari 3\n")

    def run(self):
        self.login()
        self.main_menu()


if __name__ == "__main__":
    app = management_perpustakaan()
    app.run()
