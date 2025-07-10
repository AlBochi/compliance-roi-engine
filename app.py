import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Compliance ROI Calculator",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
    }
    .header-text {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    .metric-box {
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background-color: #f0f2f6;
    }
    .positive-roi {
        color: #28a745;
        font-weight: bold;
    }
    .negative-roi {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Core calculation logic
def calculate_roi(annual_revenue, audit_costs, breach_risk, framework_multiplier=1.0):
    """Calculate compliance ROI metrics"""
    # Base compliance cost (2% of revenue, adjusted by framework complexity)
    base_compliance_cost = annual_revenue * 0.02 * framework_multiplier
    
    # Risk reduction (67% reduction with controls)
    risk_reduction = breach_risk * 0.67
    
    # Savings components:
    # 1. Audit cost reduction (60% efficiency gain)
    # 2. Breach cost avoidance (4% of revenue per breach * risk reduction)
    savings = (audit_costs * 0.6) + (annual_revenue * risk_reduction * 0.04)
    
    roi_percentage = ((savings - base_compliance_cost) / base_compliance_cost) * 100
    
    return {
        "annual_compliance_cost": base_compliance_cost,
        "estimated_annual_savings": savings,
        "roi_percentage": roi_percentage,
        "breach_risk_reduction": risk_reduction * 100,
        "net_benefit": savings - base_compliance_cost
    }

# Framework multipliers
FRAMEWORKS = {
    "SOC 2": 1.0,
    "ISO 27001": 1.2,
    "HIPAA": 1.3,
    "GDPR": 1.4,
    "PCI DSS": 1.5
}

# Industry breach risk averages (percentage)
INDUSTRY_RISKS = {
    "Healthcare": 28.5,
    "Financial Services": 23.7,
    "Technology": 19.2,
    "Retail": 25.1,
    "Manufacturing": 18.6
}

# Main app function
def main():
    st.markdown('<div class="header-text">Compliance ROI Calculator</div>', unsafe_allow_html=True)
    
    with st.expander("ℹ️ How This Calculator Works", expanded=False):
        st.write("""
        This tool calculates the financial return on investment (ROI) for compliance programs by comparing:
        - **Costs**: Implementation and maintenance of compliance controls
        - **Savings**: Reduced breach risk and audit efficiencies
        
        Key assumptions:
        - Typical compliance costs average 2% of revenue (adjusted by framework complexity)
        - Effective compliance programs reduce breach risk by 67%
        - The average cost of a breach is 4% of annual revenue
        - Compliance automation can reduce audit preparation costs by 60%
        """)
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Company Profile")
        annual_revenue = st.number_input(
            "Annual Revenue (USD)", 
            min_value=100000, 
            max_value=10000000000, 
            value=5000000,
            step=100000,
            help="Company's total annual revenue in USD"
        )
        
        industry = st.selectbox(
            "Industry",
            options=list(INDUSTRY_RISKS.keys()),
            help="Select your industry for benchmark breach risk"
        )
        
        # Set default breach risk based on industry
        default_breach_risk = INDUSTRY_RISKS[industry]
        
    with col2:
        st.subheader("Compliance Program")
        compliance_framework = st.selectbox(
            "Primary Compliance Framework",
            options=list(FRAMEWORKS.keys()),
            help="Select your primary compliance framework"
        )
        
        audit_costs = st.number_input(
            "Annual Audit/Compliance Costs (USD)",
            min_value=0,
            max_value=10000000,
            value=150000,
            step=1000,
            help="Total annual costs for audits, assessments, and compliance activities"
        )
        
        breach_risk = st.slider(
            "Current Perceived Breach Risk (%)",
            min_value=0.0,
            max_value=100.0,
            value=float(default_breach_risk),
            step=0.5,
            help="Organization's current estimated probability of a major breach"
        )
    
    # Calculate ROI
    framework_multiplier = FRAMEWORKS[compliance_framework]
    results = calculate_roi(annual_revenue, audit_costs, breach_risk, framework_multiplier)
    
    # Display metrics
    st.markdown("---")
    st.subheader("Financial Impact Analysis")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric(
            label="Annual Compliance Cost",
            value=f"${results['annual_compliance_cost']:,.0f}",
            help="Estimated annual cost to implement and maintain compliance program"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric(
            label="Estimated Annual Savings",
            value=f"${results['estimated_annual_savings']:,.0f}",
            help="Savings from reduced breach risk and audit efficiencies"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        roi_class = "positive-roi" if results['roi_percentage'] >= 0 else "negative-roi"
        st.metric(
            label="ROI Percentage",
            value=f"{results['roi_percentage']:,.1f}%",
            delta=f"{results['net_benefit']:,.0f} USD net benefit" if results['net_benefit'] >= 0 else f"-${abs(results['net_benefit']):,.0f} USD net cost",
            delta_color="normal",
            help="Return on investment percentage for compliance program"
        )
        st.markdown(f'<div class="{roi_class}">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col4:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric(
            label="Breach Risk Reduction",
            value=f"{results['breach_risk_reduction']:,.1f}%",
            help="Estimated reduction in breach probability with compliance controls"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Visualization section
    st.markdown("---")
    st.subheader("Cost-Benefit Analysis")
    
    # Prepare data for visualization
    cost_benefit_data = pd.DataFrame({
        "Category": ["Compliance Costs", "Breach Cost Avoidance", "Audit Efficiency Gains"],
        "Amount": [
            results['annual_compliance_cost'],
            annual_revenue * (breach_risk/100) * 0.67 * 0.04,  # 67% risk reduction * 4% of revenue
            audit_costs * 0.6
        ],
        "Type": ["Cost", "Benefit", "Benefit"]
    })
    
    # Create treemap visualization
    fig = px.treemap(
        cost_benefit_data,
        path=['Type', 'Category'],
        values='Amount',
        color='Type',
        color_discrete_map={'Cost':'#FF6B6B','Benefit':'#4ECDC4'},
        title="Compliance Cost vs. Benefit Breakdown"
    )
    fig.update_traces(textinfo="label+value")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    
    # Display the visualization
    st.plotly_chart(fig, use_container_width=True)
    
    # Scenario analysis
    st.markdown("---")
    st.subheader("Scenario Analysis")
    
    scenario_col1, scenario_col2 = st.columns(2)
    
    with scenario_col1:
        st.markdown("**Varying Breach Risk**")
        risk_range = [breach_risk * (1 + i/10) for i in range(-4, 5)]
        risk_data = []
        for risk in risk_range:
            if risk < 0: risk = 0
            if risk > 100: risk = 100
            scenario = calculate_roi(annual_revenue, audit_costs, risk, framework_multiplier)
            risk_data.append({
                "Breach Risk (%)": risk,
                "ROI (%)": scenario['roi_percentage'],
                "Net Benefit (USD)": scenario['net_benefit']
            })
        risk_df = pd.DataFrame(risk_data)
        fig_risk = px.line(
            risk_df,
            x="Breach Risk (%)",
            y="ROI (%)",
            title="ROI at Different Breach Risk Levels",
            markers=True
        )
        st.plotly_chart(fig_risk, use_container_width=True)
    
    with scenario_col2:
        st.markdown("**Varying Compliance Investment**")
        investment_range = [0.5, 0.75, 1.0, 1.25, 1.5]  # Multipliers of base compliance cost
        investment_data = []
        for mult in investment_range:
            adjusted_audit_costs = audit_costs * mult
            scenario = calculate_roi(annual_revenue, adjusted_audit_costs, breach_risk, framework_multiplier)
            investment_data.append({
                "Investment Multiplier": mult,
                "ROI (%)": scenario['roi_percentage'],
                "Compliance Cost (USD)": scenario['annual_compliance_cost']
            })
        investment_df = pd.DataFrame(investment_data)
        fig_invest = px.bar(
            investment_df,
            x="Investment Multiplier",
            y="ROI (%)",
            title="ROI at Different Investment Levels",
            text="ROI (%)"
        )
        st.plotly_chart(fig_invest, use_container_width=True)
    
    # Report generation
    st.markdown("---")
    st.subheader("Generate Executive Report")
    
    company_name = st.text_input("Company Name", value="Acme Corporation")
    report_date = st.date_input("Report Date", value=datetime.now())
    
    if st.button("Generate PDF Report"):
        # In a production app, you would generate a PDF here
        # For this demo, we'll show a success message
        st.success("Report generated successfully!")
        st.download_button(
            label="Download Report (PDF)",
            data="This would be the PDF binary data in a real app",
            file_name=f"Compliance_ROI_Report_{company_name}_{report_date.strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
