function fetchData() {
    return new Promise((resolve, reject)=> {
        setTimeout(()=> {
            const data = "";
        if(data) {
            resolve(data);
        } else {
            reject("Data Tidak Ada");
        }
        }, 1000);
    });
}
//memanggil promise
fetchData()
    .then((data) =>{
        console.log(data);
})
.catch((error) => {
    console.error(`Error: Unable to fetch data: ${error}`);
});