
var content1, content2, val, fin;
//This function changes content of the experiment on changing the experiment number
function loadExpFrame() {

content1 = document.getElementById("speaker").value; 
content2 = document.getElementById("vowel").value ;
content1 = content1.toString()
content2 = content2.toString()
var expnum = content1+content2
val = "wav/"+content1+content2+".wav"
//freqs = preload(expnum)
//console.log(freqs)
document.getElementById("waveform").innerHTML=""
wavesurfer = WaveSurfer.create({
  container: "#waveform",
  waveColor: "#176696",
  barHeight: 2,
  barGap: 1,
  height: 400,
  backgroundColor: "#f5f5f5",
  normalize: "true",
});
wavesurfer.load(val)
wavesurfer.on("ready", function () {
  var timeline = Object.create(WaveSurfer.Timeline);

  timeline.init({
    wavesurfer: wavesurfer,
    container: "#waveform-timeline",
  });
});

document.getElementById("main-container").style.visibility="visible";
    var source = document.getElementById('autocorr');
    var clone = source.cloneNode(true);
    clone.setAttribute("src", "graphs/autocorr/"+content1+content2+"autocorr.html");
    source.parentNode.replaceChild(clone, source);
    
    var source = document.getElementById('lpc');
    var clone = source.cloneNode(true);
    clone.setAttribute("src", "graphs/lpc/"+content1+content2+"lpc.html");
    source.parentNode.replaceChild(clone, source);
    
console.log(document.getElementById("autocorr").getAttribute("src"))
document.getElementById("f0a").innerHTML= ""
document.getElementById("f1a").innerHTML= ""
document.getElementById("f2a").innerHTML= ""
document.getElementById("f3a").innerHTML= ""
document.getElementById("F0").value=''
document.getElementById("F1").value=''
document.getElementById("F2").value=''
document.getElementById("F3").value=''
}

function checkAns(){
content1 = document.getElementById("speaker").value; 
content2 = document.getElementById("vowel").value ;
content1 = content1.toString()
content2 = content2.toString()
var expnum = content1+content2

var client = new XMLHttpRequest();
client.open('GET', 'wav/'+expnum+'.txt');
client.onreadystatechange = function() {
  window.fin = client.responseText;
  fin = fin.split("\n")
  f0 = parseInt(document.getElementById("F0").value)
  f1 = parseInt(document.getElementById("F1").value)
  f2 = parseInt(document.getElementById("F2").value)
  f3 = parseInt(document.getElementById("F3").value)
  for (i=0; i<4; i++){
  	fin[i]=parseInt(fin[i])
  }
  if (fin[0]==f0){
  	document.getElementById("f0a").innerHTML= "F0 is correct"
}
  else{
  	var diff = f0-fin[0]
  	document.getElementById("f0a").innerHTML= "F0 is wrong by " + diff + " values"
  }
  if (fin[1]==f1){
  	document.getElementById("f1a").innerHTML= "F1 is correct"
  }
  else{
  	var diff = f1-fin[1]
  	document.getElementById("f1a").innerHTML= "F1 is wrong by " + diff + " values"
  }
  if (fin[2]==f2){
  	document.getElementById("f2a").innerHTML= "F2 is correct"
  }
  else{
  	var diff = f2-fin[2]
  	document.getElementById("f2a").innerHTML= "F2 is wrong by " + diff + " values"
  }
  if (fin[3]==f3){
  	document.getElementById("f3a").innerHTML= "F3 is correct"
  }
  else{
  	var diff = f3-fin[3]
  	document.getElementById("f3a").innerHTML= "F3 is wrong by " + diff + " values"
  }

}
client.send();


}