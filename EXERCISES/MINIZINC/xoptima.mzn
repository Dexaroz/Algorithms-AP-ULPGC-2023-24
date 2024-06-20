
var 0..10: x;

constraint x mod 4 == 0;

var int: obj = (x - 7)^2;

solve minimize obj;

output ["x = ", show(x),"\n", "obj = ", show(obj)];
