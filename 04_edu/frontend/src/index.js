import axios from 'axios';

let res = axios.get(`/api/subjects/`);
console.log(res);

fetch(`/api/subjects/`)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });
