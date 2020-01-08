import subprocess
import os


class RepoManager:
    """
    Handles repo update.
    """
    def __init__(self, repo_url, dest_dir, proxy=None):
        self.repo_url = repo_url
        self.dest_dir = dest_dir
        self.proxy = proxy

    def clone_repo(self):
        args = 'git clone {} {}'.format(self.repo_url, self.dest_dir).split()
        subprocess.run(args, env=os.environ.update({'https_proxy': self.proxy}))

    def pull_repo(self):
        os.chdir(self.dest_dir)
        subprocess.run('git pull'.split())


if __name__ == '__main__':
    dress_repo_url = "https://github.com/komeiji-satori/Dress.git"
    mgr = RepoManager(dress_repo_url, r'D:\projects\tmp', '127.0.0.1:8080')
    mgr.clone_repo()