//window.onload = startInterval;

// function startInterval() {

//   $.get('/file_list', function(file_list) {
//     if (!file_list) {
//         console.log("erro a aceder ao server");
//     }
//     var cards = ''
//     for(i=0;i<file_list.filelist.length;i++){
//         //console.log(file_list.filelist[i].lista)
//         //console.log(file_list.filelist[i].nome_pasta)
//         cards+='<div class="card col-md-4">'
//         cards+='<div class="card-title">'
//         cards+='<h2>'
//         cards+=file_list.filelist[i].nome_pasta
//         cards+='<small>'
//         cards+='<button type="button" class="btn btn-outline-dark" onclick="window.location.href="/">Continue</button>'
//         cards+='</small>' 
//         cards+='</h2>'
//         cards+='<div class="task-count" >43</div>'
//         cards+='</div>'
//         cards+='<div class="card-flap flap1">'
//         cards+='<div class="card-description">'
//         cards+='<ul class="task-list">'
  
//         for(k=0;k<file_list.filelist[i].lista.length;k++){
//             // console.log(file_list.filelist[i].lista[k])
//             cards+='<li>'+file_list.filelist[i].lista[k]+'</li>'
//         }
  
//         cards+='</ul>'
//         cards+='</div>'
//         cards+='<div class="card-flap flap2">'
//         cards+='<div class="card-actions">'
//         cards+='<a class="btn" href="#">Close</a>'
//         cards+='</div>'
//         cards+='</div>'
//         cards+='</div>'
//         cards+='</div>'
//     }
//     $('#cards').append(cards)    
//   }); 





//   // $.get('/file_list', function(file_list) {
//   //   if (!file_list) {
//   //       console.log("erro a aceder ao server");
//   //   }
    
//   //   var cards = ''
//   //   $.each(file_list.filelist,function(key,value){
//   //       //console.log(file_list.filelist[i].lista)
//   //       //console.log(file_list.filelist[i].nome_pasta)
//   //       cards+='<div class="card col-md-4">'
//   //       cards+='<div class="card-title">'
//   //       cards+='<h2>'
//   //       cards+=value.nome_pasta
//   //       cards+='<small>'
//   //       cards+='<button type="button" class="btn btn-outline-dark" onclick="window.location.href="/">Continue</button>'
//   //       cards+='</small>' 
//   //       cards+='</h2>'
//   //       cards+='<div class="task-count" >43</div>'
//   //       cards+='</div>'
//   //       cards+='<div class="card-flap flap1">'
//   //       cards+='<div class="card-description">'
//   //       cards+='<ul class="task-list">'
  
//   //       $.each(value,function(key1,value1){
//   //           console.log(value1)
//   //           cards+='<li>'+value1+'</li>'
//   //       })
  
//   //       cards+='</ul>'
//   //       cards+='</div>'
//   //       cards+='<div class="card-flap flap2">'
//   //       cards+='<div class="card-actions">'
//   //       cards+='<a class="btn" href="#">Close</a>'
//   //       cards+='</div>'
//   //       cards+='</div>'
//   //       cards+='</div>'
//   //       cards+='</div>'
//   //   });
//   //   $('#cards').append(cards)    
//   // }); 


    
// }
// $.get('/file_list', function(file_list) {
//   if (!file_list) {
//       console.log("erro a aceder ao server");
//   }
//   var cards = ''
//   for(i=0;i<file_list.filelist.length;i++){
//       //console.log(file_list.filelist[i].lista)
//       //console.log(file_list.filelist[i].nome_pasta)
//       cards+='<div class="card col-md-4">'
//       cards+='<div class="card-title">'
//       cards+='<h2>'
//       cards+=file_list.filelist[i].nome_pasta
//       cards+='<small>'
//       cards+='<button type="button" class="btn btn-outline-dark" onclick="window.location.href="/">Continue</button>'
//       cards+='</small>' 
//       cards+='</h2>'
//       cards+='<div class="task-count" >43</div>'
//       cards+='</div>'
//       cards+='<div class="card-flap flap1">'
//       cards+='<div class="card-description">'
//       cards+='<ul class="task-list">'

//       for(k=0;k<file_list.filelist[i].lista.length;k++){
//           // console.log(file_list.filelist[i].lista[k])
//           cards+='<li>'+file_list.filelist[i].lista[k]+'</li>'
//       }

//       cards+='</ul>'
//       cards+='</div>'
//       cards+='<div class="card-flap flap2">'
//       cards+='<div class="card-actions">'
//       cards+='<a class="btn" href="#">Close</a>'
//       cards+='</div>'
//       cards+='</div>'
//       cards+='</div>'
//       cards+='</div>'
//   }
//   $('#cards').append(cards)    
// });   


 


$(document).ready(function(){










    var zindex = 10;
    
    $("div.card").click(function(e){
      e.preventDefault();
  
      var isShowing = false;
  
      if ($(this).hasClass("d-card-show")) {
        isShowing = true
      }
  
      if ($("div.dashboard-cards").hasClass("showing")) {
        
        $("div.card.d-card-show")
          .removeClass("d-card-show");
  
        if (isShowing) {
      
          $("div.dashboard-cards")
            .removeClass("showing");
        } else {
   
          $(this)
            .css({zIndex: zindex})
            .addClass("d-card-show");
  
        }
  
        zindex++;
  
      } else {

        $("div.dashboard-cards")
          .addClass("showing");
        $(this)
          .css({zIndex:zindex})
          .addClass("d-card-show");
  
        zindex++;
      }
     
    });
    
  
  


 });