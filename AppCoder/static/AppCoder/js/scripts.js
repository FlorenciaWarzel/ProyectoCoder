/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
const $exampleModal = $('#exampleModal')
const $iframeVideo = $('#iframeVideo')
$exampleModal.on('hidden.bs.modal', function(event){
    $iframeVideo.attr('src',null);
});