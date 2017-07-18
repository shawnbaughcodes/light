$(document).ready(function() {
     // Stuff to do as soon as the DOM is ready
     $('select').material_select();
     $('#my_popup').popup();
     $('ul.tabs').tabs();
     $('#my_popup').on('click', '.login_btn', function() {
         $('.register').hide();
         $('.login_form').show()
     })
     $('#my_popup').on('click', '.register_btn', function() {
         $('.register').show();
         $('.login_form').hide()
     })
    //  $('h1#cancel_button').click(function(){
    //      $('.reg_and_login_container').slideUp('slow', function() {
    //      })
    //      $('.index_container').slideDown('slow', function() {
    //          //Stuff to do *after* the animation takes place
    //      })
    //  })

});
