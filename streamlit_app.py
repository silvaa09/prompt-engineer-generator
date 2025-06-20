import streamlit as st

st.set_page_config(page_title="Prompt Engineer Generator", layout="centered")

st.title("🚀 Prompt Engineer Generator")
st.markdown("Effortlessly generate optimized prompts for leading AI models.")

user_objective = st.text_input("🎯 Enter your objective:", value="Write an engaging marketing email")

ai_model = st.selectbox(
    label="🤖 Choose your AI Model:", 
    options=["ChatGPT", "Claude", "Gemini", "Mistral", "GPT-NeoX"]
)

subscription_tier = st.radio(
    label="📦 Choose Subscription Tier:", 
    options=["Free", "Pro"]
)

if subscription_tier == "Free":
    st.info("Free tier: Limited to 5 prompt generations per day.")
else:
    st.success("Pro tier activated: Unlimited prompts with priority processing!")

if st.button("✨ Generate Optimized Prompt"):
    optimized_prompt = (
        f"Create a highly effective, detailed, and clear prompt tailored specifically for {ai_model}, "
        f"designed to achieve the following objective: '{user_objective}'. "
        "Include specific instructions and context needed for best results."
    )

    st.subheader("📄 Optimized Prompt:")
    st.code(optimized_prompt, language="markdown")

st.markdown("---")
st.subheader("🔐 Upgrade to Pro")
st.markdown("Enjoy unlimited prompts and advanced templates by upgrading to Pro for only $9.99/month.")

st.markdown(
    """
    <iframe src="https://buy.stripe.com/test_your_stripe_link_here"
            width="100%" height="650" frameborder="0" scrolling="no">
    </iframe>
    """, 
    unsafe_allow_html=True
)