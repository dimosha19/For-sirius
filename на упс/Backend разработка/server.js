// server.js
const express        = require('express');
const MongoClient    = require('mongodb').MongoClient;
const bodyParser     = require('body-parser');
const db             = require('./config/db');
const app            = express();
const port = 8000;
app.use(bodyParser.urlencoded({ extended: true }));

MongoClient.connect(db.url, { useUnifiedTopology: true }, (err, client) => {
    if (err) {
        console.error('An error occurred connecting to MongoDB: ', err);
    } else {
        var db = client.db('restapi');
    }
    if (err) return console.log(err);
    require('./app/routes')(app, db);
    app.listen(port, () => {
        console.log('We are live on ' + port);
    });
});