<?php
// Membuat Form Mahasiwa
function formMahasiswa()
{
    echo "
<h1>Form Mahasiswa</h1>
<form  method='POST'>
<table border='1'>
<tr><td><label for='nim'>NIM</label></td>
    <td><input type='text' name='nim' id='nim'></td></tr>
<tr><td><label for='nama'>NAMA</label></td>
    <td><input type='text' name='nama' id='nama'></td></tr>
<tr><td><label for='jurusan'>JURUSAN</label></td>
    <td><input type='text' name='jurusan' id='jurusan'></td></tr>
<tr><td></td><td><input type='submit' value='Submit'></td></tr>
</table>
</form>";
}
formMahasiswa();

echo "
<h1>Tabel Mahasiswa</h1>
<table border='1'>
<tr>
<th>No</th>
<th>NIM</th>
<th>NAMA</th>
<th>JURUSAN</th>
<th>Aksi</th>
</tr>
"; 
$result = $connect->query("SELECT * FROM tbl_mahasiswa");
if ($result->num_rows > 0) {
    $no = 1;
    while ($row = $result->fetch_assoc()) {
        echo "
        <tr>
        <td>{$no}</td>
        <td>{$row['nim']}</td>
        <td>{$row['nama']}</td>
        <td>{$row['jurusan']}</td>
        <td><a href='?delete={$row['nim']}'>Delete</a>
        <a href='?update={$row['nim']}'>Update</a></td>
        </tr>
        ";
        $no++;
    }
} else {
    echo "0 results";
}
echo "</table>";
// Panggil Function
formMahasiswa();
tampilTabel($connect);