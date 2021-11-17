function* infintePrimeGenerator() {
    // 2 is the only even prime number 
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

let ipg = infintePrimeGenerator();

for (let i = 0; i < 10001; i++) {
    prime = ipg.next().value;
}

console.log(prime);