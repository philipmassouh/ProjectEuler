function perfSquareAndAddsUp(a, b, c, sum) {
    return c % 1 === 0 && a + b + c == 1000;
}

function sol1() {
    for (let a = 1; a < 1000; a++) {
        for (let b = a; b < 1000; b++) {
            c = Math.sqrt(a*a + b*b)
            if (c % 1 == 0 && a + b + c == 1000) {
                return a*b*c
            }
        }
    }
    return (0,0,0)
}

console.log(sol1())
