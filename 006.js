let ssq = 0;
let sqs = 0;
for (let i = 1; i < 101; i++) {
    ssq += i * i;
    sqs += i
}

console.log(sqs * sqs - ssq);