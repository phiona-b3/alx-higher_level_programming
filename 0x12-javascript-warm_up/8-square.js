#!/usr/bin/node
const x = process.argv[2];
for (let i = 0; i < x; i++) {
  console.log('X'.repeat(x));
} if (isNaN(x)) {
  console.log('Missing size');
}
