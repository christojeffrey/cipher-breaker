// read from cipher js

import { cipher } from "./cipher.js";

// create a dictionary of the frequency of each letter

let frequency = {};

cipher.forEach((letter) => {
  // if the letter is not in frequency, create one and set its value to 1
  if (!frequency[letter]) {
    frequency[letter] = 1;
  } else {
    // if the letter is in frequency, add 1 to its value
    frequency[letter]++;
  }
});

console.log(frequency);
