import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import date, timedelta, datetime



st.set_page_config(layout="centered", page_icon="💬", page_title="Commenting app")

option = st.selectbox(
    'Please Select a County',
    ('Suffolk', 'Middlesex'))
if option == 'Middlesex':
    waste_option = 'Middlesex County, MA'
else:
    waste_option = 'Suffolk County, MA'


# county_url = 'https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/cases_by_county.csv'
# county_case_df = pd.read_csv(county_url, index_col=0)
# middlesex_case = county_case_df.loc[county_case_df['name'] == 'Middlesex']

req_cols = ['county', 'state', 'date', 'cases_avg', 'deaths_avg']
county_url_2022 = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-counties-2022.csv'
county_case_df = pd.read_csv(county_url_2022, index_col=0, skipinitialspace=True, usecols=req_cols)
middlesex_case_2022 = county_case_df.loc[(county_case_df['county'] == option) & (county_case_df['state'] == 'Massachusetts')]
print('yo')

# county_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-counties-2021.csv'
# print('b')
# county_case_df = pd.read_csv(county_url, index_col=0, skipinitialspace=True, usecols= req_cols)
# middlesex_case_2021 = county_case_df.loc[(county_case_df['county'] == option) & (county_case_df['state'] == 'Massachusetts')]
# print('yo')
middle_sex_data =  middlesex_case_2022



waste_url = 'https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/wastewater_by_county.csv'
waste_df = pd.read_csv(waste_url, index_col=0)
middlesex_waste = waste_df.loc[(waste_df['name']== waste_option) & (waste_df['sampling_week'] > '2021-12-31')]
print(middlesex_case_2022.columns)

title = 'Middlesex County MA Covid Cases'
labels = ['Cases', 'Normalized Virus Concentrations', 'Deaths']
colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)']

mode_size = [8, 8, 12, 8]
line_size = [2, 2, 4, 2]

fig = make_subplots(rows=3, cols=1)


config = {'staticPlot': True}

fig.add_trace(go.Scatter(x=middlesex_waste['sampling_week'], y=middlesex_waste['effective_concentration_rolling_average'],
                         mode='lines',
                         name=labels[1],
                         line=dict(color=colors[2], width=line_size[2]),
                         connectgaps=True,
                         ), row =1, col =1)

fig.add_trace(go.Scatter(x=middle_sex_data.index, y=middle_sex_data['cases_avg'], mode='lines',
    name=labels[0],
    line=dict(color=colors[1], width=line_size[2]),
    connectgaps=True,
),row =2, col =1)

fig.add_trace(go.Scatter(x=middle_sex_data.index, y=middle_sex_data['deaths_avg'], mode='lines',
    name=labels[2],
    line=dict(color=colors[0], width=line_size[2]),
    connectgaps=True,
),row =3, col =1)

fig.update_yaxes(title_text="Wastewater", row=1, col=1, title_font_family="Arial")
fig.update_yaxes(title_text="Cases", row=2, col=1, title_font_family="Arial")
fig.update_yaxes(title_text="Deaths", row=3, col=1, title_font_family="Arial")
    # endpoints
    # fig.add_trace(go.Scatter(
    #     x=[x_data[i][0], x_data[i][-1]],
    #     y=[y_data[i][0], y_data[i][-1]],
    #     mode='markers',
    #     marker=dict(color=colors[i], size=mode_size[i])
    # ))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        fixedrange = True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),

    ),
    xaxis2=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        fixedrange = True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),

    ),
    xaxis3=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        fixedrange = True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),

    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        fixedrange = True,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',),

    ),
yaxis2=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        fixedrange = True,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',),

    ),
yaxis3=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        fixedrange = True,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',),

    ),
    autosize=True,
    margin=dict(
        autoexpand=True,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
)

annotations = []
#
# # Adding labels
# for y_trace, label, color in zip(y_data, labels, colors):
#     # labeling the left_side of the plot
#     annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
#                                   xanchor='right', yanchor='middle',
#                                   text=label + ' {}%'.format(y_trace[0]),
#                                   font=dict(family='Arial',
#                                             size=16),
#                                   showarrow=False))
#     # labeling the right_side of the plot
#     annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
#                                   xanchor='left', yanchor='middle',
#                                   text='{}%'.format(y_trace[11]),
#                                   font=dict(family='Arial',
#                                             size=16),
#                                   showarrow=False))
# # Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Greater Boston Covid Cases & Wastewater ',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
# # Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Nationwide Wastewater Monitoring Network & NY Times'
                                   ,
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))

fig.update_layout(annotations=annotations)


#
# fig.update_layout(
#     xaxis=dict(
#         showline=True,
#         showgrid=False,
#         showticklabels=True,
#         linecolor='rgb(204, 204, 204)',
#         linewidth=2,
#         ticks='outside',
#         tickfont=dict(
#             family='Arial',
#             size=12,
#             color='rgb(82, 82, 82)',
#         ),
#     ),
#     yaxis=dict(
#         showgrid=True,
#         zeroline=True,
#         showline=True,
#         showticklabels=True,
#         tickfont=dict(
#             family='Arial',
#             size=12,
#             color='rgb(82, 82, 82)',),
#
#     ),
#     autosize=False,
#     margin=dict(
#         autoexpand=False,
#         l=100,
#         r=20,
#         t=110,
#     ),
#     showlegend=False,
#     plot_bgcolor='white'
# )
#
# annotations = []
# #
# # # Adding labels
# # for y_trace, label, color in zip(y_data, labels, colors):
# #     # labeling the left_side of the plot
# #     annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
# #                                   xanchor='right', yanchor='middle',
# #                                   text=label + ' {}%'.format(y_trace[0]),
# #                                   font=dict(family='Arial',
# #                                             size=16),
# #                                   showarrow=False))
# #     # labeling the right_side of the plot
# #     annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
# #                                   xanchor='left', yanchor='middle',
# #                                   text='{}%'.format(y_trace[11]),
# #                                   font=dict(family='Arial',
# #                                             size=16),
# #                                   showarrow=False))
# # # Title
# annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
#                               xanchor='left', yanchor='bottom',
#                               text='Greater Boston Covid Cases & Wastewater ',
#                               font=dict(family='Arial',
#                                         size=30,
#                                         color='rgb(37,37,37)'),
#                               showarrow=False))
# # # Source
# annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
#                               xanchor='center', yanchor='top',
#                               text='Source: Nationwide Wastewater Monitoring Network'
#                                    ,
#                               font=dict(family='Arial',
#                                         size=12,
#                                         color='rgb(150,150,150)'),
#                               showarrow=False))
#
# fig.update_layout(annotations=annotations)

#fig.show()

#cases.show()

# df_waste = middlesex_waste
# waste_cases = 'https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/cases_by_county.csv'
# waste_cases_df = pd.read_csv(waste_cases, index_col=0, engine="pyarrow")
# middlesex_waste_cases = waste_cases_df.loc[waste_cases_df['name'] == 'Middlesex County, MA']
# #print(middlesex_waste_cases.columns)
# # print(df_waste.shape, df_cases.index)
# df = pd.merge(df_waste, middlesex_waste_cases, left_on = df_waste.sampling_week, right_on=middlesex_waste_cases.date,how= 'inner')
# print(df.columns)

middlesex_waste['percent_change'] = round(middlesex_waste['effective_concentration_rolling_average'].pct_change(),2)*100
#df_calc_1 = middlesex_waste.index.drop_duplicates().nlargest(2).iloc[-1]
# print(middlesex_waste.head())
#
# percent_change = make_subplots(rows=1, cols=1)
#
# percent_change.add_trace(go.Scatter(x=middlesex_waste['sampling_week'], y=middlesex_waste['percent_change'],
#                          mode='markers',
#                          name=labels[1],
#                          line=dict(color=colors[2], width=line_size[2]),
#                          connectgaps=True,
#                          ), row =1, col =1)
#
# percent_change.update_layout(
#     xaxis=dict(
#         showline=True,
#         showgrid=False,
#         showticklabels=True,
#         linecolor='rgb(204, 204, 204)',
#         linewidth=2,
#         ticks='outside',
#         tickfont=dict(
#             family='Arial',
#             size=12,
#             color='rgb(82, 82, 82)',
#         ),
#     ),
#     yaxis=dict(
#         showgrid=True,
#         zeroline=True,
#         showline=True,
#         showticklabels=True,
#         tickfont=dict(
#             family='Arial',
#             size=12,
#             color='rgb(82, 82, 82)',),
#
#     ),
#     autosize=False,
#     margin=dict(
#         autoexpand=False,
#         l=100,
#         r=20,
#         t=110,
#     ),
#     showlegend=False,
#     plot_bgcolor='white'
# )
#st.plotly_chart(percent_change)



dc = middlesex_waste.iloc[middlesex_waste.index == max(middlesex_waste.index)].reset_index()
last_pct_change = round(dc.iloc[0]['percent_change'],2)
last_sample_week = dc.iloc[0]['sampling_week']

last_date = middle_sex_data.loc[middle_sex_data.index == max(middle_sex_data.index)]
current_cases = last_date.iloc[0]['cases_avg']
current_deaths = last_date.iloc[0]['deaths_avg']
nyt_date = last_date.index.values[0]

curr_date = datetime.strptime(nyt_date, '%Y-%m-%d').date()

seven_days_ago = curr_date - timedelta(days=7)
nearest = middle_sex_data.truncate(before=str(seven_days_ago))
nearest_df = nearest.head(1)
seven_date = nearest_df.index.values[0]
seven_cases = nearest_df.iloc[0]['cases_avg']
seven_deaths = nearest_df.iloc[0]['deaths_avg']
week_o_week_cases = round(((current_cases - seven_cases)/seven_cases),2) * 100
week_o_week_deaths = round(((current_deaths - seven_deaths)/seven_deaths),2) * 100
#nearest_tail = nearest.tail(1)
#days_for_diff = nearest_tail.index.values[0]
#st.write(nearest)

# print(middlesex_waste_cases.head())

# middlesex_waste_cases['percent_change'] = round(middlesex_waste_cases['rolling_average_cases_per_100k_centered'].pct_change(),2)*100
# dt = middlesex_waste_cases.iloc[middlesex_waste_cases.index == max(middlesex_waste_cases.index)]
# last_pct_change_ = round(dt.iloc[0]['percent_change'],2)
# last_sample_week_ = dt.iloc[0]['date']

st.title("{} County, MA Covid-19 Dashboard".format(option))



st.write('Week over Week **{}** Wastewater Percent Change since {}: **{}**%'.format(option, last_sample_week, last_pct_change))
st.write('**{}** Current Cases (Rolling 7 Day Average) as of {}: **{}** **cases**; **{}**% since {}'.format(option, nyt_date, current_cases, week_o_week_cases,seven_date))
st.write('**{}** Current Deaths (Rolling 7 Day Average) as of {}: **{}** **deaths**; **{}**% since {}'.format(option, nyt_date, current_deaths, week_o_week_deaths, seven_date))
# st.write('Week over Week **{}** Cases Percent Change since {}: **{}**%'.format(option,last_sample_week_, last_pct_change_))

st.plotly_chart(fig)#, config = {'staticPlot': True})


