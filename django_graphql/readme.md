

Building GraphQL APIs in Django with Graphene



https://www.twilio.com/blog/graphql-apis-django-graphene#:~:text=A%20GraphQL%20server%20provides%20clients,that%20uses%20queries%20and%20mutations.

https://www.twilio.com/blog/graphql-apis-django-graphene#:~:text=A%20GraphQL%20server%20provides%20clients,that%20uses%20queries%20and%20mutations.

Issuing a query
Queries are used to request data from the server. The GraphQL code below is requesting all the books from the database. Enter it in the left-side panel of the GraphIQL interface.

query {
  allBooks {
    id
    title
    author
    yearPublished
    review
  }
}
Press the play button to execute the query and see the results in the right-side panel.

Next try the following query, which requests a single book by its id:

query {
  book(bookId: 2) {
    id
    title
    author
  }
}
Note how each query can specify which of the attributes of the book model need to be returned.

Creating a book
The following GraphQL snippet defines a mutation that adds a new book to the database:

mutation createMutation {
  createBook(bookData: {title: "Things Apart", author: "Chinua Achebe", yearPublished: "1985", review: 3}) {
    book {
      title,
      author,
      yearPublished,
      review
    }
  }
}
Updating an existing book
The next GraphQL mutation updates the book with id=6:

mutation updateMutation {
  updateBook(bookData: {id: 6, title: "Things Fall Apart", author: "Chinua Achebe", yearPublished: "1958", review: 5}) {
    book {
      title,
      author,
      yearPublished,
      review
    }
  }
}
Deleting a book
The final mutation example deletes the book with id=6 from the database:

mutation deleteMutation{
  deleteBook(id: 6) {
    book {
      id
    } 
  }
}

