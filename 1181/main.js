const fs = require("fs");
const filePath = "/dev/stdin";
// const filePath = "1181/input.txt";

Array.from(new Set(fs.readFileSync(filePath).toString().split('\n').slice(1, -1))).sort((a, b)=>(a.length-b.length || (a > b ? 1 : a < b ? -1 : 0))).forEach(el=>el&&console.log(el));