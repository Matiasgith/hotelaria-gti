let form_del_comentario = document.getElementById('form_del_comentario');

form_del_comentario.addEventListener('submit', function(event){
    let text;
    if (confirm("!!!Tem certeza que deseja excluir?") ==true) {
        text = "Comentario exluido com sucesso"
        messagem_cancelada=document.querySelector(".messagem_cancelada").classList.remove('visivel');
   }else{
    text = "Exlclusão Cancelada! "
    event.preventDefault();
    messagem_cancelada=document.querySelector(".messagem_cancelada").classList.add('visivel');
    
   };

   messagem_cancelada=document.querySelector(".messagem_cancelada").innerHTML = text;
   
});