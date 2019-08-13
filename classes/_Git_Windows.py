import shlex
import subprocess as sp
import platform

if 'windows' not in platform.platform().lower():
    raise NotImplementedError("Use the `sh` module's `git` from PyPI instead!")


GitError = sp.CalledProcessError


def _call_process(execcmd, _ok_code=None, return_data=False):
    execcmd.insert(0, 'git')
    print('execcmd:', execcmd);
    proc = sp.Popen(execcmd, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    (stdout, stderr) = proc.communicate()
    retcode = proc.returncode
    if retcode != 0:
        if _ok_code and retcode in _ok_code:
            pass
        else:
            raise GitError(retcode, execcmd, stdout, stderr)

    if return_data:
        return stdout, stderr, retcode


class Git:
    # git
    def __init__(self, *args):
        if args.length > 0:
            _call_process(args)

    # git
    @staticmethod
    def __call__(*args):
        _call_process(args)

    # add
    @staticmethod
    def add(*args):
        args.insert(0, 'add')
        _call_process(execcmd)

    # branch
    @staticmethod
    def branch(*args):
        args.insert(0, 'branch')
        _call_process(execcmd)

    # Checkout
    @staticmethod
    def checkout(*args):
        args.insert(0, 'checkout')
        _call_process(execcmd)

    # commit
    @staticmethod
    def commit(*args):
        args.insert(0, 'commit')
        _call_process(execcmd)

    # Config
    @staticmethod
    def config(*args, _ok_code=None):
        args.insert(0, 'config')
        _call_process(execcmd, _ok_code=_ok_code)

    # merge
    @staticmethod
    def merge(*args):
        args.insert(0, 'merge')
        _call_process(execcmd)

    # fetch
    @staticmethod
    def fetch(*args):
        args.insert(0, 'fetch')
        _call_process(execcmd)

    # pull
    @staticmethod
    def pull(*args):
        args.insert(0, 'pull')
        _call_process(execcmd)

    # push
    @staticmethod
    def push(*args):
        args.insert(0, 'push')
        _call_process(execcmd)

    # remote.update
    class remote:  # noqa: N801
        @staticmethod
        def update(*args):
            args.insert(0, 'update')
            args.insert(0, 'remote')
            _call_process(execcmd)

    # reset
    @staticmethod
    def reset(*args):
        args.insert(0, 'reset')
        _call_process(execcmd)

    # rev-parse
    @staticmethod
    def rev_parse(*args):
        args.insert(0, 'rev-parse')
        return _call_process(execcmd, return_data=True)[0].decode('UTF-8')

    # status
    @staticmethod
    def status(*args):
        args.insert(0, 'status')
        return _call_process(execcmd, return_data=True)[0].decode('UTF-8')

    # status with colours stripped
    @staticmethod
    def status_stripped(*args):
        args.insert(0, 'status')
        args.insert(0, 'color.status=false')
        args.insert(0, '-c')
        return _call_process(execcmd, return_data=True)[0].decode('UTF-8')

    # diff
    @staticmethod
    def diff(*args):
        args.insert(0, 'diff')
        return _call_process(execcmd, return_data=True)[0].decode('UTF-8')

    # diff with colours stripped, filenames only
    @staticmethod
    def diff_filenames(*args):
        args.insert(0, '--name-only')
        args.insert(0, 'diff')
        args.insert(0, 'color.diff=false')
        args.insert(0, '-c')
        return _call_process(execcmd, return_data=True)[0].decode('UTF-8')
