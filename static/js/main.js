$(document).ready(function() {
    $('.child').slideUp(0);
    var prev;
    $('.parent-ele').click(function () { 
        // console.log();
        if(prev!=this){
            $('.child').slideUp(0);
            $('.parent-ele').find('.dropdown').removeClass('rotate');
            $('.parent-ele').removeClass('transition');
        }
        console.log(prev, this)
        $(this).find('.child').toggle(0.3);
        $(this).find('.dropdown').toggleClass('rotate');
        $(this).toggleClass('transition');
        prev=this;
    });


    if($('.topic').is(":visible")){
        $('.subject_container').hide(0);
    }

    $('.topic').click(function () {
        $('#selected_list').prepend(this);
        $('#topic_selected').prepend(this);
    });

    $('#butn_show').click(function(){
        console.log('clicked');
        $('#under').toggle();
    })


    $('.item').click(function () { 
        //topic select ,animate bounce and append in form  
        $(this).toggleClass('bounce');
        $(this).find('option').addClass('option');
        var elementToCopy = $(this).find('.option').clone();
        $('#submit_form').append(elementToCopy);
        $("#submit_form option").prop("selected", true);
    });

});
