import streamlit as st
import pandas as pd
import altair as alt


def calculator():
    st.title("Baseball Statistical Calculator")
    st.markdown("")
    st.subheader("Noah Michel :softball:")
    st.markdown("")

    plateAppearances1 = 7
    plateAppearances2 = 6
    totalPlateAppearances = plateAppearances1 + plateAppearances2

    atBats1 = 7
    atBats2 = 6
    totalABs = atBats1 + atBats2

    hits1 = 3
    hits2 = 4
    totalHits = hits1 + hits2

    singles1 = 3
    singles2 = 3
    totalSingles = singles1 + singles2

    doubles1 = 0
    doubles2 = 1
    totalDoubles = doubles1 + doubles2

    triples1 = 0
    triples2 = 0
    totalTriples = triples1 + triples2

    homeruns1 = 0
    homeruns2 = 0
    totalHomeruns = homeruns1 + homeruns2

    walks1 = 0
    walks2 = 0
    totalWalks = walks1 + walks2

    strikeouts1 = 0
    strikeouts2 = 0
    totalStrikeouts = 0

    totalBases1 = (singles1 + (doubles1 * 2) + (triples1 * 3) + (homeruns1 * 4))
    totalBases2 = (singles2 + (doubles2 * 2) + (triples2 * 3) + (homeruns2 * 4))
    totalBasesTotal = totalBases1 + totalBases2

    battingAverage = totalHits / totalABs
    onBasePercentage = (totalHits + totalWalks) / (totalABs + totalWalks)
    slgPercentage = (totalSingles + (totalDoubles*2) + (totalTriples*3) + (totalHomeruns*4))/totalABs
    OPS = slgPercentage+onBasePercentage

    statsDict = {
        "PA":
            {
                "Series 1": plateAppearances1,
                "Series 2": plateAppearances2,
                "Full Season": totalPlateAppearances
            },
        "ABs":
            {
                "Series 1": atBats1,
                "Series 2": atBats2,
                "Full Season": totalABs
            },
        "BB":
            {
                "Series 1": walks1,
                "Series 2": walks2,
                "Full Season": totalWalks
            },
        "Hits":
            {
                "Series 1": hits1,
                "Series 2": hits2,
                "Full Season": totalHits
            },
        "Doubles":
            {
                "Series 1": doubles1,
                "Series 2": doubles2,
                "Full Season": totalDoubles
            },
        "Triples":
            {
                "Series 1": triples1,
                "Series 2": triples2,
                "Full Season": totalTriples
            },
        "HRs":
            {
                "Series 1": homeruns1,
                "Series 2": homeruns2,
                "Full Season": totalHomeruns
            },
        "SOs":
            {
                "Series 1": strikeouts1,
                "Series 2": strikeouts2,
                "Full Season": totalStrikeouts
            },
        "TBs":
            {
                "Series 1": totalBases1,
                "Series 2": totalBases2,
                "Full Season": totalBasesTotal
            }
    }

    df = pd.DataFrame(statsDict, columns=["PA", "ABs", "BB", "Hits", "Doubles",
                                          "Triples", "HRs", "SOs", "TBs"])
    st.dataframe(df)

    st.markdown(":orange[Batting Average:] " + str(battingAverage.__round__(3)))
    chart_data = pd.DataFrame({"AVG": battingAverage}, index=["AVG"])
    data = pd.melt(chart_data.reset_index(), id_vars=["index"])
    chart = (
        alt.Chart(data)
        .mark_bar(size=25)
        .encode(
            x=alt.X("value", axis=alt.Axis(title='', tickCount=3), scale=alt.Scale(domain=[0.000, 1.000])),
            y=alt.Y("index", axis=alt.Axis(title='', tickCount=3)),
            color=alt.Color("variable", legend=None)
        )
        .configure_axis(grid=False)
    )
    st.altair_chart(chart, use_container_width=True)

    st.markdown(":orange[On-base Percentage:] " + str(onBasePercentage.__round__(3)))
    chart_data = pd.DataFrame({"OBP": onBasePercentage}, index=["OBP"])
    data = pd.melt(chart_data.reset_index(), id_vars=["index"])
    chart = (
        alt.Chart(data)
        .mark_bar(size=25)
        .encode(
            x=alt.X("value", axis=alt.Axis(title='', tickCount=3), scale=alt.Scale(domain=[0.000, 1.000])),
            y=alt.Y("index", axis=alt.Axis(title='', tickCount=3)),
            color=alt.Color("variable", legend=None)
        )
        .configure_axis(grid=False)
    )
    st.altair_chart(chart, use_container_width=True)

    st.markdown(":orange[Slugging Percentage:] " + str(slgPercentage.__round__(3)))
    chart_data = pd.DataFrame({"SLG": slgPercentage}, index=["SLG"])
    data = pd.melt(chart_data.reset_index(), id_vars=["index"])
    chart = (
        alt.Chart(data)
        .mark_bar(size=25)
        .encode(
            x=alt.X("value", axis=alt.Axis(title='', tickCount=3), scale=alt.Scale(domain=[0.000, 1.000])),
            y=alt.Y("index", axis=alt.Axis(title='', tickCount=3)),
            color=alt.Color("variable", legend=None)
        )
        .configure_axis(grid=False)
    )
    st.altair_chart(chart, use_container_width=True)

    st.markdown(":orange[On-base Plus Slugging:] " + str(OPS.__round__(3)))
    chart_data = pd.DataFrame({"OPS": OPS}, index=["OPS"])
    data = pd.melt(chart_data.reset_index(), id_vars=["index"])
    chart = (
        alt.Chart(data)
        .mark_bar(size=25)
        .encode(
            x=alt.X("value", axis=alt.Axis(title='', tickCount=3), scale=alt.Scale(domain=[0.000, 2.000])),
            y=alt.Y("index", axis=alt.Axis(title='', tickCount=3)),
            color=alt.Color("variable", legend=None)
        )
        .configure_axis(grid=False)
    )
    st.altair_chart(chart, use_container_width=True)
