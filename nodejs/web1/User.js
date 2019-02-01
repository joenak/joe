// User.js
var mysql = require('mysql');
var UserSchema = new mysql.Schema({
    name: String,
    email: String,
    password: String
});

mysql.model('User', UserSchema);

model.exports = mysql.model('User');