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

function playButton() {
  wavesurfer.playPause();
}

function generateSpectrum() {
  var img = document.createElement("img");
  document.getElementById("windowformtype").selectedIndex = 0;
  console.log(document.getElementById("windowformtype"));
  img.src =
    "/windowed/" + document.getElementById("audionum").value + "/rectangular";
  src = document.getElementById("windowedspecturm");
  if (!src.hasChildNodes()) {
    src.appendChild(img);
  } else {
    src.removeChild(src.lastChild);
    src.appendChild(img);
  }

  // var img = document.createElement("img");
  // document.getElementById("nfftvalue").selectedIndex = 0;
  // console.log(document.getElementById("nfftvalue"));
  // img.src = "/stft/" + document.getElementById("audionum").value + "/64";
  // src = document.getElementById("nfftspectrum");
  // if (!src.hasChildNodes()) {
  //   src.appendChild(img);
  // } else {
  //   src.removeChild(src.lastChild);
  //   src.appendChild(img);
  // }
}

function changeSpectrum(elem) {
  var img = document.createElement("img");
  img.src =
    "/windowed/" + document.getElementById("audionum").value + "/" + elem.value;
  src = document.getElementById("windowedspecturm");
  if (!src.hasChildNodes()) {
    src.appendChild(img);
  } else {
    src.removeChild(src.lastChild);
    src.appendChild(img);
  }
}

function LoadAudio(elem) {
  document.getElementById("audionum").value = elem.value;
  document.getElementById("windowformtype").selectedIndex = 0;

  src = document.getElementById("windowedspecturm");
  if (src.hasChildNodes()) {
    src.removeChild(src.lastChild);
  }
  if (elem.value == 1 || elem.value == 2) {
    wavesurfer.load("/static/wav/audio" + elem.value + ".wav");
    console.log(elem.value);
  } else {
    wavesurfer.load("/static/wav/audio2.wav");
    console.log(elem.value);
  }
}
