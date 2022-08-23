const { exec } = require("child_process");

const app = require('express')();
const PORT = 8080;

const fs = require('fs');
let file;
let array;

const getObject = () => {
    file = fs.readFileSync('API/request.txt', 'utf8');
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

setInterval(() => {
    console.log("new word on the way");
    exec("python3 ./generator/main.py", (error, stdout, stderr) => {
        if (error) {
            console.log(error);
            return;
        }
        if (stderr) {
            console.log(stderr);
            return;
        }
        console.log(stdout);
    });
}, 30000);

app.get('/word', (req, res) => {
    res.status(200).send(getObject());
});

app.listen(
    PORT,
    () => console.log(`it's alive on http://localhost:${PORT}/word`)
);