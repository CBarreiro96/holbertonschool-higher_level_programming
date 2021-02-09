#!/usr/bin/node
/*
====================== API STARWARS ==============================
It is a script that prints the title of a Star Wars
movie where the episode number matches a given integer.

You need to visit the link where this API was read.
https://swapi-api.hbtn.io/
*/
const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2] + '/';

request(url, function (error, response, body) {
  if (error === null) {
    const rbody = JSON.parse(body);
    console.log(rbody.title);
  } else {
    console.log(error);
  }
});
