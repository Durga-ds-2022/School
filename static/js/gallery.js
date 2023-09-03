// JavaScript code for filtering cards and pagination
const filterButtons = document.querySelectorAll("#filter-buttons button");
const pageCards = document.querySelectorAll(".page-card");
const pageSize = 12; // Number of cards per page

// Function to filter cards based on filter buttons and pagination
const filterAndPaginateCards = (e) => {
  document.querySelector("#filter-buttons .active").classList.remove("active");
  e.target.classList.add("active");

  const selectedFilter = e.target.dataset.filter;

  pageCards.forEach(card => {
    const cardCategory = card.dataset.name;
    const cardIndex = parseInt(card.dataset.index);

    // Apply filtering based on the selected category or show all cards
    const filterCondition = selectedFilter === "all" || cardCategory === selectedFilter;

    // Show the card if it matches the filter and falls within the current page's range
    if (filterCondition && cardIndex >= pageSize * (currentPage - 1) && cardIndex < pageSize * currentPage) {
      card.classList.remove("hide");
    } else {
      card.classList.add("hide");
    }
  });
}

let currentPage = 1; // Current page number
filterButtons.forEach(button => button.addEventListener("click", () => {
  currentPage = 1; // Reset to first page when a category is clicked
  filterAndPaginateCards(event);
}));

// Initial filtering and pagination on page load
filterAndPaginateCards({ target: filterButtons[0] }); // Assuming the first filter button is "Show all"
