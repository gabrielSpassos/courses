var fs = require("fs");

var writableStreamEvent = fs.createWriteStream('arquivoSaida.txt');
writableStreamEvent.on('finish',function(){
    console.log("Arquivo foi Escrito");
});

writableStreamEvent.write("Olá Mundo\n");

writableStreamEvent.end();