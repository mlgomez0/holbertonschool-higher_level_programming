#!/usr/bin/node
/* script that writes a string to a file */

const args = process.argv;
const file = args[2];
const content = args[3];
const fs = require('fs');
fs.writeFile(file, content, 'utf-8', function (err) {
  if (err) {
    return console.error(err);
  }
});
