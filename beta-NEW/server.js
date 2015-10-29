var express = require('express');
var multer = require('multer');
var PythonShell = require('python-shell');

var storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function(req, file, cb) {
        cb(null, file.originalname);
    }
});
var upload = multer({
    storage: storage
});

var app = express();

app.use(express.static(__dirname + '/public'));

app.post('/upload', upload.single('file'), function(req,res,next) {
    console.log(req.file.path);
    var options = {
        args: [req.file.path],
        scriptPath: 'python/'
    };
    console.log(options);
    PythonShell.run('main.py', options, function(err, res) {
        if (err) throw err;
        console.log('results: ' + res);
    });
});

app.listen(5555);