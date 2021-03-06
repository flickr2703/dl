import core.timeline
import sys

class Log:
    DEBUG = False
    def __init__(self):
        self.reset()

    def reset(self):
        self.record = []
        self.damage = {'x':{},'s':{},'f':{},'d':{},'o':{}}
        self.counts = {'x':{},'s':{},'f':{},'d':{},'o':{}}
        self.damage_dataset = {}
        self.teambuff_dataset = {}
        self.p_buff = None
        self.team_buff = 0
        self.team_doublebuffs = 0
        self.team_tension = {}
        self.act_seq = []
        self.hitattr_set = set()
        self.shift_dmg = None

    def convert_dataset(self):
        return {
            'dmg': [{'x': t, 'y': d} for t, d in sorted(self.damage_dataset.items())],
            'team': [{'x': t, 'y': d} for t, d in sorted(self.teambuff_dataset.items())],
        }

    @staticmethod
    def update_dict(dict, name: str, value):
        # if fullname:
        try:
            dict[name] += value
        except KeyError:
            dict[name] = value

    @staticmethod
    def fmt_hitattr_v(v):
        if isinstance(v, list):
            return '['+','.join(map(str, v))+']'
        if isinstance(v, dict):
            return Log.fmt_hitattr(v)
        return str(v)

    @staticmethod
    def fmt_hitattr(attr):
        return '{'+'/'.join([f'{k}:{Log.fmt_hitattr_v(v)}' for k, v in attr.items()])+'}'

    def log_shift_dmg(self, enable):
        if enable:
            self.shift_dmg = 0
        else:
            self.shift_dmg = None

    def log_hitattr(self, name, attr):
        attr_str = Log.fmt_hitattr(attr)
        if (name, attr_str) in self.hitattr_set:
            return
        self.hitattr_set.add((name, attr_str))
        log('hitattr', name, attr_str)
        return attr_str

    def log(self, *args):
        time_now = core.timeline.now()
        n_rec = [time_now, *args]
        if len(args) >= 2:
            category = args[0]
            name = args[1]
            if category == 'dmg':
                dmg_amount = float(args[2])
                if name[0:2] == 'o_' and name[2] in self.damage:
                    name = name[2:]
                if name[0] in self.damage:
                    self.update_dict(self.damage[name[0]], name, dmg_amount)
                else:
                    if name[0] == '#':
                        name = name[1:]
                        n_rec[2] = name
                    self.update_dict(self.damage['o'], name, dmg_amount)
                if name[0] == 'd' and self.shift_dmg is not None:
                    self.shift_dmg += dmg_amount
                self.update_dict(self.damage_dataset, time_now, dmg_amount)
            elif category == 'x' or category == 'cast':
                self.update_dict(self.counts[name[0]], name, 1)
                # name1 = name.split('_')[0]
                # if name1 != name:
                #     self.update_dict(self.counts[name[0]], name1, 1)
                self.act_seq.append(name)
            elif category == 'buff' and name == 'team':
                buff_amount = float(args[2])
                if self.p_buff is not None:
                    pt, pb = self.p_buff
                    self.team_buff += (time_now - pt) * pb
                self.p_buff = (time_now, buff_amount)
                self.update_dict(self.teambuff_dataset, time_now, buff_amount)
            elif category == 'buff' and name == 'team_defense':
                self.team_doublebuffs += 1
            elif category in ('energy', 'inspiration') and name == 'team':
                self.update_dict(self.team_tension, category, float(args[2]))
        if self.DEBUG:
            self.write_log_entry(n_rec, sys.stdout, flush=True)
        self.record.append(n_rec)

    def filter_iter(self, log_filter):
        for entry in self.record:
            try:
                if entry[1] in log_filter:
                    yield entry
            except:
                continue

    def write_log_entry(self, entry, output, flush=False):
        time = entry[0]
        output.write('{:>8.3f}: '.format(time))
        for value in entry[1:]:
            if isinstance(value, float):
                output.write('{:<16.3f},'.format(value))
            else:
                output.write('{:<16},'.format(value))
        output.write('\n')
        if flush:
            output.flush()

    def write_logs(self, log_filter=None, output=None):
        if output is None:
            output = sys.stdout
        if log_filter is None:
            log_iter = self.record
        else:
            log_iter = self.filter_iter(log_filter)
        for entry in log_iter:
            self.write_log_entry(entry, output)

    def get_log_list(self):
        return self.record


loglevel = 0

g_logs = Log()
log = g_logs.log
logcat = g_logs.write_logs
logget = g_logs.get_log_list
logreset = g_logs.reset