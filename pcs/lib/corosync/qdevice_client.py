import os.path

from pcs import settings
from pcs.common import reports
from pcs.common.reports.item import ReportItem
from pcs.common.str_tools import join_multilines
from pcs.lib.errors import LibraryError


def get_status_text(runner, verbose=False):
    """
    Get quorum device client runtime status in plain text
    bool verbose get more detailed output
    """
    cmd = [
        os.path.join(
            settings.corosync_qdevice_binaries, "corosync-qdevice-tool"
        ),
        "-s",
    ]
    if verbose:
        cmd.append("-v")
    stdout, stderr, retval = runner.run(cmd)
    if retval != 0:
        raise LibraryError(
            ReportItem.error(
                reports.messages.CorosyncQuorumGetStatusError(
                    join_multilines([stderr, stdout])
                )
            )
        )
    return stdout
