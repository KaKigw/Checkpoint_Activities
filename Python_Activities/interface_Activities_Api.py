from Activities_API import Find_movie
import streamlit as st

def main():
    st.title("🎬 OMDB Movie Search")
    movie_input = st.text_input("Enter a movie title:")

    if st.button("Search") and movie_input:
        with st.spinner("Fetching movie data..."):
            movie_df = Find_movie(movie_input)
            if not movie_df.empty:
                st.success(f"Found {len(movie_df)} results")
                st.dataframe(movie_df)
                
                st.subheader("Movie Posters 🎞️")
                for _, row in movie_df.iterrows():
                    st.markdown(f"**{row['Title']} ({row['Year']})**")
                    if row['Poster'] and row['Poster'] != "N/A":
                        st.image(row['Poster'], width=150)
                    else:
                        st.caption("Poster not available.")

            else:
                st.warning("No results found. Try a different title.")

if __name__ == "__main__":
    main()

