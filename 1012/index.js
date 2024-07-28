const fs = require("fs");
// const filePath = "/dev/stdin";
const filePath = "./testCase.txt";
const inputs = fs.readFileSync(filePath).toString().split("\n").map(line=>line.split(" ").map(el=>+el));
const [ TestCase ] = inputs[0];
let i=1;
for(const tc of Array(TestCase).keys()){
    const [width, height, cabbageCount] = inputs[i++];
    const cabbages = inputs.slice(i, i+cabbageCount);
    i += cabbageCount;
}