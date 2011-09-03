#!/usr/bin/perl

######################################################
# NOME: PRENOTAZIONE.cgi
######################################################
# DESCRIZIONE: pagina dedicata alla prenotazione di un
# posto per uno spettacolo
######################################################
# QUERY STRING: id=<id-spettacolo>
######################################################
# TO DO: conversione in intero del numero di posti letto da XML
######################################################

use HTML::Entities;
use XML::LibXML; # se usate XML
use CGI;
print "Content-type: text/html\n\n";

# LETTURA INPUT
my $cgi = new CGI;
my $id = $cgi->param('id'); # $input{'spettacolo'}; # ID spettacolo (XML)

# 1. GESTIONE SESSIONE
#$session=CGI::Session->load();
#if($session->is_expired || $session->is_empty){
#    print "Location: login.cgi?source=$id\n\n";
#}

# 2. LETTURA INFORMAZIONI da XML
my $parser=XML::LibXML->new();
my $document=$parser->parse_file('xml/film.xml');
my $root=$document->getDocumentElement;
@spettacolo=$root->findnodes("//spettacolo[\@id='$id']");

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="Dettagli spettacolo - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Mostra informazioni dettagliate sullo spettacolo selezionato" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film" name="keyword" />
    <title>Dettagli spettacolo - Cinema Paradiso</title>
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
        <p>Sei in: <a href="../default.html" title="">Pagina iniziale</a> &#187; Dettagli spettacolo</p>
    </div>
    <div id="content">
        <h1>Dettagli spettacolo</h1>
HTML

if(@spettacolo) {
	# Informazioni spettacolo
	my $data = $spettacolo[0]->getChildrenByTagName('data');
	my $ora = $spettacolo[0]->getChildrenByTagName('ora');
	my $posti = $spettacolo[0]->getChildrenByTagName('posti');
	# Titolo film
	my $film = ($spettacolo[0]->parentNode())->parentNode();
	my $titolo = $film->getChildrenByTagName('titolo');
	$titolo = encode_entities($titolo);
	my $maxPrenotazioni = 15; # Numero massimo di prenotazioni individuali
	$posti = int($posti);
	if($posti < $maxPrenotazioni) {$maxPrenotazioni = $posti;}
print <<HTML;
        <dl>
            <dt>Film</dt>
            <dd>$titolo</dd>
            <dt>Giorno</dt>
            <dd>$data</dd>
            <dt>Ora</dt>
            <dd>$ora</dd>
            <dt>Posti disponibili</dt>
            <dd>$posti</dd>
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
print <<HTML;
                </select>
                <input type="hidden" name="spettacolo" id="spettacolo" value="$id" />
                <input type="submit" value="Prenota biglietti" />
            </fieldset>
HTML
} else {
	print "\t\t<p>Spettacolo non disponibile.</p>\n";	
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
