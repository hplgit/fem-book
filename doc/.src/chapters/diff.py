import os, sys, commands

deqbook_files_path = {}
deqbook_files_basename = []
for dirpath, dirnames, filenames in os.walk(
    os.path.abspath(os.path.expanduser('~/vc/deqbook/doc/src/chapters'))):
    for filename in filenames:
        if (filename.endswith('do.txt') or filename.endswith('.py')) \
               and filename not in ('conf.py', 'automake_sphinx.py') \
               and 'student' not in dirpath:
            deqbook_files_basename.append(filename)
            path = os.path.join(dirpath, filename)
            if 'slides-' in path:
                filename = 'slides/' + filename
            deqbook_files_path[filename] = path

#print deqbook_files_path
#print deqbook_files_basename

update = []
for dirpath, dirnames, filenames in os.walk(os.curdir):
    for filename in filenames:
        if (filename.endswith('do.txt') or filename.endswith('.py')) \
               and filename not in ('conf.py', 'automake_sphinx.py') \
               and 'student' not in dirpath:
            if filename in deqbook_files_basename:
                path = os.path.join(dirpath, filename)
                fdm_file = path
                if 'slides-' in path:
                    filename = 'slides/' + filename
                deqbook_file = deqbook_files_path[filename]
                cmd = 'diff %s %s' % (fdm_file, deqbook_file)
                failure, output = commands.getstatusoutput(cmd)
                if output:
                    print '>>>> diffs for %s:' % filename
                    print cmd
                    print output
                    update.append(path)

print 'update these files:', ', '.join(update)
