$(function () {
    $('.startTime').datetimepicker({
        format: 'HH:mm',
        useCurrent: false
    });
    $('.endTime').datetimepicker({
        format: 'HH:mm',
        useCurrent: false
    });
    $('.feedTime').datetimepicker({
        format: 'HH:mm',
        useCurrent: false
    });
    $('.startTime').on("change.datetimepicker", function (e) {
        $('.endTime').datetimepicker('minDate', e.date);
    });
    $('.endTime').on("change.datetimepicker", function (e) {
        $('.startTime').datetimepicker('maxDate', e.date);
    });
    $('.feedTime').datetimepicker();
});