import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
data=pd.read_csv('/workspaces/Covid_case/Covid_Dashboard1.csv')


expander=st.expander('See data')
expander.write(data)

st.metric('Total covid cases',data['Total Cases'].sum())

value=data['State/UTs'].unique()
select=st.selectbox('Select state',(value))
df=data[data['State/UTs']==select]

col1,col2,col3,col4=st.columns(4)
s1=col1.metric('Total cases',df['Total Cases'].sum())
col2.metric('Total Recoveries',df['Discharged'].sum())

#dd=(df['Discharged'] / s1()) * 100

col3.metric('Deaths',df['Deaths'].sum())
col4.metric('Active',df['Active'].sum())

#df1 = pd.DataFrame(columns=['State', 'Case' ])
#df1['State'] = [value],['Case']=[s1]
#st.write(df1)


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
con.markdown("<h2 style='text-align: center;'>Active</h2>", unsafe_allow_html=True)

