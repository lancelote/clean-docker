import pytest
from click.testing import CliRunner
from docker.errors import DockerException


@pytest.fixture
def mock_docker(mocker):
    yield mocker.patch("clean_docker.main.docker")


@pytest.fixture
def mock_missing_docker(mock_docker):
    mock_docker.from_env.side_effect = DockerException("Connection aborted")


@pytest.fixture
def cli_runner():
    return CliRunner()
