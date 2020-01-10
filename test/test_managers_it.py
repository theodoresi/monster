import pytest
import os
from monster.managers import RepoManager, PhotoManager


@pytest.fixture(scope='module')
def repo_manager(tmp_path_factory):
    dress_repo_url = "https://github.com/komeiji-satori/Dress.git"
    tmp_repo_path = tmp_path_factory.mktemp('tmp_repo')
    # Actually should check the proxy is available
    return RepoManager(dress_repo_url, tmp_repo_path, '127.0.0.1:8080')


@pytest.fixture(scope='module')
def photo_manager():
    repo_root = '/home/drizzlex/projects/dress'
    return PhotoManager(repo_root)


class TestRepoManager:
    def test_clone_repo_successful(self, repo_manager):
        assert len(os.listdir(repo_manager.dest_dir)) == 0
        repo_manager.clone_repo()
        assert len(os.listdir(repo_manager.dest_dir)) > 10

    def test_pull_repo_successful(self, repo_manager):
        repo_manager.pull_repo()
        assert True


class TestPhotoManager:
    def test_photo_path_in_repo(self, photo_manager):
        photo_path = photo_manager.photo_path_in_repo()
        assert 0 < len(photo_path)
        print('Total photo:', len(photo_path))

