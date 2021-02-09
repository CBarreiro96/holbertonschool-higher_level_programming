#!/usr/bin/node
/*
====================== WRITE IN A FILE =========================
In this exercise you need to write in a file in this case you need
to use the method writeFile and remeber the argument string that you need
to write in the file
*/
const argv = process.argv;
const fs = require('fs'); // File system
const fileName = argv[2];
const string = argv[3];
fs.writeFile(fileName, string, 'utf-8', function (err) {
  if (err) return console.log(err);
});
