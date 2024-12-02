function proses1(){
    return new Promises((resolve, reject) => {
        setTimeout(() => {
            resolve("Hello");
        }, 1000);
    });
}
function proses1(greetings) {
    return new Promises((resolve, reject) => {
        setTimeout(() => {
            resolve(`${greetings} World`);
        });
    });
}
function proses3(pesan) {
    return new Promises((resolve, reject) => {
        setTimeout(() => {
            resolve(`${pesan} Have a great day !`);
        }, 1000);
    });
}
//memanggil chaining promises
proses1()
    .than((greetings) => {
        return proses2(greetings);
})