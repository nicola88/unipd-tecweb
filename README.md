CINEMA PARADISO
===============

Organizzazione del contenuto
------------------------
- /: README, pagine statiche (*.html)
    - doc/: documentazione (norme di progetto, relazione, ...)
    - img/: immagini e favicon utilizzate (locandine, ...) 
    - script/: script e pagine dinamiche in JavaScript o Perl
    - style/: fogli di stile
    - xml/: documenti (utenti.xml, cinema.xml) e relativi schemi

Sito web
--------
- Pagina iniziale (*default.html*)
    - Area utente (*area_utente.html*)
        - Aggiorna password (*aggiorna_password[_nos].html*)
    - Film (*film.html*)
    - Informazioni (*informazioni.html*)
    - Programmazione (*programmazione.html*)
- Autenticazione (*login[_nos].html*)
- Registrazione (*registrazione[_nos].html*)

Le pagine del tipo <nome>[_nos].html sono disponibili in due versioni, a seconda che il browser supporto JS (*<nome>.html*) o meno (*<nome>_nos.html*);

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

Base di dati (xml)
------------------
