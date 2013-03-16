# gathers information of all virtual machines available on the given host ($1)
#
TEMPLATE_BASE=$1
LOGIN=$2
TEMPLATE=$3
TARGET=$4


echo Deploying VM for $LOGIN
echo Template VM $TEMPLATE with target name $TARGET

S=$TEMPLATE_BASE/"$TEMPLATE".ova

echo scp $S $LOGIN:

ssh -T $LOGIN <<EOF

VBoxManage import "$TEMPLATE".ova
VBoxManage modifyvm "$TEMPLATE" --name "$TARGET" 



echo @@vms
VBoxManage list vms
echo @@runningvms
EOF
