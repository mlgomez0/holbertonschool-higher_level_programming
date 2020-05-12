#!/usr/bin/node
/*  script that prints the title of a Star Wars movie
    where the episode number matches a given integer.
 */

const args = process.argv;
const parsed = parseInt(args[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
const request = require('request');
if (!isNaN(parsed)) {
  request(url, function (error, response, body) {
    if (error) {
      return console.log(error);
    }
    console.log(JSON.parse(body).title);
  });
}
