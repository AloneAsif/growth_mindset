import streamlit as st

# Initialize session state for storing books
if "books" not in st.session_state:
    st.session_state.books = []

def add_book(title, author, publication_year, genre, read_status):
    """Add a new book to the list"""
    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read_status": read_status
    }
    st.session_state.books.append(book)
    st.success(f"Added: {title}")

def remove_book(title):
    """Remove a book by title"""
    for book in st.session_state.books:
        if book["title"].lower() == title.lower():
            st.session_state.books.remove(book)
            st.warning(f"Removed: {title}")
            return
    st.error(f"No book found with title '{title}'")

def display_books():
    """Display all books"""
    st.subheader("📖 Your Book List")
    if st.session_state.books:
        for book in st.session_state.books:
            st.write(f"**{book['title']}** by {book['author']} ({book['publication_year']}) - *{book['genre']}* [{book['read_status']}]")
    else:
        st.info("No books added yet.")

def display_statistics():
    """Display statistics about the books"""
    total_books = len(st.session_state.books)
    if total_books == 0:
        st.subheader("📊 Statistics")
        st.info("No books added yet.")
        return

    read_books = sum(1 for book in st.session_state.books if book["read_status"] == "Completed")
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    st.subheader("📊 Book Statistics")
    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books}")
    st.write(f"📖 **Percentage Read:** {percentage_read:.2f}%")

# Streamlit UI
st.title("📚 Book Manager")

# Sidebar Menu
menu = st.sidebar.radio("Navigation", ["Add Book", "Remove Book", "Display All Books", "Statistics", "Exit"])

if menu == "Add Book":
    st.subheader("➕ Add a Book")
    with st.form("Add Book"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        publication_year = st.number_input("Publication Year", min_value=1000, max_value=3000, step=1)
        genre = st.text_input("Genre")
        read_status = st.selectbox("Read Status", ["Unread", "Reading", "Completed"])
        submitted = st.form_submit_button("Add Book")
        if submitted and title:
            add_book(title, author, publication_year, genre, read_status)

elif menu == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    remove_title = st.text_input("Enter book title to remove")
    if st.button("Remove Book"):
        remove_book(remove_title)

elif menu == "Display All Books":
    display_books()

elif menu == "Statistics":
    display_statistics()

elif menu == "Exit":
    st.subheader("👋 Exiting the app...")
    st.info("Close the browser tab to exit.")

