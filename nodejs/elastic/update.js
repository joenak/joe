var client = require("./connection.js");

client.update({
    index: "joe",
    type: "test",
    body: {
        doc: {
            phone: "888-888-8888"
        }
    }
}, function(err, resp, status) {
    if (err) {
        console.log(err)
    }
    else {
        console.log(resp)
    }
});