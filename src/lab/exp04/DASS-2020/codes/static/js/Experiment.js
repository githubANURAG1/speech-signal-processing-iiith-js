

// This function provides zoom for the experiment
function zoom(elem) {
  wavesurfer.zoom(elem.value);
}

// This function handles play button
function playButton() {
  wavesurfer.playPause();
}



var content1, content2, content3, val, fin;
//This function changes content of the experiment on changing the experiment number
function loadExpFrame() {


content1 = document.getElementById("bits").value; 
content2 = document.getElementById("samp").value ;
content3 = document.getElementById("lang").value ;
content1 = content1.toString()
content2 = content2.toString()
content3 = content3.toString()
var expnum = content3+content1+content2
val = "static/media/wav/ex"+expnum+".wav"
console.log(val)
document.getElementById("waveform").innerHTML=""
window.wavesurfer = WaveSurfer.create({
  container: "#waveform",
  waveColor: "#176696",
  barHeight: 2,
  barGap: 1,
  height: 400,
  backgroundColor: "#f5f5f5",
  normalize: "true",
});
window.wavesurfer.load(val)
console.log(wavesurfer)
window.wavesurfer.on("ready", function () {
  var timeline = Object.create(WaveSurfer.Timeline);

  timeline.init({
    wavesurfer: window.wavesurfer,
    container: "#waveform-timeline",
  });
});

}



