import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def create_parquet_file(file_name):
    # name needs to take the form filename.parquet

    df = pd.DataFrame({
        'one': [-1, np.nan, 2.5],
        'two': ['foo', 'bar', 'baz'],
        'three': [True, False, True]},
        index=list('abc')
    )

    table = pa.Table.from_pandas(df)

    pq.write_table(table, file_name)

    table2 = pq.read_table(file_name)
    table2.to_pandas()
