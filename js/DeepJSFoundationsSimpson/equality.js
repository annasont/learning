// findAll(..) function that searches an array and returns an array with all coercive matches

// The coercive matching that is allowed:
// 	- exact matches (`Object.is(..)`)
// 	- strings (except "" or whitespace-only) can match numbers
// 	- numbers (except `NaN` and `+/- Infinity`) can match strings (hint: watch out for `-0`!)
// 	- `null` can match `undefined`, and vice versa
// 	- booleans can only match booleans
// 	- objects only match the exact same object

function setsMatch(arr1,arr2) {
	if (Array.isArray(arr1) && Array.isArray(arr2) && arr1.length == arr2.length) {
		for (let v of arr1) {
			if (!arr2.includes(v)) return false;
		}
		return true;
	}
	return false;
}

var myObj = { a: 2 };

var values = [
	null, undefined, -0, 0, 13, 42, NaN, -Infinity, Infinity,
	"", "0", "42", "42hello", "true", "NaN", true, false, myObj
];

var simple = [1, 7, null, 'moje', undefined, 1, 10, undefined, null];

function findAll(iAmLookingFor, arrayWithValues) {
    var matches = new Array


    if (Object.is(iAmLookingFor, 0) || Object.is(iAmLookingFor, '0')) {
        for (let v of arrayWithValues) {
            if (Object.is(v, 0) || Object.is(v, '0')) {
                matches.push(v);
            }
        }    
    }

    else if (Object.is(iAmLookingFor, '-0') || Object.is(iAmLookingFor, -0)) {
        for (let v of arrayWithValues) {
            if (Object.is(v, -0) || Object.is(v, '-0')) {
                matches.push(v);
            }
        }    
    }

    else if (Object.is(iAmLookingFor, NaN)){
        for (let v of arrayWithValues) {
            if (Object.is(v, NaN)) {
                matches.push(v);
            }
        }
    }

    else if (Object.is(iAmLookingFor, '')){
        for (let v of arrayWithValues) {
            if (Object.is(v, '')) {
                matches.push(v);
            }
        }
    }

    else if (Object.is(iAmLookingFor, false)){
        for (let v of arrayWithValues) {
            if (Object.is(v, false)) {
                matches.push(v);
            }
        }
    }

    else if (Object.is(iAmLookingFor, true)){
        for (let v of arrayWithValues) {
            if (Object.is(v, true)) {
                matches.push(v);
            }
        }
    }

    else {
        for (var v of arrayWithValues) {
            if (v == iAmLookingFor) {
                matches.push(v);
            }
        }
    }


    return matches;

}

console.log(setsMatch(findAll(null,values),[null,undefined]) === true);
console.log(setsMatch(findAll(undefined,values),[null,undefined]) === true);
console.log(setsMatch(findAll(0,values),[0,"0"]) === true);
console.log(setsMatch(findAll(-0,values),[-0]) === true);
console.log(setsMatch(findAll(13,values),[13]) === true);
console.log(setsMatch(findAll(42,values),[42,"42"]) === true);
console.log(setsMatch(findAll(NaN,values),[NaN]) === true);
console.log(setsMatch(findAll(-Infinity,values),[-Infinity]) === true);
console.log(setsMatch(findAll(Infinity,values),[Infinity]) === true);
console.log(setsMatch(findAll("",values),[""]) === true);
console.log(setsMatch(findAll("0",values),[0,"0"]) === true);
console.log(setsMatch(findAll("42",values),[42,"42"]) === true);
console.log(setsMatch(findAll("42hello",values),["42hello"]) === true);
console.log(setsMatch(findAll("true",values),["true"]) === true);
console.log(setsMatch(findAll(true,values),[true]) === true);
console.log(setsMatch(findAll(false,values),[false]) === true);
console.log(setsMatch(findAll(myObj,values),[myObj]) === true);

console.log(setsMatch(findAll(null,values),[null,0]) === false);
console.log(setsMatch(findAll(undefined,values),[NaN,0]) === false);
console.log(setsMatch(findAll(0,values),[0,-0]) === false);
console.log(setsMatch(findAll(42,values),[42,"42hello"]) === false);
console.log(setsMatch(findAll(25,values),[25]) === false);
console.log(setsMatch(findAll(Infinity,values),[Infinity,-Infinity]) === false);
console.log(setsMatch(findAll("",values),["",0]) === false);
console.log(setsMatch(findAll("false",values),[false]) === false);
console.log(setsMatch(findAll(true,values),[true,"true"]) === false);
console.log(setsMatch(findAll(true,values),[true,1]) === false);
console.log(setsMatch(findAll(false,values),[false,0]) === false);


