document.addEventListener('DOMContentLoaded', function() {

    //sidenav initialization
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmm, yyyy",
      i18n:{done:"Select"}
    });

    var selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    var modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

    var colap = document.querySelectorAll('.collapsible');
    M.Collapsible.init(colap);
  })
