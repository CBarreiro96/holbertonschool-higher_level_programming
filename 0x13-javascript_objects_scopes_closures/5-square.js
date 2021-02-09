#!/usr/bin/node
/*
  Whit the function require include modules
  that exist in separate files (4-rectangle)
  ========= Class Square ==================
  * Class square inherits from Class rectangle
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
