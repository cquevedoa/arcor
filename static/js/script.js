document.getElementById("year").innerHTML = new Date().getFullYear();


function confirmDelete() {
    if (!confirm('¿Quieres eliminar este producto?\nEsta acción no se puede deshacer!')) {
            e.preventDefault()
        }
        
}



$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})



$(function() {
  $(".btn-search".click(function() {
    var txtSearch = $("#btn-search").val();
    var dataString = 'txtSearch='+ txtSearch;

    if(txtSearch==''){
  
    } else {
      $.ajax({
        type: "POST",
        url: "/results",
        data: dataString,
        cache: false,
        beforeSend: function(html) {
            document.getElementById("results").innerHTML = '';
            $("#flash").show();
            $("#txtSearch").show();
            $(".txtSearch").html(txtSearch);
            $("#flash").html('Cargando resultados')

        },
        success: function(html) {
            $("#results").show();
            $("#results").append(html,data);
            $("#flash").hide();
            
        }
      });
    }
    return false;
  }))
})


$(document).ready(function() {
  var empDataTanle = $('#paginas').DataTable({
    'processing': true,
  'serverSide': true,
  'serverMethod': 'post',
  'ajax': {
    'url':'/'
  },
  'lengthMenu': [[5,10,25,50,-1],[5,10,25,50,"All"]],
  searching: true,
  sort: false,
  "serverSide": true,
  'columns': [
    { data: 'rnpa' },
    { data: 'nombre' },
    { data: 'marca' },
    { data: 'categoria' },
  ]
  });
  

})

// document.getElementById("txtQuery").innerHTML = "dataString";