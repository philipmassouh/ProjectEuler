function* primeGenerator(topBound) {
    const isPrime = new Array(topBound).fill(true);
    for (let i = 2; i < topBound; i++) {
        if (isPrime[i]) {
            yield i;
            for (let j = 2; j < topBound; j++) {
                if (j % i == 0) {
                    isPrime[j] = false;
                }
            }
        }
    }
}

let target = 600851475143;
let sieveMax = Math.ceil(Math.sqrt(target));

const primeGen = primeGenerator(sieveMax);
let largestPrime = 2;
let nextPrime;

while (!primeGen.next().done) {
    if (target % (nextPrime = primeGen.next().value) == 0) {
        largestPrime = nextPrime;
    }
}

console.log(largestPrime);
