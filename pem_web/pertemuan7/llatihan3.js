//control flow
//if else
let age = 20;
if (age >= 20) {
    console.log("you're eligible to vote");
}else{
    console.log("you're not eligible to vote");
}

//ternary operator
let vote =
    age >= 20? "you're eligible to vote" : "you're not eligible to vote";
console.log(vote);

let hours = new Date().getHours();

let Hours = new Date().getHours();
let discount = hours <= 1 ? "20%"
             : hours <= 3 ? "15%" 
             : "0%";
console.log(discount);


//switch
switch (day){
    case 0:
        console.log("sunday");

    case 1:
        console.log("monday");

    case 2:
        console.log("tuesday");
    case 3:
        console.log("wednesday");
    case 4: 
        console.log("thursday");
    case 5:
        console.log("friday");
    case 6:
        console.log("saturday");
        break;
    default:
        console.log("invalid day");
}