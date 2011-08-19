#!/usr/bin/perl

# nome -- descrizione
# QUERY_STRING: spettacolo=<id-spettacolo>
use CGI qw(:standard);
use XML::LibXML; # se usate XML

print "Content-type: text/html\n\n";
