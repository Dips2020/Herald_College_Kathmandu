// ⬇️1
// let a = 6;
// let b = 5;

// let sum = a + b;
// console.log("The sume of two numbers:" + sum)

// ⬇️2
// let r = 4;
// const pie = 3.14;
// let circumference_circle = 2 * pie * 4;
// console.log("datatype:" + typeof (r));
// console.log("The circumference of circle:" + circumference_circle)

// ⬇️3
// let b = prompt("Enter base of a traingle: ");
// let h = prompt("Enter height of a traingle: ");

// let area = 1 / 2 * b * h;
// alert("The area of triangle is:" + area);
// console.log(area)

//⬇️4
// let a = prompt("Enter length of the square: ")
// let area = a ** 2
// let cube = a ** 3
// alert("The area of square: " + area)
// console.log(area)
// alert("The cube of square: " + cube)
// console.log(cube)

//⬇️5
// let age = prompt("Enter the age: ")
// if (age >= 18) {
//     alert("You can vote");
//     console.log("He is allowed");
// }
// else {
//     alert("You can't vote")
//     console.log("Not allowed")
// }

//⬇️6 if else concept
// let marks = prompt("Enter the marks: ")
// if (marks >= 90) {
//     alert("Your grade is A+");
//     console.log("He is awesome");
// }
// else if (marks >= 80) {
//     alert("Your grade is A");
//     console.log("Excellent!");
// }
// else if (marks > 60 && marks <= 79) {
//     alert("Your  grade is B");
//     console.log("Good!!");
// }
// else if (marks >= 40) {
//     alert("Your are passed");
//     console.log("Do better");
// }
// else if (marks < 40) {
//     alert("Your are fail grade D");
//     console.log("Failed");
// }

//⬇️7
// // difference in global variable and local variable
// //  let difference
// function num() {
//     let a = 6;
//     if (true) {
//         let a = 5;
//         console.log(a);
//     }
//     console.log(a);
// }
// num()
// // var defference
// function num1() {
//     var b = 7;
//     if (true) {
//         var b = 9;
//         console.log(b);
//     }
//     console.log(b);
// }
// num1()

// ⬇️ 8 loop concept
// let i;
// for (i = 1; i <= 50; i++) {
//     if (i % 2 == 0) {
//         console.log(i);
//     }

// }

// ⬇️9 loop cube inside function
// function num() {
//     let i;
//     for (i = 1; i <= 50; i++) {
//         let cube = i ** 3
//         console.log("Cube:" + cube)
//     }
// }
// num()

// ⬇️10 parameter
function multiply(a, b) {
    let multiply = 1;
    multiply = a * b
    console.log(multiply)
}
multiply(2, 3);
multiply(4, 3);