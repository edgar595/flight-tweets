from flask import Flask, render_template, request, redirect, url_for
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

csv_path = "C:\\Users\\USER\\OneDrive\\Desktop\\data analysis\\Python\\tweetsplane\\Tweets.csv"
df = pd.read_csv(csv_path)

# Group the DataFrame by the 'airline' column and count the flights for each airline
airline_counts = df['airline'].value_counts().reset_index()

# Rename the columns for clarity
airline_counts.columns = ['Airline', 'Flight Count']

# Find the number of distinct airlines
num_distinct_airlines = airline_counts['Airline'].nunique()

diff_flights = f"Number of Airlines"

# Print the number of tweets in the 'text' column
num_tweets = len(df['text'])

# Data
airlines = airline_counts['Airline']
flight_counts = airline_counts['Flight Count']

# Sample data
airlines = ['Delta', 'United', 'American', 'Southwest', 'US Airways', 'Virgin America']
airline_counts = [2222, 3822, 2759, 2420, 2913, 504]

# Sample data for the sentiment distribution
sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [971, 855, 396],
    'SentimentLabel': ['Positive', 'Neutral', 'Negative']
}

# Create circular (doughnut) charts for Delta, United, and American
delta_fig = go.Figure(data=[go.Pie(
    labels=sentiment_data['Sentiment'],
    values=sentiment_data['Count'],
    customdata=sentiment_data['SentimentLabel'],  # Custom data for labels
    hole=0.3,
    hovertemplate="%{label}: %{percent} <br>%{customdata}",  # Custom hovertemplate
    showlegend=False  # Remove the legend
)])

delta_fig.update_layout(title_text='Delta Airline tweets')

united_sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [1366, 1380, 1076],
    'SentimentLabel': ['Positive', 'Neutral', 'Negative']
}

united_fig = go.Figure(data=[go.Pie(
    labels=united_sentiment_data['Sentiment'],
    values=united_sentiment_data['Count'],
    customdata=united_sentiment_data['SentimentLabel'],  # Custom data for labels
    hole=0.3,
    hovertemplate="%{label}: %{percent} <br>%{customdata}",  # Custom hovertemplate
    showlegend=False  # Remove the legend
)])

united_fig.update_layout(title_text='United Airline tweets')

# Data for American Airlines
american_sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [984, 1061, 714],
    'SentimentLabel': ['Positive', 'Neutral', 'Negative']
}

american_fig = go.Figure(data=[go.Pie(
    labels=american_sentiment_data['Sentiment'],
    values=american_sentiment_data['Count'],
    customdata=american_sentiment_data['SentimentLabel'],  # Custom data for labels
    hole=0.3,
    hovertemplate="%{label}: %{percent} <br>%{customdata}",  # Custom hovertemplate
    showlegend=False  # Remove the legend
)])

american_fig.update_layout(title_text='American Airline tweets')

# Data for US Airways
us_airways_sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [1000, 2000, 3000],
    'SentimentLabel': ['Positive', 'Neutral', 'Negative']
}

us_airways_fig = go.Figure(data=[go.Pie(
    labels=us_airways_sentiment_data['Sentiment'],
    values=us_airways_sentiment_data['Count'],
    customdata=us_airways_sentiment_data['SentimentLabel'],  # Custom data for labels
    hole=0.3,
    hovertemplate="%{label}: %{percent} <br>%{customdata}",  # Custom hovertemplate
    showlegend=False  # Remove the legend
)])

us_airways_fig.update_layout(title_text='US Airways tweets')

# Data for Southwest Airlines
southwest_sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [999, 921, 500],
    'SentimentLabel': ['Positive', 'Neutral', 'Negative']
}

southwest_fig = go.Figure(data=[go.Pie(
    labels=southwest_sentiment_data['Sentiment'],
    values=southwest_sentiment_data['Count'],
    customdata=southwest_sentiment_data['SentimentLabel'],  # Custom data for labels
    hole=0.3,
    hovertemplate="%{label}: %{percent} <br>%{customdata}",  # Custom hovertemplate
    showlegend=False  # Remove the legend
)])

southwest_fig.update_layout(title_text='Southwest Airline tweets')

# Create circular (doughnut) chart for Virgin America
virgin_america_sentiment_data = {
    'Sentiment': ['Positive', 'Neutral', 'Negative'],
    'Count': [225, 196, 83],
    'SentimentLabel': ['Positive', 'Neutral', 'Negative']
}

virgin_america_fig = go.Figure(data=[go.Pie(
    labels=virgin_america_sentiment_data['Sentiment'],
    values=virgin_america_sentiment_data['Count'],
    customdata=virgin_america_sentiment_data['SentimentLabel'],  # Custom data for labels
    hole=0.3,
    hovertemplate="%{label}: %{percent} <br>%{customdata}",  # Custom hovertemplate
    showlegend=False  # Remove the legend
)])


virgin_america_fig.update_layout(title_text='Virgin America Airline tweets')

# Sample data for the sentiment distribution of each airline
sentiment_data = {
    'Delta': {'Positive': 971, 'Neutral': 855, 'Negative': 396},
    'United': {'Positive': 1366, 'Neutral': 1380, 'Negative': 1076},
    'American': {'Positive': 984, 'Neutral': 1061, 'Negative': 714},
    'Virgin America': {'Positive': 225, 'Neutral': 196, 'Negative': 83},
    'Southwest': {'Positive': 999, 'Neutral': 921, 'Negative': 500},
    'US Airways': {'Positive': 1359, 'Neutral': 917, 'Negative': 720}
}

# Combine data for all airlines into a list
all_airlines_data = []
for airline, data in sentiment_data.items():
    airline_data = []
    for sentiment, count in data.items():
        airline_data.extend([sentiment] * count)
    all_airlines_data.append(airline_data)

# Create a single histogram with three bars for each airline
fig = go.Figure()

# Define colors for each sentiment
colors = {
    'Positive': 'green',
    'Neutral': 'gray',
    'Negative': 'red'
}

# Add bars for each airline
for airline, data in sentiment_data.items():
    for sentiment in data.keys():
        fig.add_trace(go.Bar(x=[airline], y=[data[sentiment]], name=sentiment, marker_color=colors[sentiment]))

fig.update_layout(title='Tweet Distribution for Airlines', showlegend=False, height=400)

# Sample data for flight counts by day
flight_counts_data = {
    'Day': ['2015-02-16', '2015-02-17', '2015-02-18', '2015-02-19', '2015-02-20', '2015-02-21', '2015-02-22', '2015-02-23', '2015-02-24'],
    'Flight Count': [4, 1408, 1344, 1376, 1500, 1557, 3079, 3028, 1344],
}

# Create a line plot for flight counts by day
flight_counts_fig = go.Figure(data=go.Scatter(
    x=flight_counts_data['Day'],
    y=flight_counts_data['Flight Count'],
    mode='lines+markers',
    marker=dict(color='blue'),
    line=dict(shape='linear'),
    connectgaps=True
))

flight_counts_fig.update_layout(title='Flight Counts by Day', xaxis_tickangle=-45)

# Create a Flask instance
app_flask = Flask(__name__)

# Define a route and view function for the security page
@app_flask.route('/')
def security_page():
    return render_template('security_key.html')

# Define a route and view function to handle form submission
@app_flask.route('/authenticate', methods=['POST'])
def authenticate():
    security_key = request.form.get('security_key')
    # Check if the security_key is correct (e.g., compare it to '1234')
    if security_key == '1234':
        # Redirect to the Dash app
        return redirect('/dashboard')
    else:
        # Add an error message or redirect to an error page if the key is incorrect
        return "Access Denied: Invalid Security Key"

# Create a Dash app instance
dash_app = Dash(__name__, server=app_flask, url_base_pathname='/dashboard/')


# Define the Dash app layout
dash_app.layout = html.Div([
    html.H2(" Exploring Airline Sentiment and Flight Data through Data Analysis and Visualizations", style={'color': 'White'}),

    html.Link(rel='stylesheet', href='/static/styles.css'),

html.Div([
    html.Div([
        dcc.Dropdown(
            id='option-dropdown',
            options=[
                {'label': 'Delta', 'value': 'Delta'},
                {'label': 'United', 'value': 'United'},
                {'label': 'American', 'value': 'American'},
                {'label': 'US Airways', 'value': 'US Airways'},
                {'label': 'Southwest', 'value': 'Southwest'},
                {'label': 'Virgin America', 'value': 'Virgin America'}  # Corrected typo in 'Virgin America'
            ],
            value='Delta',  # Default selected value
        ),
        dcc.Graph(id='sentiment-chart', style={'height': '365px'})
    ], style={'color': 'black', 'border-radius': '10px', 'width': '30%', 'height': '300px', 'margin-right': '20px'}),
    html.Div([
    dcc.Graph(id='graph'),
    dcc.Interval(
        id='interval-component',
        interval=15*1000,  # 15 seconds in milliseconds
        n_intervals=0  # Initialize n_intervals to 0
    )
], style={'width': '67%', 'border-radius': '10px'}),
], style={'display': 'flex', 'height': '400px', 'border': '2px solid white', 'border-radius': '10px'}),


 # Add spacing between the two HTML elements
    html.Div(style={'margin-top': '20px'}),  # Adjust margin-top as needed

    # Parent container for both elements
    html.Div([
        # Slideshow container for tweets with a bird icon at the end and border radius
        html.Div([
            html.Div(id='tweet-container', style={'color': 'black', 'flex-grow': '1'}),
            html.Img(src='/static/bird.png', style={'height': '50px', 'width': '50px', 'margin-bottom': '10px'}),
        ], style={'display': 'flex', 'flex-direction': 'row-reverse', 'color': 'blue', 'width': '30%', 'border': '2px solid white', 'border-radius': '10px', 'background-color': 'white'}),
        
        # Interval component to control slideshow timing (set to 3 seconds)
        dcc.Interval(
            id='slideshow-interval',
            interval=3000,  # milliseconds
            n_intervals=0
        ),

        # Add margin between the two elements
        html.Div(style={'width': '10px'}),  # Adjust the width for spacing
        
        # HTML element to display flight data
    html.Div([
        # Add "hello" texts with equal spacing
    html.Div(
        html.Div([
            html.Div(str(num_distinct_airlines), style={'color': 'black', 'fontSize': '36px', 'fontWeight': 'bold', 'textAlign': 'center'}),
            html.Div(diff_flights, style={'color': 'black'}),
            ], style={'display': 'inline-block', 'padding': '10px', 'fontWeight': 'bold'})),
         html.Div([
        html.Div(id='tweet-count', style={'color': 'black', 'fontSize': '36px','fontWeight': 'bold','padding': '10px'}),
        html.Div("Number of Tweets", style={'color': 'black', 'fontWeight': 'bold'}),
    ]),
    html.Div([
        html.Div("2015-02-22", style={'color': 'black', 'fontSize': '30px','fontWeight': 'bold','padding': '10px'}),
        html.Div("Day with Most tweets", style={'color': 'black', 'fontWeight': 'bold'}),
    ]),
        html.Div([
        html.Div("4", style={'color': 'black', 'fontSize': '36px','fontWeight': 'bold','padding': '10px'}),
        html.Div("Time Zones", style={'color': 'black', 'fontWeight': 'bold'}),
    ]),
    ], style={'width': '70%', 'display': 'flex', 'justify-content': 'space-between' , 'background-color': 'white', 'border-radius': '10px'}),
    ], style={'display': 'flex', 'justify-content': 'space-between' }),
      
    dcc.Interval(
        id='count-interval',
        interval=100,  # Update every 100 milliseconds (adjust as needed)
        n_intervals=0
    ),
    ])

# Callback to update the tweet count with a counting-up effect
@dash_app.callback(
    Output('tweet-count', 'children'),  # Update the 'children' property of the 'tweet-count' div
    Input('count-interval', 'n_intervals')  # Trigger the callback based on the 'count-interval' component
)
def update_tweet_count(n_intervals):
    num_tweets = 14640  # Replace with the actual number of tweets
    step = 500
    current_value = n_intervals * step
    if current_value <= num_tweets:
        return current_value
    else:
        return num_tweets

# Callback to update the displayed tweet every 3 seconds
@dash_app.callback(
    Output('tweet-container', 'children'),
    Input('slideshow-interval', 'n_intervals')
)
def update_tweet(n_intervals):
    # Calculate the index of the next tweet to display
    index = n_intervals % len(df['text'])
    return df['text'].iloc[index]

@dash_app.callback(
    Output('sentiment-chart', 'figure'),
    Input('option-dropdown', 'value')
)

def update_sentiment_chart(selected_option):
    if selected_option == 'Delta':
        return delta_fig
    elif selected_option == 'United':
        return united_fig
    elif selected_option == 'American':
        return american_fig
    elif selected_option == 'US Airways':
        return us_airways_fig  
    elif selected_option == 'Southwest':
        return southwest_fig
    elif selected_option == 'Virgin America':
        return virgin_america_fig
    
@dash_app.callback(
    Output('graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    if n_intervals % 2 == 0:
        return fig
    else:
        return flight_counts_fig
    


if __name__ == '__main__':
    # Start the Flask server
    app_flask.run(debug=True)