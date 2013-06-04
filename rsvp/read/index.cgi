#!/usr/bin/perl

use strict;

require '../../cgi-bin/header.cgi';
require '../../cgi-bin/footer.cgi';

print_header('rsvp');

print <<EOF;
	<div class="box">
	<div class="row-fluid">
	<blockquote class="clearfix">
	<img src="/img/JaneAustenSilhouette.png" alt="Jane Austen" class="pull-left span2 hidden-phone">
	<p class="lead">&ldquo;To be fond of dancing was a certain step towards falling in love&rdquo;</p>
	<p class="lead"><small class="text-info">Jane Austen, <cite class="title"><em>Pride and Prejudice</em></cite></small></p>
	</blockquote>
	<p class="lead">
	Elizabeth Cheney
	<br>
	&amp;
	<br>
	Andrew Merenbach
	</p>
	<p class="info">
	request the pleasure of your company at the celebration of their marriage
	<br>
	at
	<br>
	eleven o&rsquo;clock
	<br>
	the morning of
	<br>
	Saturday, May 11<sup>th</sup>
	</p>
	<div class="vcard info">
	<p class="fn"><a class="url" href="http://www.culverhotel.com">The Culver Hotel</a><p>
	<p class="adr">
	<span class="street-address">9400 Culver Boulevard</span><br>
	<span class="locality">Culver City</span><br>
	<span class="region">California</span><br>
	<span class="postal-code">90232</span><br>
	<span class="country-name hidden">United States</span><br>
	</p>
	</div>
	<p class="info"><em>Reception to follow</em></p>
	<div class="info"><a href="/rsvp/respond/">Respond</a></div>
	</div>
	</div>
EOF

print_footer();
