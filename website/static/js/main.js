
// JQuery initialization codes
  $(document).ready(function(){
    // to initialize the Navigation Bar
    $('.sidenav').sidenav();

    // to initialize the register form
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });

    //to open a modal using a trigger:
    $('.modal').modal();

    // function to reinitialize all to Materialize labels on the page
    M.updateTextFields();


  });
