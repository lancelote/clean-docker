from clean_docker.cli import cli
from clean_docker.main import DAEMON_CONNECTION_FAILURE


def test_missing_docker_daemon(mock_missing_docker, cli_runner):
    result = cli_runner.invoke(cli, input="y\n")
    assert result.exit_code == 1
    assert DAEMON_CONNECTION_FAILURE in result.output
