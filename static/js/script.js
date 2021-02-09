$(document).ready(function () {
    $(".like").click(function () {
        $(this).toggleClass("heart");
    });
});

$(document).ready(function () {
    setTimeout(function () {
        $('.flash').fadeOut('slow');
    }, 2000);


    $(".burger-menu").click(function () {
        $(".navigation-list").slideToggle(2000);
    });


    $(".navigation-list li a").click(function () {
        if ($(window).width() <= 800) {
            $(".navigation-list").css("display", "none");
        }
        else {
            $(".navigation-list").show();
        }
    });
});

