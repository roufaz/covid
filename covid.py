import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
data=pd.read_csv('Covid_Dashboard1.csv')


st.markdown("<h1 style='text-align: center;'><u>Covid-19 Cases in India</h1></u><br>", unsafe_allow_html=True)



expander=st.expander('See data')
expander.write(data)





value=data['State/UTs'].unique()
select=st.selectbox('Select state',(value))
df=data[data['State/UTs']==select]


col1,col2,col3,col4=st.columns(4)
s1=col1.metric('Total cases',df['Total Cases'].sum())
s2=col2.metric('Total Recoveries',df['Discharged'].sum())

#dd=(df['Discharged'] / s1()) * 100

col3.metric('Deaths',df['Deaths'].sum())

col4.metric('Active',df['Active'].sum())



figs1=px.bar(data,y='Population',x='State/UTs')
st.plotly_chart(figs1)

cc1,cc2=st.columns(2)
if cc1.button('Total Cases'):
  st.write('Total covid cases in India = ',data['Total Cases'].sum())
  



if cc2.button('Click zone'):
   cc2.subheader('Cases by Zone')
   figs = px.pie(data,values='Total Cases', names='Zone')
 
   cc2.plotly_chart(figs)



st.markdown("<br><u><h3 style='text-align: center;'>COVID-19 Statistics Dashboard</h3><br></u>", unsafe_allow_html=True)

colu1,colu2=st.columns(2)

contain=colu1.container(border=True)
contain.markdown("<h2 style='text-align: center;'>Top Covid Cases</h2>", unsafe_allow_html=True)

c1,c2=contain.columns(2)
states = data.nlargest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
states.sort_values(by='Total Cases', ascending=False)
states = states.reset_index(drop=True)
c1.subheader(" Highest Cases")
c1.dataframe(states)

states = data.nsmallest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
states = states.reset_index(drop=True)
c2.subheader("Least Cases")
c2.dataframe(states)


contain=colu2.container(border=True)
contain.markdown("<h2 style='text-align: center;'>Top Death</h2>", unsafe_allow_html=True)


co1,co2=contain.columns(2)
op_states = data.nlargest(5, 'Deaths')[['State/UTs', 'Deaths']]
op_states = op_states.reset_index(drop=True)
co1.subheader("Highest Cases")
co1.dataframe(op_states)

op_states = data.nsmallest(5, 'Deaths')[['State/UTs', 'Deaths']]
op_states = op_states.reset_index(drop=True)
co2.subheader("Least Cases")
co2.dataframe(op_states)




colu3,colu4=st.columns(2)
con=colu3.container(border=True)
con.markdown("<h2 style='text-align: center;'>Recovered</h2>", unsafe_allow_html=True)

c3,c4=con.columns(2)
states1 = data.nlargest(5, 'Discharged')[['State/UTs', 'Discharged']]
states1 = states1.reset_index(drop=True)
c3.subheader(" Highest Cases")
c3.dataframe(states1)

states1 = data.nsmallest(5, 'Discharged')[['State/UTs', 'Discharged']]
states1 = states1.reset_index(drop=True)
c4.subheader("Least Cases")
c4.dataframe(states1)

con=colu4.container(border=True)
con.markdown("<h2 style='text-align: center;'>Active</h2>", unsafe_allow_html=True)


co3,co4=con.columns(2)
op_states1 = data.nlargest(5, 'Active')[['State/UTs', 'Active']]
op_states1 = op_states1.reset_index(drop=True)
co3.subheader("Highest Cases")
co3.dataframe(op_states1)

op_states1 = data.nsmallest(5, 'Active')[['State/UTs', 'Active']]
op_states1 = op_states1.reset_index(drop=True)
co4.subheader("Least Cases")
co4.dataframe(op_states1)





st.markdown("<br><u><h3 style='text-align: center;'>COVID-19 Data Visualization</h2></u><br>", unsafe_allow_html=True)

colum1,colum2=st.columns(2)


colum1.subheader('Death Ratio')
#df_reversed = data.iloc[::-1]
fig=px.line(data,y='Death Ratio',x='State/UTs')
colum1.plotly_chart(fig)

colum2.subheader('Recoverer Rate')
#df_reversed = states1.iloc[::-1]
bar1 = px.bar(data, y='State/UTs', x='Discharged',color='Discharged',color_continuous_scale='Viridis')
colum2.write(bar1)


colum3,colum4=st.columns(2)


colum3.subheader('Active & Death plot')
fig2=px.bar(data,x='State/UTs',y=['Active','Deaths'],barmode='group',
color_discrete_sequence=['#D5D68D', '#3357FF'])
colum3.plotly_chart(fig2) 

colum4.subheader('Cases & Recovery plot')
fig3=px.bar(data,x='State/UTs',y=['Total Cases','Discharged'],barmode='group',
color_discrete_sequence=['#054105', '#D5D68D'])
colum4.plotly_chart(fig3) 



