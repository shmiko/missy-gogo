<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="/styles/bootstrap.css" type="text/css">
		<link rel="stylesheet" href="/styles/home.css" type="text/css">
		<title>Missy-Go: {{ search_query }}</title>
	</head>
	<body>
		<div class="navbar navbar-fixed-top">
			<div class="navbar-inner">
				<div class="container">
					<span class="brand">
					<h2><a href="/">Go Missy Go <strong class="orange">Found</strong></a></h2></span>
					<form class="navbar-form form-inline" action="/search" method="GET" >
		  				<input type="text" name="search_query" class="input-xlarge">
		  				<button type="submit" class="btn btn-warning"><i class="icon-search icon-white"></i></button>
					</form>
				</div>
			</div>
		</div>
		<div class="container">
			<div class="row">
				<div class="span6 offset3">
					<h3>You searched for:</h3>
					<p>{{ search_query }}</p>
					%if python_term:
					<p>{{ python_term }}></p>
					%end
				</div>
			</div>
		</div>
	</body>
</html>