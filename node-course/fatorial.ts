export const fatorial = (number) => {
    if(number === 0) {
        return 1
    }

    return number * fatorial(number - 1)
};

//exports.fatorial = fatorial;

/*
exports = module.exports

# exportando apenas a função index
module.exports = fatorial

# exportando n funções
module.exports = {
    fatorial: fatorial,
    funcao: funcao2
}
*/