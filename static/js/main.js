$(document).ready(function () {
    $('.songs').on('show.bs.collapse', toggleChevron);
    $('.songs').on('hide.bs.collapse', toggleChevron);
    $('.links').on('show.bs.collapse', hideWatchButton);
});

function hideWatchButton (event) {
    $(event.target)
        .prev('.btn-watch')
        .hide();
}

function toggleChevron (event) {
    $(event.target)
        .prev('.panel-heading')
        .find('.glyphicon')
        .toggleClass('glyphicon-chevron-down glyphicon-chevron-right');
}
