import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Ovexa AI Performance Dashboard",
    layout="wide"
)


# MOCK USER DATA
mock_user_data = {
    "Recovery Score": 81,
    "Stress Level": "Moderate",
    "Focus Potential": "High",
    "Sleep Quality": "Good",
    "Cycle Phase": "Follicular",
    "Calendar Load": "Medium"
}


recommendations = [
    {
        "title": "Deep Work Window",
        "description": "Best time for cognitively demanding work is between 9:00 AM - 12:00 PM."
    },
    {
        "title": "Meeting Guidance",
        "description": "Avoid stacking meetings in the late afternoon due to predicted energy decline."
    },
    {
        "title": "Recovery Suggestion",
        "description": "A light evening walk is recommended to support recovery balance."
    }
]


reasoning = [
    "Recovery indicators improved compared to yesterday",
    "Sleep quality remained stable for the past 3 days",
    "Calendar load is manageable during morning hours",
    "Historical focus trend is strongest before noon"
]


schedule_data = pd.DataFrame([
    {
        "Time": "9:00 AM",
        "Activity": "Strategic Planning",
        "Energy": "Optimal"
    },
    {
        "Time": "11:00 AM",
        "Activity": "Deep Focus Session",
        "Energy": "High"
    },
    {
        "Time": "2:00 PM",
        "Activity": "Team Meetings",
        "Energy": "Moderate"
    },
    {
        "Time": "6:00 PM",
        "Activity": "Light Exercise",
        "Energy": "Recovery Friendly"
    }
])


# CUSTOM STYLING
st.markdown(
    """
    <style>

    .main {
        background-color: #f8fafc;
    }

    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    .recommendation-card {
        background-color: white;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 18px;
        border-left: 6px solid #8b5cf6;
    }

    .insight-box {
        background-color: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }

    .reason-box {
        background-color: #f1f5f9;
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# HEADER
st.title("Ovexa AI Performance Intelligence")

st.markdown(
    "Personalized scheduling and wellbeing recommendations powered by behavioral and wearable insights."
)

st.divider()


# TOP METRICS
st.subheader("User Performance Signals")

metric_columns = st.columns(3)

metric_items = list(mock_user_data.items())

for index, (title, value) in enumerate(metric_items):

    column = metric_columns[index % 3]

    with column:
        st.markdown(
            f"""
            <div class='metric-card'>
                <h4 style='color:#64748b;'> {title} </h4>
                <h2 style='color:#0f172a;'> {value} </h2>
            </div>
            """,
            unsafe_allow_html=True
        )


# MAIN CONTENT
left_column, right_column = st.columns([2, 1])


# LEFT SECTION
with left_column:

    st.subheader("AI Recommendations")

    for recommendation in recommendations:

        st.markdown(
            f"""
            <div class='recommendation-card'>
                <h3>{recommendation['title']}</h3>
                <p>{recommendation['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# RIGHT SECTION
with right_column:

    st.subheader("AI Coaching Insight")

    st.markdown(
        """
        <div class='insight-box'>
            <p style='font-size:18px; line-height:1.7;'>
                Your recovery indicators and behavioral patterns suggest that today is ideal for strategic thinking and cognitively demanding work during the morning hours.
                <br><br>
                Consider keeping the afternoon lighter to maintain energy balance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Recommendation Confidence")
    st.progress(82)
    st.caption("Confidence Score: 82%")


st.divider()


# EXPLAINABILITY + SCHEDULE
explainability_column, schedule_column = st.columns(2)


# EXPLAINABILITY
with explainability_column:

    st.subheader("Why These Recommendations?")

    for reason in reasoning:

        st.markdown(
            f"""
            <div class='reason-box'>
                • {reason}
            </div>
            """,
            unsafe_allow_html=True
        )


# SCHEDULE
with schedule_column:

    st.subheader("Intelligent Daily Schedule")

    st.dataframe(
        schedule_data,
        use_container_width=True,
        hide_index=True
    )


st.divider()


# BEHAVIORAL ADAPTATION
st.subheader("Behavioral Adaptation Insights")

adaptation_columns = st.columns(3)

adaptation_items = [
    {
        "title": "Peak Productivity Window",
        "value": "9 AM - 1 PM"
    },
    {
        "title": "Preferred Work Pattern",
        "value": "Low Meeting Density"
    },
    {
        "title": "Energy Stability Trend",
        "value": "+12% This Week"
    }
]


for index, item in enumerate(adaptation_items):

    with adaptation_columns[index]:

        st.markdown(
            f"""
            <div class='metric-card'>
                <h4 style='color:#64748b;'> {item['title']} </h4>
                <h2 style='color:#0f172a;'> {item['value']} </h2>
            </div>
            """,
            unsafe_allow_html=True
        )


st.divider()

st.caption(
    "Concept visualization demonstrating AI-assisted scheduling, behavioral intelligence, and wearable-driven recommendation systems."
)
