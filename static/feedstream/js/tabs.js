$('.prodreviews').click(function(e) {
  var $this = $(this);
  if (!$this.hasClass('selected')) {
    $this.addClass('selected');
    $this.siblings('.selected').removeClass('selected')
      if($('.reviews').is(":hidden")){
      $('.questions').hide();
      $('.reviews').show();
      console.log("if")
    }else{
      console.log("else")
      $('.reviews').hide();
      $('.questions').show();
    }
  }
  e.preventDefault();
});


