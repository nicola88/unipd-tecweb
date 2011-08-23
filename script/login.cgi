#!/usr/bin/perl

######################################################
# NOME: login.cgi
######################################################
# DESCRIZIONE: gestisce la fase di autenticazione di
# un utente e la creazione di una sessione
######################################################
# QUERY STRING: username, password, js_enabled
######################################################
# TO DO: gestione destinazione (POST) - gestione sessione
######################################################
use CGI;
use CGI::Session;
use XML::LibXML;
use Digest::MD5 qw(md5_hex);
print "Content-type: text/html\n\n";

# 1. LETTURA INPUT
# CASO 1: l'utente arriva da una pagina differente accessibile solo previa autenticazione
# - Viene caricata una semplice pagina web per effettuare il login
# CASO 2: l'utente arriva da un'invocazione precedente della stessa pagina (tentativo di login fallito)
# - Vengono letti i valori dei parametri 'username' e 'password' inseriti e si determina se j
# - Si determina se javscript lato client è abilitato o meno
my $cgi=new CGI;
my $username=$cgi->param('username');
my $password=$cgi->param('password');
my $first_invocation;
my $javascript;
if( !defined($username) || !defined($password)) {$first_invocation=1;}
else {
	$first_invocation=0;
	if( !defined($cgi->param('javascript')) ) {$javascript=1;}
	else {$javascript=0;}
}

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Autenticazione - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina per l'autenticazione di utenti registrati" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film" name="keyword" />
    <title>Autenticazione - Cinema Paradiso</title>
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
    	<p>Sei in: <a href="/default.html" title="">Pagina iniziale</a> &#187; Autenticazione</p>
    </div>
    <div id="content">
        <h1>Autenticazione</h1>
HTML

# 2. VALIDAZIONE INPUT
# PRECONDIZIONI: javascript lato client disabilitato
# - nessuno campo deve essere vuoto
# - username e password devono avere lunghezza minima rispettivamente di 3 e 6 caratteri
# - username e password possono contenere qualsiasi carattere (spazi esclusi)
# Se i dati inseriti dall'utente non sono accettabili, stampo la
# pagina di login con indicate le irregolarità riscontrate.
my $msg;
my $validInput=1;
if($first_invocation==0 ) {
	$msg = "\t\t<ul>\n";
	if($username eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>username</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif ($username!~/^\S{3,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>username</strong> deve contenere almeno 3 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($password eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>password</strong> &egrave; è obbligatorio.</li>\n";
		$validInput=0;
	} elsif($password!~/^\S{6,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	$msg = $msg . "\t\t</ul>\n";
	if(!$validInput) {print $msg;}
	else {
		# 3. AUTENTICAZIONE
		# PRECONDIZIONI: validazione input terminata correttamente
		# Si verifica l'esistenza di un utente con le credenziali inserite
		# - CASO 1: credenziali corrette => creazione nuova sessione e reindirizzamento verso la pagina di destinazione
		# - CASO 2: credenziali errate: mostra la pagina di login segnalando il problema
		my $parser=XML::LibXML->new();
		my $document=$parser->parse_file('xml/utenti.xml');
		my $root=$document->getDocumentElement;
		my @users=$root->findnodes("//utente[username='$username' and password='$password']");
		if(@users) {
			# QUI creo la nuova sessione e reindirizzo a destinazione
			# l'array @users contiene l'utente cercato
			#my $session=CGI::Session->new(undef,undef,{Directory=>'../tmp'});
			#$session->param('username',$username);
			#$session->param('password',$password);
			#$session->expire('+30m'); # scadenza della sessione (30 minuti)
			#my $session_id=$session->id();
			#print "Location: ../cgi-bin/account.cgi\n\n";
			#### QUI FINISCONO I PROBLEMI... ####
		} else {
			$msg = "\t\t<p>Nome utente e password inserite non corrispondono ad alcun utente registrato.</p>";
			print $msg;
		}
	}
}

print <<HTML;
		<p>$first_invocation - $username - $password - $javascript</p>
		<form action="/cgi-bin/login.cgi" method="get" id="login">
			<fieldset>
				<legend>Inserisci le tue credenziali</legend>
				<label for="username">Nome utente</label>
				<input id="username" name="username" />
				<label for="password">Password</label>
				<input type="password" id="password" name="password" />
				<input type="submit" value="Accedi" onclick="return checkLogin()" />
			</fieldset>
			<noscript>
			<fieldset class="script">
				<input type="text" id="javascript" name="javascript" value="false" />
			</fieldset>
			</noscript>
		</form>
		<p>
			<a href="/registrazione.html" title="Registrazione">Non hai un account? Registrati, &egrave; gratis!</a>
		</p>
    </div>
    <div id="footer">
    	<a href="http://validator.w3.org/check?uri=referer"><span id="xhtml_valid" title="HTML 1.0 Strict valido"></span></a>
    	<span id="css_valid" title="CSS 2.1 valido"></span>
    	<p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p>
    </div>
</body>
</html>
HTML
