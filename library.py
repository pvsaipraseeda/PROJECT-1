import streamlit as st

# Title
st.title("📚 Library Management System")

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Search Book"])

# Temporary storage (in-memory)
if "books" not in st.session_state:
    st.session_state.books = []

# 👉 Add Book
if menu == "Add Book":
    st.header("➕ Add a New Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    year = st.number_input("Published Year", min_value=0, max_value=2100)

    if st.button("Add Book"):
        if title and author:
            st.session_state.books.append({
                "title": title,
                "author": author,
                "year": year
            })
            st.success("Book added successfully!")
        else:
            st.error("Please fill all fields")

# 👉 View Books
elif menu == "View Books":
    st.header("📖 All Books")

    if st.session_state.books:
        for i, book in enumerate(st.session_state.books, start=1):
            st.write(f"{i}. {book['title']} by {book['author']} ({book['year']})")
    else:
        st.warning("No books available")

# 👉 Search Book
elif menu == "Search Book":
    st.header("🔍 Search Book")

    search = st.text_input("Enter book title")

    if st.button("Search"):
        results = [b for b in st.session_state.books if search.lower() in b["title"].lower()]

        if results:
            for book in results:
                st.write(f"{book['title']} by {book['author']} ({book['year']})")
        else:
            st.error("Book not found")