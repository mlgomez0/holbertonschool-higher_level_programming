#!/usr/bin/node
/*  script that prints the number of movies where
    the character "Wedge Antilles , ID 18" is present.
 */

const args = process.argv;
const url = args[2];
const request = require('request');
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const allTitles = JSON.parse(body);
  for (let ti = 0; ti < allTitles.results.length; ti++) {
    for (let chater = 0; chater < allTitles.results[ti].characters.length; chater++) {
      if (allTitles.results[ti].characters[chater] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
