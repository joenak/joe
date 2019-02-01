var client = require("./connection.js");

client.index({
    index: "joe",
    type: "test",
    id: "2",
    body: {
        "firstName": "Jane",
        "lastName": "Doe",
        "state": "GA",
        "phone": "770-111-3333"
    }
}, function(err, resp, status) {
    console.log(resp);
}
)