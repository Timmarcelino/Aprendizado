/* 
**Exercício 1: Calcular a média de dois números**
Escreva uma função que receba dois números como parâmetros e retorne a média entre eles.

**Exercício 2: Verificar se um número é positivo, negativo ou zero**
Escreva uma função que receba um número como parâmetro e exiba no console se ele é positivo, negativo ou zero.

**Exercício 3: Verificar se uma palavra é um palíndromo**
Escreva uma função que receba uma palavra como parâmetro e retorne true se ela for um palíndromo (ou seja, se ela é igual quando lida de trás para frente), ou false caso contrário.

**Exercício 4: Gerar um número aleatório entre um intervalo**
Escreva uma função que receba dois números (um mínimo e um máximo) como parâmetros e retorne um número aleatório entre esse intervalo.

**Exercício 5: Contar a quantidade de vogais em uma palavra**
Escreva uma função que receba uma palavra como parâmetro e retorne a quantidade de vogais que ela possui.

**Exercício 6: Verificar se um número é primo**
Escreva uma função que receba um número como parâmetro e retorne true se ele for primo, ou false caso contrário.

**Exercício 7: Remover elementos duplicados de um array**
Escreva uma função que receba um array como parâmetro e retorne um novo array sem os elementos duplicados.

**Exercício 8: Ordenar um array de números**
Escreva uma função que receba um array de números como parâmetro e retorne um novo array com os números ordenados em ordem crescente.

**Exercício 9: Converter texto para maiúsculas ou minúsculas**
Escreva uma função que receba um texto e um parâmetro indicando se o texto deve ser convertido para maiúsculas ou minúsculas, e retorne o texto convertido.

**Exercício 10: Calcular fatorial de um número**
Escreva uma função que receba um número inteiro como parâmetro e retorne o seu fatorial. O fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n.

Esses exercícios cobrem vários conceitos importantes em JavaScript, desde funções simples até manipulação de arrays e strings. Espero que eles te ajudem a aprimorar suas habilidades na linguagem! Bom estudo! */

///
/// Exercício 1: Calcular a média de dois números
///

function calcularMedia(numero1, numero2) {
    return (numero1 + numero2) / 2
}

const resultadoMedia = calcularMedia(5, 7)
console.log(resultadoMedia)
  