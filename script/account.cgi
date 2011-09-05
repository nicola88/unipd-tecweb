#!/usr/bin/perl

# NOME
# account.cgi

# DESCRIZIONE
# Visualizza le informazioni del profilo e le prenotazioni dell'utente corrente.

# QUERY STRING
# vuota

use CGI;
use CGI::Session;
use XML::LibXML;
use HTML::Entities;

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
	# (2) RECUPERO INFORMAZIONI UTENTE
	# Recupero e visualizzo le informazioni personali e le prenotazioni
	#  dell'utente.
	my $username=$session->param('username');
	my $password=$session->param('password');
	my $parser=XML::LibXML->new();
	my $document=$parser->parse_file('xml/utenti.xml');
	my $root=$document->getDocumentElement;
	my @users=$root->findnodes("//utente[username='$username' and password='$password']");
	my $name=$users[0]->getElementsByTagName('nome');
	my $surname=$users[0]->getElementsByTagName('cognome');
	my $email=$users[0]->getElementsByTagName('email');
	$name=encode_entities($name);
	$surname=encode_entities($surname);
	$username=encode_entities($username);
	$email=encode_entities($email);
	print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it"> 
<head> 
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Area riservata - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina di riepilogo delle informazioni associate ad un utente registrato" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film, biglietti, spettacoli, proiezioni" name="keyword" />
    <title>Area riservata - Cinema Paradiso</title> 
    <link href="../style/screen.css" rel="stylesheet" type="text/css" media="screen" /> 
    <link href="../style/portable.css" rel="stylesheet" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)" /> 
    <link href="../style/print.css" rel="stylesheet" type="text/css" media="print" /> 
    <link rel="shortcut icon" href="../img/cinema.ico" /> 
</head> 
<body> 
	<p><a id="skip_nav" href="#content" title="Vai al contenuto" >Vai al contenuto</a></p> 
    <div id="header">
    	<h1><a href="../default.html" title="Pagina iniziale">Cinema Paradiso</a></h1> 
    	<h2>Programmazione e prenotazioni online</h2> 
    </div> 
    <div id="navigation">
    	<ul>
        	<li><a href="../default.html" accesskey="0">Pagina iniziale</a>
        	</li>
            <li><a href="../film.html" accesskey="1">Film</a>
            </li>
            <li><a href="../programmazione.html" accesskey="2">Programmazione</a>
            </li>
            <li><a href="../informazioni.html" accesskey="3">Informazioni</a>
            </li>
            <li><a href="notizie.cgi" accesskey="4">Notizie</a>
            </li>
        </ul>
    </div>
    <div id="path"> 
    	<p>Sei in: Area riservata</p> 
    </div> 
    <div id="content">
    	<h1>Il tuo account</h1>
	    <ul id="indice">
	    	<li><a href="#profilo">Dettagli profilo</a></li>
	    	<li><a href="#prenotazioni">Prenotazioni</a></li>
	    </ul>
	    <h2 id="profilo">Dettagli del profilo</h2>
    	<dl>
    		<dt>Nome:</dt>
    		<dd>$name</dd>
    		<dt>Cognome:</dt>
    		<dd>$surname</dd>
    		<dt>Nome utente:</dt>
    		<dd>$username</dd>
    		<dt>Indirizzo di posta elettronica:</dt>
    		<dd>$email</dd>    			
    	</dl>
    	<p class="link">
	    	<a href="../aggiorna_pwd.html" title="Cambia la password">Cambia password</a>
	    </p>
	    <h2 id="prenotazioni">Prenotazioni</h2>
HTML
	# NOTA IMPORTANTE: se non è associata alcuna prenotazione all'utente, è
	# visualizzata la stringa 'Nessuna prenotazione effettuata.', altrimenti è
	# visualizzata una tabella a tre colonne (film, spettacolo, posti prenotati)
	# contenente le prenotazioni.
	my @bookings=$root->findnodes("//utente[username='$username' and password='$password']/prenotazioni/prenotazione");
	if(@bookings){
print <<HTML;
	    <table summary="Elenco delle prenotazioni associate all'utente: film, data e ora dello spettacolo e numero di posti prenotati" title="Prenotazioni">
	    	<caption>Elenco delle prenotazioni effettuate</caption>
	    	<thead>
			<tr>
				<th scope="col" id="film">Film</th>
				<th scope="col" id="spettacolo" abbr="spett">Spettacolo</th>
				<th scope="col" id="posti">Numero di posti</th>
			</tr>
	    	</thead>
	    	<tfoot>
		   		<tr>
	    			<th scope="col">Film</th>
	    			<th scope="col">Spettacolo</th>
	    			<th scope="col">Numero di posti</th>
	    		</tr>
	    	</tfoot>
	    	<tbody>
HTML
		$document=$parser->parse_file('xml/film.xml');
		$root=$document->getDocumentElement;
		for($i=0;$i<=$#bookings;$i++){
			my $id=$bookings[$i]->getElementsByTagName('spettacolo');
			my $seats=$bookings[$i]->getElementsByTagName('posti');
			my @show=$root->findnodes("//spettacolo[\@id='$id']");
			my $date=$show[0]->getElementsByTagName('data');
			$date = &date_format_conversion($date);
			my $time=$show[0]->getElementsByTagName('ora');
			$time = substr($time,0,-3);
			my $film=($show[0]->parentNode())->parentNode();
			my $title=$film->getElementsByTagName('titolo');
			$title=encode_entities($title);
			$date=encode_entities($date);
			$time=encode_entities($time);
			$seats=encode_entities($seats);
print <<HTML;
				<tr>
					<td headers="film">$title</td>
					<td headers="spettacolo">$date alle $time</td>
					<td headers="posti">$seats</td>
				</tr>
HTML
		}
		print "\t\t</tbody>\n\t</table>\n";
	}
	else{
		print "\t\t<p>Nessuna prenotazione effettuata.</p>";
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
}

sub date_format_conversion{
	my $xml_data = $_[0];
	my $data = substr($xml_data,8,2) . "-" . substr($xml_data,5,2) . "-" . substr($xml_data,0,4);
	return $data;
}
