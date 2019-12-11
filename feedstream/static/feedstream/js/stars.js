$.fn.stars = function() {
	console.log(this)
    //from 20 x 20 stars.png
    //how this works: default star is the grey star and numeric value found
    //inside the span is multiplied to 20 (width of star)
    //naka repeat ra maong ngana xd
    console.log('nisulod ko diri omg lololololol');
    return this.each(function(i, e) {
    	// console.log(e.text());
    	$(e).html($('<span/>').width($(e).text() * 20));

    });
};



// $('.stars').stars();
