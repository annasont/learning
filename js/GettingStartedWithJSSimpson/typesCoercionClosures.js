// functions addFavouiriteBook and printFavouriteBooks moved to class Bookshelf as a methods.

class Bookshelf {
    constructor() {
        this.favouriteBooks = [];
    }

    addFavouriteBook(bookName) {
        if (!bookName.toLowerCase().includes('great')) {
            this.favouriteBooks.push(bookName);
        } 
    }
    printFavouriteBooks() {
        console.log(`Favourite books: ${String(this.favouriteBooks.length)}.`);
        for (let bok of this.favouriteBooks) {
            console.log(bok);
        }
    }

}

function loadBooks(instanceOfBookshelf) {
    fakeAjax(BOOK_API, function loopThroughBookNames(bookNames){
        for (let bookName of bookNames) {
            instanceOfBookshelf.addFavouriteBook(bookName)
        }
        instanceOfBookshelf.printFavouriteBooks()
    });
}

var BOOK_API = "https://some.url/api";


function fakeAjax(url,cb) {
	setTimeout(function fakeLoadingDelay(){
		cb([
			"A Song of Ice and Fire",
			"The Great Gatsby",
			"Crime & Punishment",
			"Great Expectations",
			"You Don't Know JS"
		]);
	},500);
}

var annasBookshelf = new Bookshelf()
loadBooks(annasBookshelf)