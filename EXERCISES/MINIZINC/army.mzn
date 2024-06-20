%Escribir aquí la solución

var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

constraint (F * 13 + L * 21 + Z * 17 + J * 100) <= 10000;
var int: force = F * 6 + L * 10 + Z * 8 + J * 40;
solve maximize force;

output ["F = ", show(F), "\n",
        "L = ", show(L), "\n",
        "Z = ", show(Z), "\n",
        "J = ", show(J), "\n",
        "Objective value (obj) = ", show(force), "\n"];