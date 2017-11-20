''' show_process.py

NXOS parsers for the following show commands:
    * 'show processes'
'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# ====================================================================
# Parser for 'show processes'
# ====================================================================
class ShowProcessesSchema(MetaParser):    
    '''Schema for show processes'''
    schema = {'process': {
                Any(): {
                    Optional('pid'): {
                        Any(): {
                            'pid': int,
                            'state': str,
                            Optional('pc'): str,
                            'start_cnt': int,
                            Optional('tty'): int,
                            'type': str,
                            'process': str
                        }
                    },
                    Optional('state'): str,
                    Optional('start_cnt'): int,
                    Optional('type'): str,
                    Optional('process'): str,
                },
            }
        }

class ShowProcesses(ShowProcessesSchema):
    '''Parser for show processes'''

    def cli(self, process=''):
        cmd = 'show processes' if not process else \
              'show processes | include {}'.format(process)
        out = self.device.execute(cmd)
        ret_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 1      S  b8dffed3            1     -     O  init
            # 10      S         0            1     -     O  ksoftirqd/1
            # -     NR         -            0     -     X  wwn
            p1 = re.compile(r'^((?P<pid>\d+)|\-)'
                             ' +(?P<state>\w+)'
                             ' +((?P<pc>\w+)|\-)'
                             ' +(?P<start_cnt>\d+)'
                             ' +((?P<tty>\d+)|\-)'
                             ' +(?P<type>\w+)'
                             ' +(?P<process>[\w\/\:\-\.]+)$')
            m = p1.match(line)
            if m:
                process = m.groupdict()['process']
                pid = m.groupdict()['pid']
                if 'process' not in ret_dict:
                    ret_dict['process'] = {}
                if process not in ret_dict['process']:
                    ret_dict['process'][process] = {}

                if pid:
                    pid = int(pid)
                    if 'pid' not in ret_dict['process'][process]:
                        ret_dict['process'][process]['pid'] = {}
                    if pid not in ret_dict['process'][process]['pid']:
                        ret_dict['process'][process]['pid'][pid] = {}
                    sub_dict = ret_dict['process'][process]['pid'][pid]
                    sub_dict['pid'] = pid
                else:
                    sub_dict = ret_dict['process'][process]

                sub_dict['process'] = process
                sub_dict['state'] = m.groupdict()['state']
                if m.groupdict()['pc']:
                    sub_dict['pc'] = m.groupdict()['pc']
                sub_dict['start_cnt'] = int(m.groupdict()['start_cnt'])
                if m.groupdict()['tty']:
                    sub_dict['tty'] = int(m.groupdict()['tty'])
                sub_dict['type'] = m.groupdict()['type']
                continue

        return ret_dict