import json
import os
import os.path
import sys


def call (cmd):
    print cmd
    os.system (cmd)



def list_managed_hosts (conf, args):
    for h in conf.managed_hosts:
        print h

def list_vm_templates (conf, args):

    if not os.path.exists (conf.template_path):
        print 'path [%s] does not exist' % conf.template_path

    def is_dir_vm_template (path):
        return path.endswith ('ova')

    for d, ds, files in os.walk (conf.template_path):
        for f in files:
            print 'template', f, is_dir_vm_template (f)


def list_vms (conf, args):
    host = args[0]

    if host not in conf.managed_hosts:
        print '[%s] is not a managed host' % host
        return

    cmd = "sh/gather_vbox_status.sh %s" % (host,)
    result = call (cmd)
    print result

    call ('pwd')


CMDS = {
    'list-managed-hosts':   list_managed_hosts,
    'list-vm-templates' :   list_vm_templates,
    'list-vms':             list_vms
}


class Config:
    config_path = None
    template_path = None
    managed_hosts = None

    def __init__ (self, path):

        print path
        with (open (path)) as f:
            self.__dict__ = json.loads (f.read())
            print 'read conf', self.__dict__

        self.config_path = path

        if None in (self.template_path, ):
            print 'INVALID CONFIGURATION'


def load_config ():
    conf = Config(os.path.expanduser ('~/.vm_manage.conf'))
    return conf


def main (args):

    cmd = args[0]
    if cmd not in CMDS:
        print 'uknown cmd', cmd
        return -1

    conf = load_config ()

    CMDS [cmd] (conf, args[1:])


if __name__ == '__main__':
    main (sys.argv [1:])
