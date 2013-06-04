#!/usr/bin/perl

use strict;

require '../cgi-bin/header.cgi';
require '../cgi-bin/footer.cgi';

print_header('rsvp');

print <<EOF;
	<div class="box">
		<p class="lead">Elizabeth Bennet &amp; Fitzwilliam Darcy</p>
		<p class="info"><a href="/rsvp/read/">Open</a></p>
	</div>
EOF

print_footer();
