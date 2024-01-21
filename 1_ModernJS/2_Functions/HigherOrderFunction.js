// Higher-Order Function
function operation(a, b, callback) {
    return callback(a, b);
}
    
function multiply(a, b) {
    return a * b;
}
    
console.log(operation(5, 3, multiply)); // Output: 15