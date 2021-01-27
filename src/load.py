"""Loads data from memory into Postgres.

Author: Adam Turner <turner.adch@gmail.com>
Notes: Python 3.8, UTF-8, tab is 4 spaces
"""

# standard library
import io
import json
# python package index
import psycopg2


class DBConfig(object):

    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port 
        self.name = name
        self.user = user 
        self.password = password

    @classmethod
    def from_json(cls, cfg_path="/home/adam/cfg/postgres-test.json"):
        with open(cfg_path, "r") as f:
            cfg = json.load(f)
        return cls(host=cfg["db_host"], port=cfg["db_port"], name=cfg["db_name"], user=cfg["db_user"], password=cfg["db_password"])

    def create_psycopg2_connection(self):
        return psycopg2.connect(host=self.host, port=self.port, database=self.name, user=self.user, password=self.password)


def copy_into_postgres(df, conn, fname):
    """Loads data into Postgres.

    Args:
        df: pandas DataFrame with the extracted data
        conn: active psycopg2 connection object
        fname: str name of the original file
    """
    print(f"`{fname}`: Loading data...")

    null_cols = [
        "col_a", "col_b", "col_c", "col_d", "col_e", "col_f", "col_g", "col_h", "col_i", "col_j", "col_k", "col_l", "col_m", 
        "col_n", "col_o", "col_p", "col_q", "col_r", "col_s", "col_t", "col_u", "col_v", "col_w", "col_x", "col_y", "col_z",
    ]
    parsed_cols = ["file_index", "file_name"] + null_cols[:df.shape[1]]
    insert_cols = ", ".join(parsed_cols)

    df.insert(loc=0, column="file_name", value=fname)

    with conn.cursor() as curs:
        with io.StringIO() as csv_buffer:
            df.to_csv(csv_buffer, sep=",", header=False, index=True)
            csv_buffer.seek(0)
            curs.copy_expert(f"COPY extract_loader_landing_zone ({insert_cols}) FROM STDIN (FORMAT csv, DELIMITER ',', HEADER FALSE);", file=csv_buffer)
    conn.commit()

    print(f"`{fname}`: Loaded data!")

    return None
