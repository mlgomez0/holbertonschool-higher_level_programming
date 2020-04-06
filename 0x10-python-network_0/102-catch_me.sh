#!/bin/bash
#Script catches the error message an put "You got me!"
curl -s -o /dev/null -w "You got me!" "0.0.0.0:5000/catch_me"
