const start = performance.now()

let count = 100_000_000;

while(count--){

}

const end = performance.now();

console.log(`Javascript: Took ${(end - start) / 1000} seconds`);
console.log(`Javascript: ${count}`)