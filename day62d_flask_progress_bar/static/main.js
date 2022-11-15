var timeout;

async function getStatus() {

  let get;
  
  try {
    const res = await fetch("/status");
    get = await res.json();
  } catch (e) {
    console.error("Error: ", e);
  }
  
  document.getElementById("innerStatus").innerHTML = get.status * 10 + "&percnt;";
  
  if (get.status == 10){
    document.getElementById("innerStatus").innerHTML += " Done.";
    clearTimeout(timeout);
    return false;
  }
   
  timeout = setTimeout(getStatus, 1000);
}

getStatus();


let btn = document.querySelector('button')

btn.addEventListener('click', () =>{
  btn.innerText = 'Sending';
  getStatus();
});




// $('#test').click(function(){
//     alert("getting status");
//   // document.getElementById("test").textContent="Submit";
//   // $(this).prop("value", "DISABLED!!");
//   // $(this).toggleClass("active"); 
//   // $(this).prop("disabled",true);
//   // getStatus();
// });