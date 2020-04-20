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

function LoadExperiment(elem) {
  /*if (elem.value == 1 || elem.value == 2 || elem.value == 3 || elem.value == 4) {
    wavesurfer.load("../wav/ex" + elem.value + ".wav");
    console.log(elem.value);
  } else {*/
    wavesurfer.load("wav/ex1.wav");
    console.log(elem.value);
 // }
}
