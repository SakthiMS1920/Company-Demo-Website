let button = document.querySelector(".arrow"),
    links = document.querySelector(".Menu");

  button.addEventListener("click",() =>{
    links.classList.toggle("display");
    
    button.children[0].classList.toggle("toggle1");
    button.children[1].classList.toggle("toggle2");
    button.children[2].classList.toggle("toggle3");

})

const pan = document.getElementById('pan');
const text = document.getElementById('text');
const subs = document.getElementsByClassName('subs');

pan.addEventListener('click',function(){
  pan.classList.toggle('active');
});

const pan1 = document.getElementById('pan1');
const text1 = document.getElementById('text');
const subs1 = document.getElementsByClassName('subs1');

pan1.addEventListener('click',function(){
  pan1.classList.toggle('active1');
});

const pan2 = document.getElementById('pan2');
const text2 = document.getElementById('text');
const subs2 = document.getElementsByClassName('subs2');

pan2.addEventListener('click',function(){
  pan2.classList.toggle('active2');
});

const pan3 = document.getElementById('pan3');
const text3 = document.getElementById('text');
const subs3 = document.getElementsByClassName('subs3');

pan3.addEventListener('click',function(){
  pan3.classList.toggle('active3');
});


const pan4 = document.getElementById('pan4');
const text4 = document.getElementById('text');
const subs4 = document.getElementsByClassName('subs4');

pan4.addEventListener('click',function(){
  pan4.classList.toggle('active4');
});


