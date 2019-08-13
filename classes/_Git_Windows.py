import shlex
import subprocess as sp
import platform

if 'windows' not in platform.platform().lower():
    raise NotImplementedError("Use the `sh` module's `git` from PyPI instead!")


GitError = sp.CalledProcessError


def _call_process(execcmd, _ok_code=None, return_data=False):
    execcmd = ('git',) + execcmd
    print('execcmd:', execcmd)
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
        if len(args) > 0:
            _call_process(args)

    # git
    @staticmethod
    def __call__(*args):
        _call_process(args)

    # add
    @staticmethod
    def add(*args):
        args = ('add',) + args
        _call_process(args)

    # branch
    @staticmethod
    def branch(*args):
        args = ('branch',) + args
        _call_process(args)

    # Checkout
    @staticmethod
    def checkout(*args):
        args = ('checkout',) + args
        _call_process(args)

    # commit
    @staticmethod
    def commit(*args):
        args = ('commit',) + args
        _call_process(args)

    # Config
    @staticmethod
    def config(*args, _ok_code=None):
        args = ('config',) + args
        _call_process(args, _ok_code=_ok_code)

    # merge
    @staticmethod
    def merge(*args):
        args = ('merge',) + args
        _call_process(args)

    # fetch
    @staticmethod
    def fetch(*args):
        args = ('fetch',) + args
        _call_process(args)

    # pull
    @staticmethod
    def pull(*args):
        args = ('pull',) + args
        _call_process(args)

    # push
    @staticmethod
    def push(*args):
        args = ('push',) + args
        _call_process(args)

    # remote.update
    class remote:  # noqa: N801
        @staticmethod
        def update(*args):
            args = ('update',) + args
            args = ('remote',) + args
            _call_process(args)

    # reset
    @staticmethod
    def reset(*args):
        args = ('reset',) + args
        _call_process(args)

    # rev-parse
    @staticmethod
    def rev_parse(*args):
        args = ('rev-parse',) + args
        return _call_process(args, return_data=True)[0].decode('UTF-8')

    # status
    @staticmethod
    def status(*args):
        args = ('status',) + args
        return _call_process(args, return_data=True)[0].decode('UTF-8')

    # status with colours stripped
    @staticmethod
    def status_stripped(*args):
        args = ('-c', 'color.status=false', 'status',) + args
        return _call_process(args, return_data=True)[0].decode('UTF-8')

    # diff
    @staticmethod
    def diff(*args):
        args = ('diff',) + args
        return _call_process(args, return_data=True)[0].decode('UTF-8')

    # diff with colours stripped, filenames only
    @staticmethod
    def diff_filenames(*args):
        args = ('-c', 'color.diff=false', 'diff', '--name-only',) + args
        return _call_process(args, return_data=True)[0].decode('UTF-8')
