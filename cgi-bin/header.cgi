#!/usr/bin/perl
use strict;
print "Content-type: text/html; charset=\"utf-8\"\n\n";

my @ALL_SLUGS = (
	'our-story',
	'the-ball',
	'rsvp'
);

sub get_title_for_slug($) {
	my $slug = shift;
	my %titles_for_slugs = (
		'our-story' => 'Our Story',
		'the-ball' => 'The Ball',
		'rsvp' => 'RSVP',
		'page-not-found' => 'Page not found'
	);
	return $titles_for_slugs{"$slug"};
}

sub get_header_class_for_slug($) {
	my $slug = shift;
	my %classes_for_slugs = (
		'our-story' => '',
		'the-ball' => '',
		'rsvp' => 'hidden'
	);
	return $classes_for_slugs{"$slug"};
}

sub get_path_for_slug($) {
	my $slug = shift;
	my %paths_for_slugs = (
		'our-story' => '/',
		'the-ball' => '/ball/',
		'rsvp' => '/rsvp/'
	);
	return $paths_for_slugs{"$slug"};
}


sub build_links($) {
	my $slug = shift;
	my $links = '';
	foreach (@ALL_SLUGS) {
		my $nav_class = ("$slug" eq "$_") ? 'active' : ''; 
		my $title = get_title_for_slug("$_");
		my $path = get_path_for_slug("$_");
		$links .= <<END_NAV;
			<li class="$nav_class">
				<a href="$path">$title</a>
			</li>
END_NAV
	}
	return $links;
}

sub print_header($) {
	my $SLUG = shift;
	my $TITLE = get_title_for_slug("$SLUG");
	my $HEADER_CLASS = get_header_class_for_slug("$SLUG");
	my $LINKS = build_links("$SLUG");
	print <<EOF;
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>$TITLE | The Romantics</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="icon" type="image/png" href="/favicon.ico">
		<link rel="shortcut icon" type="image/png" href="/favicon.ico">
		<link rel="stylesheet" type="text/css" media="screen" href="//fonts.googleapis.com/css?family=Vollkorn:400italic,700italic,400,700">
		<link rel="stylesheet" type="text/css" media="all" href="/css/screen.css">
		<link rel="stylesheet" type="text/css" media="print" href="/css/print.css">
		<link rel="stylesheet" type="text/css" media="all" href="/css/bootstrap.ab842b0d47da.css">
		<link rel="stylesheet" type="text/css" media="all" href="/css/responsive.fb6dbb18c21f.css">
		<link rel="stylesheet" type="text/css" media="all" href="/css/rsvp.css">
		<!--[if lt IE 9]>
			<script charset="utf-8" src="/js/html5shiv.js" type="text/javascript"></script>
			<script charset="utf-8" src="/js/html5shiv-printshiv.js" type="text/javascript"></script>
		<![endif]-->
		<script type="text/javascript">

	      var _gaq = _gaq || [];
	      _gaq.push(['_setAccount', 'UA-30588017-4']);
	      _gaq.push(['_trackPageview']);
	      
	      (function() {
		var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
	      })();

	    </script>
	</head>
	<body>
		<div class="navbar navbar-inverse navbar-static-top">
			<div class="navbar-inner">
				<div class="container">
					<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</a><!-- /.btn.btn-navbar -->

					<a class="brand" href="/">The Romantics</a>
					<div class="nav-collapse collapse">
						<ul class="nav">
							$LINKS
						</ul><!-- /.nav -->
					</div><!-- /.nav-collapse.collapse -->	
				</div><!-- /.container -->
			</div><!-- /.nav-inner -->
		</div><!-- /.navbar.navbar-fixed-top -->
		<div class="container">
			<div class="row">
				<div class="span6 offset3">
					<header id="header" class="$HEADER_CLASS">
						<div class="page-header">
							<h1>$TITLE</h1>
						</div><!-- /.page-header -->
					</header><!-- /#header -->
					<section id="content">
EOF
}

1;
