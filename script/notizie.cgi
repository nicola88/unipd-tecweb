#!/usr/bin/perl

######################################################
# NOME: notizie.cgi
######################################################
# DESCRIZIONE: visualizzazione delle notizie (per categorie)
######################################################
# QUERY STRING: vuota
######################################################
use CGI;
use Encode;
use HTML::Entities;
use XML::LibXML;
print "Content-type: text/html\n\n";

# 1. LETTURA INFORMAZIONI da XML
my $parser=XML::LibXML->new();
my $document=$parser->parse_file('xml/notizie.xml');
my $root=$document->getDocumentElement;
my @notizie_film=$root->findnodes("//notizia[categoria/text()=\"Programmazione\"]");
my @notizie_eventi=$root->findnodes("//notizia[categoria/text()=\"Eventi\"]");
my @notizie_avvisi=$root->findnodes("//notizia[categoria/text()=\"Avvisi\"]");

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Notizie - Cinema Paradiso</title>
    <meta content="Notizie - Cinema Paradiso" name="title" />
    <meta content="Alberto Maragno, Alessandro Benetti, Nicola Moretto" name="author" />
    <meta content="Pagina riservata alle notizie, suddivise in avvisi, eventi e programmazione" name="description" />
    <meta content="Cinema Paradiso" name="copyright" />
    <meta content="cinema, paradiso, programmazione, film, biglietti, spettacoli, proiezioni" name="keyword" />
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
            <li id="current">Notizie
            </li>
        </ul>
    </div>
    <div id="path">
        <p>Sei in: <a href="../default.html" title="">Pagina iniziale</a> &#187; Notizie</p>
    </div>
    <div id="content">
        <h1>Notizie</h1>
        <ul id="indice">
            <li><a href="#uscite">Film e programmazione</a></li>
            <li><a href="#eventi">Eventi</a></li>
            <li><a href="#avvisi">Avvisi generali</a></li>
        </ul>
HTML

print "\t\t<h2 id=\"uscite\">Film e programmazione</h2>\n";
	if(@notizie_film) {
		foreach $notizia (@notizie_film) {
			my $data = $notizia->getChildrenByTagName('data');
			my $titolo = $notizia->getChildrenByTagName('titolo');
			$titolo = encode_entities($titolo);
			my $descrizione = encode("utf-8",$notizia->getChildrenByTagName('descrizione'));
			$descrizione = encode_entities($descrizione);
print <<HTML;
		<div class="notizia">
			<h3><span class="data">$data</span> - $titolo</h3>
			<p>
				$descrizione
			</p>
		</div>
HTML
		}
	} else {
		print "\t\t<p>Nessuna notizia disponibile.</p>\n";
	}

print "\t\t<h2 id=\"eventi\">Eventi</h2>\n";
	if(@notizie_eventi) {
		foreach $notizia (@notizie_eventi) {
			my $data = $notizia->getChildrenByTagName('data');
			my $titolo = $notizia->getChildrenByTagName('titolo');
			$titolo = encode_entities($titolo);
			my $descrizione = $notizia->getChildrenByTagName('descrizione');
			$descrizione = encode_entities($descrizione);
print <<HTML;
		<div class="notizia">
			<h3><span class="data">$data</span> - $titolo</h3>
			<p>
				$descrizione
			</p>
		</div>
HTML
		}
	} else {
		print "\t\t<p>Nessuna notizia disponibile.</p>\n";
	}

print "\t\t<h2 id=\"avvisi\">Avvisi generali</h2>\n";
	if(@notizie_avvisi) {
		foreach $notizia (@notizie_avvisi) {
			my $data = $notizia->getChildrenByTagName('data');
			my $titolo = $notizia->getChildrenByTagName('titolo');
			$titolo = encode_entities($titolo);
			my $descrizione = $notizia->getChildrenByTagName('descrizione');
			$descrizione = encode_entities($descrizione);
print <<HTML;
		<div class="notizia">
			<h3><span class="data">$data</span> - $titolo</h3>
			<p>
				$descrizione
			</p>
		</div>
HTML
		}
	} else {
		print "\t\t<p>Nessuna notizia disponibile.</p>\n";
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
