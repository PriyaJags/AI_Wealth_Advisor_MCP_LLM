import streamlit as st
from tools import get_client_profile
from agent import run_agent


st.set_page_config(page_title="Wealth Advisor AI", layout="wide")

st.title("🏦 AI Wealth Advisor")
st.caption("Generate AI-powered meeting briefs for financial advisors")

# -----------------------
# CLIENT SELECTION
# -----------------------
client_name = st.selectbox("Select Client", ["john", "mary"])

client = get_client_profile(client_name)

# -----------------------
# LAYOUT
# -----------------------
left, right = st.columns([1, 2])

# -----------------------
# LEFT PANEL
# -----------------------
with left:

    st.subheader("👤 Client Profile")

    st.metric(
        label="💰 Portfolio Value",
        value=client["portfolio_value"]
    )

    st.markdown("### Client Details")

    st.markdown(f"""
**Name:** {client["name"]}

**Age:** {client["age"]}

**Risk Profile:** {client["risk"]}
""")

    st.divider()

    st.markdown("### 📂 Holdings")

    for holding in client["holdings"]:
        st.markdown(f"- {holding}")

# -----------------------
# RIGHT PANEL
# -----------------------
with right:

    st.subheader("🤖 Advisor Preparation Notes")

    if st.button("📝 Generate Meeting Brief"):

        with st.spinner("Generating insights..."):
            result = run_agent(client_name)

        st.markdown(result)