// JavaScript code for basic pagination to show 6 events per page
const pageCards = document.querySelectorAll(".page-card");
const pageSize = 6; // Number of cards per page

// Function to show the specified page
const showPage = (pageNumber) => {
  pageCards.forEach((card, index) => {
    if (index >= pageSize * (pageNumber - 1) && index < pageSize * pageNumber) {
      card.classList.remove("hide");
    } else {
      card.classList.add("hide");
    }
  });
}

let currentPage = 1; // Current page number
showPage(currentPage); // Show the initial page

// Function to handle pagination clicks
const handlePaginationClick = (pageNumber) => {
  currentPage = pageNumber;
  showPage(currentPage);
}

// Example: Assuming you have pagination buttons with IDs "page-1", "page-2", etc.
const paginationButtons = document.querySelectorAll(".pagination-button");
paginationButtons.forEach(button => {
  button.addEventListener("click", () => {
    const pageNumber = parseInt(button.dataset.page);
    handlePaginationClick(pageNumber);
  });
});
