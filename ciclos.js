let a= 0;
let repeticiones = [1,3,1,7,8,3];

// *while

while( repeticiones.includes(a)) {

  console.log(`${a++}`);
}

// *do while

do{
  console.log(`${a++}`);
}while(a<=10);



for (let y = 0; y <= 100; y+=3) {
  console.log(y);}

for (let i = 100; i >= 0; i-=3) {
 console.log(i);}





// *suma ******
let res = 0;
for(let x = 0; x <= 15; x++){
  res = res+x;
  console.log(`${x}+${res-x}=${res}`);
}
console.log(res);

let res1 = 0;
let x1 = 0;

do {
  res1 = res1 + x1;
  console.log(`${x1}+${res1-x1}=${res1}`);
  x1++;
} while (x1 <= 15);

console.log(res);