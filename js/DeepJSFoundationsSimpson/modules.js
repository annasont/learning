let deepJS = defineWorkshop();
deepJS.addStudent(313, "Frank", true);
deepJS.addStudent(410, "Suzy", true);
deepJS.addStudent(709, "Brian", false);
deepJS.addStudent(105, "Henry", false);
deepJS.addStudent(502, "Mary", true);
deepJS.addStudent(664, "Bob", false);
deepJS.addStudent(250, "Peter", true);
deepJS.addStudent(375, "Sarah", true);
deepJS.addStudent(867, "Greg", false);
deepJS.enrollStudent(410);
deepJS.enrollStudent(105);
deepJS.enrollStudent(664);
deepJS.enrollStudent(375);
deepJS.printCurrentEnrollment();
console.log("--------");
deepJS.enrollPaidStudents();
deepJS.printCurrentEnrollment();
console.log("--------");
deepJS.remindUnpaid();


// ********************************

function defineWorkshop() {

    let currentEnrollment = [];
    let studentRecords = [];


    var publicAPI = {
        addStudent, 
        enrollStudent, 
        printCurrentEnrollment, 
        enrollPaidStudents, 
        remindUnpaid}
    return publicAPI


    function addStudent(id, name, paid) {
        if (!currentEnrollment.includes(id)) {
            studentRecords.push({id, name, paid})
        }
    }

    function enrollStudent(id) {
        currentEnrollment.push(id)
    }

    function getStudentFromId(studentId) {
        return studentRecords.find(matchId);
    
        // *************************
    
        function matchId(record) {
            return (record.id == studentId);
        }
    }
    
    function printCurrentEnrollment() {
        var records = currentEnrollment.map(getStudentFromId);
    
        records.sort(sortByNameAsc);
        records.forEach(printRecord);
    }
    
    function sortByNameAsc(record1,record2){
        if (record1.name < record2.name) return -1;
        else if (record1.name > record2.name) return 1;
        else return 0;
    }
    
    function printRecord(record) {
        console.log(`${record.name} (${record.id}): ${record.paid ? "Paid" : "Not Paid"}`);
    }
    
    function enrollPaidStudents() {
        var recordsToEnroll = studentRecords.filter(needToEnroll);
    
        var idsToEnroll = recordsToEnroll.map(getStudentId);
    
        return currentEnrollment = [ ...currentEnrollment, ...idsToEnroll ];
    }
    
    function needToEnroll(record) {
        return (record.paid && !currentEnrollment.includes(record.id));
    }
    
    function getStudentId(record) {
        return record.id;
    }
    
    function remindUnpaid() {
        var unpaidIds = currentEnrollment.filter(notYetPaid).map(getStudentFromId);
    
        unpaidIds.sort(sortByNameAsc);
        unpaidIds.forEach(printRecord);
    }
    
    function notYetPaid(studentId) {
        var record = getStudentFromId(studentId);
        return !record.paid;
    }
}



