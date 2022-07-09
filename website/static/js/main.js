// To initialize the Navigation Bar
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });

// JQuery code to initialize the Navigation Bar
  $(document).ready(function(){
    $('.sidenav').sidenav();
  });

// To initialize the register form
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete');
    var instances = M.Autocomplete.init(elems, options);
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

// To open a modal using a trigger:
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
  });

// jQuery to open a modal using a trigger:
  $(document).ready(function(){
    $('.modal').modal();
  });


// function to reinitialize all the Materialize labels on the page
  $(document).ready(function() {
    M.updateTextFields();
  });