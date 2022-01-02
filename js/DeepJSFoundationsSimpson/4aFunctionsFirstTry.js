function findMatchingRecord(i, studentRecords) {
    for (let record in studentRecords) {
        if (i === studentRecords[record].id) {
            return studentRecords[record];
        }
    }
}

function recordsEnrolled(recordIds) {
    let enrolled = []
    for (let i of recordIds) {
        enrolled.push(findMatchingRecord(i, studentRecords));
    }
    return enrolled
} 

function ifPaid(studentRecords) {
    let studentsWhoPaid = []
    for (let record in studentRecords) {
        if (studentRecords[record].paid === true) {
            studentsWhoPaid.push(studentRecords[record]) 
        }
    }
    
    let studentsWhoPaidIds = [];
    for (let record in studentsWhoPaid) {
        studentsWhoPaidIds.push(studentsWhoPaid[record].id)
    }

    return studentsWhoPaidIds  
}

function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

function printRecords(recordIds) {

    let enrolled = recordsEnrolled(recordIds)

    enrolled.sort(function sortByName(a, b) {
        let fa = a.name.toLowerCase(),
            fb = b.name.toLowerCase();
    
        if (fa < fb) {
            return -1;
        }
        if (fa > fb) {
            return 1;
        }
        return 0;
    });
    
    enrolled.forEach(function display(e) {
        let paymentStatus
        if (e.paid === true) {
            paymentStatus = 'Paid';
        }
        else {
            paymentStatus = 'Not paid';
        }
        console.log(`${e.name} ${e.id}: ${paymentStatus}`);
    });

}

function paidStudentsToEnroll() {

	let studentsWhoPaidIds = ifPaid(studentRecords)
    let enrolled = currentEnrollment
    let newEnrolling = [...studentsWhoPaidIds, ...enrolled]

    return newEnrolling.filter(onlyUnique)
}



// ********************************





var currentEnrollment = [ 410, 105, 664, 375 ];

var studentRecords = [
	{ id: 313, name: "Frank", paid: true, },
	{ id: 410, name: "Suzy", paid: true, },
	{ id: 709, name: "Brian", paid: false, },
	{ id: 105, name: "Henry", paid: false, },
	{ id: 502, name: "Mary", paid: true, },
	{ id: 664, name: "Bob", paid: false, },
	{ id: 250, name: "Peter", paid: true, },
	{ id: 375, name: "Sarah", paid: true, },
	{ id: 867, name: "Greg", paid: false, },
];



printRecords(currentEnrollment);
console.log("----");
currentEnrollment = paidStudentsToEnroll();
printRecords(currentEnrollment);


/*
	Bob (664): Not Paid
	Henry (105): Not Paid
	Sarah (375): Paid
	Suzy (410): Paid
	----
	Bob (664): Not Paid
	Frank (313): Paid
	Henry (105): Not Paid
	Mary (502): Paid
	Peter (250): Paid
	Sarah (375): Paid
	Suzy (410): Paid

*/
