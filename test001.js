function findNextSquare(sq) {
  let start = 1;
  let result;
  while ((start * start) < sq) {
    start++;
  }
  if ((start * start) > sq) {
    return -1;
  } else {
        start += 1;
        return start *  start
    }
  
  
}
let magic = findNextSquare(121);
console.log(magic);