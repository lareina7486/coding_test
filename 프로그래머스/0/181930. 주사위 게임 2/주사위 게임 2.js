function solution(a, b, c) {
    let triPlus = a + b + c;
    let triPow = a**2 + b**2 + c**2;
    let triTriple = a**3 + b**3 + c**3;
    if (a === b && b === c) {
        return triPlus * triPow * triTriple;
    }

    if (a === b || b === c || a === c) {
        return triPlus * triPow;
    }

    return triPlus;
}