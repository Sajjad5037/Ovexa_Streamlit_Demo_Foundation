import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------

# PAGE CONFIG

# -----------------------------------

st.set_page_config(
page_title="Ovexa AI Intelligence",
page_icon="🧠",
layout="wide"
)

# -----------------------------------

# GLOBAL STYLING

# -----------------------------------

st.markdown(
""" <style>

```
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.main {
    background-color: #f8fafc;
}

section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 8px;
}

.subtitle {
    color: #64748b;
    font-size: 18px;
    margin-bottom: 30px;
}

.metric-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.05);
    margin-bottom: 18px;
}

.metric-title {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    color: #0f172a;
    font-size: 32px;
    font-weight: 700;
}

.recommendation-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    margin-bottom: 18px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.05);
    border-left: 6px solid #8b5cf6;
}

.recommendation-priority {
    color: #8b5cf6;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

.recommendation-title {
    color: #0f172a;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 10px;
}

.recommendation-description {
    color: #475569;
    line-height: 1.7;
    font-size: 16px;
}

.insight-box {
    background: white;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.05);
}

.section-title {
    color: #0f172a;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
}

.reason-box {
    background: #f1f5f9;
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    color: #334155;
    line-height: 1.6;
}

.timeline-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

.timeline-time {
    color: #64748b;
    font-size: 14px;
}

.timeline-title {
    color: #0f172a;
    font-size: 18px;
    font-weight: 600;
}

.timeline-energy {
    color: #8b5cf6;
    font-weight: 600;
}

</style>
""",
unsafe_allow_html=True
```

)

# -----------------------------------

# SIDEBAR

# -----------------------------------

st.sidebar.title("Ovexa")

st.sidebar.markdown("### Navigation")

st.sidebar.markdown("""

* Dashboard Overview
* AI Recommendations
* Recovery Trends
* Calendar Intelligence
* Behavioral Adaptation
* AI Coaching
* Settings
  """)

st.sidebar.divider()

st.sidebar.markdown("### AI Recommendation Confidence")

st.sidebar.progress(82)

st.sidebar.caption("Confidence Score: 82%")

# -----------------------------------

# MOCK DATA

# -----------------------------------

metrics = {
"Recovery Score": "81%",
"Stress Level": "Moderate",
"Focus Potential": "High",
"Sleep Quality": "Good",
"Cycle Phase": "Follicular",
"Calendar Density": "Medium"
}

recommendations = [
{
"priority": "HIGH IMPACT",
"title": "Deep Work Window",
"description": "Your recovery profile and behavioral patterns suggest that 9AM - 12PM is currently your strongest cognitive performance window."
},

```
{
    "priority": "MODERATE PRIORITY",
    "title": "Reduce Meeting Density",
    "description": "Energy stability is expected to decline slightly after 3PM. Consider reducing stacked meetings during the late afternoon."
},

{
    "priority": "RECOVERY OPTIMIZATION",
    "title": "Light Evening Activity",
    "description": "A low-intensity walk or recovery-friendly movement session may help maintain energy balance and improve tomorrow's readiness score."
}
```

]

reasoning = [
"Recovery indicators improved by 11% compared to yesterday",
"Sleep quality has remained stable for the past 3 days",
"Morning calendar density is lower than average",
"Historical productivity patterns indicate stronger focus before noon",
"Behavioral analysis shows improved cognitive performance after lighter evening schedules"
]

timeline = [
{
"time": "8:00 AM",
"title": "Strategic Planning",
"energy": "🟢 High Focus"
},

```
{
    "time": "11:00 AM",
    "title": "Deep Cognitive Work",
    "energy": "🟢 Peak Performance"
},

{
    "time": "2:00 PM",
    "title": "Collaborative Meetings",
    "energy": "🟡 Moderate Energy"
},

{
    "time": "6:00 PM",
    "title": "Recovery Walk",
    "energy": "🔵 Recovery Friendly"
}
```

]

# -----------------------------------

# HEADER

# -----------------------------------

st.markdown(
""" <div class='main-title'>
Ovexa AI Performance Intelligence </div>

```
<div class='subtitle'>
    AI-assisted scheduling and wellbeing recommendations powered by wearable, behavioral, and contextual signals.
</div>
""",
unsafe_allow_html=True
```

)

# -----------------------------------

# METRICS

# -----------------------------------

st.markdown(
"<div class='section-title'>Performance Signals</div>",
unsafe_allow_html=True
)

metric_columns = st.columns(3)

metric_items = list(metrics.items())

for index, (title, value) in enumerate(metric_items):

```
column = metric_columns[index % 3]

with column:

    st.markdown(
        f"""
        <div class='metric-card'>

            <div class='metric-title'>
                {title}
            </div>

            <div class='metric-value'>
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
```

# -----------------------------------

# CHARTS

# -----------------------------------

st.markdown(
"<div class='section-title'>Recovery & Energy Trends</div>",
unsafe_allow_html=True
)

chart_column_1, chart_column_2 = st.columns(2)

trend_data = pd.DataFrame({
"Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
"Recovery": [61, 68, 72, 74, 81, 79, 84],
"Energy": [58, 64, 69, 71, 76, 74, 80]
})

with chart_column_1:

```
recovery_chart = px.line(
    trend_data,
    x="Day",
    y="Recovery",
    markers=True,
    title="Recovery Trend"
)

st.plotly_chart(
    recovery_chart,
    use_container_width=True
)
```

with chart_column_2:

```
energy_chart = px.line(
    trend_data,
    x="Day",
    y="Energy",
    markers=True,
    title="Energy Stability Trend"
)

st.plotly_chart(
    energy_chart,
    use_container_width=True
)
```

# -----------------------------------

# MAIN CONTENT

# -----------------------------------

left_column, right_column = st.columns([2, 1])

# LEFT SECTION

with left_column:

```
st.markdown(
    "<div class='section-title'>AI Recommendations</div>",
    unsafe_allow_html=True
)

for recommendation in recommendations:

    st.markdown(
        f"""
        <div class='recommendation-card'>

            <div class='recommendation-priority'>
                {recommendation['priority']}
            </div>

            <div class='recommendation-title'>
                {recommendation['title']}
            </div>

            <div class='recommendation-description'>
                {recommendation['description']}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
```

# RIGHT SECTION

with right_column:

```
st.markdown(
    "<div class='section-title'>AI Coaching</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='insight-box'>

    Your recovery profile suggests strong cognitive performance during the morning hours.

    <br><br>

    Today may be a good opportunity for:
    <ul>
        <li>Strategic planning</li>
        <li>High-focus work</li>
        <li>Complex decision-making</li>
    </ul>

    To maintain energy stability, consider keeping the afternoon lighter and avoiding excessive context switching.

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### Signals Used")

st.markdown("""
✅ Sleep Quality  
✅ Recovery Trend  
✅ Calendar Density  
✅ Behavioral Patterns  
✅ Focus History  
""")
```

# -----------------------------------

# EXPLAINABILITY + TIMELINE

# -----------------------------------

explainability_column, timeline_column = st.columns(2)

# EXPLAINABILITY

with explainability_column:

```
st.markdown(
    "<div class='section-title'>Why These Recommendations?</div>",
    unsafe_allow_html=True
)

for reason in reasoning:

    st.markdown(
        f"""
        <div class='reason-box'>
            • {reason}
        </div>
        """,
        unsafe_allow_html=True
    )
```

# TIMELINE

with timeline_column:

```
st.markdown(
    "<div class='section-title'>Intelligent Daily Timeline</div>",
    unsafe_allow_html=True
)

for item in timeline:

    st.markdown(
        f"""
        <div class='timeline-card'>

            <div class='timeline-time'>
                {item['time']}
            </div>

            <div class='timeline-title'>
                {item['title']}
            </div>

            <div class='timeline-energy'>
                {item['energy']}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
```

# -----------------------------------

# BEHAVIORAL ADAPTATION

# -----------------------------------

st.markdown(
"<div class='section-title'>Behavioral Adaptation Insights</div>",
unsafe_allow_html=True
)

adaptation_columns = st.columns(3)

adaptation_items = [
{
"title": "Peak Productivity Window",
"value": "9 AM - 1 PM"
},

```
{
    "title": "Preferred Work Pattern",
    "value": "Low Meeting Density"
},

{
    "title": "Energy Stability Trend",
    "value": "+12% This Week"
}
```

]

for index, item in enumerate(adaptation_items):

```
with adaptation_columns[index]:

    st.markdown(
        f"""
        <div class='metric-card'>

            <div class='metric-title'>
                {item['title']}
            </div>

            <div class='metric-value'>
                {item['value']}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
```

# -----------------------------------

# FOOTER

# -----------------------------------

st.divider()

st.caption(
"Concept visualization demonstrating AI-assisted scheduling, explainable recommendation systems, wearable-driven behavioral intelligence, and adaptive performance optimization."
)
