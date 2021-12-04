sum = 0;
for (v of BigInt(Math.pow(2,1000)).toString()) {
    sum += parseInt(v)
}

console.log(sum)
