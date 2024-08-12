const number=[1,2,3,4,5];
console.log(number);
console.log(number.length);
number.shift();
console.log(number);
number.pop();
console.log(number);
number.push(21);
console.log(number);
for(const i of number){
    console.log(i);
}

fruits=['Apple','Banana','orange'];
for( const i of fruits){
    console.log(i);
}

const n=10;
while(n<10){
    console.log("Looping");
}