function* fibGenerator() {
    let [a,b] = [0,1];
    while (true) {
        yield a;
        [a,b] = [b, a + b];
    }
}

const fib = fibGenerator();
let sum = 0;

while ((b = fib.next().value) < 4000000) {
    sum += b % 2 == 0 ? b : 0;
}

console.log(sum)

