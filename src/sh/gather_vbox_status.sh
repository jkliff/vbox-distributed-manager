# gathers information of all virtual machines available on the given host ($1)
#

LOGIN=$1
echo Running VMs as given for $LOGIN
ssh -T $LOGIN <<'EOF'

echo @@vms
VBoxManage list vms
echo @@runningvms
RUNNING=`VBoxManage list runningvms`

if [[ ${#RUNNING} -gt 0 ]] ; then

    echo $RUNNING

    echo "$RUNNING" | while read NAME UUID ; do
        echo @@ip-$NAME ;
        VBoxManage guestproperty enumerate $UUID | grep V4/IP | awk '{print $4}' | sed -e 's/,//';
    done

fi
EOF
