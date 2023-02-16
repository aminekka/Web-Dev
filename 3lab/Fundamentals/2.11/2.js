alert( alert(1) || 2 || alert(3) );
//answer is 1 then 2 because alert(1) outputs 1 and then 2 because its truly also
// won't show us 3 beause || doesn't reach this value