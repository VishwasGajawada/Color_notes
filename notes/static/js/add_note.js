selects = document.querySelector('#id_color');
note = document.querySelector('.new-note')
function changed(){
    var opt = selects.options[selects.selectedIndex];
    note.style.backgroundColor = opt.value;
}

selects.addEventListener('change',()=>changed());
changed();
