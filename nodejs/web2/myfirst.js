var http = require('http');
var dt = require('./myfirstmodule.js');
var fs = require('fs');

http.createServer(function (req, res) {
    fs.readFile('demo.html', function (err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write("The current date and time is: " + dt.myDateTime());
        res.write(data);
        res.end();
    });
}).listen(8080);

