$(document).ready(function() {
	$(".dropdown-expanded").hover(
		function() { $('.dropdown-menu', this).fadeIn("fast");
	},
		function() { $('.dropdown-menu', this).fadeOut("fast");
	});
});
