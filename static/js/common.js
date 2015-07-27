$(function () {
    var iv; //timer for interval
    var div = $('#content');
    $('#left').mousedown(function () {
        iv = setInterval(function () {
            div.scrollLeft(div.scrollLeft() - 50);c
            //console.log('downLeft');
        }, 20);
    });
    $('#right').mousedown(function () {
        iv = setInterval(function () {
            div.scrollLeft(div.scrollLeft() + 50);
            //console.log('downRight');
        }, 20);
    });
    $('#left,#right').on('mouseup mouseleave', function () {
        clearInterval(iv);
        //console.log('up or leave');
    });
});