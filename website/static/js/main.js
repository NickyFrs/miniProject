
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

    // to initialize the accordion in the task page
     $('.collapsible').collapsible();

    // initialize the tooltip features
    $('.tooltipped').tooltip();

    // initializes the calendar (date picker)
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
        done: "select"
      }
    });

    // initializes the select field in the add task form
    $('select').formSelect();
  });

