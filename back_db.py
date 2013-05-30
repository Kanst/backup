#!/usr/bin/python
#! -*- coding: utf-8 -*-
# Backup postgresdb
# Output file: name_db-day-?-y-m-d-H:M.sql

import subprocess, os, argparse, datetime

def main():
    m = argparse.ArgumentParser(description="Backup postgresql: %(prog)s. Output file: name_db-day-?-y-m-d-H:M.sql")
    # m.add_argument("--dir","-t",type=str,default='~/backup/postgres/',
    #                 help="Path to backup")
    # m.add_argument("--dbname","-n",type=str,
    #                 default="template1", action="store",
    #                         help="Name for database")
    m.add_argument("--day","-d", type=int, default=6,
                    help='Days stored backup')
    # m.add_argument("--selectel_user","-u", type=str,default='',help='User selectel')
    # m.add_argument("--selectel_pass","-p", type=str,default='',help='Password selectel')
    # m.add_argument("--dir_storage","-a", type=str, default='backup',help='Storage dir')

    options = m.parse_args()
    options =  vars(options)
    # back_dir = options['dir']
    # back_db = options['dbname']
    # back_day = options['day']
    # back_selectel_user = options['selectel_user']
    # back_selectel_pass = options['selectel_pass']
    # back_dir_storage = options['dir_storage']

    #
    #   CONFIG
    #
    back_dir = '~/backup/'
    back_postgre_dir = 'postgresql/'
    back_db_postgre = 'mydb3'
    back_selectel_user = ''
    back_selectel_pass = ''
    back_dir_storage = 'backup'
    #
    #   CONFIG
    #
    back_dir = os.path.expanduser(back_dir)
    back_day = options['day']

    #Creade dir postgre
    if not os.path.isdir(os.path.expanduser(back_dir + back_postgre_dir)):
        os.makedirs(os.path.expanduser(back_dir + back_postgre_dir))

    # Backup db postgre
    name_file = os.path.expanduser(back_dir + back_postgre_dir + back_db_postgre + '-day-' + str(back_day) + '-' + datetime.datetime.today().strftime('%y-%m-%d-%H:%M') + '.sql')
    # print name_file
    vhod = 'pg_dump -C -f ' + name_file + ' ' + back_db_postgre

    # print vhod
    p = subprocess.Popen([vhod], shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    err = p.stderr.read()
    # print out
    # print err

    # Backup to storage selectel
    stor = 'supload -u ' + back_selectel_user + ' -k ' + back_selectel_pass + ' -d ' + str(back_day) + 'd -r ' + back_dir_storage + ' ' +  back_dir

    # print stor

    p = subprocess.Popen([stor], shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out1 = p.stdout.read()
    err1 = p.stderr.read()
    # print out1
    # print err1
    # rm postgres back file
    os.remove(name_file)


if __name__ == '__main__':
    main()
