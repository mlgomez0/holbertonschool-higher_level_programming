#!/usr/bin/node
/*  script that prints the number of movies where
    the character "Wedge Antilles , ID 18" is present.
 */

const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const allTitles = JSON.parse(body).results;
  let count = 0;
  for (const i in allTitles) {
    const allChars = allTitles[i].characters;
    for (let idx = 0; idx < allChars.length; idx++) {
      if (allChars[idx] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
