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
  const charId = '18';
  for (const i in allTitles) {
    const allChars = allTitles[i].characters;
    for (let idx = 0; idx < allChars.length; idx++) {
      const cId = allChars[idx].split('/');
      if (cId[cId.length - 2] === charId) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
