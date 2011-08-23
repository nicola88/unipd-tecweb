function validate(input, pattern)
{
	var errorCode=0;
	/* ERROR CODE
	 * 0: valore valido
	 * 1: valore vuoto o non definito
	 * 2: valore in formato non valido rispetto al pattern
	 * */
	if(input == null || input == "") {errorCode=1;}
	else if(pattern != null && !pattern.test(input)) {errorCode=2;}
	return errorCode;
}

function checkRegistration() {
	var input = document.forms["registrazione"];
	var msg = "Errori riscontrati:\n";
	var validationError = false;
	var patternMail = /^[\w\-\+\.]+@[\w\-\+\.]+\.[\w\-\+\.]+$/;
	var patternUsername = /^\S{3,}$/;
	var patternPassword = /\S{6,}/;
	
	if(input["nome"].value == null || input["nome"].value == "")
	{
		msg = msg + "+ Il campo 'Nome' è obbligatorio\n";
		validationError = true;
	}
	if(input["cognome"].value == null || input["cognome"].value == "")
	{
		msg = msg + "+ Il campo 'Cognome' è obbligatorio\n";
		validationError = true;
	}
	switch( validate(input["email"].value,patternMail) )
	{
		case 1: msg = msg + "+ Il campo 'Posta elettronica' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Posta elettronica' contiene un valore non valido\n"; validationError=true; break;
	}
	
	switch( validate(input["username"].value,patternUsername) )
	{
		case 1: msg = msg + "+ Il campo 'Nome utente' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Nome utente' deve contenere almeno 3 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	switch( validate(input["password"].value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Password' deve contenere almeno 6 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	switch( validate(input["password_confirm"].value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Conferma password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Conferma password' deve contenere almeno 6 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	if(input["password"].value != input["password_confirm"].value)
	{
		msg = msg + "+ Le password indicate non coincidono!\n";
		validationError = true;
	}
	if(validationError) {alert(msg); return false;}
	else return true;
}

function checkLogin() {
	var input = document.forms["login"];
	var msg = "Errori riscontrati:\n";
	var validationError = false;
	var patternUsername = /^\S{3,}$/;
	var patternPassword = /\S{6,}/;
	
	switch( validate(input["username"].value,patternUsername) )
	{
		case 1: msg = msg + "+ Il campo 'Nome utente' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Nome utente' deve contenere almeno 3 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	switch( validate(input["password"].value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Password' deve contenere almeno 6 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	if(validationError) {alert(msg); return false;}
	else return true;
}

function updatePassword() {
	var input = document.forms["aggiorna_password"];
	var validationError = false;
	var msg = "Errori riscontrati:\n";
	var patternUsername = /^\S{3,}$/;
	var patternPassword = /\S{6,}/;
	
	switch( validate(input["username"].value,patternUsername) )
	{
		case 1: msg = msg + "+ Il campo 'Nome utente' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Nome utente' deve contenere almeno 3 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	switch( validate(input["pwd_corrente"].value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Password attuale' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Password attuale' deve contenere almeno 6 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	switch( validate(input["pwd_nuova"].value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Nuova password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Nuova password' deve contenere almeno 6 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	switch( validate(input["pwd_nuova_conferma"].value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Conferma nuova password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Conferma nuova password' deve contenere almeno 6 caratteri (spazi non ammessi)\n"; validationError=true; break;
	}
	if(input["pwd_nuova"].value != input["pwd_nuova_conferma"].value)
	{
		msg = msg + "+ Le nuove password indicate non coincidono!";
		validationError=true;
	}
	if(validationError) {alert(msg); return false;}
	else return true;
}

