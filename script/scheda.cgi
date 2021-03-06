#!/usr/bin/perl

######################################################
# NOME: scheda.cgi
######################################################
# DESCRIZIONE: visualizza la scheda di un film
######################################################
# QUERY STRING: film=<id_film>
######################################################
# TO DO: titolo e path pagina in caso di film assente
######################################################
use CGI;
use CGI::Session;
use HTML::Entities;
use XML::LibXML;
print "Content-type: text/html\n\n";

# 1. LETTURA INPUT
my $cgi=new CGI;
my $id = $cgi->param('film');

# 3. LETTURA INFORMAZIONI da XML
# Recupera le informaziomi sul film richiesto dal file XML
my $parser=XML::LibXML->new();
my $document=$parser->parse_file('xml/film.xml');
my $root=$document->getDocumentElement;
my @lista = $root->findnodes("//film[\@id='$id']");
if(@lista) {
	$film = $lista[0];
	@titolo = $film->getChildrenByTagName('titolo');
	$lang_titolo = $titolo[0]->getAttribute('lang');
	$titolo = $titolo[0]->textContent();
} else {
	$titolo = "Film non disponibile";
}

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta content="$titolo - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="$titolo: informazioni dettagliate e orari degli spettacoli" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film, biglietti, spettacoli, proiezioni" name="keyword" />
    <title>$titolo - Cinema Paradiso</title>
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
        <p>Sei in: <a href="../default.html">Pagina iniziale</a> &#187; <a href="../film.html">Film</a> &#187; $titolo</p>
    </div>
    <div id="content">
HTML

if(@lista) {
	my @attori = $film->findnodes("cast/attore");
	my $durata = $film->getChildrenByTagName('durata');
	my @genere = $film->findnodes("generi/genere");
	my $nazione = $film->getChildrenByTagName('nazione');
	my @regista = $film->getChildrenByTagName('regista');
	my $lang_regista = $regista[0]->getAttribute('lang');
	my $anno = $film->getChildrenByTagName('anno');
	my $tagline = $film->getChildrenByTagName('tagline');
	my $locandina = "../img/" . $id . ".jpg"; # Nome locandina = <id_film>
	my $trama = $film->getChildrenByTagName('trama');
	$titolo = encode_entities($titolo);
	$tagline = encode_entities($tagline);
	$trama = encode_entities($trama);
	$regista = encode_entities($regista[0]->textContent());
	$nazione = encode_entities($nazione);
	if($lang_titolo ne "it") {print "\t\t<h1 lang=\"$lang_titolo\" xml:lang=\"$lang_titolo\">$titolo</h1>\n";}
	else {print "\t\t<h1>$titolo</h1>\n";}
print <<HTML;
        <blockquote id="tagline"><p>
             $tagline
        </p></blockquote>
        <img class="locandina" src="$locandina" alt="Locandina '$titolo'" height="240" width="160" />
        <dl class="scheda">
            <dt>Titolo:</dt>
HTML
	if($lang_titolo ne "it") {print "\t\t\t<dd lang=\"$lang_titolo\" xml:lang=\"$lang_titolo\">$titolo</dd>\n";}
	else {print "\t\t\t<dd>$titolo</dd>\n";}
	print "\t\t\t<dt>Genere:</dt>\n\t\t\t\t<dd>";
	$lista_generi = "";
	foreach $value (@genere) {$value=$value->textContent(); $value = encode_entities($value); $lista_generi = $lista_attori . "$value, ";}
	$lista_generi = substr($lista_generi,0,-2);
	print "$lista_generi</dd>\n\t\t\t<dt>Regista:</dt>\n";
	
	if($lang_regista ne "it") {print "\t\t\t<dd lang=\"$lang_regista\" xml:lang=\"$lang_regista\">$regista</dd>\n";}
	else {print "\t\t\t<dd>$regista</dd>\n";}
	
	print "\t\t\t<dt>Attori:</dt>\n\t\t\t\t<dd>";
	$lista_attori = "";
	foreach $attore (@attori) {
		$lang_attore = $attore->getAttribute('lang');
		$value=$attore->textContent();
		$value = encode_entities($value);
		if($lang_attore ne "it") {$lista_attori = $lista_attori . "<span lang=\"$lang_attore\" xml:lang=\"$lang_attore\">$value</span>, ";}
		else {$lista_attori = $lista_attori . "$value, ";}
	}
	$lista_attori = substr($lista_attori,0,-2);
	print "$lista_attori</dd>\n";
print <<HTML;
			<dt>Nazionalità (Anno):</dt>
            <dd>$nazione ($anno)</dd>
            <dt>Durata:</dt>
            <dd>$durata minuti</dd>
        </dl>
        <p class="link">
            <a href="../programmazione.html">Orario spettacoli</a>
        </p>
        <h2>Descrizione</h2>
        <p>$trama
        </p>
HTML
} else {
	print "\t\t<p>Nessun film disponibile.</p>";		
}

print <<HTML;
    </div>
    <div id="footer">
        <p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p>
    </div>
</body>
</html>
HTML
