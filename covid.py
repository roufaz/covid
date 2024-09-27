import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
data=pd.read_csv('/workspaces/covid/Covid_Dashboard1.csv')


expander=st.expander('See data')
expander.write(data)

st.metric('Total covid cases',data['Total Cases'].sum())

value=data['State/UTs'].unique()
select=st.selectbox('Select state',(value))
df=data[data['State/UTs']==select]

col1,col2,col3,col4=st.columns(4)
s1=col1.metric('Total cases',df['Total Cases'].sum())
s2=col2.metric('Total Recoveries',df['Discharged'].sum())

#dd=(df['Discharged'] / s1()) * 100

col3.metric('Deaths',df['Deaths'].sum())

col4.metric('Active',df['Active'].sum())




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






colum1,colum2=st.columns(2)

colum1.subheader('Death Ratio')
#df_reversed = data.iloc[::-1]
fig=px.bar(data,x='Death Ratio',y='State/UTs',color='Death Ratio',color_continuous_scale='Viridis')
colum1.plotly_chart(fig)

colum2.subheader('Recoverer Rate')
#df_reversed = states1.iloc[::-1]
bar1 = px.bar(data, y='State/UTs', x='Discharged', title='Recovery Ratio by State (%)',
color='Death Ratio',color_continuous_scale='Plasma')
colum2.write(bar1)


colum3,colum4=st.columns(2)
#fig1 = px.pie(data,values='Death Ratio', names='Zone', title='Pie Chart Example')
#colum3.plotly_chart(fig1)

colum3.subheader('Active & Death plot')
fig2=px.bar(data,x='State/UTs',y=['Active','Deaths'],barmode='group',
color_discrete_sequence=['#1f77b4', '#ff7f0e'])
colum3.plotly_chart(fig2) 

colum4.subheader('Cases & Recovery plot')
fig3=px.bar(data,x='State/UTs',y=['Total Cases','Discharged'],barmode='group',
color_discrete_sequence=['#28a745', '#dc3545'])
colum4.plotly_chart(fig3) 