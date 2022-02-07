Publishing this to PyPI to keep [this Stack Overflow answer](https://stackoverflow.com/a/70994925/1870832) handy for the future, and because I have some improvements planned. Namely:
* more comprehensive testing
* optional :in-memory: sqlite execution
* optional [duckdb](https://duckdb.org/docs/api/python)
* since duckdb uses vectorized operations to target high-performance on OLAP queries, default behavior should probably use `duckdb` for OLAP queries (e.g. anything with a `group by`), and `sqlite` for other (transactional) queries.