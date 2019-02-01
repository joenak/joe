var client = require("./connection.js");

client.search({
    index: "joe",
    type: "test",
    body: {
        query: {
            match: { "firstName": "John" }
        }
    }
}, function(err, resp, status) {
    if (err) {
        console.log(err);
    }
    else {
        console.log("--- Response ---");
        console.log(resp);
        console.log("--- Hits ---");
        resp.hits.hits.forEach(function(hit) {
            console.log(hit);
        })
    }
}
)