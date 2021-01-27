"""Entrypoint.

Author: Adam Turner <turner.adch@gmail.com>
Notes: Python 3.8, UTF-8, tab is 4 spaces
"""

# standard library
import multiprocessing as mp
import os
import pathlib
import sys
# local modules
import extract
import load


def pipeline(fpath):
    fname = fpath.split("/")[-1]
    ftype = fname.lower().split(".")[-1]
    print(f"`{fname}`: Start of pipeline.")

    if ftype == "pdf":
        df = extract.dataframe_from_pdf(fpath)
    elif ftype in ("xls", "xlsx", "xlsm"):
        df = extract.dataframe_from_xlsx(fpath)

    conn = load.DBConfig.from_json("/home/adam/cfg/postgres-test.json").create_psycopg2_connection()
    try:
        load.copy_into_postgres(df, conn, fname)
    finally:
        conn.close()
    print(f"`{fname}`: End of pipeline.")

    return None


if __name__ == "__main__":
    dir = sys.argv[1]

    fpaths = tuple(os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)))

    pipelines = tuple(mp.Process(target=pipeline, args=(fpath,)) for fpath in fpaths)

    for p in pipelines:
        p.start()

    for p in pipelines:
        p.join()
