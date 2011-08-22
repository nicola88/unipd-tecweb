#!/usr/bin/perl

######################################################
# NOME: registrazione_conferma.cgi
######################################################
# DESCRIZIONE: elabora le informazioni necessarie alla
# registrazione di un utente
######################################################
# QUERY STRING: nome, cognome, email, username,
# password, password_confirm, javascript
######################################################
use CGI;
use CGI::Session;
use XML::LibXML;
use Digest::MD5 qw(md5_hex);
print "Content-type: text/html\n\n";

# 1. LETTURA INPUT
# - Lettura valori dei parametri dalla pagina di registrazione
# (nome, cognome, email, username, password con conferma)
# - Verifica abilitazione javascript lato client
my $cgi=new CGI;
my $nome = $cgi->param('nome');
my $cognome = $cgi->param('cognome');
my $email = $cgi->param('email');
my $username = $cgi->param('username');
my $password = $cgi->param('password');
my $password_confirm = $cgi->param('password_confirm');
my $javascript = $cgi->param('javascript');

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Registrazione utente - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina di elaborazione della procedura di registrazione di un utente" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film" name="keyword" />
    <title>Registrazione - Cinema Paradiso</title>
    <link href="/style/screen.css" rel="stylesheet" type="text/css" media="screen" />
    <link href="/style/portable.css" rel="stylesheet" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)" />
    <link href="/style/print.css" rel="stylesheet" type="text/css" media="print" />
    <script type="text/javascript" src="/script/validation.js"></script>
    <link rel="shortcut icon" href="/img/cinema.ico" />
</head>
<body>
	<p><a id="skip_nav" href="#content" title="Vai al contenuto" >Vai al contenuto</a></p>
    <div id="header">
    	<h1><a href="/default.html" title="Pagina iniziale">Cinema Paradiso</a></h1>
    	<h2>Programmazione e prenotazioni online</h2>
    </div>
    <div id="account">
    	<p><a href="/cgi-bin/account.cgi" accesskey="8" title="Area riservata">Area riservata</a> | <a href="/registrazione.html" accesskey="9" title="Registrazione">Registrati</a></p>
    </div>
    <div id="navigation">
    	<ul>
        	<li><a href="/default.html" accesskey="0">Pagina iniziale</a>
        	</li>
            <li><a href="/film.html" accesskey="1">Film</a>
            </li>
            <li><a href="/programmazione.html" accesskey="2">Programmazione</a>
            </li>
            <li><a href="/informazioni.html" accesskey="3">Informazioni</a>
            </li>
            <li><a href="/cgi-bin/notizie.cgi" accesskey="4">Notizie</a>
            </li>
        </ul>
    </div>
    <div id="path">
    	<p>Sei in: <a href="/default.html" title="">Pagina iniziale</a> &#187; Registrazione</p>
    </div>
    <div id="content">
    	<h1>Registrazione</h1>
HTML

# 2. VALIDAZIONE INPUT
# PRECONDIZIONE: javascript disabilitato lato client
# - email: formato a@b.c (ove a, b e c sono stringhe contenenti caratteri alfanumerici, '-', '+' e '.')
# - username: lunghezza minima: 3 caratteri - ammessi tutti i caratteri (spazi esclusi)
# - password[_confirm]: lunghezza minima: 6 caratteri - ammessi tutti i caratteri (spazi esclusi)
my $msg;
if(defined($javascript)) {$javascript=1;}
else {
	$validInput=1;
	$msg = "\t\t<ul>\n";
	if($nome eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Nome</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	}
	if($cognome eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Cognome</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	}
	if($email eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Posta elettronica</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif($email!~/^[\w\-\+\.]+@[\w\-\+\.]+\.[\w\-\+\.]+$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Posta elettronica</strong> dev'essere del tipo x\@x.x (ove x rappresenta una sequenza di almeno 1 carattere).</li>\n";
		$validInput=0;
	}
	if($username eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Nome utente</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif($username!~/^\S{3,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Nome utente</strong> deve contenere almeno 3 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($password eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Password</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif($password!~/^\S{6,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($password_confirm eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Conferma password</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif($password_confirm!~/^\S{6,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Conferma password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($password ne $password_confirm) {
		$msg = $msg . "\t\t\t<li>Le password fornite non coincidono.</li>\n";
		$validInput=0;
	}
	$msg = $msg . "\t\t</ul>\n";
}
if($validInput==1) {
	# 3. REGISTRAZIONE su XML
	# - Se i valori immessi sono corretti, le informazioni vengono salvate nel file XML
	# - Altrimenti, viene mostrata la form di registrazione con il riepilogo degli errori riscontrati
	my $file='xml/utenti.xml';
	my $parser=XML::LibXML->new();
	my $document=$parser->parse_file('xml/utenti.xml');
	my $root=$document->getDocumentElement;
	#my @users=$root->findnodes("/utenti");
	#my $new_user="<utente><nome>$name</nome><cognome>$surname</cognome><email>$email</email><username>$username</username><password>$password</password><prenotazioni /></utente>";
	#my $fragment=$parser->parse_balanced_chunk($new_user);
	#my $position=@users;
	#@users[$position]->appendChild($fragment);
	print "\t\t<p>La procedura di registrazione è terminata correttamente. &Egrave; possibile accedere all'area riservata a <a href=\"/cgi/bin/account.cgi\" title=\"Area riservata\">questo indirizzo</a>.</p>";
} else {
	print $msg;
print <<FORM;
        <form action="/cgi-bin/registrazione.cgi" method="get" id="registrazione">
		    <fieldset>
				<legend>Informazioni personali</legend>
				<label for="nome">Nome</label>
				<input name="nome" id="nome" value="$nome" />
				<label for="cognome">Cognome</label>
				<input id="cognome" name="cognome" value="$cognome"/>
				<label for="email">Posta elettronica</label>
				<input id="email" name="email" value="$email" />
			</fieldset>
			<fieldset>
				<legend>Informazioni del profilo</legend>
				<label for="username">Nome utente</label>
				<input id="username" name="username" value="$username" />
				<label for="password">Password</label>
				<input type="password" id="password" name="password"/>
				<label for="password_confirm">Conferma password</label>
				<input type="password" id="password_confirm" name="password_confirm"/>
				<input type="submit" value="Procedi" />
			</fieldset>
			<noscript>
			<fieldset class="script">
				<input type="text" id="javascript" name="javascript" value="false" />
			</fieldset>
			</noscript>
		</form>
FORM
}

print <<HTML;
    </div>
    <div id="footer">
    	<a href="http://validator.w3.org/check?uri=referer"><span id="xhtml_valid" title="HTML 1.0 Strict valido"></span></a>
    	<span id="css_valid" title="CSS 2.1 valido"></span>
    	<p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p>
    </div>
</body>
</html>
HTML
