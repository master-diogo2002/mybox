async function createFolder(){
    await Swal.fire({
        background: '#2c2f33',
        confirmButtonColor:'#7289da',
        title: 'Create Folder',
        input: 'text',
        inputLabel: 'Folder Name',
        showClass: {popup: 'animate__animated animate__fadeInDown'},
        hideClass: {popup: 'animate__animated animate__fadeOutUp'},
        // inputValue: inputValue,
        showCancelButton: true,
        inputValidator: (value) => {
          if (!value) {
            return 'Invalid Name'
          }else{
            sendRequest(value);
          }
        }
      })
    console.log('here');
    location.reload();
}


async function createcat(){
  await Swal.fire({
      background: '#2c2f33',
      confirmButtonColor:'#7289da',
      title: 'Create Folder',
      input: 'text',
      inputLabel: 'Folder Name',
      showClass: {popup: 'animate__animated animate__fadeInDown'},
      hideClass: {popup: 'animate__animated animate__fadeOutUp'},
      // inputValue: inputValue,
      showCancelButton: true,
      inputValidator: (value) => {
        if (!value) {
          return 'Invalid Name'
        }else{
          sendRequest_cat(value);
        }
      }
    })
  console.log('here');
  location.reload();
}


function sendRequest(folder_name){
    const Http = new XMLHttpRequest();
    const url='/create/'+folder_name;
    Http.open("GET", url);
    Http.send();

}

function sendRequest_cat(folder_name){
  const Http = new XMLHttpRequest();
  const url= window.location.href+'/create/'+folder_name;
  Http.open("GET", url);
  Http.send();
}


