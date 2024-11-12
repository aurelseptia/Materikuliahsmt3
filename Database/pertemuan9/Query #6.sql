SELECT
tbl_pengadaan.kode_pengadaan,
tbl_pengadaan.tgl_pengadaan,
tbl_supplier.kode_supplier,
tbl_supplier.nama_supplier,
tbl_supplier.alamat_supplier,
tbl_barang.kode_barang,
tbl_barang.nama-barang,
tbl_detail_pengadaan.jumlah AS QTY,
(tbl_detail_pengadaan.total_harga /
(tbl.dtail_pengadaan.jumlah*40)) AS Harga_satuan,
tbl_detail_pengadaan.jumlah
FROM tbl_pengadaan
JOIN tbl_supplier ON tbl_supplier.kode_supplier = 
tbl_pengadaan.kode_supplier
JOIN tbl_barang ON tbl_barang.kode_barang =
tbl_detai_pengadaan.kode_barang
JOIN tbl_detail_pengadaan ON tbl_detail_pengadaan.kode_pengadaan
WHERE tbl_pengadaan.kode_pengadaan = "PGD002"