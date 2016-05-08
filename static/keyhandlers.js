document.addEventListener('keydown', function(event) 
{
    if(event.keyCode == 82) // key r
    {
        var xhr = new XMLHttpRequest();
        xhr.timeout = 2000;
        xhr.open("get", "/random", true);
        xhr.send();
        xhr.responseType = 'text';
        xhr.onload = function()
        {
            console.log(xhr.response);;
            var pic = document.getElementById("moepicture")            
            pic.src = xhr.response;
        }
    }
    else if(event.keyCode == 39) 
    {
     //   alert('Right was pressed');
    }
}
);
