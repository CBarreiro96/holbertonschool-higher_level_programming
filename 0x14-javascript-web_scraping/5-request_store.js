#!/usr/bin/node
\*
============== Loripsum ===================
script that gets the contents of a webpage
and stores it in a file.
*/
const argv = process.argv;
const url = argv[2];
const fileName = argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(fileName, body, 'utf8', function (err) {
      if (err) return console.log(err);
    });
  }
});
