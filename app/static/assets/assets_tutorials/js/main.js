var aktDropMenuId = document.getElementById("akt-drop-menuid");

aktDropMenuId.addEventListener("click",fnDrop);

 function fnDrop(){
 
  var aktDropMenu = document.getElementById("akt-drop-menu");
  
  aktDropMenu.style.display = "block";
   
};

/*var aktDropMenu = document.getElementById("akt-drop-menu");
aktDropMenu.onmouseleave = function(){
  aktDropMenu.style.display = "none";
    
};*/

var aktClosebtn = document.getElementById("akt-closebtn");

aktClosebtn.onclick = function(){
  var aktDropMenu = document.getElementById("akt-drop-menu");
  
  aktDropMenu.style.display = "none";  
};
