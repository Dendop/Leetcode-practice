class Media {
  constructor(title){
    this._title = title;
    this._isCheckedOut = false;
    this._ratings = [];
  }
  get title(){
    return this._title;
  }
  get isCheckedOut(){
    return this._isCheckedOut;
  }
  get ratings(){
    return this._ratings;
  }
  set isCheckedOut(con){
    this._isCheckedOut = con;
  }
  toggleCheckedOutStatus(con) {
    this._isCheckedOut = !this._isCheckedOut;
  }
  getAverageRating() {
    if (this._ratings.length === 0) return 0;
    let average = (this._ratings.reduce((acc,curr) => acc + curr)) / this._ratings.length;
    return `Average: ${average}`;
  }
  addRating(num) {
    this._ratings.push(num);
  }
};

const myCD = new Media('Eminen');
myCD._ratings = [4,3,2,4]

console.log(myCD.getAverageRating())
console.log(myCD)

myCD.addRating(9);
console.log(myCD.ratings);

