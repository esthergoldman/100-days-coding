
//clear buttom RELOAD PAGE

function clean(){
	window.location.reload();
} 

 // close
// Wire-up an on click event listener.
document.getElementById("close").addEventListener("click", function() {
    // Emit a "close" message to main.
    self.port.emit("close");
  });


function createBubble(){
    const section = document.querySelector('section')
    const createElement = document.createElement('span')
    var size = Math.random() * 60;

    createElement.style.width = 20 + size + 'px';
    createElement.style.height = 20 + size + 'px';
    createElement.style.left = Math.random() * innerWidth + "px";
    section.appendChild(createElement);

    setTimeout(() =>{
        createElement.remove()
    },4000)

}