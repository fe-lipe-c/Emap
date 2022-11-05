"""A set of general tools to auxiliate in the simulations."""

import pandas as pd
import altair as alt


def get_dataframe(rv_list, column_name):
    """Transform a list of random variables into a dataframe."""
    rv_df = pd.DataFrame(rv_list, columns=column_name)
    rv_df["index"] = rv_df.index
    return rv_df


# def get_dataframe_list()


def plot_density(
    rv_list,
    chart_name,
    save=True,
    color_theme="#4c78a8",
    supp_min=0,
    supp_max=0,
    step=0.5,
):
    """Plot a r.v. density."""
    rv_df = get_dataframe(rv_list, [f"{chart_name}_rv"])
    if supp_min == 0:
        supp_min = rv_list.min()
    else:
        pass
    if supp_max == 0:
        supp_max = rv_list.max()
    else:
        pass

    df_chart = (
        alt.Chart(rv_df, title=chart_name)
        .transform_density(
            f"{chart_name}_rv",
            as_=[f"{chart_name}_rv", "density"],
        )
        .mark_bar()
        .encode(
            alt.X(
                f"{chart_name}_rv",
                bin=alt.Bin(
                    extent=[round(supp_min), round(supp_max)],
                    step=step,
                ),
                title="values",
            ),
            alt.Y(
                "density:Q",
                title=None,
                # axis=None,
            ),  # scale=alt.Scale(domain=[0, 1])),
            color=alt.ColorValue(color_theme),
        )
    )

    if save:
        df_chart.save(f"{chart_name}.html")
    else:
        return df_chart


def plot_density_nparams(rv_list, param_list, chart_name, step=0.5):
    """Plot a r.v. density with different parameters."""

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
        string_list.append(string_parameters)

    supp_min = 0
    supp_max = 0
    for df_rv in rv_list:

        supp_min = min(min(df_rv), supp_min)
        supp_max = max(max(df_rv), supp_max)

    chart_list = []
    for i, df_rv in enumerate(rv_list):
        chart_list.append(
            plot_density(
                df_rv,
                f"{string_list[i]}",
                save=False,
                color_theme=list_colors[i],
                supp_min=supp_min,
                supp_max=supp_max,
                step=step,
            )
        )

    # return chart_list
    chart_total = []
    for char_nr in range(round(len(chart_list) / 3)):
        chart_total.append(chart_list[char_nr * 3])

    for j, chart_in_list in enumerate(chart_list):
        if j <= 2 and j > 0:
            chart_total[0] = alt.hconcat(chart_total[0], chart_in_list).resolve_scale(
                y="shared"
            )
        elif j > 3 and j <= 5:
            chart_total[1] = alt.hconcat(chart_total[1], chart_in_list).resolve_scale(
                y="shared"
            )
        elif j > 6 and j <= 8:
            chart_total[2] = alt.hconcat(chart_total[2], chart_in_list).resolve_scale(
                y="shared"
            )
        else:
            pass

    char_final = chart_total[0]
    for char_f in chart_total[1:]:
        char_final = alt.vconcat(char_final, char_f).resolve_scale(y="shared")

    char_final.save(f"{chart_name}_" + chart_name + ".html")
