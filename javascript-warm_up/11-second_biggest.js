#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  const unique = [...new Set(numbers)];
  unique.sort((a, b) => b - a);
  console.log(unique[1]);
}
