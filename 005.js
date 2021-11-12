let x = 20;

while (1) {

    let success = true;

    for (let i = 19; i > 1; i--) {

        if (x % i != 0) {

            success = false;

            break;
        }
    }

    if (success) {
        break;
    }
    
    x += 20;
}

console.log(x);

