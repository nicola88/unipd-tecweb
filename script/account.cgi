#!/usr/bin/perl

# account -- Visualizza la pagina riservata con dati personali e prenotazioni effettuate
# QUERY_STRING: formato della QUERY_STRING (lista argomenti e valori)
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
	    <p>
	    	<dl>
	    		<dt>Nome:</dt>
	    		<dd>nome</dd>
	    		<dt>Cognome:</dt>
	    		<dd>cognome</dd>
	    		<dt>Nome utente</dt>
	    		<dd>username</dd>
	    		<dt>Indirizzo di posta elettronica:</dt>
	    		<dd>mail</dd>    			
	    	</dl>
	    	<a href="/aggiorna_pwd.html" title="Cambia la password">Cambia password</a>
	    </p>
	    <h3 id="prenotazioni">Prenotazioni</h3>
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
	    		<!-- Nessuna prenotazione -->
	    		<tr>
	    			<td colspan="3">Nessuna prenotazione effettuata.</td>
	    		</tr>
	    	</tbody>
	    </table>
    </div> 
    <div id="footer"> 
    	<a href="http://validator.w3.org/check?uri=referer"><span id="xhtml_valid" title="HTML 1.0 Strict valido"></span></a> 
    	<span id="css_valid" title="CSS 2.1 valido"></span> 
    	<p>Cinema Paradiso - Via Guardiani della Notte, 15 (AR)</p> 
    </div> 
</body> 
</html>
HTML