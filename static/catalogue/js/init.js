$('html, body').css({
    'overflow': 'hidden'
})
setTimeout(function(){
    $('html, body').css({
        'overflow': 'auto'
    })
    .animate({
        scrollTop: 0
    }, 100);
}, 500);
$(document).ready(function(){
    load_data();
    $(window).scroll(function(){
        // когда проскролено 80% экрана догружаем
        if($(window).scrollTop() + $(window).height() >= $(document).height()*0.8) {
            load_data();
        }
    });
});