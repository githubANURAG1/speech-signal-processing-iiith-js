// This function defines the wavesurfer waveform and its related information
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

// The function handling the play and pause button event

function playButton() {
  wavesurfer.playPause();
}

// This functions handle the main container whenver any change is brought to the audio file option

function generateSpectrum() {
  document.getElementById("main-container").style.visibility = "visible";
  document.getElementById("lporder").selectedIndex = "0";
  document.getElementById("lptype").selectedIndex = "0";
  loadExcitation();
  loadLogEnergy();
  loadPitchContour();
}

// This function handles Excitation spectrum

function loadExcitation() {
  var order_elem = document.getElementById("lporder");
  var order_val = order_elem.options[order_elem.selectedIndex].value;

  var lp_type = document.getElementById("lptype");
  var lp_value = lp_type.options[lp_type.selectedIndex].text;

  var source = document.getElementById("excitationspectrum");
  var clone = source.cloneNode(true);
  clone.setAttribute(
    "src",
    "graphs/" +
      lp_value +
      "/" +
      lp_value +
      "-wav" +
      document.getElementById("audionums").value +
      "-order" +
      order_val +
      ".html"
  );
  source.parentNode.replaceChild(clone, source);
}

// This function handles energy contour

function loadLogEnergy() {
  var source = document.getElementById("logenergycontour");
  var clone = source.cloneNode(true);
  clone.setAttribute(
    "src",
    "graphs/logenergy/audio" +
      document.getElementById("audionums").value +
      "log_energy.html"
  );
  source.parentNode.replaceChild(clone, source);
}

// This function handles pitch contour
function loadPitchContour() {
  var source = document.getElementById("pitchcontour");
  var clone = source.cloneNode(true);
  clone.setAttribute(
    "src",
    "graphs/pitch/audio" +
      document.getElementById("audionums").value +
      "pitch.html"
  );
  source.parentNode.replaceChild(clone, source);
}

// This function Loads audio on startup of the page.
function LoadAudio(elem) {
  document.getElementById("main-container").style.visibility = "hidden";
  document.getElementById("audionums").value = elem.value;

  if (elem.value == 1) {
    wavesurfer.load("wav/audio1.wav");
    console.log(elem.value);
  }
  if (elem.value == 2) {
    wavesurfer.load("wav/audio2.wav");
    console.log(elem.value);
  }
  if (elem.value == 3) {
    wavesurfer.load("wav/audio3.wav");
    console.log(elem.value);
  }
  if (elem.value == 4) {
    wavesurfer.load("wav/audio4.wav");
    console.log(elem.value);
  }
}
