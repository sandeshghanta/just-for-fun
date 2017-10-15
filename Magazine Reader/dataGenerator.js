var fs = require('fs');
var path = require('path');

if (process.argv.length <= 2) {
   console.log("Usage: " + __filename + " path/to/directory");
   process.exit(-1);
}



var dir = process.argv[2];

var data = {};

var comics = fs.readdirSync(dir);
comics.forEach(function(comic){
    var folder = dir + '/' + comic;
    console.log(folder);
    if(fs.statSync(folder).isDirectory()){
        data[comic] = fs.readdirSync(folder);
        data[comic].forEach(function(file,i){
            var folder = dir + '/' + encodeURIComponent(comic);
            data[comic][i] = folder + '/' + data[comic][i];
        });
    }
});

var json = JSON.stringify(data);
fs.writeFile('data.json',json,{encoding: 'utf-8'},function(err){
    console.log("done");
});