import streamlit as st
import datetime
import yfinance as yf
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(page_title='My Finance App', layout='wide')

st.write('# Precio Stock Online')

st.sidebar.image('img/thebridge.png')
st.sidebar.image('img/yahoo.png')

productos = {'TESLA':'tsla',
             'GOOGLE':'goog',
             'NETFLIX':'nflx',
             'META':'meta',
             'APPLE':'aapl',
             'AMAZON':'amzn',
             'IBEX 35':'^ibex',
             'PETROLEO':'bz=f',
             'ORO':'gc=f',
             'PLATA':'si=f',
             'EURO/USD':'eurusd=x',
             'REPSOL':'rep.mc',
             'IBERDROLA':'ibe.mc',
             'ETHEREUM':'eth-usd'}
desc = {'TESLA':'USD',
        'GOOGLE':'USD',
        'NETFLIX':'USD',
        'META':'USD',
        'APPLE':'USD',
        'AMAZON':'USD',
        'IBEX 35':'EUR',
        'PETROLEO':'USD',
        'ORO':'USD',
        'PLATA':'USD',
        'EURO/USD':'USD',
        'REPSOL':'EUR',
        'IBERDROLA':'EUR',
        'ETHEREUM':'USD'}
producto = st.sidebar.selectbox(
    'Selecciona el producto',
    ('TESLA', 'GOOGLE', 'NETFLIX', 'IBERDROLA', 'META', 'APPLE',
     'AMAZON', 'IBEX 35', 'PETROLEO', 'ORO', 'PLATA',
     'EURO/USD', 'REPSOL', 'ETHEREUM')
    )

inicio = st.sidebar.date_input('Seleccione la fecha de inicio',
					  datetime.date(2022,1,5))

fin = st.sidebar.date_input('Seleccione la fecha final',
					  datetime.date(2024,1,5))

intervalo = st.sidebar.selectbox('Selecciona el intervalo',
								 ('1d','5d','1mo','3mo'))

productoData = yf.Ticker(productos[producto])
productoDf = productoData.history(interval=intervalo,
					 start=str(inicio),
					 end=str(fin))

c1, c2, c3, c4 = st.columns((1,1,1,1))
c1.write('#### ' + producto + ' (' + productos[producto].upper() + ')\n Divisa en ' + desc[producto])

dif_close = productoDf.Close[-1] - productoDf.Close[-2]
c2.metric(label='Ultimo valor de cierre',
          value=round(productoDf.Close[-1], 4),
          delta= str(round(dif_close,4)) +' MA (' + str(round(dif_close/productoDf.Close[-2]*100, 4)) + '%)')

dif_open = productoDf.Open[-1] - productoDf.Open[-2]
c3.metric(label='Ultimo valor de apertura',
          value=round(productoDf.Open[-1], 4),
          delta= str(round(dif_open,4)) +' MA (' + str(round(dif_open/productoDf.Open[-2]*100, 4)) + '%)')

dif_volume = productoDf.Volume[-1] - productoDf.Volume[-2]
c4.metric(label='Volumen actual',
          value=round(productoDf.Volume[-1], 4),
          delta= str(round(dif_volume,4)) +' MA (' + str(round(dif_volume/productoDf.Volume[-2]*100, 4)) + '%)')

fig_row1 = make_subplots(rows=1, cols=2,
			  subplot_titles=('Valor de apertura','Valor de cierre'))
fig_row1.add_trace(go.Scatter(x=productoDf.index, y=productoDf.Open),
							  row=1, col=1)
fig_row1.add_trace(go.Scatter(x=productoDf.index, y=productoDf.Close),
							  row=1, col=2)
fig_row1.update_layout(height=400, width=800,
					   showlegend=False)
st.plotly_chart(fig_row1)

fig_volume = px.line(productoDf, x=productoDf.index, y=productoDf.Volume)
fig_volume.update_layout(height=400, width=800,
						 title = {'text':'Volume',
				'y':0.9,
				'x':0.5,
				'xanchor':'center',
				'yanchor':'top',
				'font':{'size':15}
				})
st.plotly_chart(fig_volume)

fig_row2 = make_subplots(rows=1, cols=2,
			  subplot_titles=('Valor maximo','Valor minimo'))
fig_row2.add_trace(go.Scatter(x=productoDf.index, y=productoDf.High),
							  row=1, col=1)
fig_row2.add_trace(go.Scatter(x=productoDf.index, y=productoDf.Low),
							  row=1, col=2)
fig_row2.update_layout(height=400, width=800,
					   showlegend=False)
st.plotly_chart(fig_row2)
