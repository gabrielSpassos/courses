import {fatorial} from "./fatorial";

const argv = require('yargs').demandOption('num').argv;

console.log('n-fatorial');

const number = argv.num;

console.log(`O fatorial do número ${number} é ${fatorial(number)}`);
