function getSequenceLength(start) {
    value = start;
    l = 1
    while (value > 1) {
        l += 1
        if (value % 2 == 0) {
            value /= 2;
        } else {
            value = (3 * value) + 1;
        }
    }
    return l;
}

longestChain = [0,0]

for (let i = 0; i < 1000000; i++) {
    l = getSequenceLength(i);
    if (l > longestChain[1]) {
        longestChain = [i, l]
    }
}

console.log(longestChain);