import os

import sqlalchemy


def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a TCP connection pool for a Cloud SQL instance of MySQL."""
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_host = "cartcompanion:us-central1:cartcompanion-db" # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    db_user = "shrutika"  # e.g. 'my-db-user'
    db_pass = "shrutika"  # e.g. 'my-db-password'
    db_name = "cartcompanion"  # e.g. 'my-database'
    db_port = "3306"  # e.g. 3306

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        ),
        # ...
    )
    return pool

print(connect_tcp_socket())