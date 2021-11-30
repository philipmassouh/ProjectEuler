// pretty slow later on, we can blindly choose sieve top bound but I don't like that
function* infintePrimeGenerator() {
    // 2 is the only even prime number, we iterate on odds
    yield 2;

    let i = 3;
    let x;
    while (true) {
        x = 1;

        do 
            x += 2;
        while (i % x != 0 && x < i)

        if (x == i)
            yield i;

        i += 2;
    }
}

const primeGen = infintePrimeGenerator();
let nextPrime;

for (let i = 0; i < 10001; i++) {
    nextPrime = primeGen.next()
}

console.log(nextPrime.value)
