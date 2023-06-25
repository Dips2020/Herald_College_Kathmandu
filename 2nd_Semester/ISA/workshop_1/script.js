

// var rate = parseFloat(document.getElementById("rate").value);
// var output = document.getElementById("rateval");

// // Set the initial value of the output element
// output.innerHTML = rate.value;

// // Add an event listener to update the output element when the slider value changes
// slider.oninput = function () {
//     output.innerHTML = this.value;
// };
// function compute() {

//     var principal = parseFloat(document.getElementById("principal").value);



//     var years = parseFloat(document.getElementById("years").value);


//     var interest = (principal * rate * years) / 100;

//     document.getElementById("result").textContent = "Interest: " + interest.toFixed(2);

//     result.innerHTML =
//         "If you deposit <mark>" +
//         principal +
//         "</mark>,<br>at an interest rate of <mark>" +
//         rate +
//         "%</mark>.<br>You will receive an amount of <mark>" +
//         amount +
//         "</mark>,<br>in the year <mark>" +
//         futureYear +
//         "</mark>.";
// }


var slider = document.getElementById("rate");
var output = document.getElementById("rateval");

output.innerHTML = slider.value;

slider.oninput = function () {
    output.innerHTML = this.value;
};

function compute() {
    var principal = parseFloat(document.getElementById("principal").value);
    var years = parseFloat(document.getElementById("years").value);

    // Convert the rate from percentage to decimal
    var rate = parseFloat(output.innerHTML) / 100;
    if (principal <= 0.0 || years <= 0.0 || rate <= 0) {
        alert("Principal cannot be zero or negative \n Years cannot be zero or negative \n Rate cannot be zero or negative")
    }

    var interest = principal * rate * years;

    var result = document.getElementById("result").textContent = "Interest: " + interest.toFixed(2);
    console.log(result);
}