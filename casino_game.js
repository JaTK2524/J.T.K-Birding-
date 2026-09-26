let money = Number(localStorage.getItem("winnings")) || 100;

const play = document.getElementById("play");
const guess = document.getElementById("guess");
const MoneyDisplay = document.getElementById("money");
const bet = document.getElementById("bet");
const resultDisplay = document.getElementById("result")

MoneyDisplay.textContent = "Coins: " + money;

play.addEventListener("click", function() {
     const choices = ["Heads", "Tails", "Third-Face"];
     const result = choices[Math.floor(Math.random() * choices.length)];
     
     const chosenGuess = guess.value;
     const chosenBet = Number(bet.value);
     
     if (chosenBet <= 0 || chosenBet > money) {
         resultDisplay.textContent = "Please place a valid bet.";
         return;
         
         }
     if (result === chosenGuess) {
         money += chosenBet;
         
         resultDisplay.textContent  = 
           "You won! The result was " + result + ". You receive " + chosenBet + " coins!"; 
           } else {
                    money -= chosenBet;
                    
                    resultDisplay.textContent = "You lost! The result was " + result + ". You lose " + chosenBet + " coins."
                    }
           
           MoneyDisplay.textContent = "Coins: " + money;
           
           localStorage.setItem("winnings", money);
           
    });  
    const audio = document.getElementById("casinoMusic")
    const button = document.getElementById("muteButton")
    
    button.addEventListener("click", function() {
     audio.muted = !audio.muted
     
     if (audio.muted) {
         button.textContent = "🔇";
         } else {
                  audio.play()
                  button.textContent = "🔊";
                   }
                    });
         
