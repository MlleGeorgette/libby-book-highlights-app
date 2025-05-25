import pandas as pd
import streamlit as st
import html


# Read CSV files
titles_df = pd.read_csv('./dataframes/titles_df.csv')
highlights_df = pd.read_csv('./dataframes/highlights_df.csv')
bookmarks_df = pd.read_csv('./dataframes/bookmarks_df.csv')

titles_df['isbn'] = titles_df['isbn'].astype(str)
highlights_df['isbn'] = highlights_df['isbn'].astype(str)
bookmarks_df['isbn'] = bookmarks_df['isbn'].astype(str)

## Test streamlit app
st.title("Georgette's Book Highlights")

# Select book from reading_journey df
selected_book = st.selectbox('Select a book:', titles_df['title'])

# Filter reading_journey to get details of the selected book
book_details = titles_df[titles_df['title'] == selected_book].iloc[0]

# Display book details
st.image(book_details['cover_url'], width=150)
st.write(f"**Title**: {book_details['title']}")
st.write(f"**Author**: {book_details['author']}")

# filter highlights by the selected book's isbn
book_highlights = highlights_df[highlights_df['isbn'] == book_details['isbn']]

# Display highlights with a colored background based on the hex code
st.subheader('Highlights')
if not book_highlights.empty:
    for index, row in book_highlights.iterrows():
        highlight_color = row['color']  # Hex color code
        highlight_quote = row['quote']
        highlight_note = str(row.get('note', '') or '')

        # Create a styled block for each highlight
        st.markdown(
            f"""
            <div style="background-color: {highlight_color}; padding: 10px; margin: 5px; border-radius: 5px;">
                <p style="color: black; font-weight: bold;">Highlight:</p>
                <p style="color: black;">{highlight_quote}</p>
                {'<p style="color: black; font-style: italic; margin-top: 5px;"><strong>Note:</strong> ' + highlight_note + '</p>' if pd.notna(highlight_note) and highlight_note.strip() != "" else ''}
            </div>
            """, unsafe_allow_html=True)     


else:
    st.write("No highlights available for this book.")

# Display bookmarks (for audiobook notes)
book_bookmarks = bookmarks_df[bookmarks_df['isbn']] == str(book_details['isbn'])
book_bookmarks = book_bookmarks[book_bookmarks['note'].notna() & (book_bookmarks['note'].str.strip() != '')]

if not book_bookmarks.empty:
    st.subheader("Bookmarks (Notes)")
    for _, row in book_bookmarks.iterrows():
        bookmark_note = str(row.get('note', '') or '')
        st.markdown(f"""
                    <div style="background-color: #f0f0f0; padding: 10px; margin: 5px; border-radius: 5px;">
                <p style="color: black; font-style: italic;"><strong>Note:</strong> {note}</p>
            </div>
            """, unsafe_allow_html=True)