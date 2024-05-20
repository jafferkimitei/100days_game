const randomNumber = Math.floor(Math.random() * 100) + 1;
let guesses = 0;
let guessesRemaining = 10; // Adjustable for difficulty

const submitButton = document.getElementById('submitButton');
const guessInput = document.getElementById('guessInput');
const messageElement = document.getElementById('message');
const difficultySelect = document.getElementById('difficulty');
const resetButton = document.getElementById('resetButton');

difficultySelect.addEventListener('change', function() {
  const difficulty = difficultySelect.value;
  if (difficulty === 'easy') {
    guessesRemaining = 10;
  } else if (difficulty === 'medium') {
    guessesRemaining = 7;
  } else {
    guessesRemaining = 5;
  }
});

submitButton.addEventListener('click', function() {
  guesses++;
  guessesRemaining--;
  const guess = parseInt(guessInput.value);

  if (guess === randomNumber) {
    messageElement.textContent = `Congratulations! You guessed the number in ${guesses} guesses!`;
  } else if (guess > randomNumber) {
    messageElement.textContent = `Too high! You have ${guessesRemaining} guesses remaining.`;
  } else {
    messageElement.textContent = `Too low! You have ${guessesRemaining} guesses remaining.`;
  }

  guessInput.value = ''; // Clear the guess input field

  // Check if guesses are depleted or number is guessed
  if (guessesRemaining === 0 || guess === randomNumber) {
    submitButton.disabled = true; // Disable submit button if out of guesses
  }
});

resetButton.addEventListener('click', function() {
  randomNumber = Math.floor(Math.random() * 100) + 1;
  guesses = 0;
  messageElement.textContent = '';
  submitButton.disabled = false; // Re-enable submit button if disabled
  guessesRemaining = difficultySelect.value === 'easy' ? 10 : (difficultySelect.value === 'medium' ? 7 : 5);
});
