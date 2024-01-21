// Write a JavaScript function that generates all combinations of a string.
function substrings(str1) {

    var array1 = [];
  
    for (var x = 0, y = 1; x < str1.length; x++, y++) {
      array1[x] = str1.substring(x, y);
    }
  
    // Initialize an empty array to store all combinations
    var combi = [];
    var temp = "";
    
    // Calculate the total number of combinations using the formula 2^n
    var slent = Math.pow(2, array1.length);
  
    // Generate all combinations using bitwise operations
    for (var i = 0; i < slent; i++) {
      temp = "";
      
      // Iterate through each character in the array
      for (var j = 0; j < array1.length; j++) {
        // Check if the j-th bit of the binary representation of i is set
        if (i & Math.pow(2, j)) {
          // If set, append the corresponding character to the temporary string
          temp += array1[j];
        }
      }
  
      // If the temporary string is not empty, add it to the combinations array
      if (temp !== "") {
        combi.push(temp);
      }
    }
  
    // Log the generated combinations, joined by newline, to the console
    console.log(combi.join("\n"));
  }
  
  // Call the substrings function with the input string "dog"
  substrings("dog"); 
  