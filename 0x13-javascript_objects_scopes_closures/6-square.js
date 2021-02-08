#!/usr/bin/node
/*
   class Square that defines a square
   and inherits from Square of 5-square.js
*/
const Square5 = require('./5-square');

class Square extends Square5 {
  /*
    method charPrint(c) that prints
    the rectangle using the character c
  */
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
