// Add books that do not include word "great" to favouriteBooks
// Print out favourite books

function addFavouriteBook(bookName) {
    if (!bookName.toLowerCase().includes('great')) {
        favouriteBooks.push(bookName);
    }
}

function printFavouriteBooks() {
    console.log(`Favourite books: ${String(favouriteBooks.length)}.`)
    for (let bok of favouriteBooks) {
        console.log(bok)
    }
}

var favouriteBooks = [];

addFavouriteBook("A Song of Ice and Fire");
addFavouriteBook("The Great Gatsby");
addFavouriteBook("Crime & Punishment");
addFavouriteBook("Great Expectations");
addFavouriteBook("You Don't Know JS");

printFavouriteBooks()