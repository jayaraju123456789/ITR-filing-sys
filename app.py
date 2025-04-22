import streamlit as st

def suggest_itr(resident_status, income_type, business_income, agri_income, capital_gains):
    if resident_status == "Resident" and income_type == "Salary" and not business_income and not agri_income and not capital_gains:
        return "ITR-1 (Sahaj) is suitable for you."
    elif resident_status in ["Resident", "Non-Resident"] and income_type == "Salary" and not business_income and capital_gains:
        return "ITR-2 is suitable for you."
    elif business_income:
        return "ITR-3 is suitable for you if you have income from Business or Profession."
    elif resident_status == "Resident" and income_type == "Presumptive Income (Section 44AD, 44ADA, 44AE)":
        return "ITR-4 (Sugam) is suitable for you."
    else:
        return "Please consult a tax expert for complex cases or special conditions."

def main():
    st.title("💼 ITR Relation Manager")
    st.subheader("Let me suggest the right ITR form for you!")

    resident_status = st.selectbox("Select your Residential Status:", ["Resident", "Non-Resident", "Resident but Not Ordinarily Resident"])
    income_type = st.selectbox("Select your primary Income Type:", ["Salary", "Business/Profession", "Capital Gains", "Other Sources", "Presumptive Income (Section 44AD, 44ADA, 44AE)"])
    business_income = st.checkbox("Do you have income from Business or Profession?")
    agri_income = st.checkbox("Do you have Agricultural Income exceeding ₹5000?")
    capital_gains = st.checkbox("Do you have Capital Gains Income?")

    if st.button("Suggest ITR Form"):
        suggestion = suggest_itr(resident_status, income_type, business_income, agri_income, capital_gains)
        st.success(suggestion)

if __name__ == "__main__":
    main()
