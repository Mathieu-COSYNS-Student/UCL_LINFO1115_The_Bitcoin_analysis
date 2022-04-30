from helper_file import Graph, count_triangles, plot


def total_triadic_closures(dataframe):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: Returns the total amount of triadic closures that arrise between the median timestamp of the dataframe until the last timestamp.
    Reminder: The triadic closures do not take into account the sign of the edges.
    """

    df = dataframe

    median = df['Timestamp'].median(axis=0)
    graph, df_included, df_excluded = Graph.create(
        df, task=2, on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)

    nt = 0
    new_triangles_over_time = [nt]
    time = [median]

    for _, row in df_excluded.iterrows():
        t0, _, _ = count_triangles(
            graph, edge=(row['Source'], row['Target']))
        graph.add_edge(row['Source'],
                       row['Target'],
                       meta={'weight': row['Weight']},
                       on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)
        t1, _, _ = count_triangles(
            graph, edge=(row['Source'], row['Target']))
        nt += t1 - t0
        new_triangles_over_time.append(nt)
        time.append(row['Timestamp'])

    plot(new_triangles_over_time, time, "Graph of accumulated triadic closure over time,\nstarting at the median timestamp until the end",
         "Timestamp", "Accumulated triadic closure", png="images/accumulated_triadic_closure.png", graphics=False)

    return nt
