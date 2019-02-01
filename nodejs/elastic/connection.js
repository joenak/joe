var elasticsearch = require("elasticsearch");

var client = new elasticsearch.Client( {
    hosts: [
        'http://172.16.248.183:9200/'
    ]
});

module.exports = client;