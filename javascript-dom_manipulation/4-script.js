// Script that adds a li element to a list when the user clicks on the element with id add_item
document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.getElementById('add_item');
  addItem.addEventListener('click', function () {
    const myList = document.querySelector('.my_list');
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});



