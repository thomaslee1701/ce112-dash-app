from dash import callback
from dash_extensions import EventListener
from dash_extensions.enrich import DashProxy, html, Input, Output, State, dcc
from dash.exceptions import PreventUpdate
from components import *

app = DashProxy()

app.layout = html.Div(
    children=[
        html.Div([
            html.H1('CE 112'),
            html.H3('Water Rate Setting'),
            html.P('Thomas Lee'),
            html.Hr(),
        ]),
        html.P('Rate Setting', style={'font-size':'40px'}),
        html.P('1.1 Visualizing Results From Lab', style={'font-size':'26px'}),
        html.P('Our group was assigned the "revenue stability" philosophy for deciding our rate structure. As stated in the reading, charging a flat fee provides great financial stability by removing the dependency of water demand variance on our revenue. Unfortunately, having just a flat fee may result in excessive water use, so we decided to instead have fairly high service charges for all customer types (low use, high use, commercial, and industrial) and lower flow charges. We adjusted our flow charge for each group to be around 30 percent of the total monthly bill (aside from "Low Use"). This yielded an annual change of over 712 million dollars, falling comfortably within our revenue requirement of 700 million +/- 20 million. In the percent annual revenue chart, we see that each group contributes 20-25 percent of our annual revenue.'),
        html.Br(),
        html.Center([
            residential_service_charge_elem,
            tier_1_flow_charge_elem,
            tier_2_flow_charge_elem,
            commercial_service_charge_elem,
            commercial_flow_charge_elem,
            industrial_service_charge_elem,
            industrial_flow_charge_elem,
            ],      
        ),
        html.Div(
            plot_dropdown,
        ),
        html.Center(
            dcc.Graph(id="dropdown_fig"),
        ),
        html.Center(
                [
                    html.Div([
                        "Customers to show: \n",
                        dcc.Checklist(['Low Use', 'High Use', 'Commercial', 'Industrial'], value=['Low Use', 'High Use', 'Commercial', 'Industrial'], id="customer_monthly_bill_checklist"),
                    ], id='customer_checkbox')
                ], style={'padding': 5, 'flex': 1}
            ),
        html.P('1.2 Effect of Increasing Rates on Monthly Revenue', style={'font-size':'26px'}),
        html.P('I was curious how increasing the various rates would affect monthly revenue. From looking at the figure below, we can see that the growth rate of "High Use Flow Charge" exceeds the other charge types. In other words, if we had to choose one of our rates to increase, increasing the "High Use Flow Charge" would yield the greatest increase in monthly revenue. Something worth noting is that the growth rate of "Industrial Flow Charge" and "Commercial Flow Charge" are both higher than "Low Use Flow Charge" despite there being so many more low use customers. If we wanted to increase our revenue, this chart could be a motivator for first targeting high use, commercial, and industrial flow charges.'),
        html.Center(
            dcc.Graph(figure=increasing_rates_fig()),
        ),
        
        html.Hr(),
        html.P('Drought', style={'font-size':'40px'}),
        html.P('2.1 Drought Monthly Bills', style={'font-size':'26px'}),
        html.P('When there is a drought, water usage goes down. Low use customers use 10 percent less water, and high use customers use 40 percent less water. There is no change in commercial and industrial water usage, so I did not include them in this figure. I annotated the figure with the decrease in revenue during the drought from flow charges. As expected, the high use customers have the largest impact on our revenue. Our annual change is now 67 million dollars under our revenue requirement.'),
        html.Center(
            dcc.Graph(id='drought_comparison_fig')
        ),
        html.Center(
            dcc.Graph(id='drought_annual_revenue_fig')
        ),
        html.P('2.2 Effect of Increasing Rates on Monthly Revenue During Drought', style={'font-size':'26px'}),
        html.P('We will have to increase rates somewhere in order to bring our revenue back up to our requirement. From visualizing the effect of increasing the various rates during the drought, we can observe that "Industrial Flow Charge" now has the highest rate of growth. "Low Use Flow Charge" is now above "High Use Flow Charge" because of the dramatic decrease in water usage by the "High Use" group.'),
        html.Center(
            dcc.Graph(figure=drought_increasing_rates_fig()),
        ),
        html.P('2.3 Proposed Rate Increases', style={'font-size':'26px'}),
        html.P('Using the information from the previous figures, we can motivate the increases our group decided to choose. We decided to target the "Commercial" and "Industrial" groups the most. Those groups ended up contributing 16 million and 39 million more to our annual revenue. This decision was made by once again following our "Revenue Stability" philosophy. Commercial and industrial customers have more consistent water usage, so this solution would have the least variance. In addition to increasing costs for commercial and industrial customers, we also dramatically increased the flow charge for the "High Use" group. Overall, they still pay less than they would previously, so we were comfortable with this decision. Low use customers also received a small increase in charges.'),
        html.Br(),
        html.Center([
            surcharge_residential_service_charge_input,
            surcharge_tier_1_flow_charge_input,
            surcharge_tier_2_flow_charge_input,
            surcharge_commercial_service_charge_input,
            surcharge_commercial_flow_charge_input,
            surcharge_industrial_service_charge_input,
            surcharge_industrial_flow_charge_input,
            ],      
        ),
        html.Center(
            dcc.Graph(id='surcharge_drought_annual_revenue_fig')
        ),
    ], style={"font-family": "Verdana"}
)

if __name__ == '__main__':
    app.run(debug=True)
