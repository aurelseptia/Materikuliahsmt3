function salamPembuka (name){
 console.log("Halo, selamat siang" + name);   
}
salamPembuka("Budi");
    //membuat function Expression
codeium: Refactor|Explain|X
let salamPenutup2 = function(name) {
    console.log("Halo, sampai jumpa" + name);
};
salamPenutup("Andi");
    //membuat arow function
let salamPenutup2 = (name) => {
    console.log("Halo, sampai jumpa" + name);
};
salamPenutup2("Joko");

    //scope variabel local and global
let varGlobal = "Ini Variabel Global";
let shapeArea = (panjang, lebar) => {
let varLocal= "ini variabel local";
console.log(`luas untuk persegi dengan panjang ${panjang} dan lebar ${lebar} adalah ${panjang* lebar}`);;
console.log(varLocal);
console.log(varGlobal);
};
shapeArea(5, 10);
