#!/usr/bin/node
/*  searches the second biggest integer in the list of arguments */

const args = process.argv;
const newArgs = args.slice(2).sort();
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(newArgs[newArgs.length - 2]);
}
