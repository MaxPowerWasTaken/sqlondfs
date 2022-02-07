SQL On DFs - Easily execute an arbitrary SQL query on Pandas DataFrames

Publishing this to PyPI to keep [this Stack Overflow answer](https://stackoverflow.com/a/70994925/1870832) handy for the future, and because I have some improvements planned. Namely:
- [ ] more comprehensive testing
- [x] optional :in-memory: sqlite execution
- [x] debug mode
- [ ] optional [duckdb](https://duckdb.org/docs/api/python)
- [ ] since duckdb uses vectorized operations to target high-performance on OLAP queries, default behavior should probably use `duckdb` for OLAP queries (e.g. anything with a `group by`), and `sqlite` for other (transactional) queries.

Useage Example:
Given a couple dataframes like:
```
df_ab = pd.DataFrame({"a": [1,2,3], "b": [2,2,2]})
df_ac = pd.DataFrame({"a": [1,2,3], "c": [3,3,3]})
```
... you can execute a SQL query joining them with:

```
q = "select ab.*, ac.c from df_ab ab left join df_ac ac on ab.a = ac.a"
result = sql_on_dfs.execute(q)
```

test:
```
assert result.equals(pd.DataFrame({"a": [1,2,3], "b": [2,2,2], "c": [3,3,3]})) # passes
```

