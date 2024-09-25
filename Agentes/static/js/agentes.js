(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn =>{
        btn.addEventListener('click', (e)=>{
            const confirmation = confirm("Seguro qeu desea eliminiar");
            if (!confirmation){
                e.preventDefault();
            } 
        });
    });
})();
