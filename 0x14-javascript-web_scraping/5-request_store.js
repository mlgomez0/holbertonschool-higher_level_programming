#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file */

const args = process.argv;
const url = args[2];
const path = args[3];
const fs = require('fs');
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(path, body, 'utf-8', function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
