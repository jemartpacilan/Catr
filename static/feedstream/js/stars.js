$.fn.stars = function() {
    //from 16 x 16 stars.png
    //how this works: default star is the grey star and numeric value found
    //inside the span is multiplied to 16 (width of star)
    //naka repeat ra maong ngana xd
    return this.each(function(i, e) { $(e).html($('<span/>').width($(e).text() * 20)); });
};



$('.stars').stars();