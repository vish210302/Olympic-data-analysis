import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot  as plt
import plotly.figure_factory as ff
import preprocessor
import helper
import scipy

df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')

df=preprocessor.preprocess(df,region_df)
st.sidebar.title("Olympics Analysis")
user_menu=st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)
#st.dataframe(df)
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country= helper.country_year_list(df)
    selected_year=st.sidebar.selectbox('Select Year',years)
    selected_country = st.sidebar.selectbox('Select Country', country)
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year=='Overall' and selected_country=='Overall':
        st.title('Overall Tally')
    if selected_year!='Overall' and selected_country=='Overall':
        st.title('Medal Tally in ' +str(selected_year))
    if selected_year=='Overall' and selected_country!='Overall':
        st.title(selected_country+' Overall Performance')
    if selected_year!='Overall' and selected_country!='Overall':
        st.title(selected_country+' Performance in ' +str(selected_year)+'Olympics')
    st.table(medal_tally)

if user_menu=='Overall Analysis':
    editions=df['Year'].unique().shape[0] -1
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athletes=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]
    st.title('Top Statistics')
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Editons")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time=helper.data_over_time(df,'region')
    st.title("Participating Nations Over the Years")
    fig = px.line(nations_over_time, x="Edition", y='region')
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    st.title("Events Over the Time")
    fig = px.line(events_over_time, x="Edition", y='Event')
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    st.title("Athletes Over the Time")
    fig = px.line(athletes_over_time, x="Edition", y='Name')
    st.plotly_chart(fig)

    st.title("Events Over The Time(Every Sport)")
    fig,ax=plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True,fmt='d')
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list=df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport=st.selectbox('Select a sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)
if user_menu=='Country-wise Analysis':
    st.sidebar.title("Country-wise Analysis")
    region_list = df["region"].dropna().unique().tolist()
    region_list.sort()
    selected_country=st.sidebar.selectbox('Select a country',region_list)
    country_df=helper.yearwise_medal_tally(df,selected_country)
    st.title(selected_country + " " + "Medal Tally Over the Years")
    fig = px.line(country_df, x="Year", y='Medal')
    st.plotly_chart(fig)

    st.title(selected_country+ " "+"excels in the following sport")
    pt=helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax=sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes"+selected_country)
    sm=helper.most_successful_country(df, selected_country)
    st.table(sm)
if user_menu == 'Athlete-wise Analysis':
    st.title("Athlete-wise Analysis")
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4],
                             ['Overall Age', 'Gold Medallist', 'Silver Medallist', 'Bronze Medallist'], show_hist=False,
                             show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    x=[]
    name=[]
    famous_sports=['Basketball','Judo','Football','Athletics','Swimming','Tug-Of-War','Gymnastics','Shooting','Cycling','Wrestling','Boxing','Hockey','Weightlifting','Tennis','Archery','Table Tennis','Rugby',
'Golf']
    for sport in famous_sports:
        temp_df=athlete_df[athlete_df['Sport']==sport]
        x.append(temp_df[temp_df['Medal']=='Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(x,name, show_hist=False,show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title('Distribution of Age wrt Sports(Gold Medallist')
    st.plotly_chart(fig)

    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    st.title('Height vs Weight')
    selected_sport = st.selectbox('Select a sport', sport_list)
    temp_df= helper.weight_v_height(df, selected_sport)
    fig,ax=plt.subplots(figsize=(10,10))
    ax=sns.scatterplot(x=temp_df['Weight'],y=temp_df['Height'],hue=temp_df["Medal"],style=temp_df['Sex'],s=60)
    st.pyplot(fig)

    final=helper.men_women(df)
    st.title('Men and Women Participation Over the Years')
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False,height=600,width=1000)
    st.plotly_chart(fig)
