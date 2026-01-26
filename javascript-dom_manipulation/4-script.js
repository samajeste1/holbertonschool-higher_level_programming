// Task 4: List of elements
// Add a new li element to the list when clicking #add_item
document.getElementById('add_item').addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
