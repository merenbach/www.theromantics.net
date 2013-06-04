#!/usr/bin/perl

use strict;

require '../header.cgi';
require '../footer.cgi';

# Header
print_header('page-not-found');

# Content
print <<EOF;
	<p class="lead">Permit me to suggest that you have perhaps read too far ahead.  Please consider returning to a previous chapter.</p>
EOF

# Footer
print_footer();

