#!/usr/bin/perl

######################################################
# NOME: aggiorna_pwd_conferma.cgi
######################################################
# DESCRIZIONE: elabora la richiesta di modifica della
# password dell'utente corrente
######################################################
# QUERY STRING: username, pwd_corrente, pwd_nuova, pwd_nuova_conferma, javascript
######################################################
use CGI;
use CGI::Session;
use XML::LibXML;
use Digest::MD5 qw(md5_hex);
print "Content-type: text/html\n\n";

# 1. LETTURA INPUT
my $cgi=new CGI;
my $username = $cgi->param('username');
my $pwd_corrente = $cgi->param('pwd_corrente');
my $pwd_nuova = $cgi->param('pwd_nuova');
my $pwd_nuova_conferma = $cgi->param('pwd_nuova_conferma');
my $javascript = $cgi->param('javascript');

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Cambia password - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina di elaborazione della richiesta di aggiornamento della password per un account utente" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film" name="keyword" />
    <title>Cambia password - Cinema Paradiso</title>
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
    	<p>Sei in: <a href="/default.html" title="">Pagina iniziale</a> &#187; Cambia password</p>
    </div>
    <div id="content">
    	<h1>Cambia password</h1>
    	<ul>
    		<li>$username</li>
    		<li>$pwd_corrente</li>
    		<li>$pwd_nuova - $pwd_nuova_conferma</li>
    		<li>$javascript</li>
    	</ul>
HTML

my $msg;
my $validInput=1;
if(defined($javascript)) {
	# 2. VALIDAZIONE INPUT
	$msg = "\t\t<ul>\n";
	if($username eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Nome utente</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif ($username!~/^\S{3,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Nome utente</strong> deve contenere almeno 3 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($pwd_corrente eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Password attuale</strong> &egrave; è obbligatorio.</li>\n";
		$validInput=0;
	} elsif($pwd_corrente!~/^\S{6,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Password attuale</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($pwd_nuova eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Nuova password</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif($pwd_nuova!~/^\S{6,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Nuova password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($pwd_nuova_conferma eq "") {
		$msg = $msg . "\t\t\t<li>Il campo <strong>Conferma password</strong> &egrave; obbligatorio.</li>\n";
		$validInput=0;
	} elsif($pwd_nuova_conferma!~/^\S{6,}$/) {
		$msg = $msg . "\t\t\t<li>Il valore immesso nel campo <strong>Conferma password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
		$validInput=0;
	}
	if($pwd_nuova ne $pwd_nuova_conferma) {
		$msg = $msg . "\t\t\t<li>Le password fornite non coincidono.</li>\n";
		$validInput=0;
	}
	$msg = "\t\t</ul>\n";
	if($validInput==0) {print $msg;}
}

if($validInput==1) {
	$pwd_corrente = md5_hex($pwd_corrente);
	my $parser=XML::LibXML->new();
	my $document=$parser->parse_file('xml/utenti.xml');
	my $root=$document->getDocumentElement;
	@users=$root->findnodes("//utente[username='$username' and password='$pwd_corrente']");
	print "\t\t\t<p>@users</p>";
	if(@users) {
		# 3. AGGIORNAMENTO PASSWORD su XML
		$pwd_nuova=md5_hex($pwd_nuova);
		# $user = $users[0];
	} else {
		print "\t\t\t<p>Nessun utente registrato corrisponde alle informazioni inserite.</p>";
		$validInput=0;
	}
}

if($validInput==0) {
print <<FORM;
    	<form action="/cgi-bin/aggiorna_pwd.cgi" method="get" id="cambia_password">
    		<fieldset>
    			<legend>Inserisci la nuova password</legend>
    			<label for="username">Nome utente</label>
    			<input id="username" name="username" value="$username" />
    			<label for="pwd_corrente">Password attuale:</label>
    			<input type="password" id="pwd_corrente" name="pwd_corrente" title="Inserisci la password corrente" />
    			<label for="pwd_nuova">Nuova password:</label>
    			<input type="password" id="pwd_nuova" title="Inserisci la nuova password" />
    			<label for="pwd_nuova_conferma">Conferma nuova password:</label>
    			<input type="password" id="pwd_nuova_conferma" title="Ripeti la nuova password per conferma" />
    			<input type="submit" value="Aggiorna password" />
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

