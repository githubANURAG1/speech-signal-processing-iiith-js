var wavesurfer = WaveSurfer.create({
  container: "#waveform",
  waveColor: "#176696",
  barHeight: 2,
  barGap: 1,
  height: 200,
  backgroundColor: "#f5f5f5",
  normalize: "true",
});

function clearcontent(element) {
  element.value = "";
}

function playButton() {
  wavesurfer.playPause();
}

function generateSpectrum() {
    document.getElementById("main-container").style.visibility = "visible";
  document.getElementById("windowformtype").selectedIndex = 0;
  changeSpectrum("rectangular");
  document.getElementById("nfftvalue").selectedIndex = 0;
  changefft(64);
  document.getElementById("ordervalue").selectedIndex = 0;
  changeorder(1);
}

function changeSpectrum(elem) {
    
    var source = document.getElementById("windowedspectrums");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','/graphs/window/line-'+document.getElementById("audionum").value+'-'+elem+'.html')
    source.parentNode.replaceChild(clone,source);
}

function changefft(elem) {
    var source = document.getElementById("nfftspectrum");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','/graphs/logspectrum/stft-wav'+document.getElementById("audionum").value+'-nfft'+elem+'.html')
    source.parentNode.replaceChild(clone,source);
}

function changeorder(elem) {
    
    var source = document.getElementById("lpresidual");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','/graphs/lpresidual/lpresidual-wav'+document.getElementById("audionum").value+'-order'+elem+'.html')
    source.parentNode.replaceChild(clone,source);

  generate_spectrum(elem);
}

function generate_spectrum(elem) {
    var source = document.getElementById("lpspectrum");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','/graphs/lpspectrum/lpspectrum-wav'+document.getElementById("audionum").value+'-order'+elem+'.html')
    source.parentNode.replaceChild(clone,source);
}

function LoadAudio(elem) {
  document.getElementById("audionum").value = elem.value;
  document.getElementById("windowformtype").selectedIndex = 0;
    
    document.getElementById("main-container").style.visibility = "hidden";

  var source = document.getElementById("windowedspectrums");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','')
    source.parentNode.replaceChild(clone,source);
    
    var source = document.getElementById("nfftspectrum");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','')
    source.parentNode.replaceChild(clone,source);
    
    var source = document.getElementById("lpresidual");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','')
    source.parentNode.replaceChild(clone,source);
    
    var source = document.getElementById("lpspectrum");
    var clone = source.cloneNode(true);
    clone.setAttribute('src','')
    source.parentNode.replaceChild(clone,source);
    
  if (elem.value == 1 || elem.value == 2) {
    wavesurfer.load("/static/wav/audio" + elem.value + ".wav");
    console.log(elem.value);
  } else {
    wavesurfer.load("/static/wav/audio2.wav");
    console.log(elem.value);
  }
}
