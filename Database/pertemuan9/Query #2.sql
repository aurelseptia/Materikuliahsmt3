CREATE TABLE tnl_pengadaan(
kode_pengadaan VARCHAR (20) PRIMARY KEY,
tgl_pengadaan DATE,
kode_supplier VARCHAR(20),
FOREIGN KEY (kode_supplier)
REFERENCES tbl_supplier(kode_supplier));
SELECT * FROM tbl_supplier;