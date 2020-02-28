
$(function () {
    $('#{{ plant.title }}-datetimepicker1').datetimepicker({
        format: 'HH:mm',
        useCurrent: false
    });
    $('#{{ plant.title }}-datetimepicker2').datetimepicker({
        format: 'HH:mm',
        useCurrent: false
    });
    $('#{{ plant.title }}-datetimepicker3').datetimepicker({
        format: 'HH:mm',
        useCurrent: false
    });
    $("#{{ plant.title }}-datetimepicker1").on("change.datetimepicker", function (e) {
        $('#{{ plant.title }}-datetimepicker2').datetimepicker('minDate', e.date);
    });
    $("#{{ plant.title }}-datetimepicker2").on("change.datetimepicker", function (e) {
        $('#{{ plant.title }}-datetimepicker1').datetimepicker('maxDate', e.date);
    });
    $('#{{ plant.title }}-datetimepicker3').datetimepicker();
});