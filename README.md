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
Viene riportata di seguito la struttura gerarchica del sito web: per ciascuna pagina è riportato un titolo breve e - tra parentesi - il nome del file corrispondente; i nomi di file privi di estensione sono da intendersi pagine dinamiche generate mediante script Perl.
 
- Pagina iniziale (default.html)
    - Film (film.html)
        - Scheda film (scheda)
            - Prenotazione biglietti (prenotazione + prenotazione_conferma)
    - Programmazione (programmazione.html)
    - Informazioni (informazioni.html)
    - Notizie (notizie)    
    - Area utente (account)
        - Cambia password (aggiorna_pwd.html | aggiorna_pwd_nos.html) + (aggiorna_pwd_conferma)
- Login (login.html | login_nos.html)
    - Controllo sessione (controlla_sessione)
- Registrazione (registrazione.html | registrazione_nos.html) + (registrazione_conferma)

Le pagine disponibili in duplice versione (con o prive del suffisso _nos) sono accessibili sia in browser con supporto JavaScript abilitato sia disabilitato o non supportato.

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
