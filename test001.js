let number = 8
let fill = []
const summation = (num) => {
    do {
        fill.push(num);
        num--;
    } while(num != 0)
    return fill.reduce((acc, val) => acc+ val,0);
};

console.log(summation(number));