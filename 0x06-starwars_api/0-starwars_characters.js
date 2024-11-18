#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
console.log('Movie ID:', movieId); // Debugging line

if (!movieId) {
  console.log('Please provide a Movie ID.');
  process.exit(1);
}

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
    return;
  }

  const filmData = JSON.parse(body);

  console.log('Film Data:', filmData); // Debugging line

  if (filmData.detail && filmData.detail === 'Not found') {
    console.log('Movie not found!');
    return;
  }

  console.log(`Characters from: ${filmData.title}`);

  const charactersUrls = filmData.characters;

  charactersUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

