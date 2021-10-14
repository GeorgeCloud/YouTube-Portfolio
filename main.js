const ul_list = document.getElementById("shop-items");

async function loadData() {
  const res = await fetch('./resources/video_data.json')
  const json = await res.json()
  return json
}

loadData().then(data => {
  for (let i = 0; i < data['videos'].length; i += 1){
    const currentItem = data['videos'][i];

    const newLi = document.createElement('li');
    ul_list.appendChild(newLi);

    const figure = document.createElement('figure');
    newLi.appendChild(figure);

    const img = document.createElement('img');
    img.className = `thumbnail item-${i}`;
    img.src = currentItem.file_img_url;
    figure.appendChild(img);

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
    audio_source.src = currentItem.file_path;
    audio_source.type = "audio/mp4";
    audio_tag.appendChild(audio_source);
  }
})
