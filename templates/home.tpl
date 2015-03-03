<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Missy-Go!</title>
		
		<style type="text/css">@import url("/custom404/css/stylesheet.css");</style>
		<style type="text/css">@import url("/custom404/css/blue.css");</style>
		
		<!-- Import google jquery -->
		<script type="text/javascript" src="http://www.google.com/jsapi"></script>
		
		<script type="text/javascript">
		google.load("jquery", "1.3.1");
		google.setOnLoadCallback(function() {
			 
			 //---------------- ColorChanger ----------------//
			 
			 // Change stylesheet to Blue	 
	  		 $(".colorblue").click(function(){
	  		 	$("link").attr("href", "css/blue.css");
			    return false;
			});
			   
			// Change stylesheet to Red
			$(".colorred").click(function(){
				$("link").attr("href", "css/red.css");
				return false;
			});
			
			// Change stylesheet to Grey
			$(".colorgrey").click(function(){
				$("link").attr("href", "css/grey.css");
				return false;
			});
			
			// Change stylesheet to Brown
			$(".colorbrown").click(function(){
				$("link").attr("href", "css/brown.css");
				return false;
			});
			
			// Change stylesheet to Brown
			$(".colorgreen").click(function(){
				$("link").attr("href", "css/green.css");
				return false;
			});
			
			
			//---------------- Show and hide Colorchanger ----------------//
			
			$("#colors").hide();
			
			// Show colors when #showChanger clicked
			$("a#showChanger").click(function() {
				$("#colors").slideToggle("slow");
			});
		});
		</script> 
		
		<!-- PNGFix for IE6 -->
		<script type="text/javascript" src="/custom404/js/jquery.pngFix.js"></script> 
		
		<!-- Active pngfix -->
		<script type="text/javascript"> 
    		$(document).ready(function(){ 
      		$(document).pngFix(); 
    	}); 
		</script> 
		
	</head>
<body>

	<!-- Warp around everything -->
	<div id="warp">
	
		
		<!-- Header top -->
		<div id="header_top"></div>
		<!-- End header top -->
		
		
		<!-- Header -->
		<div id="header">
			<h2>Missy-Go!</h2>
			<h5>Soon to Be.</h5>
		</div>
		<!-- End Header -->
		
		
		<!-- The content div -->
		<div id="content">
		
			<!-- text -->
			<div id="text">
				<!-- The info text -->
				<p>Sorry, Not quite ready.</p>
                <br>
				<h3>Bored? We suggest the links below...</h3>
				<!-- End info text -->
				
				<!-- Page links -->
				<ul>
					<li><a href="/">» Home</a></li>
					<li><a href="/unit6/blog">» Blog</a></li>
					<li><a href="/unit6/machan">» Ascii Art</a></li>
					<li><a href="/search">» Missy-Go Search</a></li>
					<li><a href="http://calmapit.com">» CalMapIt</a></li>
					<li><a href="http://shmik.com">» Shmik</a></li>
					<li><a href="http://calmapit-tripstomp.rhcloud.com/">» Park Locator</a></li>
					
				</ul>
				<!-- End page links -->	
			</div>
			<!-- End info text -->
		
		
			<!-- Book icon -->
			<img id="book" src="/custom404/images/img-01.png" alt="Book iCon">
			<!-- End Book icon -->
			
			<div style="clear:both;"></div>
		</div>
		<!-- End Content -->
		
		
		<!-- Footer -->
		<div id="footer">
			
			<!-- Twitter -->
			
			
			<p id="twitter_text">

			&nbsp;&nbsp;&nbsp;&nbsp;Template by <a style="text-decoration: none; color: gray;" href="http://annata.com">Annata(@annanta)</a> 			

			</p>
	    <!-- End Twitter -->
			
			

			
			<div style="clear:both;"></div>
		</div>
		<!-- End Footer -->
		
		
		<!-- Footer bottom -->
		<div id="footer_bottom"></div>
		<!-- End Footer bottom -->
	
	
		<!-- Social Media list -->
		<ul id="socialmedia">
			<li>
				<a href="http://www.facebook.com/nitishparkar"><img src="/custom404/images/socialmedia/facebook_32.png" alt="Facebook"></a>
			</li>
			
				
			<li>
				<a href="https://plus.google.com/u/0/106062886030684944859/about"><img src="/custom404/images/socialmedia/google_plus_32.png" alt="Google+"></a>
			</li>
				<li>
				<a href="http://in.linkedin.com/in/nitishparkar"><img src="/custom404/images/socialmedia/Linkedin_32.png" alt="LinkedIn"></a>
			</li>
			
			<li>
				<a href="http://twitter.com/nitishsp"><img src="/custom404/images/socialmedia/twitter_32.png" alt="Twitter"></a>
			</li>
				
		</ul>
		<!-- End Social media -->
		
		
		<div style="clear:both;"></div>


	</div>
	<!-- End Warp around everything -->
	


	
</body>
</html>