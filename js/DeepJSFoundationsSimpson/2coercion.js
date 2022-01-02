// validation functions that check user inputs

function isValidName(name) {
    // Must be a string
    // Must be non empty
    // Must contain non-whitespace of at least 3 characters

    if (typeof name != 'string') {
        return false;
    } 
    var noOfNonWhiteSpaces = howManyNonWhiteSpaces(name);
    
    if (noOfNonWhiteSpaces < 3) {
        return false;
    }

    return true

    /********************** */
    function howManyWhiteSpaces(s) {
        var numberOfWhiteSpaces = 0;
        for (let character of s) {
            if (character === ' ' || character === '\t' || character === '\n') {
                numberOfWhiteSpaces += 1;
            }
        }
        return numberOfWhiteSpaces;
      }
    
    function howManyNonWhiteSpaces(s) {
        var nameLength = s.length;
        var whiteSpaces = howManyWhiteSpaces(s);
        return nameLength - whiteSpaces;
    }

}

function hoursAttended(attended, length) {
    // either parameter may only be a string or number
    // both parameters should be treated as numbers
	// both numbers must be 0 or higher
	// both numbers must be whole numbers
	// `attended` must be less than or equal to `length`

    var attendedIsString = ifString(attended);
    var attendedIsNumber = ifNumber(attended);
    var lengthIsString = ifString(length);
    var lengthIsNumber = ifNumber(length);
    var attendedIsEmpty = ifEmpty(attended);
    var lengthIsEmpty = ifEmpty(length);
    var attendedCanConvertsToNumber = ifCanConvertsToNumber(attended);
    var lengthCanConvertsToNumber = ifCanConvertsToNumber(length);

    if (!attendedIsString && !attendedIsNumber) {
        return false;
    }
    else if (!lengthIsString && !lengthIsNumber) {
        return false;
    }
    else if (attendedIsEmpty || lengthIsEmpty) {
        return false;
    }
    else if (!attendedCanConvertsToNumber || !lengthCanConvertsToNumber) {
        return false;
    }
    else if (Number(attended) > Number(length)) {
        return false
    } 
    else if (!Number.isInteger(Number(attended)) || !Number.isInteger(Number(length))) {
        return false
    }
    return true

    /********************** */

    function ifString(v) {
        return typeof v === 'string'
    }

    function ifNumber(v) {
        return typeof v === 'number'
    }

    function ifEmpty(v) {
        return v === '';
    }

    function ifCanConvertsToNumber(v) {
        if (Object.is(Number(v), NaN)) {
            return false;
        }
        return true;
    }
}


console.log(isValidName("Frank") === true);
console.log(hoursAttended(6,10) === true);
console.log(hoursAttended(6,"10") === true);
console.log(hoursAttended("6",10) === true);
console.log(hoursAttended("6","10") === true);

console.log(isValidName(false) === false);
console.log(isValidName(null) === false);
console.log(isValidName(undefined) === false);
console.log(isValidName("") === false);
console.log(isValidName("  \t\n") === false);
console.log(isValidName("X") === false);
console.log(hoursAttended("",6) === false);
console.log(hoursAttended(6,"") === false);
console.log(hoursAttended("","") === false);
console.log(hoursAttended("foo",6) === false);
console.log(hoursAttended(6,"foo") === false);
console.log(hoursAttended("foo","bar") === false);
console.log(hoursAttended(null,null) === false);
console.log(hoursAttended(null,undefined) === false);
console.log(hoursAttended(undefined,null) === false);
console.log(hoursAttended(undefined,undefined) === false);
console.log(hoursAttended(false,false) === false);
console.log(hoursAttended(false,true) === false);
console.log(hoursAttended(true,false) === false);
console.log(hoursAttended(true,true) === false);
console.log(hoursAttended(10,6) === false);
console.log(hoursAttended(10,"6") === false);
console.log(hoursAttended("10",6) === false);
console.log(hoursAttended("10","6") === false);
console.log(hoursAttended(6,10.1) === false);                                           
console.log(hoursAttended(6.1,10) === false);
console.log(hoursAttended(6,"10.1") === false);
console.log(hoursAttended("6.1",10) === false);
console.log(hoursAttended("6.1","10.1") === false);

