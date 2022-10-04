#!/usr/bin/node
const x = process.argv[2];
for (let i = 0; i < x; i++) {
  console.log('C is fun');
} if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
