//I need js to load file only when section is reached

videos_dir = '../video_slides'

chapters = [
  'Intro1',
  'Intro2',
  'Admin',
  'Book',
  'HowTo',
  'Overview',
  'Chap2_00',
  'Chap2_01',
  'Chap2_02',
  'Chap2_03',
]
counter = 0;
num_slides = chapters.length

add_attributes = function(slide){
    section = `<section><script src="js/add_video_slide.js" slide_scene="${slide}"/></section>`
    frags = loadFile(`video_slides/${slide}.txt`, slide)
    this.innerHTML =  `<section data-background-video="./video_slides/${slide}.mp4" id=${slide} data-background-color="#000000" id="vid" type="videoslide">
   ${frags}
  </section>`
}

function loadFile(filePath) {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
      result = xmlhttp.responseText;
    }
    return result;
  }

get_all_slides = function(){
  chapters.forEach(element => {
    frags = loadFile(`../video_slides/${element}.txt`);
    // note = loadFile(`notes/${slide}.txt`)
    document.write(`
    <section data-background-video="./video_slides/${element}.mp4" id=${element} data-background-color="#000000" id="vid" type="videoslide">
    ${frags}
    </section>`)
    });
  window.location.reload()
}

get_next_slide = function(){
  if(counter<num_slides){
    counter++;
    element = chapters[counter];
    frags = loadFile(`../video_slides/${element}.txt`);
    // note = loadFile(`notes/${slide}.txt`)
    document.write(`
    <section data-background-video="./video_slides/${element}.mp4" id=${element} data-background-color="#000000" id="vid" type="videoslide">
    ${frags}
    </section>`);
    }
}

get_slides_one_by_one = function()
{
  element = chapters[0];
  frags = loadFile(`../video_slides/${element}.txt`);
  // note = loadFile(`notes/${slide}.txt`)
  document.write(`
  <section data-background-video="./video_slides/${element}.mp4" id=${element} data-background-color="#000000" id="vid" type="videoslide">
  ${frags}
  </section>`);
}
get_slides_one_by_one()
setInterval(get_next_slide, 500)