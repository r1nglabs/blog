function main() {
  const body = document.querySelector('body');
  body.append(render('data/DSC_6446.JPG'));
  body.append(render('data/DSC_7316.JPG'));
}

function render(path) {
  const photo = document.createElement('div');
  photo.className = 'photo';
  photo.style.backgroundImage = `url('${path}')`;
  const glass_layer = document.createElement('div');
  glass_layer.className = 'glass-layer';

  const img = document.createElement('img');
  img.src = path;
  glass_layer.append(img);
  photo.append(glass_layer);
  return photo
}

main();
