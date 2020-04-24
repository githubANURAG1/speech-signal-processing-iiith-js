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

wavesurfer.on("ready", function() {
  var timeline = Object.create(WaveSurfer.Timeline);

  timeline.init({
    wavesurfer: wavesurfer,
    container: "#waveform-timeline"
  });
});

function LoadAudio(elem) {
  if (elem.value == 1 || elem.value == 2) {
    wavesurfer.load("/static/wav/audio" + elem.value + ".wav");
    console.log(elem.value);
  } else {
    wavesurfer.load("/static/wav/audio2.wav");
    console.log(elem.value);
  }
}
