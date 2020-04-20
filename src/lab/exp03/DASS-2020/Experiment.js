// This js file is for page 1 and 2
/*
// This function defines the wavesurfer waveform and its related information
var wavesurfer = WaveSurfer.create({
  container: "#waveform",
  waveColor: "#176696",
  barHeight: 2,
  barGap: 1,
  height: 400,
  backgroundColor: "#f5f5f5",
  normalize: "true",
});

// When page is loaded load timeline
wavesurfer.on("ready", function () {
  var timeline = Object.create(WaveSurfer.Timeline);

  timeline.init({
    wavesurfer: wavesurfer,
    container: "#waveform-timeline",
  });
});

// This function provides zoom for the experiment
function zoom(elem) {
  wavesurfer.zoom(elem.value);
}

// This function handles play button
function playButton() {
  wavesurfer.playPause();
}




function preload() {
  var ctr=0
  for (let i=0; i<3; i++){
    for (let j=0; j<3; j++){
      var contentval=[];
     contentval[ctr] = loadStrings("wav/"+i+j+".txt");
     ctr++;
  }
}
  return contentval;

}




function setup() {
  noCanvas();
  //console.log(content1phn);
}
*/
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
document.getElementById("autocorr").setAttribute("src", "graphs/autocorr/"+content1+content2+"autocorr.html")
document.getElementById("lpc").setAttribute("src", "graphs/lpc/"+content1+content2+"lpc.html")
console.log(document.getElementById("autocorr").getAttribute("src"))
}

