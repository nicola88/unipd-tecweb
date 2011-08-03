#!/usr/bin/perl

# Scheda film -- pagina per visualizzazione della scheda di un film
# QUERY_STRING: film=<id_film>
use XML::LibXML; # se usate XML

print "Content-type: text/html\n\n";

# VARIABILI
my $attori = "Lista degli attori";
my $durata = "Durata (in min.)";
my $genere = "Genere";
my $nazione = "Nazione";
my $regista = "Regista";
my $titolo = "Titolo film";
my $anno = "Anno";
my $tagline = "Everyone has a past. Every legend has a beginning.";
my $locandina = "http://placehold.it/160x240"; # Nome locandina = <id_film>

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>$titolo - Cinema Paradiso</title>
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
    	<p>Sei in: <a href="/default.html">Pagina iniziale</a> &#187; <a href="/film.html">Film</a> &#187; $titolo</p>
    </div>
    <div id="content">
    	<h1>$titolo ($anno)</h1>
    	<blockquote id="tagline"><p>
			 $tagline
		</p></blockquote>
		<img class="locandina" src="$locandina" alt="Locandina '$titolo'" height="240" width="160" />
		<dl class="scheda">
			<dt>Titolo:</dt>
			<dd>$titolo</dd>
			<dt>Genere:</dt>
			<dd>$genere</dd>
			<dt>Regista:</dt>
			<dd>$regista</dd>
			<dt>Attori:</dt>
			<dd>$attori</dd>
			<dt>Nazionalità (anno):</dt>
			<dd>$nazione ($anno)</dd>
			<dt>Durata:</dt>
			<dd>$durata</dd>
		</dl>
   		<p class="link">
   			<a href="/programmazione.html">Orario spettacoli</a>
   		</p>
		<h2>Descrizione</h2>
		<p>
			James Bond &egrave; ancora privo della licenza di uccidere, ma non per questo meno pericoloso. Due omicidi da professionista
			in rapida successione gli valgono la promozione al rango di &quot;00&quot;. Nella sua prima missione, il neoagente 007
			viene inviato da M, capo dei servizi segreti britannici, in Madagascar, alle Bahamas e infine in Montenegro. Qui Bond deve vedersela
			con Le Chiffre, uno spregiudicato banchiere minacciato dalle organizzazioni terroristiche che finanzia. Nel tentativo di raccogliere
			i fondi di cui ha bisogno, Le Chiffre organizza una partita di poker con una posta molto alta al Casino Royale. M incarica
			l'avvenente agente del Tesoro Vesper Lynd di tenere d'occhio Bond. Sulle prime scettico circa il contributo di Vesper alla missione,
			Bond vede crescere il proprio interesse nei confronti della sua partner man mano che insieme affrontano i pericoli. Messo a dura prova
			insieme alla compagna dall'astuzia e dalla crudeltà di Le Chiffre, Bond impara la lezione più importante: mai fidarsi di nessuno.
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