#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.error('Movie ID is required');
  process.exit(1);
}

// Star Wars API URL for films
const filmsUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie data
request(filmsUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Check if movie data contains characters
  if (!movieData.characters) {
    console.error('No characters found in the movie data');
    process.exit(1);
  }

  // Function to fetch character data and print the name
  const fetchCharacter = (url, callback) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        process.exit(1);
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      callback();
    });
  };

  // Fetch and print each character
  const fetchAllCharacters = (urls) => {
    if (urls.length === 0) return;

    const url = urls.shift();
    fetchCharacter(url, () => fetchAllCharacters(urls));
  };

  fetchAllCharacters(movieData.characters);
});