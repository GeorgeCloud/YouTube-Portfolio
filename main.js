// import data from './resources/video_data.js';

const itemsCart = [];
const ul_list = document.getElementById("shop-items");

async function loadData() {
  const res = await fetch('./resources/video_data.json')
  const json = await res.json()
  return json
}

// TODO: On change in file update

loadData().then(data => {
  for (let i = 0; i < data['videos'].length; i += 1){
    const currentItem = data['videos'][i];

    const newLi = document.createElement('li');
    ul_list.appendChild(newLi);

    const figure = document.createElement('figure');
    newLi.appendChild(figure);

    // Image Thumbnail
    const img = document.createElement('img');
    img.className = `thumbnail item-${i}`;
    img.src = currentItem.file_img_url;
    figure.appendChild(img);

    // Newly added
    const div = document.createElement('div');
    div.className = "item-player-desc";
    figure.appendChild(div);

    const figcation_decr = document.createElement('figcaption')
    figcation_decr.innerText = currentItem.file_name;
    div.appendChild(figcation_decr);

    const audio_tag = document.createElement('audio');
    audio_tag.controls = true;
    div.appendChild(audio_tag);

    const audio_source = document.createElement('source');
    // let newPath = ""
    // console.log(currentItem.file_path)
    // currentItem.file_path.forEach((item, i) => {
    //   console.log(item)
    // });

    audio_source.src = currentItem.file_path;
    audio_source.type = "audio/mp4";
    audio_tag.appendChild(audio_source);

    // const button = document.createElement('button');
    // button.id = data[i].name;
    // button.dataset.price = data[i].price;
    // button.className = "add-to-cart";
    // button.innerHTML = "Add to Cart";
    // figure.appendChild(button);
  }
  // debugger;
  // do something with json data here...
  // console.log(data)
})
