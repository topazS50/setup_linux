import os
import pandas as pd
import itertools
import subprocess
import re
import glob


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


count_ = itertools.count()
MODE_EXIT = count_.next()
MODE_LIST = count_.next()
MODE_SELECT = count_.next()
MODE_ADD = count_.next()
MODE_DEL = count_.next()
MODE_TOP = count_.next()
MODE_BOTTOM = count_.next()
MODE_DOWN = count_.next()
MODE_DONE = count_.next()
MODE_PEND = count_.next()
MODE_EDIT = count_.next()
MODE_MOVE = count_.next()
MODE_VOID = count_.next()
DONE = count_.next()
DEL = count_.next()

BARS = '---------'
MAX_PRINT = 10
EDITOR = 'nano'

ROOTDIR = os.path.join(os.path.expanduser('~'), '.todo')
CSV = os.path.join(ROOTDIR, 'todo.csv')
CSV_BKP = os.path.join(ROOTDIR, 'todo.csv~')
CSV_DONE = os.path.join(ROOTDIR, 'done.csv')
CSV_PEND = os.path.join(ROOTDIR, 'pend.csv')


def fill_empty_cells(df):
    slice_ = df['status'].isnull()
    df.loc[slice_, 'status'] = 0
    slice_ = df['time_added'].isnull()
    df.loc[slice_, 'time_added'] = df.loc[slice_, 'time_updated']
    slice_ = df['importance'].isnull()
    df.loc[slice_, 'importance'] = 0
    return df


def display_list(df):
    mode = MODE_SELECT
    arg_ = ''
    df = fill_empty_cells(df)
    df['status'] = df['status'].apply(int)
    df = df[df['status'] == 0]
    df['importance'] = df['importance'].apply(int)
    df = df.sort_values(by='task', ascending=False)
    df = df.sort_values(by='time_added', ascending=False)
    df = df.sort_values(by=['importance', 'time_updated'], ascending=False)
    df = df.reset_index(drop=True)
    os.system('clear')
    print BARS
    counter_ = 0
    for id_, row in df[['task', 'time_added', 'time_updated', 'importance', 'status']].iterrows():
        if id_ == 0:
            print bcolors.OKGREEN + str(id_) + ' ' + str(row[0]) + ' ' + str(row[1][4:8]) + ' ' + str(row[2][4:8]) + ' ' + str(row[3]) + ' ' + str(row[4]) + bcolors.ENDC
        else:
            print id_, row[0], row[1][4:8], row[2][4:8], row[3], row[4]
        if counter_ == MAX_PRINT:
            print BARS + '   ',
            mode, arg_ = select_mode()
            if mode != MODE_VOID:
                break
            counter_ = 0
        else:
            print BARS
        counter_ += 1
    return df, mode, arg_


def now_():
    return pd.datetime.now().strftime("%Y%m%d.%H%M.%S.%f")


def add_item(df, input_, importance_=0):
    df = df.append(pd.DataFrame([[input_, now_(), now_(), importance_]], columns=['task', 'time_added', 'time_updated', 'importance']), ignore_index=True)
    return df


def save_csv(i, df):
    basename = str(df.iloc[i]['time_added']) + '-' + str(df.iloc[i]['task']).replace('/', '_') + '.csv'
    df[i:i+1].to_csv(os.path.join(ROOTDIR, 'todo', basename), sep='\t', index=False)


def select_mode():
    input_ = raw_input('(a)add, (at)add top, (l)list, (d)delete, (t)top, (dw)down, (done), (e)exit :')
    arg_ = input_.split(' ')
    input_ = arg_[0]
    if input_ == 'a':
        mode = MODE_ADD
    elif input_ == 'l':
        mode = MODE_LIST
    elif input_ in ['']:
        mode = MODE_VOID
    elif input_ in ['e']:
        mode = MODE_EXIT
    elif input_ == 'd':
        mode = MODE_DEL
    elif input_ == 't':
        mode = MODE_TOP
    elif input_ == 'b':
        mode = MODE_BOTTOM
    elif input_ == 'dw':
        mode = MODE_DOWN
    elif input_ == 'done':
        mode = MODE_DONE
    elif input_ == 'pend':
        mode = MODE_PEND
    elif input_ == 'ed':
        mode = MODE_EDIT
    return mode, arg_


def main():
    mode_read = 1
    df = pd.DataFrame()
    try:
        if mode_read == 0:
            df = pd.read_csv(CSV, sep='\t', index_col=0)
        elif mode_read == 1:
            listdir_ = glob.glob(os.path.join(ROOTDIR, 'todo') + '/*.csv')
            for file_ in listdir_:
                df_in = pd.read_csv(file_, sep='\t')
                df = df.append(df_in)
            df = df.reset_index(drop=True)
    except:
        df = pd.DataFrame(columns=['task', 'status'])
    mode = MODE_LIST
    while mode != MODE_EXIT:
        if mode == MODE_LIST:
            df, mode, arg_ = display_list(df)
        elif mode == MODE_SELECT:
            mode, arg_ = select_mode()
        elif mode == MODE_ADD:
            input_ = raw_input('task: ')
            if input_ == '':
                mode = MODE_LIST
            else:
                if len(arg_) == 1:
                    importance = 0
                else:
                    importance = arg_[1]
                df = add_item(df, input_, importance)
                save_csv(len(df)-1, df)
        elif mode == MODE_DEL:
            id_delete = int(raw_input('id to delete: '))
            print str(df.loc[id_delete])
            input_ = raw_input('delete this?[y/N]: ')
            if input_ == 'y':
                df.loc[id_delete, 'status'] = DONE
                save_csv(id_delete, df)
                mode = MODE_LIST
                df = df.drop([id_delete])
                df = df.reset_index(drop=True)
            mode = MODE_LIST
        elif mode == MODE_TOP:
            i = int(raw_input('id to bring top: '))
            df.loc[i, 'time_updated'] = now_()
            save_csv(i, df)
            df.to_csv(CSV, sep='\t')
            mode = MODE_LIST
        elif mode == MODE_DONE:
            id_ = int(raw_input('id done: '))
            df.loc[id_, 'status'] = DONE
            save_csv(id_, df)
            mode = MODE_LIST
        elif mode == MODE_PEND:
            id_ = int(raw_input('id done: '))
            with open(CSV_PEND, 'a') as fa:
                df.loc[id_:id_].to_csv(fa, header=False)
            df = df.drop([id_])
            df = df.reset_index(drop=True)
            mode = MODE_LIST
        elif mode == MODE_EDIT:
            id_ = int(raw_input('id edit: '))
            fileedit = re.sub('[ .,:]', '', df.loc[id_]['task'])
            subprocess.check_call(EDITOR + ' ' + os.path.join(ROOTDIR, fileedit), shell=True)
            mode = MODE_LIST
        elif mode == MODE_VOID:
            mode = MODE_EXIT


#    for i in range(len(df)):
#        basename = str(df.iloc[i]['time_added']) + '-' + str(df.iloc[i]['task']).replace('/', '_') + '.csv'
#        df[i:i+1].to_csv(os.path.join(ROOTDIR, 'todo', basename), sep='\t', index=False)
    df.to_csv(os.path.join(ROOTDIR, 'todo.csv'), sep='\t')

if __name__ == '__main__':
    main()
