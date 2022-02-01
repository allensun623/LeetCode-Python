const clickSign = () => {
  try {
    var main = document.getElementsByTagName('main')[0];
    var divBtn = main.getElementsByTagName('div')[1];
    var signBtn = divBtn.getElementsByTagName('button')[0];
    signBtn.click();
    return true;
  } catch (e) {
    return false;
  }
};

const clickSave = () => {
  try {
    const name = 'Xinyan Li';
    var form = document.querySelector('form');
    var saveBtn = form.querySelectorAll('button')[1];
    var formInput = form.querySelector('input');
    // formInput.setAttribute('value', name);
    formInput.addEventListener(
      'change',
      !saveBtn.disabled && formInput.value == name && saveBtn.click(),
    );
  } catch (e) {}
};

var intervalId = window.setInterval(function () {
  /// call your function here
  var clicked = false;
  if (!clicked) {
    clicked = clickSign();
  }
  clicked && clickSave();
}, 10000);

var form = document.querySelector('form');
var formInput = form.querySelector('input');
formInput.setAttribute('value', 'Lun Sun');
formInput.setAttribute('error', '');
formInput.setAttribute('aria-invalid', 'false');
// form.querySelector('input').value = 'Lun Sun';

// get save button
var saveBtn = form.querySelectorAll('button')[1];
saveBtn.disabled = false;
saveBtn.click();
