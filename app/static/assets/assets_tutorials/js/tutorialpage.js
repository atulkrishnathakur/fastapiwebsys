var chptrid = document.getElementById("chptr-id");

chptrid.onclick = function(){
    var verfixid = document.getElementById("ver-fix-id");
    verfixid.style.display="block";
    verfixid.style.width="243px";
    verfixid.style.zIndex="1100";
    verfixid.style.top="43px";
    verfixid.style.height="93%";
};
var closeid = document.getElementById("akt-closeid");
closeid.onclick = function(){
  var verfixid = document.getElementById("ver-fix-id");
  verfixid.style.display="none";
};


function ttrlExampleHelp(helpObj){
 
    helpObj.setAttribute("title","Click on example code for expand.");
    
}