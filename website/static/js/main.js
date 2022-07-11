
// JQuery code to initialize the Navigation Bar
  $(document).ready(function(){
    $('.sidenav').sidenav();
  });


//  JQuery code to initialize the register form
  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });
  });


// jQuery to open a modal using a trigger:
  $(document).ready(function(){
    $('.modal').modal();
  });


// function to reinitialize all the Materialize labels on the page
  $(document).ready(function() {
    M.updateTextFields();
  });