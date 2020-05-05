#!/usr/bin/node
/* script that prints the addition of 2 integers */

const args = process.argv;
const inta = parseInt(args[2]);
const intb = parseInt(args[3]);

function add (a, b) {
  console.log(a + b);
}
add(inta, intb);
