<html>
<head> 
	<title>My Base Template</title>
	<style type="text/css">
			#sddm
	{	margin: 0;
		padding: 0;
		z-index: 30}

	#sddm li
	{	margin: 0;
		padding: 0;
		list-style: none;
		float: left;
		font: bold 11px arial}

	#sddm li a
	{	display: block;
		margin: 0 1px 0 0;
		padding: 4px 10px;
		width: 60px;
		background: #5970B2;
		color: #FFF;
		text-align: center;
		text-decoration: none}

	#sddm li a:hover
	{	background: #49A3FF}

	#sddm div
	{	position: absolute;
		visibility: hidden;
		margin: 0;
		padding: 0;
		background: #EAEBD8;
		border: 1px solid #5970B2}

		#sddm div a
		{	position: relative;
			display: block;
			margin: 0;
			padding: 5px 10px;
			width: auto;
			white-space: nowrap;
			text-align: left;
			text-decoration: none;
			background: #EAEBD8;
			color: #2875DE;
			font: 11px arial}

		#sddm div a:hover
		{	background: #49A3FF;
			color: #FFF}
	</style>
	<script>

		var timeout	= 500;
		var closetimer	= 0;
		var ddmenuitem	= 0;

		// open hidden layer
		function mopen(id)
		{	
			// cancel close timer
			mcancelclosetime();

			// close old layer
			if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';

			// get new layer and show it
			ddmenuitem = document.getElementById(id);
			ddmenuitem.style.visibility = 'visible';

		}
		// close showed layer
		function mclose()
		{
			if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
		}

		// go close timer
		function mclosetime()
		{
			closetimer = window.setTimeout(mclose, timeout);
		}

		// cancel close timer
		function mcancelclosetime()
		{
			if(closetimer)
			{
				window.clearTimeout(closetimer);
				closetimer = null;
			}
		}

		// close layer when click-out
		document.onclick = mclose; 

	</script>
</head>
<body onLoad="start()">
	<ul id="sddm">
    <li><a href="#" 
        onmouseover="mopen('m1')" 
        onmouseout="mclosetime()">Home</a>
        <div id="m1" 
            onmouseover="mcancelclosetime()" 
            onmouseout="mclosetime()">
        <a href="/articles/">Create a Article</a>
        <a href="/articles/all">List of Articles</a>
        <a href="/edit/">Edit Profile</a>
        <a href="/logout/">Logout</a>
        <a href="/add_user/">Add a User</a>
        </div>
    </li>

    <li><a href="#" 
        onmouseover="mopen('m2')" 
        onmouseout="mclosetime()">FrontEnd</a>
        <div id="m2" 
            onmouseover="mcancelclosetime()" 
            onmouseout="mclosetime()">
        <a href="/front/">QuickSort</a>
        <a href="/front/">QuickSort</a>
        <a href="/front/">QuickSort</a>
        <a href="/front/">QuickSort</a>
        </div>
    </li>
	</ul>
	<div style="clear:both"></div>
	<div id="page">
	<div id="content">
		{% block content %}{% endblock %}
	</div>	
	</div>
</body>
</html>