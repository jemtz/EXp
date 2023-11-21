//* OPERADORES ARITMETICOS
//todo: + suma
//todo: - resta
//todo: * multiplicacion
//todo: / division
//todo: % porcentaje
//todo: ** potencia
//todo: ++ incremento
//todo: -- decremento
let a,b,c,d,e,f,g,h;

a=5+2
console.log(a);

b=9-12
console.log(b);

c = a*b
console.log(c);

d = c/3
console.log(d);
console.log(typeof(d));

e = 3**3
console.log(e);

f = 10%20
console.log(f);

g = f++
console.log(g)

h = e--
console.log(h)



let noEsZ,$noEsX,_noEsY;
noEsZ=0
$noEsX=2

noEsZ --
console.log(noEsZ);
--noEsZ
console.log(noEsZ);
noEsZ ++
console.log(noEsZ);
++ noEsZ
console.log(noEsZ);

$noEsX ++
console.log($noEsX);
++ $noEsX 
console.log($noEsX);
$noEsX --
console.log($noEsX);
-- $noEsX
console.log($noEsX);

//! OPERADORES DE ASIGNACION ******************

let asignacionOp

asignacionOp = 10
console.log(asignacionOp);
asignacionOp += 10
console.log(asignacionOp);
asignacionOp -= 3
console.log(asignacionOp);
asignacionOp *= 2
console.log(asignacionOp);
asignacionOp /= 4
console.log(asignacionOp);
asignacionOp %= 6
console.log(asignacionOp);
asignacionOp **= 2
console.log(asignacionOp);


//! OPERADORES LOGICOS *************
// * And = &&
// * ej. a&&b
// * Or = ||
// * ej. a&&b

let var1, var2;
var1=true;
var2=false;

console.log(`${var1} && ${var2} -> ${var1&&var2}`);
console.log(`${var1} || ${var2} -> ${var1||var2}`);

console.log(`${!var1} -> ${!var1}`);
console.log(`${!var2} -> ${!var2}`);


let dato1 = 1, dato2 = 2;
prueba =1.2
prueba ++

prueba**2

let dentroderango = prueba >= dato1 && prueba <= dato2 
                  ? `El numero generado pertenece al rango ${dato1}-${dato2}`
                  :`El numero generado no pertenece al rango ${dato1}-${dato2}`;

console.log(dentroderango);

// *********************HW****************
// ejercicio 
//* El numero generado pertenece al rango {min}-{max}
// *else: El numero generado no pertenece al rango {min}-{max}
