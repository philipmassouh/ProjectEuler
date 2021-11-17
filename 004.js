
function isPalindrome(number) {
    return number == number.toString().split('').reverse().join('')
}

let largest = 0;
for (let i = 999; i > 99; i--) {
    for (let j = i - 1; j > 100; j--) {
        let product = i * j;
        if (product > largest && isPalindrome(product)) {
            largest = product;
        }
    }
}

console.log(largest);
