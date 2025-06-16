const fibonacci = function(n) {
    let num = Number(n);
    if (num >= 2) {
        return fibonacci(n-1) + fibonacci(n-2);
    } else if ( num < 0 ) {
        return "OOPS";
    } else {
        return num;
    }
    
};

// Do not edit below this line
module.exports = fibonacci;