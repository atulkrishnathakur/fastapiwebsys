$(document).ready(function(){
   $("#translate-open").click(function(){
     $("#akt-translater").fadeIn();
     $("#translate-close").fadeIn();
     $("#translate-open").fadeOut();
   });
   
     $("#translate-close").click(function(){
     $("#akt-translater").fadeOut();
     $("#translate-close").fadeOut();
     $("#translate-open").fadeIn();
   });
   $("#search-open").click(function(){
     $("#akt-search").fadeIn();
     $("#search-close").fadeIn();
     $("#search-open").fadeOut();
     $("#gsc-i-id1").attr("placeholder","akt search");
   });
   
   $("#search-close").click(function(){
     $("#akt-search").fadeOut();
     $("#search-close").fadeOut();
     $("#search-open").fadeIn();
   });
});