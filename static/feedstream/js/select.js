$(document).ready(function() {
    $("input.select[type='button']").click(function() {
        var radioValue = $("input[name='package']:checked").val();
        if (radioValue) {
            $.ajax({
                url: "/api/caterers/" + window.location.href.split('/')[window.location.href.split('/').length - 2] + "/"
            }).then(function(caterer) {
                $.ajax({
                    url: "/api/packages/" + radioValue
                }).then(function(package) {
                    console.log(package.id)
                    $('.package').append('<h5>' + package.package_name + '</h5>')
                    $.ajax({
                        url: "/api/menus/"
                    }).then(function(menus) {
                        for (let menu in menus) {
                            console.log(caterer.id + " " + package.id)
                            if (package.id == menus[menu].package && menus[menu].caterer === caterer.id) {
                                console.log(menus[menu].package)
                                $.ajax({
                                    url: "/api/courses/" + menus[menu].course
                                }).then(function(courses) {
                                    console.log(courses.course_name)
                                    $('.package_items').append('<div class = "package_items_container">' +
                                        '<input class="item_price" type="number" readonly value="' +
                                        courses.course_price + '" name="' + menus[menu].id + 'x">' +
                                        '<input type="text" name="' + menus[menu].id +
                                        '" value = "' + courses.course_name + '" readonly><input value="1" ' +
                                        'type ="number" name="' + menus[menu].id + 'z" min = "0"></div>');

                                    solveTotal();
                                })
                            }
                        }
                    });
                })
            })
        }
    });
});