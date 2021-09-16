// polyfill for 'Object.is'

Object.is = function ObjectIs(a, b) {
    if (Number.isNaN(a) === true && Number.isNaN(b) === true) {
        return true;
    }
    else if (a === 0 && b === 0) {
        if (Infinity / a === -Infinity && Infinity / b === -Infinity) {
            return true;
        }
        else if (Infinity / a === Infinity && Infinity / b === Infinity) {
            return true;
        }
        else {
            return false;
        }
    }
    else if (a === b) {
        return true;
    }
    else {
        return false;
    }
};

console.log(Object.is(42,42) === true);
console.log(Object.is("foo","foo") === true);
console.log(Object.is(false,false) === true);
console.log(Object.is(null,null) === true);
console.log(Object.is(undefined,undefined) === true);
console.log(Object.is(NaN,NaN) === true);
console.log(Object.is(-0,-0) === true);
console.log(Object.is(0,0) === true);

console.log(Object.is(-0,0) === false);
console.log(Object.is(0,-0) === false);
console.log(Object.is(0,NaN) === false);
console.log(Object.is(NaN,0) === false);
console.log(Object.is(42,"42") === false);
console.log(Object.is("42",42) === false);
console.log(Object.is("foo","bar") === false);
console.log(Object.is(false,true) === false);
console.log(Object.is(null,undefined) === false);
console.log(Object.is(undefined,null) === false);