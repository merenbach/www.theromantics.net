#!/usr/bin/perl

use strict;

require 'cgi-bin/header.cgi';
require 'cgi-bin/footer.cgi';

# Header
print_header('our-story');

# Content
print <<EOF;
	<img class="pull-left span2 hidden-phone" src="/img/JaneAustenSilhouette.png" alt="Jane Austen">
	<article class="book-page">
		<p>The story of how our hero met our heroine does not begin, I am sorry to say, with any cases of kidnapping or intrigue or any other such staples of a traditional romance. This young couple met, prosaically enough, as college freshmen in the summer of 2004. They met through sheer chance, having distanced themselves from the weary bustle of orientation activities. They spoke of their family backgrounds and of their plans for the future, the former as respectable as the latter.</p>
		<p>Parting ways as orientation drew to a close, they had the good fortune to be reintroduced by a mutual acquaintance during the school term. Being reserved by nature, our hero and heroine remained friends for an extended period without a single spirited declaration of affection being made! Such reserve perhaps makes for a better relationship than for an engaging story, but the two found themselves thoroughly in sympathy when they made the decision to date in the summer of 2006. Their friends were perhaps surprised to find the lifelong technophile with an unfortunate penchant for wordplay drawn to the inveterate bookworm with a disdain for the same, but they found that their differences acted as a complement rather than a constraint.</p>
		<p>Dear reader, their courtship was not marked by discoveries of ancient animosity between their two lines. During the ensuing five and a half years, no spurned fianc&eacute;s appeared to mar their happiness, nor did any political upheavals conspire to separate the young pair. Rather, the couple grew together as they established themselves in their respective spheres of web development and librarianship.</p>
		<p>To the delight and relief of their connections, they have made the decision to wed May of 2013 in <abbr title="Culver City, California">&#8212;shire</abbr>. They look forward to celebrating this occasion with family and friends in an intimate ceremony free of hysterics or scandal but full of affection and felicity.</p>
	</article>
EOF

# Footer
print_footer();

