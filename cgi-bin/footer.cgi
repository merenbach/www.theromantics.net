#!/usr/bin/perl
use strict;

sub print_footer() {
	print <<EOF;
		</section><!-- /.content -->
		<footer id="footer" class="text-center">
			<p class="text-info">
				<small>Copyright &copy; 2012 <a class="text-info" href="http://www.lizcheney.com">Elizabeth Cheney</a> and <a class="text-info" href="http://www.merenbach.com">Andrew Merenbach</a></small>
			</p>
			<p class="text-info">
				<small>CSS3 <a href="http://www.sitepoint.com/pure-css3-paper-curls/">Page curls</a> courtesy of <a href="http://www.sitepoint.com/author/craig-buckler/">Craig Buckler</a>.</small>
			</p>
		</footer>
		<script src="http://code.jquery.com/jquery.js"></script>
		<script charset="utf-8" src="/js/bootstrap.min.js" type="text/javascript"></script>
		<script type="text/javascript">
		    var clicky = { log: function(){ return; }, goal: function(){ return; }};
		    var clicky_site_ids = clicky_site_ids || [];
		    clicky_site_ids.push(66628576);
		    var clicky_custom = {};
		    (function() {
		      var s = document.createElement('script');
		      s.type = 'text/javascript';
		      s.async = true;
		      s.src = '//static.getclicky.com/js';
		      ( document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0] ).appendChild( s );
		    })();
		    </script>
		<noscript><p><img alt="Clicky" width="1" height="1" src="//in.getclicky.com/66628576ns.gif"/></p></noscript>
	</body>
	</html>
EOF
}

1;
