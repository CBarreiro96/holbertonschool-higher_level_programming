#!/usr/bin/node
/*
================= STATUS CODE ========================
script that display the status code of a GET request.
In this exercise require the method request
*/
const argv = process.argv;
const url = argv[2];
const request = require('request');
request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
