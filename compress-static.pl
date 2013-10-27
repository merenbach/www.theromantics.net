#!/usr/bin/perl
#
# Compress and rename static assets
#
# Adapted from <http://northtonowhere.com/2013/04/03/gzipping-octopress/>
# Find command: <http://perldoc.perl.org/File/Find.html>

# This script is run prior to upload

use warnings;
use strict;

my $dir_path = (scalar(@ARGV) == 0) ? '.' : "$ARGV[0]";

use File::Find;

find (\&wanted, ("$dir_path"));
sub wanted {
    if (/(.*\.(?:html|css|js|xml|txt)$)/i) {
        print "Compressing $File::Find::name\n";
        if (! -f "$_.en.gz" or -M "$_.en.gz" > -M "$_") {
            system ("gzip --best --force --stdout $_ > $_.en.gz");
        }
        rename "$_", "$_.en";
    }
}
