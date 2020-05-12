#!/usr/bin/node
/* script that display the status code of a GET request.
   doc used : https://github.com/request/request
 */

const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
