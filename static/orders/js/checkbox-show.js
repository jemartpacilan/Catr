// $(function() {
//     $(".package_name").click(function() {
//         console.log($(this));
//         console.log($(this).parent());
//         console.log($(this).parent().parent());
//         if ($(this).is(":checked")) {
//             $(".menu_items").show();
//             console.log("asd")
//         } else {
//             $(".menu_items").hide();
//         }
//     });
// });

$('.package_container').on('click', function(event) {
    if (event.target != this) {
        if (event.target.type == 'checkbox') {
            // console.log('tae ' + event.target.id)
            if ($("#" + event.target.id).is(":checked")) {
            	// console.log($("#" + event.target.id).parent().parent().parent().children()[1]);
            	item_list = $("#" + event.target.id).parent().parent().parent().children()[1];
                $("#" + item_list.id).show();
                // console.log("asd")
            } else {
                $("#" + item_list.id).hide();
            }
        }
        // console.log(event.target.type)
        // console.log('yellow')
        // console.log(this)
        // alert('You clicked a descendent of #container.');
        // var selected = $(".package_name .package_list input:checked").map(function(i, el) { return el.name; }).get();
        // alert("selected = [" + selected + "]\nas string = \"" + selected.join(";") + "\"");

    } else {
        // alert('You actually clicked #container itself.');
    }
});