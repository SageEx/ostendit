{% extends "Software/header.html" %}
{% block content %}
<div style="clear:both"></div>
<ul id="search-results">

</ul>
<p>
	PageNumber: <input type="text" id="pageNumber" name="page"/>{% csrf_token %}
	<input type="button" onclick="loadPage()" value="Pages"/>
</p>

<form action="" id="numPost" name="post">{% csrf_token %}
	<p>number of Posts: <select id="dis" name="number" size="1" onChange="go()">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		</select>
	</p>
	<script type="text/javascript">
		function go(){
			str = document.post.number.options[document.post.number.selectedIndex].value;
			window.location.href = '/temp/'+str;
		}

	</script>
</form>
    <div id="main">
        <!-- Posts  -->
        <ul>
        <script>
        	$(document).ready(function(){
        		$('#search').keyup(function(){
        			$.ajax({
            			type: "POST",
            			url: "/search/",
            			data: { 
                			'search_text' : $('#search').val(),
                			'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            			},
            			success: searchSuccess,
            			dataType: 'html',
        			});
        		});
        	});

        	function searchSuccess(data, textStatus, jqXHR){
    			$('#search-results').html(data);
			}

			function loadPage(){

				var num = document.getElementById('pageNumber').value;
				window.location.href = "/page="+num+"/pages/";
			}

			/*function loadPosts(){

				var num1 = document.getElementById('postNumber').value;
				{{ posts.paginator.num_pages }} = num1;
				alert(4);
			}*/

        </script>
            {% for post in posts.object_list %}
      
					<div id="title">{{ post.title }}</div>
	            	<ul>
	           			<div id="time">{{ post.created }}</div>
	       	    		<div id="bdy" class="pst{{post.id}}" width="500px">{{ post.body|linebreaks }}</div>
	            	</ul>
	            	<a href = "/load/{{post.id}}"/>Read More</a>
	            	<script>
	            		$(function() {

							var showChar = 60, showtxt = "more", hidetxt = "less";
							var str4 = '.pst' + {{ post.id }};
							$(str4).each(function() {
								var content = $(this).text();
								if (content.length > showChar) {
									var con = content.substr(0, showChar);
									var hcon = content.substr(showChar, content.length - showChar);
									var txt= con +  '<span class="dots">...</span><span class="morecontent"><span>' + hcon + '</span>&nbsp;&nbsp;<a href="" class="moretxt' + {{ post.id }} + '">' + showtxt + '</a></span>';
									$(this).html(txt);
									document.getElementById('bdy').style.width = '500px';
									document.getElementById('bdy').style.display = 'block';
								}
							});
							var str2 = '.moretxt' + {{ post.id }};
							$(str2).click(function() {
								if ($(this).hasClass("sample")) {
									$(this).removeClass("sample");
									$(this).text(showtxt);
								} else {
									$(this).addClass("sample");
									$(this).text(hidetxt);
								}
								$(this).parent().prev().toggle();
								$(this).prev().toggle();
								return false;
							});
						});
					</script>
				
            {% endfor %}
        </ul>

	<!-- For the paginator -->
	    {% if posts.object_list and posts.paginator.num_pages > 1 %}
		<div id = "pagination" style = "margin-top : 20px ; margin-left : -20px; ">
			<span id="step-links">
				{% if posts.has_previous %}
					<a href="/page={{posts.previous_page_number}}/pages/">&nbsp;&nbsp;&nbsp;Older Posts &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </a>
				{% endif %}	
				<span id="current">
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page{{posts.number}} of {{posts.paginator.num_pages}}
				</span>	 
				{% if posts.has_next %}
					<a href="/page={{posts.next_page_number}}/pages/">Latest Posts</a>			
				{% endif %}
			</span>					
		</div>
	    {% endif %}
    </div>
{% endblock %}
