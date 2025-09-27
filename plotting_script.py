import pandas as pd
import plotly.graph_objects as go

#load csv
df_original = pd.read_csv('EEG and ECG data_02_raw.csv', comment='#')

#remove unnecessary columns
df = df_original.drop(['X3:', 'Trigger', 'Time_Offset', 'ADC_Status', 'ADC_Sequence', 'Event', 'Comments'], axis=1)

#defining ecg and eeg data
ecg_df = df[['X1:LEOG', 'X2:REOG', 'CM']]
non_eeg_cols = ['X1:LEOG', 'X2:REOG', 'Time', 'CM']
eeg_df = df[[c for c in df.columns if c not in non_eeg_cols]]

#create figure
fig = go.Figure()

# add ECG traces (start visible)
for col in ecg_df.columns:
    if col != 'CM':
        fig.add_trace(
            go.Scatter(
            x=df['Time'],
            y=ecg_df[col],
            mode='lines',
            name=col,
            yaxis = 'y1',
            visible=True
        )
    )
    #create a separation between CM and other ECG traces
    else:
        fig.add_trace(
            go.Scatter(
                x=df['Time'],
                y=df['CM'],
                mode='lines',
                name='CM',
                visible=True,
                line=dict(
                    color='green',
                    width=2,
                    dash='dot'
                )
            )
        )

# add EEG traces (start hidden)
for col in eeg_df.columns:
    fig.add_trace(
        go.Scatter(
        x=df['Time'],
        y=eeg_df[col],
        mode='lines',
        name=col,
        yaxis = 'y2',
        visible=False
    ))


#set up initial state -- choose ecg to be visible
len_ecg = len(ecg_df.columns)
len_eeg = len(eeg_df.columns)
total_len = len_ecg +len_eeg

vis_ecg = [True]*len_ecg + [False]*len_eeg
vis_eeg = [False]*len_ecg + [True]*len_eeg
vis_both = [True]*total_len

fig.update_layout(
    #creating default look
    title_text = 'ECG/EEG Signals vs Time',
    title_x = 0.5,
    title_xanchor = 'center',
    xaxis_title='Time (s)',
    yaxis = dict(
        title = 'ECG: Amplitude (µV)',
    ),
    yaxis2 = dict(
        title = 'EEG: Amplitude (µV)',
        overlaying = 'y',
        side = 'right'
    ),
    template='plotly_white',

    #moving legend because its default position covers right y-axis
    legend=dict(
        x=0.5,
        y=1.15,
        xanchor='center',
        yanchor='top',
        orientation='h'
    ),


    #creating dropdown menu
    updatemenus=[dict(
        type='dropdown',
        direction='down',
        showactive=True,
        x=0.0, xanchor='left', y=1.25, yanchor='top',
        active=0,
        buttons=[
            dict(label='ECG Channels',
                 method='update',
                 args=[{'visible': vis_ecg}]),
            dict(label='EEG Channels',
                 method='update',
                 args=[{'visible': vis_eeg}]),
            dict(label='ECG + EEG Channels',
                 method='update',
                 args=[{'visible': vis_both}])
        ]
    )]
)

fig.show()


