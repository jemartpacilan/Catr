$(document).ready(function() {
    $("input[name='package']").change(function() {
      $("#foo").html("");
        $("#foo1").html("");
          $("div.div2").hide();
        var radioVal = $("input[name='package']:checked").val();
        // console.log('hello123')
        if (radioVal) {
            $.ajax({
                url: "/api/caterers/" + window.location.href.split('/')[window.location.href.split('/').length - 2] + "/"
            }).then(function(caterer) {
                $.ajax({
                    url: "/api/packages/" + radioVal
                }).then(function(package) {
                    console.log(package.id)
                    $('.package_title').append('<h4>' + package.package_name + '</h4>')
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
                                    console.log(menus[menu]);
                                    $('.menu_items').append('<div class = "menu_items_container"><div class="image_item_container"></div>' +
                                    '<input type="text" name="' + menus[menu].id +'" value = "' + courses.course_name + '" readonly><label>'+ courses.course_name+'</label>'
                                    +'<input class="item_price" type="number" readonly value="' +
                                    courses.course_price + '" name="' + menus[menu].id + 'x"><label class = "price">'+ courses.course_price+'</label></div>')
                                    // $.ajax({
                                    //   url: "/api/images/"
                                    // }).then(function(images){
                                    //       for(let image in images){
                                    //         if( images[image].menu == menus[menu].id){
                                    //           console.log(images[image].menu + "SASD" + menus[menu].id);
                                    //           console.log("ta" + menus[menu].id);
                                    //           console.log("hello gwapo ko")
                                    //           // console.log("hello"+images[menu].menu)
                                    //           $('.image_item_container').append('<img src = "'+ images[image].image_binary+'"/>')
                                    //         }
                                    //       }
                                    //
                                    // })
                                })
                            }
                        }
                    });
                })
            })
        }
    });
});
