"""A set of general tools to auxiliate in the simulations."""

import pandas as pd
import altair as alt


def get_dataframe(rv_list, column_name):
    """Transform a list of random variables into a dataframe."""
    rv_df = pd.DataFrame(rv_list, columns=column_name)
    rv_df["index"] = rv_df.index
    return rv_df


# def get_dataframe_list()


def plot_histogram(rv_list, chart_name, save=True, color_theme="#4c78a8"):
    """Plot a r.v. histogram."""
    rv_df = get_dataframe(rv_list, [f"{chart_name}_rv"])

    df_chart = (
        alt.Chart(rv_df, title=chart_name)
        .mark_bar()
        .encode(
            alt.X(
                f"{chart_name}_rv",
                bin=alt.Bin(
                    extent=[round(rv_list.min()), round(rv_list.max())],
                ),
                title="values",
            ),
            alt.Y("count()", title="frequency"),
            color=alt.ColorValue(color_theme),
        )
        #
        # .configure_axis(titleFontSize=20, labelFontSize=20)
        # .configure_title(fontSize=20)
    )

    if save:
        df_chart.save(f"{chart_name}.html")
    else:
        return df_chart


def plot_histogram_nparams(rv_list, param_list, chart_name):
    """Plot a r.v. histograms with different parameters."""
    # df_list = []

    list_colors = [
        "#4c78a8",
        "#f58518",
        "#e45756",
        "#72b7b2",
        "#54a24b",
        "#eeca3b",
        "#b279a2",
        "#ff9da6",
        "#9d755d",
        "#bab0ac",
    ]
    string_list = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    for param in param_list:

        string_parameters = ""
        for p in range(len(param)):
            string_parameters += "_" + letters[p] + "=" + str(param[p]) + "_"
            print(string_parameters)
        string_list.append(string_parameters)

    # for i, rv in enumerate(rv_list):
    #     df_list.append(get_dataframe(rv, [f"{chart_name}_rv (a = {param_list[i]})"]))

    chart_list = []
    for i, df_rv in enumerate(rv_list):
        print(f"{string_list[i]}")
        print(type(string_list[i]))
        chart_list.append(
            plot_histogram(
                df_rv,
                f"{string_list[i]}",
                save=False,
                color_theme=list_colors[i],
            )
        )

    # return chart_list
    chart_total = chart_list[0]
    for chart_in_list in chart_list[1:]:
        chart_total = chart_total | chart_in_list

    chart_total.save(f"{chart_name}_" + chart_name + ".html")
