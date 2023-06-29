function playGame(userChoice) {
    const loader = document.getElementById('loader');
    const resultCard = document.querySelector('.result-card');
    const resultMessage = resultCard.querySelector('.result-message');

    // to show the loading
    loader.style.display = 'block';

    // Hide the result card
    resultCard.classList.remove('show');



    // Delay the result calculation for 1.5 second
    setTimeout(function () {
        const result = determineWinner(userChoice, computerChoice);

        // Update the result message
        resultMessage.textContent = result;

        // Hide the loading
        loader.style.display = 'none';

        // Show the result card
        resultCard.classList.add('show');
    }, 1500);
}



// Generate a random choice for the computer
function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
}
// Generate a random choice for the computer
const computerChoice = getComputerChoice();

let computerMessage = `Computer played: ${computerChoice},Computer Win!`;
let userMessage = `Computer played: ${computerChoice}, You Win! `



function determineWinner(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
        return "It's a draw!";
    } else if (
        (userChoice === 'rock' && computerChoice === 'paper') ||
        (userChoice === 'paper' && computerChoice === 'scissors') ||
        (userChoice === 'scissors' && computerChoice === 'rock')
    ) {
        return `Computer played: ${computerChoice}, Computer Wins!`;
    } else {
        return `Computer played: ${computerChoice}, You Win!`;
    }
}


// Determine the winner based on the choices
// function determineWinner(userChoice, computerChoice) {
//     if (userChoice === computerChoice) {
//         return "It's a draw!";
//     } else {
//         switch (userChoice) {
//             case 'scissors':
//                 return computerChoice === 'rock' ? `${computerMessage} \n` : `${userMessage}!`;
//             case 'paper':
//                 return computerChoice === 'scissors' ? `${computerMessage}` : `${userMessage}!`;
//             case 'rock':
//                 return computerChoice === 'paper' ? `${computerMessage}` : `${userMessage}!`;
//             default:
//                 return 'Invalid choice. Please try again!';
//         }
//     }
// }