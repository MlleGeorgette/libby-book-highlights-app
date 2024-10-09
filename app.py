import pandas as pd
import streamlit as st


# Read CSV files
reading_journey_df = pd.read_csv('./dataframes/reading_journey_df.csv')
highlights_df = pd.read_csv('./dataframes/highlights_df.csv')

## Test streamlit app
st.title("Georgette's Book Highlights")

# Select book from reading_journey df
selected_book = st.selectbox('Select a book:', reading_journey_df['title'])

# Filter reading_journey to get details of the selected book
book_details = reading_journey_df[reading_journey_df['title'] == selected_book].iloc[0]

# Display book details
st.image(book_details['cover_url'], width=150)
st.write(f"**Title**: {book_details['title']}")
st.write(f"**Author**: {book_details['author']}")

# filter highlights by the selected book's isbn
book_highlights = highlights_df[highlights_df['isbn'] == book_details['isbn']]

# Display highlights
# st.subheader('Highlights')
# if not book_highlights.empty:
#     for index, row in book_highlights.iterrows():
#         st.markdown(f"* **Highlight:** {row['quote']}")
#         #st.markdown(f"* **Colour:** {row['color']}")

# else:
#     st.write("No highlights available for this book.")

# Display highlights with a colored background based on the hex code
st.subheader('Highlights')
if not book_highlights.empty:
    for index, row in book_highlights.iterrows():
        highlight_color = row['color']  # Hex color code
        highlight_text = row['quote']

        # Create a styled block for each highlight
        st.markdown(
            f"""
            <div style="background-color: {highlight_color}; padding: 10px; margin: 5px; border-radius: 5px;">
                <p style="color: black; font-weight: bold;">Highlight:</p>
                <p style="color: black;">{highlight_text}</p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.write("No highlights available for this book.")