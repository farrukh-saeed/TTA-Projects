function Greetings() {
	var FirstName = document.getElementById("FirstName").value;
	var LastName  = document.getElementById("LastName").value;
	let FullName  = FirstName + LastName ;
	document.getElementById("FullName").value=FullName;
	
      }

 function clearText() {
	 document.getElementById('FullName').value ="";
 }

 function currentDateTime() {

	 const d = new Date();
	document.getElementById("date").innerHTML = d;
 }
 	// 6 Times Table 
 	var a, b = 6;
	for (i = 1; i < 11; i ++) {
 	a = i * b ;
 	// console.log("" +b+ "X" +i+ "=", a);
	 document.write("Times ( " +b+ "X" +i+ " ) = ", "", a + "<br>");
}

