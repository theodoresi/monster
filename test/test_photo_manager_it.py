import pytest
from monster import photo_manager


@pytest.fixture
def repo_manager(tmp_path):
    dress_repo_url = "https://github.com/komeiji-satori/Dress.git"
    return photo_manager.RepoManager(dress_repo_url, tmp_path, '127.0.0.1:8080')


class TestRepoManager:
    def test_clone_repo_successful(self, repo_manager):
        repo_manager.clone_repo()

