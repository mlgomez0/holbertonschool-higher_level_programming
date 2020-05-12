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
  let count = 1;
  for (let i = 0; i < data.characters.length; i++) {
    let charList = data.characters[i];
    console.log(charList);
    request(charList, function (error, response, body) {
      console.log(charList);
      const dataCharIdList = data.characters[i].split('/');
      const dataCharId = dataCharIdList[dataCharIdList.length - 2]
      if (error) {
        return console.log(error);
      }
      const dataChar = JSON.parse(body);
      console.log(dataCharId, count);
      if (dataCharId === count) {
        console.log(dataChar.name);
      }
      count = count + 1;
    });
  }
});
