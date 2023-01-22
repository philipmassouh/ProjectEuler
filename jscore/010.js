/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

// we can use a sieve since the problem has an upper bound
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

let sum = 0n;

for (let a of primeGenerator(2000000)) { 
    sum += BigInt(a);
}

console.log(sum);