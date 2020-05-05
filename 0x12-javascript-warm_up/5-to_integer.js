#!/usr/bin/node
/* prints  if the first argument can be converted to an integer */

const args = process.argv;
const parsed = parseInt(args[2]);
if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsed);
}
