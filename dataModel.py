from __future__ import print_function

import mysql.connector
import os
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


class dataModel():
    """data models for the applications"""

    def __init__(self) -> None:
        self.create_table_init_()

    def connect_to_db(self):
        """conect to data base"""
        config = {
            "user": "zami",
            "password": "zami123",
            "host": "127.0.0.1",
            "database": "perpustakaan",
            "raise_on_warnings": True,
        }
        cnx = mysql.connector.connect(**config)
        return cnx

    def create_table_init_(self):
        """
        create initial table:
            1. anggota
            2. petugas
            3. buku
            4. rak buku
            5. peminjaman
            6. pengembalian
        """
        TABLES = {}

        TABLES[
            "anggota"
        ] = """
            CREATE TABLE IF NOT EXISTS `anggota` (
                `id_anggota` INT(25) NOT NULL AUTO_INCREMENT,
                `nama_anggota` VARCHAR(60) NOT NULL UNIQUE,
                `kelas_anggota` INT(2) NOT NULL,
                `no_telp_anggota` CHAR(13),
                `alamat_anggota` VARCHAR(100),
                PRIMARY KEY (`id_anggota`)
            ) ENGINE=InnoDB;
        """
        TABLES[
            "petugas"
        ] = """
            CREATE TABLE IF NOT EXISTS `petugas` (
                `id_petugas` INT(25) NOT NULL AUTO_INCREMENT,
                `nama_petugas` VARCHAR(50) NOT NULL UNIQUE,
                `jabatan_petugas` VARCHAR(50),
                `no_telp_petugas` CHAR(13),
                `alamat_petugas` VARCHAR(100),
                PRIMARY KEY (`id_petugas`)
            ) ENGINE=InnoDB;
        """
        TABLES[
            "rak_buku"
        ] = """
            CREATE TABLE IF NOT EXISTS `rak_buku` (
                `id_rak_buku` INT(11) NOT NULL AUTO_INCREMENT,
                `nama_rak_buku` VARCHAR(5) NOT NULL,
                `lokasi_rak_buku` VARCHAR(50),
                PRIMARY KEY (`id_rak`)
            ) ENGINE=InnoDB;
        """
        TABLES[
            "buku"
        ] = """
            CREATE TABLE IF NOT EXISTS `buku` (
                `id_buku` INT(25) NOT NULL AUTO_INCREMENT,
                `kode_buku` VARCHAR(5) NOT NULL,
                `judul_buku` VARCHAR(50) NOT NULL,
                `penulis_buku` VARCHAR(25),
                `penerbit_buku` VARCHAR(25),
                `tahun_terbit_buku` YEAR,
                `stock_buku` INT(11),
                `id_rak` INT(11),
                PRIMARY KEY (`id_buku`),
                CONSTRAINT `buku_id_rak` FOREIGN KEY (`id_rak`)
                    REFERENCES `rak_buku` (`id_rak_buku`) ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """
        TABLES[
            "peminjaman"
        ] = """
            CREATE TABLE IF NOT EXISTS `peminjaman` (
                `id_peminjaman` INT(11) NOT NULL AUTO_INCREMENT,
                `tanggal_peminjaman` DATE NOT NULL,
                `tanggal_kembali` DATE NOT NULL,
                `id_buku` INT(25),
                `id_anggota` INT(25),
                `id_petugas` INT(25),
                PRIMARY KEY (`id_peminjaman`),
                CONSTRAINT `peminjaman_id_buku` FOREIGN KEY (`id_buku`)
                    REFERENCES `buku` (`id_buku`) ON DELETE CASCADE,
                CONSTRAINT `peminjaman_id_anggota` FOREIGN KEY (`id_anggota`)
                    REFERENCES `anggota` (`id_anggota`) ON DELETE CASCADE,
                CONSTRAINT `peminjaman_id_petugas` FOREIGN KEY (`id_petugas`)
                    REFERENCES `petugas` (`id_petugas`) ON DELETE CASCADE
            ) ENGINE=InnoDB;
        """
        TABLES[
            "pengembalian"
        ] = """
            CREATE TABLE IF NOT EXISTS `pengembalian` (
                `id_pengembalian` INT(11) NOT NULL AUTO_INCREMENT,
                `tanggal_pengembalian` DATE NOT NULL,
                `denda` INT(11),
                `id_buku` INT(25),
                `id_anggota` INT(25),
                `id_petugas` INT(25),
                PRIMARY KEY (`id_pengembalian`),
                CONSTRAINT `pengembalian_id_buku` FOREIGN KEY (`id_buku`)
                    REFERENCES `buku` (`id_buku`) ON DELETE CASCADE,
                CONSTRAINT `pengembalian_id_anggota` FOREIGN KEY (`id_anggota`)
                    REFERENCES `anggota` (`id_anggota`) ON DELETE CASCADE,
                CONSTRAINT `pengembalian_id_petugas` FOREIGN KEY (`id_petugas`)
                    REFERENCES `petugas` (`id_petugas`) ON DELETE CASCADE
            ) ENGINE=InnoDB
            """
        cnx = self.connect_to_db()
        with cnx.cursor() as cursor:
            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    cursor.execute(table_description)
                    print("Creating table {}: ".format(table_name), end="")
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        os.system('cls')
                    else:
                        print(err.msg)
                else:
                    print("OK")
        os.system('cls')
        cnx.close()

    def _get_id(self, table, value: tuple):
        """get id for given name from given table name"""
        query = (
            f"SELECT id_{table} FROM {table} WHERE {value[0]} = '{value[1]}'"
        )
        # print('_get_id: ', query)
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query)
                id_ = cursor.fetchone()
                # print('_get_id: ', id_)
                if id_ is not None:
                    return id_[0]
                
        except mysql.connector.Error as err:
            print("_get_id: ", err, err.msg)
            return None
    
    def _change_stock(self, kode_buku, delta):
        """edit jumlah stock buku"""
        q_current_stock = f"SELECT stock_buku FROM buku WHERE kode_buku = '{kode_buku}'"
        q_change_stock = "UPDATE buku SET stock_buku = {} WHERE kode_buku = '{}'"
        cnx = self.connect_to_db()
        current_stock = 0
        try:
            cursor = cnx.cursor()
            cursor.execute(q_current_stock)
            current_stock = cursor.fetchone()[0]
            if current_stock > 0:
                current_stock += delta
                # update stock
                cursor.execute(q_change_stock.format(current_stock, kode_buku))
                cnx.commit()
                print('stock buku {} diupdate: {}'.format(kode_buku, current_stock))
        except mysql.connector.Error as err:
            print('_change_stock__current_stock: ', err.msg)
        

    def add_petugas(
        self, nama_petugas, jabatan_petugas, telp_petugas, alamat_petugas
    ):
        """Add new petugas"""
        query = (
            "INSERT INTO petugas "
            "(nama_petugas, jabatan_petugas, no_telp_petugas, alamat_petugas) "
            "VALUES (%(nama)s, %(jabatan)s, %(telp)s, %(alamat)s)"
        )
        data_petugas = {
            "nama": nama_petugas,
            "jabatan": jabatan_petugas,
            "telp": telp_petugas,
            "alamat": alamat_petugas,
        }
        # masukkan petugas baru
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query, data_petugas)
                cnx.commit()
                print("add_petugas: petugas berhasil ditambahkan")
        except mysql.connector.Error as err:
            print("add_petugas: ", err.msg)
        cnx.close()

    def add_anggota(
        self,
        nama_anggota: str,
        kelas_anggota: int,
        telp_anggota: str,
        alamat_anggota: str,
    ):
        """add new anggota"""
        data_anggota = {
            "nama": nama_anggota,
            "kelas": kelas_anggota,
            "telp": telp_anggota,
            "alamat": alamat_anggota,
        }
        query = """
            INSERT INTO anggota 
            (nama_anggota, kelas_anggota, no_telp_anggota, alamat_anggota) 
            VALUES (%(nama)s, %(kelas)s, %(telp)s, %(alamat)s)
        """
        # masukan anggota baru
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query, data_anggota)
                cnx.commit()
                print("add_anggota: anggota berhasil ditambahkan")
        except mysql.connector.Error as err:
            print("add_anggota: ", err, " ", err.msg)
        cnx.close()

    def add_buku(
        self,
        kode_buku: str,
        judul_buku: str,
        penulis_buku: str,
        penerbit_buku: str,
        tahun_terbit_buku,
        stock_buku: int,
        nama_rak_buku: str,
    ):
        """add new buku"""
        id_rak = self._get_id('rak_buku', ('nama_rak_buku', nama_rak_buku))
        data_buku = {
            "kode": kode_buku,
            "judul": judul_buku,
            "penulis": penulis_buku,
            "penerbit": penerbit_buku,
            "tahun": tahun_terbit_buku,
            "stock": stock_buku,
            "id_rak": id_rak,
        }
        query = """
            INSERT INTO buku 
            (kode_buku, judul_buku, penulis_buku, penerbit_buku, tahun_terbit_buku, stock_buku, id_rak) 
            VALUES (%(kode)s, %(judul)s, %(penulis)s, %(penerbit)s, %(tahun)s, %(stock)s, %(id_rak)s)
        """
        # masukkan buru baru
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query, data_buku)
                cnx.commit()
                print("add_buku: buku berhasil ditambahkan")
        except mysql.connector.Error as err:
            print("add_buku: ", err, " ", err.msg)
        cnx.close()

    def add_rak_buku(self, nama_rak, lokasi_rak):
        """add new rak buku"""
        data_rak_buku = {"nama": nama_rak, "lokasi": lokasi_rak}
        query = """
            INSERT INTO rak_buku
            (nama_rak_buku, lokasi_rak_buku)
            VALUES (%(nama)s, %(lokasi)s)
        """
        # masukkan data rak baru
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query, data_rak_buku)
                id_rak = cursor.lastrowid
                cnx.commit()
                print("add_rak_buku: rak_buku berhasil ditambhakan")
                cnx.close()
                return id_rak
        except mysql.connector.Error as err:
            print("add_rak_buku: ", err, err.msg)
            cnx.close()

    def add_peminjaman(self, kode_buku, nama_anggota, nama_petugas):
        """add new peminjaman"""
        tgl_pinjam = date.today()
        tgl_kembali = tgl_pinjam + timedelta(days=14)  # 2 minggu dikembalikan
        id_buku = self._get_id("buku", ("kode_buku", kode_buku))
        id_anggota = self._get_id("anggota", ("nama_anggota", nama_anggota))
        id_petugas = self._get_id("petugas", ("nama_petugas", nama_petugas))
        data_peminjaman = {
            "tgl_pinjam": tgl_pinjam,
            "tgl_kembali": tgl_kembali,
            "id_buku": id_buku,
            "id_anggota": id_anggota,
            "id_petugas": id_petugas,
        }
        query = """
            INSERT INTO peminjaman
            (tanggal_peminjaman, tanggal_kembali, id_buku, id_anggota, id_petugas) 
            VALUES (%(tgl_pinjam)s, %(tgl_kembali)s, %(id_buku)s, %(id_anggota)s, %(id_petugas)s)
        """
        cnx = self.connect_to_db()
        success = False
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query, data_peminjaman)
                cnx.commit()
                print("add_peminjaman: data peminjaman berhasil ditambahkan")
                success = True
                self._change_stock(kode_buku, -1)
        except mysql.connector.Error as err:
            print("add_peminjaman: ", err, err.msg)
        cnx.close()

        # self._change_stock(kode_buku, -1)

    def add_pengembalian(self, kode_buku, nama_anggota, nama_petugas):
        """add data pengembalian"""
        tgl_pengembalian = date.today()
        # print("data pengembalian:\n\t- nama buku\t: itu\n\t- nama\t\t: aku\n\t- petugas\t: kamu")
        denda = 0
        id_buku = self._get_id("buku", ("kode_buku", kode_buku))
        id_anggota = self._get_id("anggota", ("nama_anggota", nama_anggota))
        id_petugas = self._get_id("petugas", ("nama_petugas", nama_petugas))
        data_pengembalian = {
            "tgl_pengembalian": tgl_pengembalian,
            "denda": denda,
            "id_buku": id_buku,
            "id_anggota": id_anggota,
            "id_petugas": id_petugas,
        }
        query = """
            INSERT INTO pengembalian
            (tanggal_pengembalian, denda, id_buku, id_anggota, id_petugas)
            VALUES (%(tgl_pengembalian)s, %(denda)s, %(id_buku)s, %(id_anggota)s, %(id_petugas)s)
        """
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query, data_pengembalian)
                cnx.commit()
                print("add_pengembalian: pengembalian sudah ditambahkan")
                self._change_stock(kode_buku, 1)
        except mysql.connector.Error as err:
            print("add_pengembalian: ", err, err.msg)
        cnx.close()
    
    def get_all_nama_rak_buku(self):
        """get all nama rak buku"""
        query = "SELECT nama_rak_buku FROM rak_buku"
        value = []
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query)
                all_nama_rak_buku = cursor.fetchall()
                for nama in all_nama_rak_buku:
                    value.append(nama[0])
                return value
        except mysql.connector.Error as err:
            print('get_all_nama_rak_buku: ', err.msg)
    
    def _get_all_data_from_table(self, table_name):
        """Get all data from table"""
        q_all_buku = f"SELECT * FROM {table_name}"
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(q_all_buku)
                all_data_buku = cursor.fetchall()
            return all_data_buku
            cnx.close()
        except mysql.connector.Error as err:
            print('_get_all_data_from_table: ', err.msg)
        cnx.close()

    def _get_data_table_where(self, table_name, conditions):
        """Get data from table with given one conditions"""
        query = F"SELECT * FROM {table_name} WHERE {conditions[0]} = {conditions[1]}"
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query)
                all_data_buku = cursor.fetchone()
            return all_data_buku
            cnx.close()
        except mysql.connector.Error as err:
            print('_get_data_table_where: ', err.msg)
        cnx.close()

    def _update_data_table_where(self, table_name, set_to, conditions):
        '''"""Update table with given value and condition"""'''

        query = f"UPDATE {table_name} SET {set_to[0]} = '{set_to[1]}' WHERE {conditions[0]} = {conditions[1]}"
       
        cnx = self.connect_to_db()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(query)
                cnx.commit()
                return True
        except mysql.connector.Error as err:
            print('_update_data_table_where: ', err.msg)
            return False
        cnx.close()



if __name__ == "__main__":
    # pass
    data = dataModel()
    # data.add_petugas("zami", "librarian", 8567883938, "mangunan")
    # data.add_anggota(
    #     "yusuf",
    #     11,
    #     '8736788474',
    #     'plosokursi'
    # )
    # data.add_rak_buku('B612', 'block B')
    # data.add_buku('fisdas1', 'Fisika dasar 1', 'Tipler Paul A.', 'Mc Grill', 2006, 5, 'B612')
    # data.add_peminjaman('fisdas1', 'yusuf', 'zami')
    # data.add_pengembalian('fisdas1', 'yusuf', 'zami')


