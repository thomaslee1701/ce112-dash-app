from dash import callback
from dash_extensions import EventListener
from dash_extensions.enrich import DashProxy, html, Input, Output, State, dcc
from dash.exceptions import PreventUpdate
import constants
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

#####################################
### SLIDERS AND INPUTS FOR PARAMS ###
#####################################

residential_service_charge_elem = html.Div(
    ["Residential Service Charge ($/month/customer): ",
    EventListener(dcc.Input(id='residential_service_charge', value=30, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='residential_service_charge_input'),
    dcc.Slider(id='residential_service_charge_slider', value=30, min=0, max=100, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 101, 10)}),
    ], style={'width':'500px'}
)
@callback(Output('residential_service_charge_slider', 'value'), Input("residential_service_charge_input", "n_events"), State('residential_service_charge_input', 'event'))
def residential_service_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('residential_service_charge', 'value'), Input('residential_service_charge_slider', 'drag_value'))
def residential_service_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

tier_1_flow_charge_elem = html.Div(
    ["Tier 1 Residential Flow Charge ($/month/customer): ",
    EventListener(dcc.Input(id='tier_1_flow_charge', value=3.25, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='tier_1_flow_charge_input'),
    dcc.Slider(id='tier_1_flow_charge_slider', value=3.25, min=0, max=20, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 21, 2)}),
    ], style={'width':'500px'}
)
@callback(Output('tier_1_flow_charge_slider', 'value'), Input("tier_1_flow_charge_input", "n_events"), State('tier_1_flow_charge_input', 'event'))
def tier_1_flow_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('tier_1_flow_charge', 'value'), Input('tier_1_flow_charge_slider', 'drag_value'))
def tier_1_flow_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

tier_2_flow_charge_elem = html.Div(
    ["Tier 2 Residential Flow Charge ($/month/customer): ",
    EventListener(dcc.Input(id='tier_2_flow_charge', value=7, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='tier_2_flow_charge_input'),
    dcc.Slider(id='tier_2_flow_charge_slider', value=7, min=0, max=20, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 21, 2)}),
    ], style={'width':'500px'}
)
@callback(Output('tier_2_flow_charge_slider', 'value'), Input("tier_2_flow_charge_input", "n_events"), State('tier_2_flow_charge_input', 'event'))
def tier_2_flow_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('tier_2_flow_charge', 'value'), Input('tier_2_flow_charge_slider', 'drag_value'))
def tier_2_flow_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

commercial_service_charge_elem = html.Div(
    ["Commercial Service Charge ($/month/customer): ",
    EventListener(dcc.Input(id='commercial_service_charge', value=120, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='commercial_service_charge_input'),
    dcc.Slider(id='commercial_service_charge_slider', value=120, min=0, max=500, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 501, 50)}),
    ], style={'width':'500px'}
)
@callback(Output('commercial_service_charge_slider', 'value'), Input("commercial_service_charge_input", "n_events"), State('commercial_service_charge_input', 'event'))
def commercial_service_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('commercial_service_charge', 'value'), Input('commercial_service_charge_slider', 'drag_value'))
def commercial_service_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

commercial_flow_charge_elem = html.Div(
    ["Commercial Flow Charge ($/month/customer): ",
    EventListener(dcc.Input(id='commercial_flow_charge', value=7, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='commercial_flow_charge_input'),
    dcc.Slider(id='commercial_flow_charge_slider', value=7, min=0, max=30, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 31, 2)}),
    ], style={'width':'500px'}
)
@callback(Output('commercial_flow_charge_slider', 'value'), Input("commercial_flow_charge_input", "n_events"), State('commercial_flow_charge_input', 'event'))
def commercial_flow_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('commercial_flow_charge', 'value'), Input('commercial_flow_charge_slider', 'drag_value'))
def commercial_flow_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

industrial_service_charge_elem = html.Div(
    ["Industrial Service Charge ($/month/customer): ",
    EventListener(dcc.Input(id='industrial_service_charge', value=1200, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='industrial_service_charge_input'),
    dcc.Slider(id='industrial_service_charge_slider', value=1200, min=0, max=2500, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 2501, 250)}),
    ], style={'width':'500px'}
)
@callback(Output('industrial_service_charge_slider', 'value'), Input("industrial_service_charge_input", "n_events"), State('industrial_service_charge_input', 'event'))
def industrial_service_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('industrial_service_charge', 'value'), Input('industrial_service_charge_slider', 'drag_value'))
def industrial_service_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

industrial_flow_charge_elem = html.Div(
    ["Industrial Flow Charge ($/month/customer): ",
    EventListener(dcc.Input(id='industrial_flow_charge', value=7, type='number'), events=[{'event':'change', 'props':['srcElement.value']}], logging=True, id='industrial_flow_charge_input'),
    dcc.Slider(id='industrial_flow_charge_slider', value=7, min=0, max=30, updatemode='drag', step=0.01, marks={i:str(i) for i in range(0, 31, 2)}),
    ], style={'width':'500px'}
)
@callback(Output('industrial_flow_charge_slider', 'value'), Input("industrial_flow_charge_input", "n_events"), State('industrial_flow_charge_input', 'event'))
def industrial_flow_charge_input(_, e):
    if e is None:
        raise PreventUpdate()
    return float(e['srcElement.value'])
@callback(Output('industrial_flow_charge', 'value'), Input('industrial_flow_charge_slider', 'drag_value'))
def industrial_flow_charge_slider(drag_value):
    if drag_value is None:
        return
    return drag_value

###################
### CHOOSE PLOT ###
###################
plot_dropdown = dcc.Dropdown(
    options=['Monthly Bill by Customer', 'Agency Annual Revenue by Customer', '% Annual Revenue Chart by Customer'],
    value='Monthly Bill by Customer',
    id='plot_dropdown'
)

###########################
### DROPDOWN PLOT LOGIC ###
###########################
@callback(
    Output(
        component_id="dropdown_fig", component_property="figure"
    ),
    Input(component_id='plot_dropdown', component_property='value'),
    Input(component_id="residential_service_charge", component_property="value"),
    Input(component_id="tier_1_flow_charge", component_property="value"),
    Input(component_id="tier_2_flow_charge", component_property="value"),
    Input(component_id="commercial_service_charge", component_property="value"),
    Input(component_id="commercial_flow_charge", component_property="value"),
    Input(component_id="industrial_service_charge", component_property="value"),
    Input(component_id="industrial_flow_charge", component_property="value"),
    Input(component_id="customer_monthly_bill_checklist", component_property="value"),   
)
def dropdown_fig(
    dropdown_selection,
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
    commercial_service_charge,
    commercial_flow_charge,
    industrial_service_charge,
    industrial_flow_charge,
    include_elems,
):
    if dropdown_selection == 'Monthly Bill by Customer':
        return customer_monthly_bill_fig(
            residential_service_charge,
            tier_1_residential_flow_charge,
            tier_2_residential_flow_charge,
            commercial_service_charge,
            commercial_flow_charge,
            industrial_service_charge,
            industrial_flow_charge,
            include_elems,
        )
    elif dropdown_selection == 'Agency Annual Revenue by Customer':
        return customer_annual_revenue_fig(
            residential_service_charge,
            tier_1_residential_flow_charge,
            tier_2_residential_flow_charge,
            commercial_service_charge,
            commercial_flow_charge,
            industrial_service_charge,
            industrial_flow_charge,
            include_elems,
        )
    elif dropdown_selection == '% Annual Revenue Chart by Customer':
        return percent_annual_revenue_fig(
            residential_service_charge,
            tier_1_residential_flow_charge,
            tier_2_residential_flow_charge,
            commercial_service_charge,
            commercial_flow_charge,
            industrial_service_charge,
            industrial_flow_charge,
            include_elems,
        )

#########################
### PLOT MONTHLY BILL ###
#########################
@callback(
    Output(component_id='customer_checkbox', component_property='style'),
    Input(
        component_id="plot_dropdown", component_property="value"
    ),
)
def checklist_visibility(
    dropdown_selection
):
    if dropdown_selection == 'Monthly Bill by Customer':
        return {'visibility':'visible'}
    else:
        return {'visibility':'hidden'}

def customer_monthly_bill_fig(
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
    commercial_service_charge,
    commercial_flow_charge,
    industrial_service_charge,
    industrial_flow_charge,
    include_elems,
):
    low_monthly_service_charge = residential_service_charge
    low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['ccf_per_month']
    low_monthly_total_charge = low_monthly_service_charge + low_monthly_flow_charge
    
    high_monthly_service_charge = residential_service_charge
    high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    high_monthly_total_charge = high_monthly_service_charge + high_monthly_flow_charge
    
    commercial_monthly_service_charge = commercial_service_charge
    commercial_monthly_flow_charge = commercial_flow_charge * constants.commercial_use_params['ccf_per_month']
    commercial_monthly_total_charge = commercial_monthly_service_charge + commercial_monthly_flow_charge
    
    industrial_monthly_service_charge = industrial_service_charge
    industrial_monthly_flow_charge = industrial_flow_charge * constants.industrial_use_params['ccf_per_month']
    industrial_monthly_total_charge = industrial_monthly_service_charge + industrial_monthly_flow_charge

    df = pd.DataFrame(
        {
            "x": ["Low Use"]*3 + ["High Use"]*3 + ["Commercial"]*3 + ["Industrial"]*3,
            "y": [
                low_monthly_total_charge, low_monthly_flow_charge, low_monthly_service_charge,
                high_monthly_total_charge, high_monthly_flow_charge, high_monthly_service_charge,
                commercial_monthly_total_charge, commercial_monthly_flow_charge, commercial_monthly_service_charge,
                industrial_monthly_total_charge, industrial_monthly_flow_charge, industrial_monthly_service_charge,
            ],
            "Expense Type": ['Monthly Total Charge', 'Monthly Flow Charge', 'Monthly Service Charge'] * 4,
        }
    ) # In long format
    df[f'% of Monthly Bill'] = np.round(df["y"] / np.repeat([low_monthly_total_charge, high_monthly_total_charge, commercial_monthly_total_charge, industrial_monthly_total_charge], 3), 2) * 100
    df = df[df['x'].isin(include_elems)]
        
    fig = px.bar(df, x="x", y="y", color='Expense Type', barmode="group", hover_name='Expense Type', hover_data={'x': False, 'y': False, 'Expense Type': False, f'% of Monthly Bill': True}, width=1300, height=600)
    fig.update_layout(
        title="Monthly Bill for Customer Types",
        xaxis_title="Customer Type",
        yaxis_title="Montly Bill (Dollars)",
    )
    texts = [df['y'][::3], df['y'][1::3], df['y'][2::3]]
    for i, t in enumerate(texts):
        fig.data[i].text = ['${:,.2f}'.format(text) for text in t]
        fig.data[i].textposition = 'outside'
    return fig

##################################
### PLOT AGENCY ANNUAL REVENUE ###
##################################
    
def customer_annual_revenue_fig(
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
    commercial_service_charge,
    commercial_flow_charge,
    industrial_service_charge,
    industrial_flow_charge,
    include_elems,
):
    low_monthly_service_charge = residential_service_charge
    low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['ccf_per_month']
    low_monthly_total_charge = low_monthly_service_charge + low_monthly_flow_charge
    
    high_monthly_service_charge = residential_service_charge
    high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    high_monthly_total_charge = high_monthly_service_charge + high_monthly_flow_charge
    
    commercial_monthly_service_charge = commercial_service_charge
    commercial_monthly_flow_charge = commercial_flow_charge * constants.commercial_use_params['ccf_per_month']
    commercial_monthly_total_charge = commercial_monthly_service_charge + commercial_monthly_flow_charge
    
    industrial_monthly_service_charge = industrial_service_charge
    industrial_monthly_flow_charge = industrial_flow_charge * constants.industrial_use_params['ccf_per_month']
    industrial_monthly_total_charge = industrial_monthly_service_charge + industrial_monthly_flow_charge
    
    
    low_annual_revenue = 12 * constants.low_use_params ['n_customers'] * low_monthly_total_charge
    high_annual_revenue = 12 * constants.high_use_params ['n_customers'] * high_monthly_total_charge
    commercial_annual_revenue = 12 * constants.commercial_use_params ['n_customers'] * commercial_monthly_total_charge
    industrial_annual_revenue = 12 * constants.industrial_use_params ['n_customers'] * industrial_monthly_total_charge
    
    annual_revenue = low_annual_revenue + high_annual_revenue + commercial_annual_revenue + industrial_annual_revenue
    
    df = pd.DataFrame(
            {
                "Customer": ["Low Use"] + ["High Use"] + ["Commercial"] + ["Industrial"],
                "Annual Revenue": np.array([low_annual_revenue, high_annual_revenue, commercial_annual_revenue, industrial_annual_revenue])/1000000,
            }
        ) # In long format

    fig = px.bar(df, x='Annual Revenue', y='Customer', title='Agency Annual Revenue by Customer', orientation='h', color='Customer', width=1300, height=600)
    fig.update_layout(
        title="Agency Annual Revenue by Customer",
        xaxis_title="Annual Revenue (Millions)",
        yaxis_title="Customer Type",
        hovermode=False
    )
    
    texts = df['Annual Revenue']
    for i, t in enumerate(texts):
        fig.data[i].text = '${:,.2f}'.format(round(t, 2))
        fig.data[i].textposition = 'outside'
        
    fig.add_annotation(x=4, y=4,
            text=f"Annual Change (+/-) to Reserve Fund: {'${:,.2f}'.format(annual_revenue - constants.revenue_requirement)}",
            showarrow=False,
            font_size=20,
            xshift=300
    )
    
    return fig
    
###################################
### PLOT % ANNUAL REVENUE CHART ###
###################################

def percent_annual_revenue_fig(
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
    commercial_service_charge,
    commercial_flow_charge,
    industrial_service_charge,
    industrial_flow_charge,
    include_elems,
):
    low_monthly_service_charge = residential_service_charge
    low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['ccf_per_month']
    low_monthly_total_charge = low_monthly_service_charge + low_monthly_flow_charge
    
    high_monthly_service_charge = residential_service_charge
    high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    high_monthly_total_charge = high_monthly_service_charge + high_monthly_flow_charge
    
    commercial_monthly_service_charge = commercial_service_charge
    commercial_monthly_flow_charge = commercial_flow_charge * constants.commercial_use_params['ccf_per_month']
    commercial_monthly_total_charge = commercial_monthly_service_charge + commercial_monthly_flow_charge
    
    industrial_monthly_service_charge = industrial_service_charge
    industrial_monthly_flow_charge = industrial_flow_charge * constants.industrial_use_params['ccf_per_month']
    industrial_monthly_total_charge = industrial_monthly_service_charge + industrial_monthly_flow_charge
    
    
    low_annual_revenue = 12 * constants.low_use_params ['n_customers'] * low_monthly_total_charge
    high_annual_revenue = 12 * constants.high_use_params ['n_customers'] * high_monthly_total_charge
    commercial_annual_revenue = 12 * constants.commercial_use_params ['n_customers'] * commercial_monthly_total_charge
    industrial_annual_revenue = 12 * constants.industrial_use_params ['n_customers'] * industrial_monthly_total_charge
        
    df = pd.DataFrame(
            {
                "Customer": ["Low Use"] + ["High Use"] + ["Commercial"] + ["Industrial"],
                "Annual Revenue": np.array([low_annual_revenue, high_annual_revenue, commercial_annual_revenue, industrial_annual_revenue]),
            }
        ) # In long format

    fig = px.pie(df, values='Annual Revenue', names='Customer', title=f'% of Annual Revenue Contribution by Customer', labels={'Customer':'Customer Type'}, hover_data={'Annual Revenue':True})
    fig.update_traces(textposition='inside', textinfo='percent+label')

    return fig

##################################
### Impact of Increasing Rates ###
##################################
residential_service_charge_fn = lambda rate: rate * (constants.low_use_params['n_customers'] + constants.high_use_params['n_customers'])/1000000
tier_1_flow_charge_fn = lambda rate: rate * constants.low_use_params['n_customers'] * constants.low_use_params['ccf_per_month']/1000000
tier_2_flow_charge_fn = lambda rate: rate * constants.high_use_params['n_customers'] * constants.high_use_params['ccf_per_month']/1000000
commercial_service_charge_fn = lambda rate: rate * constants.commercial_use_params['n_customers']/1000000
commercial_flow_charge_fn = lambda rate: rate * constants.commercial_use_params['n_customers'] * constants.commercial_use_params['ccf_per_month']/1000000
industrial_service_charge_fn = lambda rate: rate * constants.industrial_use_params['n_customers']/1000000
industrial_flow_charge_fn = lambda rate: rate * constants.industrial_use_params['n_customers'] * constants.industrial_use_params['ccf_per_month']/1000000

def increasing_rates_fig():
    rates = np.arange(0, 101)
    long_charges = np.hstack([
        np.vectorize(residential_service_charge_fn)(rates),
        np.vectorize(tier_1_flow_charge_fn)(rates),
        np.vectorize(tier_2_flow_charge_fn)(rates),
        np.vectorize(commercial_service_charge_fn)(rates),
        np.vectorize(commercial_flow_charge_fn)(rates),
        np.vectorize(industrial_service_charge_fn)(rates),
        np.vectorize(industrial_flow_charge_fn)(rates),
    ])
    long_rates = list(rates) * 7
    charge_type = np.repeat(['Residential Service Charge', 'Low Use Flow Charge', 'High Use Flow Charge', 'Commercial Service Charge', 'Commercial Flow Charge', 'Industrial Service Charge', 'Industrial Flow Charge'], len(rates))
    df = pd.DataFrame({
        'Monthly Revenue': long_charges,
        'Rate': long_rates,
        'Charge Type': charge_type,
    })
    fig = px.line(df, x='Rate', y='Monthly Revenue', color='Charge Type', width=1300, height=600, hover_name='Charge Type', hover_data={'Charge Type':False, 'Rate':True})
    fig.update_layout(
        title='Visualizing Effect of Increasing Rates',
        yaxis_title='Monthly Revenue (MM)',
        xaxis_title='Rate (Dollars)',
    )
    return fig

###############
### DROUGHT ###
###############

@callback(
    Output(
        component_id="drought_comparison_fig", component_property="figure"
    ),
    Input(component_id="residential_service_charge", component_property="value"),
    Input(component_id="tier_1_flow_charge", component_property="value"),
    Input(component_id="tier_2_flow_charge", component_property="value"),  
)
def drought_comparison_residential_monthly_bill_fig(
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
):
    low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['ccf_per_month']
    low_monthly_total_charge = residential_service_charge + low_monthly_flow_charge 
    drought_low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['drought_ccf_per_month']
    drought_low_monthly_total_charge = residential_service_charge + drought_low_monthly_flow_charge
    
    high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    high_monthly_total_charge = residential_service_charge + high_monthly_flow_charge
    drought_high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['drought_ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    drought_high_monthly_total_charge = residential_service_charge + drought_high_monthly_flow_charge

    df = pd.DataFrame(
        {
            "Customer Type": ["Low Use"]*6 + ["High Use"]*6,
            "Monthly Bill": [
                low_monthly_total_charge, low_monthly_flow_charge, residential_service_charge, drought_low_monthly_total_charge, drought_low_monthly_flow_charge, residential_service_charge,
                high_monthly_total_charge, high_monthly_flow_charge, residential_service_charge, drought_high_monthly_total_charge, drought_high_monthly_flow_charge, residential_service_charge, 
            ],
            "Expense Type": ['Monthly Total Charge', 'Monthly Flow Charge', 'Monthly Service Charge','(Drought) Monthly Total Charge', '(Drought) Monthly Flow Charge', '(Drought) Monthly Service Charge'] * 2,
        }
    )
    df[f'% of Monthly Bill'] = np.round(df["Monthly Bill"] / np.repeat([low_monthly_total_charge, drought_low_monthly_total_charge, high_monthly_total_charge, drought_high_monthly_total_charge], 3), 2) * 100
        
    fig = px.bar(df, x="Customer Type", y="Monthly Bill", color='Expense Type', barmode="group", hover_name='Expense Type', hover_data={'Customer Type': False, 'Monthly Bill': False, 'Expense Type': False, f'% of Monthly Bill': True},
            color_discrete_map={
            'Monthly Total Charge': 'rgba(99,110,250,0.5)',
            'Monthly Flow Charge': 'rgba(239,85,59,0.5)',
            'Monthly Service Charge': 'rgba(0,204,150,0.5)',
            '(Drought) Monthly Total Charge': 'rgba(99,110,250,1)',
            '(Drought) Monthly Flow Charge': 'rgba(239,85,59,1)',
            '(Drought) Monthly Service Charge': 'rgba(0,204,150,1)',
            },
            width=1300, height=600)
    fig.update_layout(
        title="Monthly Bill for Customer Types",
        xaxis_title="Customer Type",
        yaxis_title="Montly Bill (Dollars)",

    )
    
    texts = [
        [low_monthly_total_charge, high_monthly_total_charge],
        [low_monthly_flow_charge, high_monthly_flow_charge],
        [residential_service_charge, residential_service_charge],
    ]
    differences = [
        [round(drought_low_monthly_total_charge - low_monthly_total_charge, 2), round(drought_high_monthly_total_charge - high_monthly_total_charge, 2)],
        [round(drought_low_monthly_flow_charge - low_monthly_flow_charge, 2), round(drought_high_monthly_flow_charge - high_monthly_flow_charge, 2)],
        [0, 0]
    ]
    for i, t in enumerate(texts):
        fig.data[i].text = ['${:,.2f}'.format(text) for text in t]
        fig.data[i].textposition = 'outside'
    for i, t in enumerate(differences):
        sign = ['+' if elem >= 0 else '-' for elem in t]
        fig.data[i+3].text = [sign[i] + '${:,.2f}'.format(abs(text)) for i, text in enumerate(t)]
        fig.data[i+3].textposition = 'inside'
    
    return fig

@callback(
    Output(
        component_id="drought_annual_revenue_fig", component_property="figure"
    ),
    Input(component_id="residential_service_charge", component_property="value"),
    Input(component_id="tier_1_flow_charge", component_property="value"),
    Input(component_id="tier_2_flow_charge", component_property="value"),
    Input(component_id="commercial_service_charge", component_property="value"),
    Input(component_id="commercial_flow_charge", component_property="value"),
    Input(component_id="industrial_service_charge", component_property="value"),
    Input(component_id="industrial_flow_charge", component_property="value"),
)
def drought_customer_annual_revenue_fig(
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
    commercial_service_charge,
    commercial_flow_charge,
    industrial_service_charge,
    industrial_flow_charge,
):
    low_monthly_service_charge = residential_service_charge
    low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['ccf_per_month']
    low_monthly_total_charge = low_monthly_service_charge + low_monthly_flow_charge
    
    high_monthly_service_charge = residential_service_charge
    high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    high_monthly_total_charge = high_monthly_service_charge + high_monthly_flow_charge
    
    commercial_monthly_service_charge = commercial_service_charge
    commercial_monthly_flow_charge = commercial_flow_charge * constants.commercial_use_params['ccf_per_month']
    commercial_monthly_total_charge = commercial_monthly_service_charge + commercial_monthly_flow_charge
    
    industrial_monthly_service_charge = industrial_service_charge
    industrial_monthly_flow_charge = industrial_flow_charge * constants.industrial_use_params['ccf_per_month']
    industrial_monthly_total_charge = industrial_monthly_service_charge + industrial_monthly_flow_charge
    
    low_annual_revenue = 12 * constants.low_use_params ['n_customers'] * low_monthly_total_charge
    high_annual_revenue = 12 * constants.high_use_params ['n_customers'] * high_monthly_total_charge
    commercial_annual_revenue = 12 * constants.commercial_use_params ['n_customers'] * commercial_monthly_total_charge
    industrial_annual_revenue = 12 * constants.industrial_use_params ['n_customers'] * industrial_monthly_total_charge
    
    drought_low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['drought_ccf_per_month']
    drought_low_monthly_total_charge = residential_service_charge + drought_low_monthly_flow_charge
    drought_low_annual_revenue = 12 * constants.low_use_params ['n_customers'] * drought_low_monthly_total_charge
    
    drought_high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['drought_ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    drought_high_monthly_total_charge = residential_service_charge + drought_high_monthly_flow_charge    
    drought_high_annual_revenue = 12 * constants.high_use_params ['n_customers'] * drought_high_monthly_total_charge

    annual_revenue = low_annual_revenue + high_annual_revenue + commercial_annual_revenue + industrial_annual_revenue
    drought_annual_revenue = drought_low_annual_revenue + drought_high_annual_revenue + commercial_annual_revenue + industrial_annual_revenue
    df = pd.DataFrame(
            {
                "Customer": ["Low Use", "High Use", "Commercial", "Industrial", "(Drought) Low Use", "(Drought) High Use", "(Drought) Commercial", "(Drought) Industrial", ],
                "Annual Revenue": np.array([low_annual_revenue, high_annual_revenue, commercial_annual_revenue, industrial_annual_revenue, drought_low_annual_revenue, drought_high_annual_revenue, commercial_annual_revenue, industrial_annual_revenue])/1000000,
            }
        ) # In long format

    fig = px.bar(df, x='Annual Revenue', y='Customer', title='Agency Annual Revenue by Customer', orientation='h', color='Customer', width=1600, height=800,
                 color_discrete_map={
                'Low Use': 'rgba(99,110,250,0.5)',
                'High Use': 'rgba(239,85,59,0.5)',
                'Commercial': 'rgba(0,204,150,0.5)',
                'Industrial': 'rgba(171,99,250, 0.5)',
                '(Drought) Low Use': 'rgba(99,110,250,1)',
                '(Drought) High Use': 'rgba(239,85,59,1)',
                '(Drought) Commercial': 'rgba(0,204,150,1)',
                '(Drought) Industrial': 'rgba(171,99,250,1)',
            })
    fig.update_layout(
        title="Agency Annual Revenue by Customer",
        xaxis_title="Annual Revenue (Millions)",
        yaxis_title="Customer Type",
        hovermode=False
    )
    
    
    texts = df['Annual Revenue']
    for i, t in enumerate(texts[:4]):
        fig.data[i].text = '${:,.2f}'.format(round(t, 2))
        fig.data[i].textposition = 'outside'
        
    differences = np.array(df['Annual Revenue'][4:]) - np.array(df['Annual Revenue'][:4])
    for i, t in enumerate(differences):
        sign = '+' if t >= 0 else '-'
        fig.data[i+4].text = sign + '${:,.2f}'.format(abs(round(t, 2)))
        fig.data[i+4].textposition = 'inside'

    fig.add_annotation(x=10, y=8,
            text=f"(Drought) Annual Change (+/-) to Reserve Fund: {'${:,.2f}'.format(drought_annual_revenue - constants.revenue_requirement)}",
            showarrow=False,
            font_size=20,
            xshift=300
    )
    return fig

def drought_increasing_rates_fig():
    rates = np.arange(0, 101)
    residential_service_charge_fn = lambda rate: rate * (constants.low_use_params['n_customers'] + constants.high_use_params['n_customers'])/1000000
    tier_1_flow_charge_fn = lambda rate: rate * constants.low_use_params['n_customers'] * constants.low_use_params['drought_ccf_per_month']/1000000
    tier_2_flow_charge_fn = lambda rate: rate * constants.high_use_params['n_customers'] * constants.high_use_params['drought_ccf_per_month']/1000000
    commercial_service_charge_fn = lambda rate: rate * constants.commercial_use_params['n_customers']/1000000
    commercial_flow_charge_fn = lambda rate: rate * constants.commercial_use_params['n_customers'] * constants.commercial_use_params['drought_ccf_per_month']/1000000
    industrial_service_charge_fn = lambda rate: rate * constants.industrial_use_params['n_customers']/1000000
    industrial_flow_charge_fn = lambda rate: rate * constants.industrial_use_params['n_customers'] * constants.industrial_use_params['drought_ccf_per_month']/1000000

    long_charges = np.hstack([
        np.vectorize(residential_service_charge_fn)(rates),
        np.vectorize(tier_1_flow_charge_fn)(rates),
        np.vectorize(tier_2_flow_charge_fn)(rates),
        np.vectorize(commercial_service_charge_fn)(rates),
        np.vectorize(commercial_flow_charge_fn)(rates),
        np.vectorize(industrial_service_charge_fn)(rates),
        np.vectorize(industrial_flow_charge_fn)(rates),
    ])
    long_rates = list(rates) * 7
    charge_type = np.repeat(['Residential Service Charge', 'Low Use Flow Charge', 'High Use Flow Charge', 'Commercial Service Charge', 'Commercial Flow Charge', 'Industrial Service Charge', 'Industrial Flow Charge'], len(rates))
    df = pd.DataFrame({
        'Monthly Revenue': long_charges,
        'Rate': long_rates,
        'Charge Type': charge_type,
    })
    fig = px.line(df, x='Rate', y='Monthly Revenue', color='Charge Type', width=1300, height=600, hover_name='Charge Type', hover_data={'Charge Type':False, 'Rate':True})
    fig.update_layout(
        title='Visualizing Effect of Increasing Rates',
        yaxis_title='Monthly Revenue (MM)',
        xaxis_title='Rate (Dollars)',
    )
    return fig

########################
### Surcharge Effect ###
########################

surcharge_residential_service_charge_input = html.Div(
    ["Surcharge Residential Service Charge (%): ", 
     dcc.Input(value=2, id='surcharge_residential_service_charge_input', type='number')
     ]
)
surcharge_tier_1_flow_charge_input = html.Div(
    ["Surcharge Tier 1 Flow Charge (%): ", 
     dcc.Input(value=5, id='surcharge_tier_1_flow_charge_input', type='number')
     ]
)
surcharge_tier_2_flow_charge_input = html.Div(
    ["Surcharge Tier 2 Flow Charge (%): ", 
     dcc.Input(value=30, id='surcharge_tier_2_flow_charge_input', type='number')
     ]
)
surcharge_commercial_service_charge_input = html.Div(
    ["Surcharge Commercial Service Charge (%): ", 
     dcc.Input(value=5, id='surcharge_commercial_service_charge_input', type='number')
     ]
)
surcharge_commercial_flow_charge_input = html.Div(
    ["Surcharge Commercial Flow Charge (%): ", 
     dcc.Input(value=10, id='surcharge_commercial_flow_charge_input', type='number')
     ]
)
surcharge_industrial_service_charge_input = html.Div(
    ["Surcharge Industrial Service Charge (%): ", 
     dcc.Input(value=10, id='surcharge_industrial_service_charge_input', type='number')
     ]
)
surcharge_industrial_flow_charge_input = html.Div(
    ["Surcharge Industrial Flow Charge (%): ", 
     dcc.Input(value=25, id='surcharge_industrial_flow_charge_input', type='number')
     ]
)

@callback(
    Output(
        component_id="surcharge_drought_annual_revenue_fig", component_property="figure"
    ),
    Input(component_id="residential_service_charge", component_property="value"),
    Input(component_id="tier_1_flow_charge", component_property="value"),
    Input(component_id="tier_2_flow_charge", component_property="value"),
    Input(component_id="commercial_service_charge", component_property="value"),
    Input(component_id="commercial_flow_charge", component_property="value"),
    Input(component_id="industrial_service_charge", component_property="value"),
    Input(component_id="industrial_flow_charge", component_property="value"),
    
    Input(component_id="surcharge_residential_service_charge_input", component_property="value"),
    Input(component_id="surcharge_tier_1_flow_charge_input", component_property="value"),
    Input(component_id="surcharge_tier_2_flow_charge_input", component_property="value"),
    Input(component_id="surcharge_commercial_service_charge_input", component_property="value"),
    Input(component_id="surcharge_commercial_flow_charge_input", component_property="value"),
    Input(component_id="surcharge_industrial_service_charge_input", component_property="value"),
    Input(component_id="surcharge_industrial_flow_charge_input", component_property="value"),
)
def surcharge_drought_customer_annual_revenue_fig(
    residential_service_charge,
    tier_1_residential_flow_charge,
    tier_2_residential_flow_charge,
    commercial_service_charge,
    commercial_flow_charge,
    industrial_service_charge,
    industrial_flow_charge,
    surcharge_residential_service_charge_increase,
    surcharge_tier_1_flow_charge_increase,
    surcharge_tier_2_flow_charge_increase,
    surcharge_commercial_service_charge_increase,
    surcharge_commercial_flow_charge_increase,
    surcharge_industrial_service_charge_increase,
    surcharge_industrial_flow_charge_increase,
):
    low_monthly_service_charge = residential_service_charge
    low_monthly_flow_charge = tier_1_residential_flow_charge * constants.low_use_params['ccf_per_month']
    low_monthly_total_charge = low_monthly_service_charge + low_monthly_flow_charge
    
    high_monthly_service_charge = residential_service_charge
    high_monthly_flow_charge = constants.tier_1_residential_threshold * tier_1_residential_flow_charge + (constants.high_use_params['ccf_per_month'] - constants.tier_1_residential_threshold) * tier_2_residential_flow_charge
    high_monthly_total_charge = high_monthly_service_charge + high_monthly_flow_charge
    
    commercial_monthly_service_charge = commercial_service_charge
    commercial_monthly_flow_charge = commercial_flow_charge * constants.commercial_use_params['ccf_per_month']
    commercial_monthly_total_charge = commercial_monthly_service_charge + commercial_monthly_flow_charge
    
    industrial_monthly_service_charge = industrial_service_charge
    industrial_monthly_flow_charge = industrial_flow_charge * constants.industrial_use_params['ccf_per_month']
    industrial_monthly_total_charge = industrial_monthly_service_charge + industrial_monthly_flow_charge
    
    low_annual_revenue = 12 * constants.low_use_params ['n_customers'] * low_monthly_total_charge
    high_annual_revenue = 12 * constants.high_use_params ['n_customers'] * high_monthly_total_charge
    commercial_annual_revenue = 12 * constants.commercial_use_params ['n_customers'] * commercial_monthly_total_charge
    industrial_annual_revenue = 12 * constants.industrial_use_params ['n_customers'] * industrial_monthly_total_charge
    
    surcharge_residential_service_charge = residential_service_charge*(1+surcharge_residential_service_charge_increase/100)
    surcharge_tier_1_residential_flow_charge = tier_1_residential_flow_charge*(1+surcharge_tier_1_flow_charge_increase/100)
    surcharge_tier_2_residential_flow_charge = tier_2_residential_flow_charge*(1+surcharge_tier_2_flow_charge_increase/100)
    
    surcharge_commercial_service_charge = commercial_service_charge*(1+surcharge_commercial_service_charge_increase/100)
    surcharge_commercial_flow_charge = commercial_flow_charge*(1+surcharge_commercial_flow_charge_increase/100)
    surcharge_industrial_service_charge = industrial_service_charge*(1+surcharge_industrial_service_charge_increase/100)
    surcharge_industrial_flow_charge = industrial_flow_charge*(1+surcharge_industrial_flow_charge_increase/100)
        
    drought_low_monthly_flow_charge = surcharge_tier_1_residential_flow_charge * constants.low_use_params['drought_ccf_per_month']
    drought_low_monthly_total_charge = surcharge_residential_service_charge + drought_low_monthly_flow_charge
    drought_low_annual_revenue = 12 * constants.low_use_params['n_customers'] * drought_low_monthly_total_charge
    
    drought_high_monthly_flow_charge = constants.tier_1_residential_threshold * surcharge_tier_1_residential_flow_charge + (constants.high_use_params['drought_ccf_per_month'] - constants.tier_1_residential_threshold) * surcharge_tier_2_residential_flow_charge
    drought_high_monthly_total_charge = surcharge_residential_service_charge + drought_high_monthly_flow_charge    
    drought_high_annual_revenue = 12 * constants.high_use_params['n_customers'] * drought_high_monthly_total_charge

    drought_commercial_monthly_flow_charge = surcharge_commercial_flow_charge * constants.commercial_use_params['drought_ccf_per_month']
    drought_commercial_monthly_total_charge = surcharge_commercial_service_charge + drought_commercial_monthly_flow_charge
    drought_commercial_annual_revenue = 12 * constants.commercial_use_params['n_customers'] * drought_commercial_monthly_total_charge

    drought_industrial_monthly_flow_charge = surcharge_industrial_flow_charge * constants.industrial_use_params['drought_ccf_per_month']
    drought_industrial_monthly_total_charge = surcharge_industrial_service_charge + drought_industrial_monthly_flow_charge
    drought_industrial_annual_revenue = 12 * constants.industrial_use_params['n_customers'] * drought_industrial_monthly_total_charge

    drought_annual_revenue = drought_low_annual_revenue + drought_high_annual_revenue + drought_commercial_annual_revenue + drought_industrial_annual_revenue
        
    df = pd.DataFrame(
            {
                "Customer": ["Low Use", "High Use", "Commercial", "Industrial", "(Surcharge) Low Use", "(Surcharge) High Use", "(Surcharge) Commercial", "(Surcharge) Industrial", ],
                "Annual Revenue": np.array([low_annual_revenue, high_annual_revenue, commercial_annual_revenue, industrial_annual_revenue, drought_low_annual_revenue, drought_high_annual_revenue, drought_commercial_annual_revenue, drought_industrial_annual_revenue])/1000000,
            }
        ) # In long format

    fig = px.bar(df, x='Annual Revenue', y='Customer', title='Agency Annual Revenue by Customer', orientation='h', color='Customer', width=1300, height=600,
                 color_discrete_map={
                'Low Use': 'rgba(99,110,250,0.5)',
                'High Use': 'rgba(239,85,59,0.5)',
                'Commercial': 'rgba(0,204,150,0.5)',
                'Industrial': 'rgba(171,99,250, 0.5)',
                '(Surcharge) Low Use': 'rgba(99,110,250,1)',
                '(Surcharge) High Use': 'rgba(239,85,59,1)',
                '(Surcharge) Commercial': 'rgba(0,204,150,1)',
                '(Surcharge) Industrial': 'rgba(171,99,250,1)',
            })
    fig.update_layout(
        title="Agency Annual Revenue by Customer",
        xaxis_title="Annual Revenue (Millions)",
        yaxis_title="Customer Type",
        hovermode=False
    )
    
    
    texts = df['Annual Revenue']
    for i, t in enumerate(texts[:4]):
        fig.data[i].text = str(round(t, 2))
        fig.data[i].textposition = 'outside'
        
    differences = np.array(df['Annual Revenue'][4:]) - np.array(df['Annual Revenue'][:4])
    for i, t in enumerate(differences):
        sign = '+' if t > 0 else '-'
        fig.data[i+4].text = sign + '${:,.2f}'.format(abs(round(t, 2)))
        fig.data[i+4].textposition = 'inside'

    fig.add_annotation(x=10, y=8,
            text=f"(Surcharge) Annual Change (+/-) to Reserve Fund: {'${:,.2f}'.format(drought_annual_revenue - constants.revenue_requirement)}",
            showarrow=False,
            font_size=20,
            xshift=300
    )
    return fig
