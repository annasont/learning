function findStudentById(studentId) { 
    return studentRecords.find(function matchId(record) {
        return record.id === studentId;
    })
}

function printRecords(recordIds) {

    let enrolled = recordIds.map(findStudentById);

    enrolled.sort(function sortByName(record1, record2) {
        let lowerCaseName1 = record1.name.toLowerCase(),
            lowerCaseName2 = record2.name.toLowerCase();
    
        if (lowerCaseName1 < lowerCaseName2) {
            return -1;
        }
        else if (lowerCaseName1 > lowerCaseName2) {
            return 1;
        }
        return 0;
    });
    
    enrolled.forEach(function displayRecord(record) {
        console.log(`${record.name} ${record.id}: ${record.paid ? "Paid" : "Not paid"}`);
    });

}

function paidStudentsToEnroll() {
    let idsToEnroll = studentRecords.filter(function checkPaidStatus(record) {
        return record.paid === true && (!currentEnrollment.includes(record.id))
    })
    .map(function getId(record) {
        return record.id
    });
    
    return [...currentEnrollment, ...idsToEnroll]
}


function remindUnpaid(recordIds) {
	
    let  unpaid = studentRecords.filter(function findUnpaid(record) {
        return record.paid === false && (recordIds.includes(record.id))
    })
    .map(function getId(record) {
        return record.id
    })
    printRecords(unpaid)
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
console.log("----");
remindUnpaid(currentEnrollment);

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
	----
	Bob (664): Not Paid
	Henry (105): Not Paid
*/
