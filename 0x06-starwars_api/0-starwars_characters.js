#!/usr/bin/node
/**
 * Script that prints all characters of a Star wars movie.
 *
 * Usage:
 *      ./0-starwars_characters.js <Movie ID>
 */

const request = require('request');
const starWarsApi = 'https://swapi-api.alx-tools.com/api/';
const movieId = process.argv[2];

if (process.argv.length === 3) {
  const people = `${starWarsApi}people`;

  request(people, (error, response, body) => {
    if (error) throw error;
    console.log('statusCode:', response && response.statusCode);
    console.log('Body:', parseInt(body));
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
}
