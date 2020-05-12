#!/usr/bin/node
/*  script that prints all characters of a Star Wars movie.
    with a given movie ID.
 */

const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const data = JSON.parse(body);
  for (let i = 0; i < data.characters.length; i++) {
    request(data.characters[i], function (error, response, body) {
      if (error) {
        return console.log(error);
      }
      const dataChar = JSON.parse(body);
      console.log(dataChar.name);
    });
  }
});
