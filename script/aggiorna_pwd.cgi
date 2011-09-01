#!/usr/bin/perl

# NOME
# aggiorna_pwd.cgi

# DESCRIZIONE
# Elabora la richiesta di modifica della password corrente da parte dell'utente.

# QUERY STRING
# username, pwd_corrente, pwd_nuova, pwd_nuova_conferma, javascript

use CGI;
use CGI::Session;
use XML::LibXML;
use Digest::MD5 qw(md5_hex);

# (1) VERIFICA AUTENTICAZIONE UTENTE
# Verifico se l'utente è autenticato (in caso contrario, redireziono alla pagina
# di login).
$session=CGI::Session->load();
if($session->is_expired || $session->is_empty){
	# utente non autenticato
	print "Location: login.cgi\n\n";
}
else{
	# utente autenticato
	# (1) LETTURA INPUT FORM
	# Leggo i valori ricevuti dalla form di aggiornamento della password
	# (username, password corrente, nuova password, conferma della nuova password
	# e JavaScript).
	my $cgi=new CGI;
	my $username=$cgi->param('username');
	my $password=$cgi->param('pwd_corrente');
	my $new_password=$cgi->param('pwd_nuova');
	my $new_password_confirm=$cgi->param('pwd_nuova_conferma');
	my $javascript=$cgi->param('javascript');
	# (2) VALIDAZIONE INPUT (JAVASCRIPT DISABILITATO)
	# Se JavaScript è disabilitato lato client, valido i valori in input secondo i
	# seguenti vincoli:
	# - nessuno dei campo dati deve essere vuoto;
	# - username e password devono corrispondere a un utente registrato;
	# - lo username deve contenere almeno 3 caratteri qualsiasi, spazi esclusi;
	# - tutte le password devono contenere almeno 6 caratteri qualsiasi, spazi
	#   esclusi.
	# Se i valori in input non superano la validazione, ristampo la pagina di
	# aggiornamento della password indicando gli errori riscontrati.
	my $error;
	my $correct_input=1;
	if(defined($javascript)){
		$error="\t\t<ul>\n";
		if($username eq ""){
			$error=$error."\t\t\t<li>Il campo <strong>Nome utente</strong> &egrave; obbligatorio.</li>\n";
			$correct_input=0;
		}elsif($username!~/^\S{3,}$/){
			$error=$error."\t\t\t<li>Il valore immesso nel campo <strong>Nome utente</strong> deve contenere almeno 3 caratteri (spazi non ammessi).</li>\n";
			$correct_input=0;
		}
		if($password eq ""){
			$error=$error."\t\t\t<li>Il campo <strong>Password attuale</strong> &egrave; obbligatorio.</li>\n";
			$correct_input=0;
		}elsif($password!~/^\S{6,}$/){
			$error=$error."\t\t\t<li>Il valore immesso nel campo <strong>Password attuale</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
			$correct_input=0;
		}
		if($new_password eq ""){
			$error=$error."\t\t\t<li>Il campo <strong>Nuova password</strong> &egrave; obbligatorio.</li>\n";
			$correct_input=0;
		}elsif($new_password!~/^\S{6,}$/){
			$error=$error."\t\t\t<li>Il valore immesso nel campo <strong>Nuova password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
			$correct_input=0;
		}
		if($new_password_confirm eq ""){
			$error=$error."\t\t\t<li>Il campo <strong>Conferma password</strong> &egrave; obbligatorio.</li>\n";
			$correct_input=0;
		}elsif($new_password_confirm!~/^\S{6,}$/){
			$error=$error."\t\t\t<li>Il valore immesso nel campo <strong>Conferma password</strong> deve contenere almeno 6 caratteri (spazi non ammessi).</li>\n";
			$correct_input=0;
		}
		if($new_password ne $new_password_confirm){
			$error=$error."\t\t\t<li>Le password fornite non coincidono.</li>\n";
			$correct_input=0;
		}
		$error=$error."\t\t</ul>\n";
		if($correct_input==1){
			$error=undef; # ripulisco $error
		}
	}
	if($correct_input==1){
		$password=md5_hex($password);
		my $parser=XML::LibXML->new();
		my $document=$parser->parse_file('xml/utenti.xml');
		my $root=$document->getDocumentElement;
		@users=$root->findnodes("//utente[username='$username' and password='$password']");
		if($session->param('username')==$username && $session->param('password')==$password && @users){
			# (3) AGGIORNAMENTO PASSWORD
			# Aggiorno la password dell'utente (sia nel file XML sia nella sessione
			# corrente sul server) e redireziono alla pagina dell'area utente.
			$new_password=md5_hex($new_password);
			my @node=$root->findnodes("//utente[username='$username' and password='$password']/password/text()");
			$node[0]->setData($new_password);
			open(OUT,">xml/utenti.xml");
			print OUT $document->toString;
			close(OUT);
			$session->param('password',$new_password);
			&redirect_to_account_page();
		}
		else{
			$error="\t\t\t<p>Username e password utente non corretti.</p>";
			&print_password_change_page($error);
		}
	}
	else{
		&print_password_change_page($error);
	}
}

# FUNZIONE N°1: STAMPA PAGINA AGGIORNAMENTO PASSWORD
sub print_password_change_page{
	print "Content-type: text/html\n\n";
	# prima parte del codice XHTML della pagina
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
HTML
	# messaggi di avviso per l'utente
	print $_[0];
	# seconda parte del codice XHTML della pagina
print <<HTML;
    	<form action="/cgi-bin/aggiorna_pwd.cgi" method="get">
    		<fieldset>
    			<legend>Inserisci la nuova password</legend>
    			<label for="username">Nome utente</label>
    			<input id="username" name="username" />
    			<label for="pwd_corrente">Password attuale:</label>
    			<input type="password" id="pwd_corrente" name="pwd_corrente" />
    			<label for="pwd_nuova">Nuova password:</label>
    			<input type="password" id="pwd_nuova" name="pwd_nuova" />
    			<label for="pwd_nuova_conferma">Conferma nuova password:</label>
    			<input type="password" id="pwd_nuova_conferma" name="pwd_nuova_conferma" />
    			<input type="submit" value="Aggiorna password" />
    		</fieldset>
    		<noscript>
			<fieldset class="script">
				<input type="text" id="javascript" name="javascript" value="false" />
			</fieldset>
			</noscript>
    	</form>
    	<p class="aiuto">
    		La nuova password deve contenere almeno 6 caratteri (spazi non ammessi).
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
}

# FUNZIONE N°2: REDIREZIONE PAGINA ACCOUNT UTENTE
sub redirect_to_account_page{
	print "Content-type: text/html\n\n";
	# codice XHTML della pagina
print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="refresh" content="0; url=account.cgi" />
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
<body />
</html>
HTML
}

