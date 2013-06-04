#!/usr/bin/perl

use strict;

require '../../cgi-bin/header.cgi';
require '../../cgi-bin/footer.cgi';

print_header('rsvp');

print <<EOF;
	<div class="box">
		<div class="row-fluid">
			<div class="span10 offset1">
				<header class="clearfix">
					<img src="/img/JaneAustenSilhouette.png" alt="Jane Austen" class="pull-left span2 hidden-phone">
					<p class="lead">Come celebrate with us!</p>
					<p class="info muted">Kindly respond by April 4<sup>th</sup>, 2013.</p>
				</header>
				<br>
				<p>So good of you to drop by! Here are some details regarding your party.</p>
				<p>The following guests are listed as planning to attend:</p>
				<ul class="unstyled text-center">
					<li>Elizabeth Bennett</li>
					<li>Fitzwilliam Darcy</li>
				</ul>
				<p>If you need to make any changes to your invitation, please feel free to get in touch with us.</p>
			</div> 
		</div> 
	</div>
EOF

print_footer();
