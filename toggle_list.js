function toggleList(element) {
    const content = element.nextElementSibling;
    const icon = element.querySelector('.toggle-icon');
  
    // Toggle the content visibility
    if (content.style.maxHeight) {
      content.style.maxHeight = null; // Collapse the content
      icon.textContent = '+'; // Change icon to +
    } else {
      content.style.maxHeight = content.scrollHeight + 'px'; // Expand the content
      icon.textContent = '-'; // Change icon to -
    }
  }