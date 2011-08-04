#!/usr/bin/perl

# nome -- descrizione
# QUERY_STRING: spettacolo=<id-spettacolo>
use CGI qw(:standard);
use XML::LibXML; # se usate XML

print "Content-type: text/html\n\n";

# Memorizza gli argomenti passati nella query string in variabili locali
my $cgi = new CGI;
my $spettacolo = $cgi->param('spettacolo'); # $input{'spettacolo'}; # ID spettacolo (XML)

# Validazione input query string
my $validationError=0;
# ERRORE 1: valore vuoto per l'elemento spettacolo
if(!$spettacolo) {
	$validationError=1;
}
# Leggo in XML le informazioni relative allo spettacolo (i dati letti da xml sono supposti validi e non richiedono controlli):
my $film = "Titolo film";
my $data = "03/07/2011";
my $ora = "09:30";
my $posti = 10;
my $maxPrenotazioni = 15; # Numero massimo di prenotazioni individuali
if($posti<$maxPrenotazioni) {
	$maxPrenotazioni = $posti;
}

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Prenotazione biglietti - Cinema Paradiso</title>
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
    	<p>Sei in: <a href="/default.html" title="">Pagina iniziale</a> &#187; Prenotazione biglietti</p>
    </div>
    <div id="content">
    	<h1>Prenotazione biglietti</h1>
    	<p>Codice errore: $validationError.</p>
    	<ul id="indice">
    		<li><a href="#spettacolo">Informazioni spettacolo</a></li>
    		<li><a href="#prenotazione">Informazioni prenotazione</a></li>
    	</ul>
    	<h2 id="spettacolo">Informazioni spettacolo</h2>
    	<dl>
    		<dt>Film</dt>
    		<dd>$film</dd>
    		<dt>Giorno</dt>
    		<dd>$data</dd>
    		<dt>Ora</dt>
    		<dd>$ora</dd>
    	</dl>
    	<h2 id="prenotazione">Informazioni prenotazione</h2>
    	<form action="" method="post">
    		<fieldset>
    			<legend>Seleziona il numero di biglietti</legend>
    			<label for="posti">Posti da prenotare</label>
    			<select id="posti" name="posti">
HTML
for($count=1; $count <= $maxPrenotazioni; $count++) {
	print "\t\t\t\t<option>$count</option>\n";
}
print <<HTML
    			</select>
    			<input type="hidden" name="spettacolo" id="spettacolo" value="$spettacolo" />
    			<input type="submit" value="Conferma la prenotazione" />
    		</fieldset>
    </div>
    <div id="footer">
    	<a href="http://validator.w3.org/check?uri=referer"><span id="xhtml_valid" title="HTML 1.0 Strict valido"></span></a>
    	<span id="css_valid" title="CSS 2.1 valido"></span>
    	<p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p>
    </div>
</body>
</html>
HTML
