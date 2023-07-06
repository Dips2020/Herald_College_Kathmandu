let winMsg = "!! Victory !!";
let loseMsg = "!! Crushing Defeat !!";
let tieMsg = "!! Tie !!";
let moveList = ["rock", "paper", "scissors"];


// this is for loading symbol
const loadingSymbol = document.querySelector("#loader");
// this is for result card
const resultCard = document.querySelector("#result");
// this is for result message
const resultMsg = document.querySelector("#result_msg");
const tryAgainPart = document.querySelector("#tryAgain")
const mainContainer = document.querySelector("#mainContainer");


function button_click(userChoice) {
    tryAgainPart.style.display = "block"
    loadingSymbol.style.display = "block";
    resultCard.style.display = "none";
    // result card will appear after 1.5 seconds
    setTimeout(function () {
        loadingSymbol.style.display = "none";
        resultCard.style.display = "flex";

        // random move for the computer
        let computerChoice = moveList[Math.floor(Math.random() * moveList.length)];

        console.log("User's choice: " + userChoice);
        console.log("Computer's choice: " + computerChoice);

        // choosing the winner
        let result = [];
        if (userChoice === computerChoice) {
            result = tieMsg;
        } else if (
            (userChoice === "rock" && computerChoice === "scissors") ||
            (userChoice === "scissors" && computerChoice === "paper") ||
            (userChoice === "paper" && computerChoice === "rock")
        ) {
            result = winMsg;
        } else {
            result = loseMsg;
        }

        // Displaying the choices of user and computer
        // resultMsg.textContent = `You played: ${userChoice}, Computer played: ${computerChoice}. ${result}`;
        // !-----⬇️
        resultMsg.innerHTML = `<span style="font-size:30px;">You played : <span style="color: #6f0000; font-size:30px;">${userChoice}</span></span> <br><span style="font-size:30px;">Computer played: <span style="color: #6f0000; font-size:30px;">${computerChoice}</span> </span> <br><span style="color: #200122; font-size:40px;">${result}</span>`;
    }, 1500);

    // for try again part
    function tryAgain() {
        resultCard.style.display = "none";
        mainContainer.style.display = "flex";
    }
    document.querySelector("#tryAgain").addEventListener("click", tryAgain);
}


