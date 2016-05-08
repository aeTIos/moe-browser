document.addEventListener('keydown', function(event) {
    if(event.keyCode == 37) {
       var xhr = new XMLHttpRequest();
       xhr.timeout = 2000;
       xhr.open("get", "/nexturl", true);
       xhr.send();
       xhr.responseType = 'text';
       console.log(xhr.response);
       console.log(xhr.responseText);
       console.log("test");
}
    else if(event.keyCode == 39) {
        alert('Right was pressed');
    }
});
