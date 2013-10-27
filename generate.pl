#!/usr/bin/perl

use strict;
use warnings;

use File::Copy;
use File::Path;

my @dirs = (
	'css',
	'img',
	'js',
	'ball',
	'rsvp',
	'rsvp/read',
	'rsvp/respond'
);

my @assets = (
    'favicon.ico',
	'favicon.png',
	'.htaccess',
	'robots.txt',
	'css/bootstrap.ab842b0d47da.css',
	'css/print.css',
	'css/responsive.fb6dbb18c21f.css',
	'css/rsvp.css',
	'css/screen.css',
	'js/bootstrap.min.js',
	'js/jquery-1.9.1.js',
	'img/glyphicons-halflings.png',
	'img/glyphicons-halflings-white.png',
	'img/JaneAustenSilhouette.png'
);

my @templates = (
    'index.html',
	'ball/index.html',
	'rsvp/index.html',
	'rsvp/read/index.html',
	'rsvp/respond/index.html'
);


mkpath "public/$_" foreach (@dirs);

foreach (@assets) {
	copy("source/$_", "public/$_") or die "Copy $_ failed! $!";
}

foreach (@templates) {
	system("python render.py '$_' > 'public/$_'");
}

system("perl compress-static.pl public");
