CINEMA PARADISO
===============

Organizzazione del contenuto
------------------------
- /: README, pagine statiche (*.html)
    - doc/: documentazione (norme di progetto, relazione, ...)
    - img/: immagini e favicon utilizzate (locandine, ...) 
    - script/: script e pagine dinamiche in JavaScript o Perl
    - style/: fogli di stile
    - template/: modelli per pagine statiche (html) e dianmiche (perl)
    - xml/: documenti (utenti.xml, cinema.xml) e relativi schemi

Struttura
---------
Viene riportata di seguito la struttura gerarchica del sito web: per ciascuna pagina è riportato un titolo breve e - tra parentesi - il nome del file corrispondente.
 
- Pagina iniziale (default.html)
    - Film (film.html)
        - Scheda film (scheda.cgi)
            - Spettacolo (spettacolo.cgi)
	            - Prenotazione biglietti (prenotazione.cgi + prenotazione_conferma.cgi)
    - Programmazione (programmazione.html)
    - Informazioni (informazioni.html)
    - Notizie (notizie.cgi)    
    - Area utente (account.cgi)
        - Cambia password (aggiorna_pwd.html + aggiorna_pwd_conferma.cgi)
- Login (login.cgi)
- Registrazione (registrazione.html | registrazione_nos.html) + (registrazione_conferma)

Documentazione (doc)
--------------------
- **guida-configurazione.odt**: guida e consigli per la configurazione dell'ambiente di lavoro (Mercurial & Bitbucket, Eclipse IDE, XAMPP Web Server, ...);
- **norme-progetto.odt**: norme e convenzioni di lavoro;
- **relazione.odt**: relazione finale destinata alla consegna;

Immagini (img)
--------------

Pagine dinamiche (script)
-------------------------

Presentazione (style)
---------------------
- **screen.css**
- **portable.css**
- **print.css**

Modelli (template)
------------------
- **xhtml.html**
- **perl**

Base di dati (xml)
------------------
