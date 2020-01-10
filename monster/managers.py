import subprocess
import os
import shlex
import logging
from monster.models import Photo

logging.basicConfig()
logger = logging.getLogger(__name__)


class RepoManager:
    """
    RepoManager handles repo clone/pull
    """
    def __init__(self, repo_url, dest_dir, proxy=None):
        self.repo_url = repo_url
        self.dest_dir = dest_dir
        self.proxy = proxy
        if self.proxy is not None:
            os.environ.update({
                'https_proxy': self.proxy,
                'http_proxy': self.proxy
            })

    def clone_repo(self):
        cmd = 'git clone {} {}'.format(self.repo_url, self.dest_dir)
        logger.info('Running: {} [proxy: {}]'.format(cmd, self.proxy))
        subprocess.run(shlex.split(cmd))

    def pull_repo(self):
        cmd = 'git pull'
        logger.info('Running: {} [proxy: {}]'.format(cmd, self.proxy))
        subprocess.run(shlex.split(cmd), cwd=self.dest_dir)


class PhotoManager:
    PHOTO_EXTENSIONS = ['.jpg', '.png']

    def __init__(self, repo_root):
        self.repo_root = repo_root

    def photo_path_in_repo(self):
        photo_path = []
        for root, dirs, files in os.walk(self.repo_root):
            # Skip hidden directories, e.g. .git, .pytest_cache
            dirs[:] = [each for each in dirs if not each.startswith('.')]
            photo_path.extend([os.path.join(root, f) for f in files
                               if os.path.splitext(f)[-1].lower() in PhotoManager.PHOTO_EXTENSIONS])
        return photo_path
