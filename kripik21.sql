-- Membuat database
CREATE DATABASE kripik21;

-- Menggunakan database yang baru dibuat
USE kripik21;

-- Membuat tabel reservations
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- ID unik untuk setiap reservasi
    name VARCHAR(255) NOT NULL,                -- Nama pemesan
    email VARCHAR(255) NOT NULL,               -- Email pemesan
    datetime DATETIME NOT NULL,                -- Tanggal dan waktu reservasi
    people INT NOT NULL,                       -- Jumlah orang
    message TEXT,                              -- Pesan khusus
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Waktu data dibuat
);
