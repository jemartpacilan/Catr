$('.payment-method').click(function(e) {
  $(this).addClass('activepayment');
  $(this).siblings().removeClass('activepayment');
});
