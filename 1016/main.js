const input = require("fs").readFileSync(process.platform == 'linux' ? "/dev/stdin" : process.argv.at(2)).toString().trim();
const [min, max] = input.split(" ").map(el=>+el);
const nums = [];

for (let i=min; i<=max; ++i) {
    for(let num=2; num<=Math.sqrt(i);++num) {
        
    }
    console.log(i);
}