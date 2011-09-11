#!/usr/bin/perl

# prenotazione.cgi
# QUERY_STRING: spettacolo=<id-spettacolo>
use CGI qw(:standard);
use CGI::Session;
use XML::LibXML; # se usate XML

$session=CGI::Session->load();
if($session->is_expired || $session->is_empty) {
    die("Nessun utente autenticato. La procedura di prenotazione biglietti è fallita. Si prega di autenticarsi e ripetere la procedura.");
}

# LETTURA QUERY STRING
my $cgi = new CGI;
my $id = $cgi->param('spettacolo');
my $posti = $cgi->param('posti');
my $username = $session->param('username');

# SCRITTURA XML
my $parser=XML::LibXML->new();
my $document=$parser->parse_file('xml/utenti.xml');
my $root=$document->getDocumentElement;
my @prenotazioni=$root->findnodes("//utente[username='$username']/prenotazioni");
my $parent = $prenotazioni[0];


# Controllo se esiste una prenotazione precedente per lo stesso spettacolo (id)
# Se c'è semplicemente aggiungo i posti a quelli esistenti, altrimenti creo un nodo prenotazione nuovo
my @prenotazione=$parent->findnodes("//prenotazione[spettacolo='$id']");
if (@prenotazione) {
	# Se c'è la prenotazione
	# aggiungi i posti nella prenotazione
	$posti_tot = $prenotazione[0]->getChildrenByTagName('posti');
	$posti_tot = int($posti_tot) + int($posti) ;
	my @node=$prenotazione[0]->findnodes("//posti/text()");
    $node[0]->setData($posti_tot);
    open(OUT,">xml/utenti.xml");
    print OUT $document->toString;
    close(OUT);
}
else {
	# Se non c'è la prenotazione la creo come figlio di $parent
	my $prenotazione="\t\t\t<prenotazione>\n\t\t\t\t<spettacolo>$id</spettacolo>\n\t\t\t\t<posti>$posti</posti>\n\t\t\t</prenotazione>\n";
	my $fragment=$parser->parse_balanced_chunk($prenotazione);
	$parent->appendChild($fragment);
	open(OUT,">xml/utenti.xml");
	print OUT $document->toString;
	close(OUT);
}

# Aggiorno il numero di posti disponibili in film.xml
$document=$parser->parse_file('xml/film.xml');
$root=$document->getDocumentElement;
my $posti_disponibili=$root->findnodes("//spettacolo[\@id='$id']/posti");
$posti_disponibili = int($posti_disponibili) - int($posti);
my @value = $root->findnodes("//spettacolo[\@id='$id']/posti/text()");
$value[0]->setData($posti_disponibili);
open(OUT,">xml/film.xml");
print OUT $document->toString;
close(OUT); 

# TODO
# Manca di dare un messaggio che sono stati prenotati con successo # posti per lo spettacolo del giorno voluto ...

# Altro problema è che se si prenotano + posti di quelli disponibili il numero va in negativo
# quindi nel form spettacolo bisogna controllare che i posti disponibili siano > di quelli che si vuole prenotare altrimenti viene 
# segnalato un errore e si ritorna alla pagina

# In pratica devo fare questo codice e stampargli a video un messaggio sullo script spettacolo 
# $document=$parser->parse_file('xml/film.xml');
# $root=$document->getDocumentElement;
# my @node=$root->findnodes("//spettacolo[\@id='$id']/posti/text()");
# my $posti_rimanenti=int(@node[0])
# if ($posti > $posti_rimanenti)
#	Segnala errore
# else
#   fai la prenotazione

print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Prenotazione biglietti - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina dedicata all'elaborazione della richiesta di prenotazione dei biglietti" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film, biglietti, spettacoli, proiezioni" name="keyword" />
    <title>Prenotazione biglietti - Cinema Paradiso</title>
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
    <div id="account">
        <p><a href="account.cgi" accesskey="8" title="Area riservata">Area riservata</a> | <a href="../registrazione.html" accesskey="9" title="Registrazione">Registrati</a></p>
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
        <p>Sei in: <a href="../default.html">Pagina iniziale</a> &#187; <a href="../programmazione.html">Programmazione</a> &#187; Prenotazione biglietti</p>
    </div>
    <div id="content">
        <h1>Prenotazione biglietti</h1>
        <p>Prenotazione effettuata con successo. Per consultarla, accedere <a href="account.cgi" title="Area riservata">all'area riservata</a>.</p>
    </div>
    <div id="footer">
        <p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p>
    </div>
</body>
</html>
HTML
