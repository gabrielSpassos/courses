var fs = require("fs");

fs.readFile("arquivo.txt",lerProntoCallback);
function lerProntoCallback(erro, bufferDeDados){
    if(!erro){ 
        console.log("conteúdo de arquivo.txt",bufferDeDados.toString());
    }else{
        console.log(erro);
    }
}