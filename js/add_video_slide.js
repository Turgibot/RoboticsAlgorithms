var env = PRODUCTION
var slide = document.currentScript.getAttribute('slide_scene');
function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  console.log("load")
  return result;
}
frags = loadFile(`video_slides/${slide}.txt`)
note = loadFile(`notes/${slide}.txt`)
if(env=='LOCAL'){
  document.write(`
<section data-background-video="./video_slides/${slide}.mp4" id=${slide} data-background-color="#000000" id="vid" type="videoslide">
 ${frags}
 <aside class="notes">
    ${note}
  </aside>
</section>`)
}
else{
  document.write(`
  <section data-background-video="./video_slides/${slide}.mp4" id=${slide} data-background-color="#000000" id="vid" type="videoslide">
   ${frags}
  </section>`)
}
