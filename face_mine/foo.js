
var fs = require('fs');

function binaryRead(file) {
    var bitmap = fs.readFileSync(file);
    return new Buffer(bitmap.toString('binary'),'binary');
}

var oxfordEmotion = require("node-oxford-emotion")("32622b4d753d4a88b470b63da536a794");
var imageData = "./faces/11.png"
var emotion = oxfordEmotion.recognize("image", binaryRead(imageData), function(cb) {
    console.log(cb);
    var data = JSON.parse(cb)[0]["scores"];
    var max = 0;
    var maxKey = null;
    for (key in data) {
        var val = data[key];
        if (val > max) {
            max = val;
            maxKey = key;
        }
    }
    console.log(maxKey);
});

