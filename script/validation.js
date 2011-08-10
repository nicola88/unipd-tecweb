function validateInput(input, pattern)
{
	var errorCode=0;
	/* ERROR CODE
	 * 0: valore valido
	 * 1: valore vuoto
	 * 2: valore in formato non valido rispetto al pattern
	 * */
	
	if(input == null || input == "")
	{
		errorCode=1;
	}
	else if(pattern != null && !pattern.test(input))
	{
		errorCode=2;
	}
	return errorCode;
}

function validateLogin() {
	var input = document.getElementById("login");
	var msg = "Errori riscontrati:\n";
	var validationError = false;
	
	if(input.username.value == null || input.username.value == "")
	{
		msg = msg + "+ Il campo 'Nome utente' è obbligatorio\n";
		validationError = true;
	}
	if(input.password.value == null || input.password.value == "")
	{
		msg = msg + "+ Il campo 'Password' è obbligatorio";
		validationError = true;
	}
	
	if(validationError) alert(msg);
	return false;
}

function validateRegistration() {
	var input = document.getElementById("registrazione");
	var msg = "Errori riscontrati:\n";
	var validationError = false;
	var patternMail = /^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+$/;
	var patternUsername = /[a-zA-Z0-9]+/;
	var patternPassword = /\S{6,}/;
	if(input.nome.value == null || input.nome.value == "")
	{
		msg = msg + "+ Il campo 'Nome' è obbligatorio\n";
		validationError = true;
	}
	if(input.cognome.value == null || input.cognome.value == "")
	{
		msg = msg + "+ Il campo 'Cognome' è obbligatorio\n";
		validationError = true;
	}
	if(input.mail.value == null || input.mail.value == "")
	{
		msg = msg + "+ Il campo 'Posta elettronica' è obbligatorio\n";
		validationError = true;
	}
	else if( !patternMail.test(input.mail.value) )
	{
		msg = msg + "+ Il campo 'Posta elettronica' contiene un valore non valido\n";
		validationError = true;
	}
	
	if(input.username.value == null || input.username.value == "")
	{
		msg = msg + "+ Il campo 'Nome utente' è obbligatorio\n";
		validationError = true;
	}
	else if( !patternUsername.test(input.username.value) )
	{
		msg = msg + "+ Il campo 'Nome utente' contiene un valore non valido\n";
		validationError = true;
	}
	
	if(input.password.value == null || input.password.value == "")
	{
		msg = msg + "+ Il campo 'Password' è obbligatorio\n";
		validationError = true;
	}
	if(input.password_confirm.value == null || input.password_confirm.value == "")
	{
		msg = msg + "+ Il campo 'Conferma password' è obbligatorio\n";
		validationError = true;
	}
	if(input.password.value != input.password_confirm.value)
	{
		msg = msg + "Le password indicate non coincidono!\n";
		validationError = true;
	}
	else if( !patternPassword.test(input.password.value) )
	{
		msg = msg + "+ Il campo 'Password' contiene un valore non valido\n";
		validationError = true;
	}
	
	if(validationError) alert(msg);
}

function updatePassword() {
	var input = document.getElementById("aggiorna_password");
	var validationError = false;
	var msg = "Errori riscontrati:\n";
	var patternPassword = /\S{6,}/;
	
	switch( validateInput(input.pwd_corrente.value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Password corrente' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Password corrente' contiene un valore non valido\n"; validationError=true; break;
	}
	switch( validateInput(input.pwd_nuova.value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Nuova password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Nuova password' contiene un valore non valido\n"; validationError=true; break;
	}
	switch( validateInput(input.pwd_nuova_conferma.value,patternPassword) )
	{
		case 1: msg = msg + "+ Il campo 'Conferma nuova password' è obbligatorio\n"; validationError=true; break;
		case 2: msg = msg + "+ Il campo 'Conferma nuova password' contiene un valore non valido\n"; validationError=true; break;
	}
	if(input.pwd_nuova.value != input.pwd_nuova_conferma.value)
	{
		msg = msg + "Le nuove password indicate non coincidono!";
		validationError=true;
	}
	if(validationError) alert(msg);
}

