#!/usr/bin/node
const SquarePrime = require('./5-square.js');
class Square extends SquarePrime {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
