#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const args = process.argv.slice(2).map(Number);
  const srtargs = args.sort((a, b) => b - a);
  console.log(srtargs[1]);
}
