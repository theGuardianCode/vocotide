const app = require('express')();
const PORT = 8080;

const fs = require('fs');
let file;
let array;

const getObject = () => {
    file = fs.readFileSync('request.txt', 'utf8');
    array = file.split('\n');

    let definitions = [];
    for (let i = 1; i < array.length; i++) {
        definitions.push(array[i]);
    }

    let response = {
        word: array[0],
        definitions: definitions
    };
    return response;
};

app.get('/word', (req, res) => {
    res.status(200).send(getObject());
});

app.listen(
    PORT,
    () => console.log(`it's alive on http://localhost:${PORT}/word`)
);