#!/usr/bin/perl

# Notizie -- pagina dedicata alla visualizzazione delle notizie
use XML::LibXML; # se usate XML

print "Content-type: text/html\n\n";

print <<HTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it" xml:lang="it">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Pagina - Cinema Paradiso</title>
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
    	<p>Sei in: <a href="/default.html" title="">Pagina iniziale</a> &#187; pagina_corrente</p>
    </div>
    <div id="content">
    	<h1>Notizie</h1>
    	<ul id="indice">
    		<li><a href="#uscite">Film e programmazione</a></li>
    		<li><a href="#eventi">Eventi</a></li>
    		<li><a href="#avvisi">Avvisi generali</a></li>
    	</ul>
    	<h2 id="uscite">Film e programmazione</h2>
    	<div class="notizia">
    		<h3><span class="data" title="22 novembre 2005">22/11/2006</span> - Casino Royale da domani al cinema.</h3>
    		<p>Esce domani al cinema <span lang="en" xml:lang="en"><em>Casino Royale</em></span> con 3 proiezioni:
    		alle ore xx, yy e zz. Per conoscere gli orari degli spettacoli per la prossima settimana, consultare la pagina dedicata alla
    		<a href="/programmazione.html" title="Programmazione">programmazione</a>.
    		</p>
    	</div>
    	<h2 id="eventi">Eventi</h2>
    	<h2 id="avvisi">Avvisi generali</h2>
    	<div class="notizia">
    		<h3><span class="date" title="11 luglio 2011">11/07/2011</span> - Rilascio al pubblico della versione di anteprima del sito.</h3>
    		<p>&Egrave; accessibile al pubblico la versione di anteprima del nuovo sito del <em>Cinema Paradiso</em>. Nei prossimi giorni
    		verranno introdotte nuove funzionalità al fine di offrirVi un servizio migliore; chiunque lo desideri, può già provarlo e farci sapere
    		il suo giudizio.
    		</p>
    	</div>
    </div>
    <div id="footer">
    	<a href="http://validator.w3.org/check?uri=referer"><span id="xhtml_valid" title="HTML 1.0 Strict valido"></span></a>
    	<span id="css_valid" title="CSS 2.1 valido"></span>
    	<p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p>
    </div>
</body>
</html>
HTML
