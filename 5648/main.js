const input = require("fs").readFileSync(process.platform == 'linux' ? "/dev/stdin" : process.argv.at(2)).toString().trim();
console.log(
    input.replaceAll("\n"," ").trim().split(" ").slice(1).filter(a=>a).map(el=>+Array.from(el).reverse().join("").trim())
    .sort((a,b)=>a-b).join("\n")
);