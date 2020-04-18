var wavesurfer = WaveSurfer.create({
    container: "#waveform",
    waveColor: "#176696",
    barHeight: 2,
    barGap: 1,
    height: 200,
    backgroundColor: "#f5f5f5",
    normalize: "true"
  });
  
  function clearcontent(element) {
    element.value = "";
  }
  
// The function handling the play and pause button event

function playButton() {
  wavesurfer.playPause();
}

function generateSpectrum(){
    document.getElementById("main-container").style.visibility = 'visible';
    loadExcitation(1);
    loadLogEnergy();
    loadPitchContour();
}

function loadExcitation(elem){
    var source = document.getElementById("excitationspectrum");
    var clone = source.cloneNode(true);
    clone.setAttribute("src","/graphs/lpresidual/lpresidual-wav" +document.getElementById("audionums").value +"-order"+elem+'.html');
    source.parentNode.replaceChild(clone, source);
    
}

function loadLogEnergy(){
    var source = document.getElementById("logenergycontour");
    var clone = source.cloneNode(true);
    clone.setAttribute("src","/graphs/logenergy/audio" +document.getElementById("audionums").value +"log_energy.html");
    source.parentNode.replaceChild(clone, source);
}

function loadPitchContour() {
    var source = document.getElementById("pitchcontour");
    var clone = source.cloneNode(true);
    clone.setAttribute("src","/graphs/pitch/audio" +document.getElementById("audionums").value +"pitch.html");
    source.parentNode.replaceChild(clone, source);
}
  
  function LoadAudio(elem) {
      
    document.getElementById("main-container").style.visibility = 'hidden';
    document.getElementById("audionums").value = elem.value;
      
    if (elem.value == 1) {
      wavesurfer.load("/static/wav/audio1.wav");
      console.log(elem.value);
    }
    if (elem.value == 2) {
        wavesurfer.load("/static/wav/audio2.wav");
        console.log(elem.value);
      }
    if (elem.value == 3) {
        wavesurfer.load("/static/wav/audio3.wav");
        console.log(elem.value);
      }
    if (elem.value == 4) {
        wavesurfer.load("/static/wav/audio4.wav");
        console.log(elem.value);
      } 
  }
  