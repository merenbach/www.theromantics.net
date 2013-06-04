#!/usr/bin/perl

use strict;

require '../cgi-bin/header.cgi';
require '../cgi-bin/footer.cgi';

print_header('the-ball');

print <<EOF;
	<article>
		<p>The marriage of Elizabeth Cheney and Andrew Merenbach will occur upon the 11<sup>th</sup> of May, 2013, at the Culver Hotel in Culver City, California. The ceremony begins at 11 A.M. with the reception, including luncheon and dancing, to follow.</p>
	</article>
EOF

print_footer();
