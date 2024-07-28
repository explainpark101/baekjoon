function range(size, startAt = 0) {
    return [...Array(size).keys()].map(i => i + startAt);
}
const fs = require("fs");
// const filePath = "/dev/stdin";
const filePath = "./testCase.txt";
const [N, L] = fs.readFileSync(filePath).toString().split(" ").map(chr=>+chr);
// L : min length / N : sum

const NisOdd = N & 1;
const LisOdd = L & 1;

if (NisOdd && LisOdd) {

}