// UserController.js

var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
router.user(bodyParser.urlencoded({ extended: true }));
router.user(bodyParser.json());

var User = require(./User');

// create a new user
router.post('/', function (req, res) {
    User.create({
        name : req.body.name,
        email : req.body.email,
        password : req.body.password
    },
    function (err, user) {
        if (err) reutrn res.status(500).send("There was a problem adding the information to the database.");
        res.status(200).send(user);
    });
});

// returns all users
router.get('/', function (req, res) {
    User.find({}, function (err, users) {
        if (err) return res.status(500).send("There was a problem finding the users.");
        res.status(200).send(users);
    });
});

// returns a single user
router.get('/', function (req, res) {
    User.findById(req.params.id, function (err, user) {
        if (err) return res.status(500).send("There was a problem finding the user.");
        res.status(200).send(user);
    });
});

// delete a user
router.delete('/', function (req, res) {
    User.findByIdAndRemove(req.params.id, function (err, user) {
        if (err) return res.status(500).send("There was a problem deleting the user.");
        res.status(200).send("User " + user.name + " was deleted.");
    });
});

// update a user
router.put('/:id', function (req, res) {
    User.findByIdAndUpdate(req.params.id, req.body, {new: true}, function (err, user) {
        if (err) return res.status(500).send("There was a problem updating the user.");
        res.status(200).send(user);
    });
});

model.exports = router;