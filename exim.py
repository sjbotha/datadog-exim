# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from new versions of the Agent...
    from datadog_checks.base import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version < 6.6.0
    from checks import AgentCheck

from datadog_checks.base.utils.subprocess_output import get_subprocess_output

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

class eximCheck(AgentCheck):
    def check(self, instance):
        files, err, retcode = get_subprocess_output(["exim", "-bpc"], self.log, raise_on_empty_output=True)
        queue_count = int(files.strip())
        self.gauge('exim.queued.messages.count', queue_count, tags=['TAG_KEY:TAG_VALUE'])
