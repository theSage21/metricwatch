import os
from subprocess import check_output
import matplotlib.pyplot as plt

ROOT = os.getcwd()
MON_PATH = os.path.join(ROOT, 'monitored')
FILE = '.performance_metrics'

projects = os.listdir(MON_PATH)

data = {}
print('READING Projects')
for project in projects:
    data[project] = {'commits': [], 'plots': {}}
    p_path = os.path.join(MON_PATH, project)
    print('reading data for', p_path)
    cmd = 'cd {} &&' + ' git log {file}| grep commit'.format(file=FILE)
    try:
        out = check_output(cmd.format(p_path), shell=True).decode().strip()
    except:
        print('     {} is not persent in project'.format(FILE))
        continue
    else:
        # Get actual data points
        commits = [i.strip().split(' ')[1] for i in out.split('\n')]
        data[project]['commits'] = commits
        cmd = 'cd {} && git show {}:' + '{file}'.format(file=FILE)
        for index, com in enumerate(commits):
            print('     Commit', com)
            c = cmd.format(p_path, com)
            out = check_output(c, shell=True).decode().strip()
            lines = out.split('\n')
            for line in lines:
                key, val = line.strip().split(':')
                key = key.strip()
                val = float(val.strip())
                if key in data[project].keys():
                    data[project]['plots'][key]['com'].append(index)
                    data[project]['plots'][key]['val'].append(val)
                else:
                    data[project]['plots'][key] = {'com': [index],
                                                   'val': [val]}
# ------------------------plotting
n_projects = len(data)
if n_projects > 0:
    plt.subplots(figsize=(10, n_projects*5))
    for index, (project, com_and_plots) in enumerate(data.items()):
        plt.subplot(n_projects, 1, index+1)
        com = com_and_plots['commits']
        plots = com_and_plots['plots']
        for key, points in plots.items():
            x = list(range(len(com)))
            y = [(v if i in x else None)
                 for i, v in zip(points['com'], points['val'])]
            plt.plot(x, y, 'o', label=key)
        plt.title(project)
    labels = [str(c) for c in com]
    plt.gca().set_xticklabels(labels, rotation=90)
    plt.legend()
    plt.savefig('graph.svg')
