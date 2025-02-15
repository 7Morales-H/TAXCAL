import streamlit as st

# Title
st.title("Jaffrey, NH Property Tax Calculator")

# User input
property_value = st.number_input("Enter your property value ($)", min_value=0, value=225000)

# Fixed tax data
current_total_tax_rate = 32.80
school_percentage = 0.50
municipal_percentage = 0.32
state_ed_percentage = 0.06
county_percentage = 0.12
current_budget = 33_760_452
budget_decrease = 3_000_000
new_budget = current_budget - budget_decrease

# Calculate total property valuation
current_school_tax_rate = current_total_tax_rate * school_percentage
total_valuation = (current_budget / current_school_tax_rate) * 1000

# New school tax rate
new_school_tax_rate = (new_budget / total_valuation) * 1000
new_total_tax_rate = new_school_tax_rate + (current_total_tax_rate * (1 - school_percentage))

# Calculate taxes
current_tax = (property_value / 1000) * current_total_tax_rate
new_tax = (property_value / 1000) * new_total_tax_rate
tax_savings = current_tax - new_tax

# Display results
st.write(f"**Current Property Tax:** ${current_tax:.2f}")
st.write(f"**New Property Tax (After $3M Budget Cut):** ${new_tax:.2f}")
st.write(f"**Tax Savings:** ${tax_savings:.2f}")