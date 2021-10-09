

let deepJS = {
    currentEnrollment: [],
    studentRecords: [],
    addStudent: function(id,name,paid) {
		this.studentRecords.push({ id, name, paid, });
	},
    enrollStudent: function(id) {
		if (!this.currentEnrollment.includes(id)) {
			this.currentEnrollment.push(id);
		}
	},
	printCurrentEnrollment: function() {
		this.printRecords(this.currentEnrollment);
	},
    enrollPaidStudents: function() {
		this.currentEnrollment = this.paidStudentsToEnroll();
		this.printCurrentEnrollment();
	},
	remindUnpaidStudents: function() {
		this.remindUnpaid(this.currentEnrollment);
	},
	getStudentFromId: function(studentId) {
		return this.studentRecords.find(matchId);
		function matchId(record) {
			return (record.id == studentId);
		}
	},
	printRecords: function(recordIds) {
		var records = recordIds.map(this.getStudentFromId.bind(this));
		records.sort(this.sortByNameAsc);
		records.forEach(this.printRecord);
	},
	sortByNameAsc: function(record1,record2){
		if (record1.name < record2.name) return -1;
		else if (record1.name > record2.name) return 1;
		else return 0;
	},
	printRecord: function(record) {
		console.log(`${record.name} (${record.id}): ${record.paid ? "Paid" : "Not Paid"}`);
	},
	paidStudentsToEnroll: function() {
		var recordsToEnroll = this.studentRecords.filter(this.needToEnroll.bind(this));
		var idsToEnroll = recordsToEnroll.map(this.getStudentId);
		return [ ...this.currentEnrollment, ...idsToEnroll ];
	},
	needToEnroll: function(record) {
		return (record.paid && !this.currentEnrollment.includes(record.id));
	},
	getStudentId: function(record) {
		return record.id;
	},
	remindUnpaid: function(recordIds) {
		var unpaidIds = recordIds.filter(this.notYetPaid.bind(this));
		this.printRecords(unpaidIds);
	},
	notYetPaid: function(studentId) {
		var record = this.getStudentFromId(studentId);
		return !record.paid;
	}
}

deepJS.addStudent(311,"Frank",/*paid=*/true);
deepJS.addStudent(410,"Suzy",/*paid=*/true);
deepJS.addStudent(709,"Brian",/*paid=*/false);
deepJS.addStudent(105,"Henry",/*paid=*/false);
deepJS.addStudent(502,"Mary",/*paid=*/true);
deepJS.addStudent(664,"Bob",/*paid=*/false);
deepJS.addStudent(250,"Peter",/*paid=*/true);
deepJS.addStudent(375,"Sarah",/*paid=*/true);
deepJS.addStudent(867,"Greg",/*paid=*/false);

deepJS.enrollStudent(410);
deepJS.enrollStudent(105);
deepJS.enrollStudent(664);
deepJS.enrollStudent(375);

deepJS.printCurrentEnrollment();
console.log("----");
deepJS.enrollPaidStudents();
console.log("----");
deepJS.remindUnpaidStudents();
