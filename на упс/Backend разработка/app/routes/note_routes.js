var ObjectID = require('mongodb').ObjectID;

module.exports = function(app, db) {
    app.get('/:id', (req, res) => {
        const id = req.params.id;
        const details = { '_id': new ObjectID(id) };
        db.collection('links').findOne(details, (err, item) => {
            db.collection('links').findOneAndUpdate(details, {$set: {viewCount: item.viewCount + 1}});
            if (err) {
                res.send({'error': 'An error has occurred'});
            } else {
                res.send({redirectTo: item.urlToShorten});
            }
        });
    });
    app.get('/:id/views', (req, res) => {
        const id = req.params.id;
        const details = { '_id': new ObjectID(id) };
        db.collection('links').findOne(details, (err, item) => {
            if (err) {
                res.send({'error': 'An error has occurred'});
            } else {
                res.send({'viewCount': item.viewCount});
            }
        });
    });
    app.post('/shorten', (req, res) => {
        const note = { urlToShorten: req.body.urlToShorten, viewCount: 0};
        const details = { 'urlToShorten': note.urlToShorten };
        db.collection('links').count(details, (err, item) => {
            console.log(item);
            if (item) {
                db.collection('links').findOne(details, (err, itemForid) => {
                    var re = {"status": "Already created", "shortenedUrl": "http://localhost:8000/" + itemForid._id};
                    res.send(re)
                });
            }
            else {
                db.collection('links').insert(note, (err, result) => {
                    if (err) {
                        res.send({ 'error': 'An error has occurred' });
                    } else {
                        var resIfCreated = {"status": "Created", "shortenedUrl": "http://localhost:8000/" + result.ops[0]._id};
                        res.send(resIfCreated);
                    }
                });
            }
        });
    });
};