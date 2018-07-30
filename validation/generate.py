import os
import sys

import shakecast
import workbook

if __name__ == '__main__':
    pp_fig, capacity_fig, acc_diff_fig, disp_diff_fig = workbook.run()
    pp_fig2, impact_fig = shakecast.run()

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'

    if not os.path.exists(path):
        os.makedirs(path)

    # save workbook validation figures
    pp_fig.savefig(os.path.join(path, 'perf_point1'))
    capacity_fig.savefig(os.path.join(path, 'capcity_comp'))
    acc_diff_fig.savefig(os.path.join(path, 'acc_diff'))
    disp_diff_fig.savefig(os.path.join(path, 'disp_diff'))

    # save shakecast figures
    pp_fig.savefig(os.path.join(path, 'perf_point2'))
    impact_fig.savefig(os.path.join(path, 'impact_fig'))