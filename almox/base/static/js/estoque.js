
$(document).ready(function(){
    $('#add-item').click(function(ev){
        ev.preventDefault();
        var count = $('#estoque').children().length;
        var tmplMarkup = $('#item-estoque').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#estoque').append(compiledTmpl);

        // update form count
        $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

        // some animate to scroll to view our new form
        $('html, body').animate({
          scrollTop: $("#add-item").position().top - 200
        }, 800);

    });
});


