#!/usr/bin/node
let maxi = 0;
const arg = process.argv.slice(2);
if (arg.length > 1) {
  arg.sort();
  maxi = arg[arg.length - 2];
}
console.log(maxi);
