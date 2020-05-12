#!/usr/bin/node
/* script that reads and prints the content of a file */

const args = process.argv;
const file = args[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  process.stdout.write(data);
});
