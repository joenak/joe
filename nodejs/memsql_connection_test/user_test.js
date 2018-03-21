//  This is used to test connectivity to each MemSQL node for spark_user_ro
var args = process.argv;
var username = "root";
var pwd = "ve0otWIdmqWz4DKS";
var mysql = require('mysql');
var sparkuser = "spark_user_ro";
var sparkuserpwd = "H4wr3!qbI$74tNEvP";
var con = mysql.createConnection({
    host: args[2],
    user: username,
    password: pwd
});
 con.connect();
var query = 'SELECT HOST FROM information_schema.LEAVES UNION ALL SELECT HOST FROM information_schema.AGGREGATORS WHERE HOST != "127.0.0.1"'
con.query(query, function (error, results, fields) {
    if (error) {
        console.log(error)
    }
    else {
        results.forEach((server, index) => {
            var test = mysql.createConnection({
                host: server.HOST,
                user: sparkuser,
                password: sparkuserpwd
            });
            test.connect(function(err) {
                if (err) {
                    console.log("Error connecting to " + server.HOST + " using " + sparkuser);
                }
                else {
                    console.log("Successful connection to " + server.HOST + " using " + sparkuser);
                }
            });
            test.end();
        });
    }