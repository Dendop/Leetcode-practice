const add = function(n1,n2) {
	let result = n1 + n2;
    return result;
};

const subtract = function(n1,n2) {
	let result = n1 - n2;
    return result;
};

const sum = function(arr) {
    let result = arr.reduce((acc, curr) => acc + curr, 0);
    return result;
};

const multiply = function(arr) {
    let result = 1
    for (let i = 0; i < arr.length; i++) {
        result *= arr[i];
    }
    return result;
};

const power = function(n1,n2) {
	let result = n1 ** n2;
    return result;
};

const factorial = function(n) {
	let result = 1;
    for (let i = n; i > 0; i--){
        result *= i;
        
    }
    return result;
};

// Do not edit below this line
module.exports = {
  add,
  subtract,
  sum,
  multiply,
  power,
  factorial
};