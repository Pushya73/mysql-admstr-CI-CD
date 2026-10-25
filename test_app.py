
from unittest.mock import patch
import app


def test_get_db_connection_uses_environment_variables():
    with patch.dict("os.environ", {
        "DB_HOST": "db",
        "DB_PORT": "3306",
        "DB_USER": "testuser",
        "DB_PASSWORD": "testpass",
        "DB_NAME": "testdb"
    }):
        with patch("app.mysql.connector.connect") as mock_connect:
            app.get_db_connection()

            mock_connect.assert_called_once_with(
                host="db",
                port=3306,
                user="testuser",
                password="testpass",
                database="testdb"
            )
