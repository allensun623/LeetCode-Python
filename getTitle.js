'use strict';

const { time } = require('console');
const fs = require('fs');
const https = require('https');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function () {
  inputString = inputString.split('\n');
  main();
});

function readLine() {
  return inputString[currentLine++];
}

async function getMovieList(year) {
  // write your code here
  let movies = [];
  const url = `https://jsonmock.hackerrank.com/api/movies?Year=${2015}`;

  let url = 'https://jsonmock.hackerrank.com/api/movies?Year=2015';

  https
    .get(url, (res) => {
      body = '';

      res.on('data', (chunk) => {
        body += chunk;
        chuck.map((item) => time.Title);
      });

      res.on('end', () => {
        console.log(JSON.parse(body));
      });
    })
    .on('error', (error) => {
      console.error(error);
    });
  return movies;
}

async function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const year = readLine().trim();

  const results = await getMovieList(year);

  if (results.length > 0) {
    for (const result of results) {
      ws.write(`${result}\n`);
    }
  } else {
    ws.write('No Results Found');
  }

  ws.end();
}
