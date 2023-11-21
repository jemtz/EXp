//TODO: funciones en js
//? --> Bloque de codigo reutilizable

//* -> Sintaxis
/**
 * fuction <Nombre>(<Parametros>){
 *  <Cuerpo>
 *  return<ValorRetorno>
 * }
 * 
 * Codigo legible
 * Mantenimiento sencillo
 * 
 */

function sumaFunction(a,b) {
  return a+b;
}

console.log(sumaFunction(3,4));



function pMessage(message) {
  console.log(message);
  return message
}
console.log(pMessage('Mensaje 1'));

// *Paso por valor
let y = null
function cambiaValor(valor) {
  console.log(valor);
  valor = 100  
  console.log(valor);
}

console.log(cambiaValor(y));
console.log(y);

// * -> Paso por referencia
let parametro = [3,2,4];
function cambioReferencia(param) {
  param[0] = 100
}

console.log(cambioReferencia(parametro));
console.log(parametro);

// * -> Funciones recursivas
//**
/** fuction miFunction(<Parametros>){
 *  <Cuerpo><miFunction>
 *  return<ValorRetorno>
 * }
 * 
 * Codigo legible
 * Mantenimiento sencillo
 * 
*/



function fRecursiva(params) {
  for (let i = 0; i < array.length; i++) {
    let element = array[i];
    if(element != 6) {
      console.log('El numero no es 6');
    }else{
      console.log('El numero es 6');
    }
  }

}

// TODO: HW CALCULAR EL FACTORIAL DE UN NUMERO
// ? Una funcion recursiva es aquella que se llama a si misma

function factorialRecursiva(param) {

  if (param == 0){
    return 1
  }
  else{
    let res = param * factorialRecursiva(param-1)
    console.log(`${res/(param)}*${param} = ${res}`);
    return res}
}
console.log(factorialRecursiva(5));




