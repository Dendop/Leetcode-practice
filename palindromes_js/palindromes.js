const palindromes = function (str) {
    let low_str = str.toLowerCase();
    low_str = low_str.replace(/[!.? ,]/g,"");
    let new_str = low_str.split('').reverse().join('');
    return new_str === low_str;
};

// Do not edit below this line
module.exports = palindromes;