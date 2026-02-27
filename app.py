'''
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(music_title):
    response = requests.get("https://saavn.sumit.co/api/search/songs?query={}".format(music_title))
    data = response.json()
    return data['data']['results'][0]['image'][2]['Link']

def recommend(musics):
    music_index = music[music['title']==musics].index[0]
    distancecs = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_music=[]
    recommended_music_poster =[]
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music.iloc[i[0]].title)
        recommended_music_poster.append(fetch_poster(music_title))
    return recommended_music, recommended_music_poster
music_dict = pickle.load(open('/Users/test/Desktop/Task2/musicrec.pkl','rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open('/Users/test/Desktop/Task2/similarities.pkl','rb'))
st.title('Music Recommender System')

selected_music_name = st.selectbox('Select a music you like', music['title'].values)
if st.button('Recommed'):
    names, posters = recommend(selected_music_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
        '''
import streamlit as st
import pickle
import pandas as pd
import requests


# ---------- Fetch Poster ----------
def fetch_poster(music_title):
    try:
        response = requests.get(
            f"https://saavn.sumit.co/api/search/songs?query={music_title}"
        )
        data = response.json()
        return data['data']['results'][0]['image'][2]['Link']
    except:
        return "https://via.placeholder.com/300x300?text=No+Image"


# ---------- Recommend Function ----------
def recommend(selected_music):
    music_index = music[music['title'] == selected_music].index[0]
    distances = similarity[music_index]

    music_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_music = []
    recommended_posters = []

    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music_title)
        recommended_posters.append(fetch_poster(music_title))

    return recommended_music, recommended_posters


# ---------- Load Data ----------
music_dict = pickle.load(open('musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open('similarities.pkl', 'rb'))

# ---------- Streamlit UI ----------
st.title("🎵 Music Recommender System")

selected_music_name = st.selectbox(
    "Select a music you like",
    music['title'].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_music_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
