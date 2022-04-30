from helper_file import Graph, count_triangles, plot


def end_balanced_degree(dataframe):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: Returns the final balance degree of the graph (as defined in the project statement).
    Reminder: Take into account that the graph is weighted now.
    """

    df = dataframe

    median = df['Timestamp'].median(axis=0)
    graph, df_included, df_excluded = Graph.create(
        df, task=3, on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)

    t, bt, wbt = count_triangles(graph)
    balance_degree = (bt + (2/3 * wbt)) / t

    balance_degree_over_time = [balance_degree]
    time = [median]

    for _, row in df_excluded.iterrows():
        t0, bt0, wbt0 = count_triangles(
            graph, edge=(row['Source'], row['Target']))
        graph.add_edge(row['Source'],
                       row['Target'],
                       meta={'weight': row['Weight']},
                       on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)
        t1, bt1, wbt1 = count_triangles(
            graph, edge=(row['Source'], row['Target']))
        t += t1 - t0
        bt += bt1 - bt0
        wbt += wbt1 - wbt0
        balance_degree = (bt + (2/3 * wbt)) / t
        balance_degree_over_time.append(balance_degree)
        time.append(row['Timestamp'])

    t, bt, wbt = count_triangles(graph)
    balance_degree = (bt + (2/3 * wbt)) / t

    plot(balance_degree_over_time, time, "Graph of the balance degree over time,\nstarting at the median timestamp until the end",
         "Timestamp", "Balance degree", png="images/balance_degree_over_time.png", graphics=False)

    return balance_degree
