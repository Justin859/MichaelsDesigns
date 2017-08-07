$(document).ready(function(){
    $("form").submit(function(){
        document.getElementById("overlay").style.display = "block";
    });
});

$(window).bind("pageshow", function(event) {
    $("#overlay").hide();
});