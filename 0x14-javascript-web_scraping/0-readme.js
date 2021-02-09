#!/usr/bin/node
/*
==================== README =========================
To  interact with your computer and read file, you
need to use require and the method readFile.
In this case the exercise is about reads and prints
the content of a file.

*/
const argv = process.argv;
const fs = require('fs');// File System module
const fileName = argv[2];
fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
});
