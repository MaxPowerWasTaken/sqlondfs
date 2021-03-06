import pandas as pd
import sql_on_dfs


def test_small_left_join_inmemory():
    df_ab = pd.DataFrame({"a": [1,2,3], "b": [2,2,2]})
    df_ac = pd.DataFrame({"a": [1,2,3], "c": [3,3,3]})
    df_abc = pd.DataFrame({"a": [1,2,3], "b": [2,2,2], "c": [3,3,3]})

    q = "select ab.*, ac.c from df_ab ab left join df_ac ac on ab.a = ac.a"
    assert sql_on_dfs.execute(q, inmemory=True).equals(df_abc)  # Passes


def test_small_left_join_ondisk():
    df_ab = pd.DataFrame({"a": [1,2,3], "b": [2,2,2]})
    df_ac = pd.DataFrame({"a": [1,2,3], "c": [3,3,3]})
    df_abc = pd.DataFrame({"a": [1,2,3], "b": [2,2,2], "c": [3,3,3]})

    q = "select ab.*, ac.c from df_ab ab left join df_ac ac on ab.a = ac.a"
    assert sql_on_dfs.execute(q, inmemory=False, debug=True).equals(df_abc)  # Passes