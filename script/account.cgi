#!/usr/bin/perl

######################################################
# NOME: account.cgi
######################################################
# DESCRIZIONE: visualizza e informazioni sul profilo
# e le prenotazioni associate all'utente corrente
######################################################
# QUERY STRING: vuota
######################################################
# TO DO: tabella prenotazioni
######################################################

use CGI;
use CGI::Session;
use XML::LibXML;
print "Content-type: text/html\n\n";

# 1. GESTIONE SESSIONE
#my $session = CGI::Session->load() or die "Nessuna sessione aperta.";
#if($session->is_empty() || $session->is_expired()){
#	# non esiste una sessione attiva
#	print "Location: /cgi-bin/404.cgi\n\n";
#}
my $username='nmoretto'; # $session->param('username');
my $password='d0ef51379636616a1e351fa3bec115e6'; # $session->param('password'); # hash MD5!

# 2. LETTURA INFORMAZIONI UTENTE da XML
my $parser=XML::LibXML->new();
my $document=$parser->parse_file('xml/utenti.xml');
my $root=$document->getDocumentElement;
my @users=$root->findnodes("//utente[username='$username' and password='$password']");
my $nome=$users[0]->getElementsByTagName('nome');
my $cognome=$users[0]->getElementsByTagName('cognome');
my $email=$users[0]->getElementsByTagName('email');

# 3. GENERAZIONE PAGINA WEB
print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it"> 
<head> 
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Area riservata - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina di riepilogo delle informazioni associate ad un utente registrato" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film" name="keyword" />
    <title>Area riservata - Cinema Paradiso</title> 
    <link href="/style/screen.css" rel="stylesheet" type="text/css" media="screen" /> 
    <link href="/style/portable.css" rel="stylesheet" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)" /> 
    <link href="/style/print.css" rel="stylesheet" type="text/css" media="print" /> 
    <link rel="shortcut icon" href="/img/cinema.ico" /> 
</head> 
<body> 
	<p><a id="skip_nav" href="#content" title="Vai al contenuto" >Vai al contenuto</a></p> 
    <div id="header">
    	<h1><a href="/default.html" title="Pagina iniziale">Cinema Paradiso</a></h1> 
    	<h2>Programmazione e prenotazioni online</h2> 
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
    	<p>Sei in: Area riservata</p> 
    </div> 
    <div id="content">
	    <ul id="indice">
	    	<li><a href="#profilo">Dettagli profilo</a></li>
	    	<li><a href="#prenotazioni">Prenotazioni</a></li>
	    </ul>
	    <h3 id="profilo">Dettagli del profilo</h3>
    	<dl>
    		<dt>Nome</dt>
    		<dd>$nome</dd>
    		<dt>Cognome</dt>
    		<dd>$cognome</dd>
    		<dt>Nome utente</dt>
    		<dd>$username</dd>
    		<dt>Indirizzo di posta elettronica:</dt>
    		<dd>$email</dd>    			
    	</dl>
    	<p>
	    	<a href="/aggiorna_pwd.html" title="Cambia la password">Cambia password</a>
	    </p>
	    <h3 id="prenotazioni">Prenotazioni</h3>
HTML

my $user = $users[0];
my @prenotazioni = $user->getElementsByTagName('prenotazione');
if(!@prenotazioni) {
	print "\t\<p>Nessuna prenotazione effettuata.</p>";
} else {
print <<HTML;
		<p>$user - @prenotazioni</p>
	    <table summary="" title="Prenotazioni">
	    	<caption>Elenco delle prenotazioni effettuate</caption>
	    	<thead>
			<tr>
				<th>Film</th>
				<th>Spettacolo</th>
				<th>Numero di posti</th>
			</tr>
	    	</thead>
	    	<tfoot>
		   		<tr>
	    			<th>Film</th>
	    			<th>Spettacolo</th>
	    			<th>Numero di posti</th>
	    		</tr>
	    	</tfoot>
	    	<tbody>
HTML
	foreach $prenotazione (@prenotazioni) {
		my $id_spettacolo = $prenotazione->getChildrenByTagName('spettacolo');
		my $posti = $prenotazione->getChildrenByTagName('posti');
		
		my $parser=XML::LibXML->new();
		my $document=$parser->parse_file('xml/film.xml');
		my $root=$document->getDocumentElement;
		my @spettacolo=$root->findnodes("//spettacolo[\@id='$id_spettacolo']");
		my $data = $spettacolo[0]->getChildrenByTagName('data');
		my $ora = $spettacolo[0]->getChildrenByTagName('ora');
		my $film = ($spettacolo[0]->parentNode())->parentNode();
		my $titolo = $film->getChildrenByTagName('titolo');
print <<HTML;
				<tr>
					<td>$titolo</td>
					<td>$data $ora</td>
					<td>$posti</td>
				</tr>
HTML
	}
print "\t\t</tbody>\n\t</table>\n";
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
