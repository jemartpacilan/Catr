// parse id through websites link
var add = window.location.href.split('/');
var id = add[add.length - 2];
var runningtotal = 0;
// end
$(document).ready(function() {
    $('.stars').stars();
    $.ajax({
        url: '/orders/ajax/search/' + id,
        success: function(data) {
            for (i in data.courses) {
                $("datalist#option_food").append('<option id="' + data.courses[i][0] +
                    '"name = "' + data.courses[i][0] + '" value = "' + data.courses[i][1] + '"></option> ');
            }
            // remove dupes
            var map = {};
            $('datalist option').each(function() {
                // console.log(this.value);
                if (map[this.value]) {
                    $(this).remove()
                }
                map[this.value] = true;
            })
            // end of remove dupes
            // remove items existing already in tray
            $(".mycart li").each(function() {
                var todelete = $(this).text()
                $('datalist option').each(function() {
                    if ($(this).val() == todelete) {
                        $(this).remove()
                    }
                })
            });
            //end of remove
        }
    });

    // add item to tray
    $("input#course_search").change(function() {
        var text = $(this).val();
        var obj = $("#option_food").find("option[value='" + text + "']")

        if (obj != null && obj.length > 0) {
            var name = String(obj.attr('name'));
            obj = String(obj.attr('value'));
            // calls retrieve course view
            $.ajax({
                url: '/orders/ajax/retrieveCourse/' + id,
                data: {
                    'name': obj
                },
                success: function(data) {
                    // console.log(data.price[0])
                    price = data.price[0]
                    $('.package_items').append('<div class="package_items_container">' +
                        '<input class="item_price" type="number" readonly value="' + price +
                        '" name="' + name + 'x"><input type="text" id="package" name="' +
                        name + '" value = "' + obj + '" readonly><input type ="number"' +
                        ' class="q_spinner" value="1" name="' + name + 'z" min = "1"></div>')
                    // clear
                    $('input#course_search').val('');
                    // end clear
                    // remove from datalist
                    // var courselist = document.querySelector("#option_food");
                    document.getElementById("option_food").options.namedItem(name).remove();
                    // end of remove datalist
                    solveTotal();
                }
            });
        }
    });
    // end of add

    // remove item from tray
    $("input.remove_button[type=button]").click(function() {
        var toberemoved = $(this).parent().parent().text();
        $.ajax({
            url: '/orders/ajax/remove/' + id,
            data: {
                'item': toberemoved,
            },
            success: function(data) {
                $(".mycart li").each(function() {
                    if ($(this).text() == toberemoved) {
                        // removes the item in the cart
                        $(this).remove()
                        // end of remove from cart
                        // adds the removed item back from the dropdown list
                        $.ajax({
                            url: '/orders/ajax/add/' + id,
                            data: {
                                'item': toberemoved,
                            },
                            success: function(data) {
                                $("datalist#option_food").append('<option id="' + data.course[0][0] +
                                    '"name = "' + data.course[0][0] + '" value = "' + data.course[0][1] +
                                    '"></option> ');
                            }
                        });
                        // end of add item back
                    }
                });
            }
        });
    });
    // end of remove from tray

    // auto multiply when quantity of food is changed
    $(document).on("change paste keyup", "input[type='number']", function() {
        // console.log($(this).data("done"))
        if (!$(this).data("done")) {
            $(this).data("defaultValue", $(this).parent().children()[1].value)
            $(this).data("done", true)
        }
        // console.log($(this))
        if (!$(this).data("previousValue") ||
            $(this).data("previousValue") != $(this).val()) {
            priceapiece = $(this).data("defaultValue");
            // console.log(priceapiece);
            new_val = (priceapiece * $(this).val()).toFixed(2);
            // console.log(new_val);
            $(this).parent().children()[1].value = new_val
            // console.log($(this).parent().children()[0].value)
            // console.log("changed" + $(this).val());
            $(this).data("previousValue", $(this).val());
            solveTotal();
        }
        // console.log("hello");
    });

    // $("input").each(function () {
    //     $(this).data("previousValue", $(this).val());
    // });

})

function solveTotal(){
    // console.log(runningtotal);
    runningtotal = 0;
    $("div.package_items").children().each(function () {
        // console.log(typeof $(this).children()[0].value);
        // console.log(parseFloat($(this).children()[0].value));
        let x = parseFloat($(this).children()[1].value);
        runningtotal += x;
        // runningtotal = runningtotal.toFixed(2);
        console.log(typeof runningtotal)
    });
    console.log('Running Total: ' + runningtotal.toFixed(2));
    $("span.running_total").html("PHP: " + runningtotal.toFixed(2));
}
