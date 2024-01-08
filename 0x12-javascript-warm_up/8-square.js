#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const n = parseInt(process.argv[2]);
  let row = '';
  let i = 1;
  while (i <= n) {
    row += 'X';
    i++;
  }
  i = 1;
  while (i <= n) {
    console.log(row);
    i++;
  }
}
