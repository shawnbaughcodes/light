$(document).ready(function() {
     // Stuff to do as soon as the DOM is ready
     $('h3#enter_button').click(function(){
         $('.index_container').slideUp('slow', function() {
             $('div.reg_and_login_container').slideDown('slow', function() {
             })
         });
     });
     $('h1#cancel_button').click(function(){
         $('.reg_and_login_container').slideUp('slow', function() {
         })
         $('.index_container').slideDown('slow', function() {
             //Stuff to do *after* the animation takes place
         })
     })
     $('a.new_review').click(function(){
         $('div.all_reviews').slideUp('fast', function() {
             $('#review_form').show('slow')
             //Stuff to do *after* the animation takes place
         })
     })
     $('a.cancel').click(function(){
         $('#review_form').hide('fast')
         $('.all_reviews').slideDown('slow', function() {
             //Stuff to do *after* the animation takes place
         })
     })
});
