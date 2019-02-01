var client = require("./connection.js");

client.indices.create( {
    index: 'joe'
}, function(err, resp, status) {
    if (err) {
        console.log(err);
    }
    else {
        console.log("create", resp);
    }
});