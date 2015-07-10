$(document).ready(function () {
    $('.songs').on('show.bs.collapse', toggleChevron);
    $('.songs').on('hide.bs.collapse', toggleChevron);
    $('.songs').on('hide.bs.collapse', pauseVideo);
    $('.links').on('show.bs.collapse', toggleWatch);
    $('.links').on('hide.bs.collapse', toggleWatch);
});

function toggleWatch (event) {

    var uri = $(event.target).attr('data-src');
    $(event.target).attr('src', uri);

    $(event.target)
        .prev('.btn-watch')
        .toggle();
}

function pauseVideo (event) {
    var iframe = $(event.target).find('iframe')[0];
    if (iframe) {
        iframe.contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
        console.log('video paused');
    } else {
        console.log('no video to pause found');
    }
}

function toggleChevron (event) {
    $(event.target)
        .prev('.panel-heading')
        .find('.glyphicon')
        .toggleClass('glyphicon-chevron-down glyphicon-chevron-right');
}


