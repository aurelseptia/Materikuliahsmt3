// // membuat loops dengan for
for(let i = 10; i > 1; i--){
    //template literal string
console.log(`ini perulangan ke ${i + 1}`);
console.log("ini perulangan ke " + (i + 1));
console.log("ini perulangan ke ", i);
}
for (let i = 0; i < 10; i++) {
    // template literal string
console.log(`ini perulangan ke $(i + 1)`);
console.log("ini perulangan ke", i);
console.log("ini perulangan ke", i);
}
    //loops dengan while
    let j = 1;
while ( j < 10){
    console.warn(`ini perulangan ke ${j}`);
    j++;
}
    //contoh menampilkan data mahasiswa
let mahasiswa = ["Budi", "Andi", "Jokoo", "Joni"];
for(let i = 0; i < mahasiswa.length; i++){
    console.log(mahasiswa[i]);
}

