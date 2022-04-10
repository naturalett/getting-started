<!-- Install kops -->
```bash
brew update && brew install kops
```

<!-- Generate a ssh keygen -->
```bash
ssh-keygen -t rsa
```

<!-- Create S3 bucket -->
```bash
export BUCKET_NAME=<YOUR_BUCKET_NAME>
aws s3 mb s3://clusters.${BUCKET_NAME}.tutorial
```

<!-- Export parameters -->
```bash
export SSH_Public_Key=<path to pub key file>
export KOPS_STATE_STORE=s3://clusters.${BUCKET_NAME}.tutorial
export KOPS_CLUSTER_NAME="k8s-cluster.k8s.local"
export MASTER_SIZE="t3.small"
export NODE_SIZE="t3.micro"
export ZONES="us-east-1a"
export CLUSTER_CIDR="10.31.0.0/16"
```

<!-- Create kops cluster -->
```bash
kops create cluster \
--name=${KOPS_CLUSTER_NAME} \
--network-cidr=${CLUSTER_CIDR} \
--node-count 1 \
--zones $ZONES \
--node-size $NODE_SIZE \
--master-size $MASTER_SIZE \
--master-zones $ZONES \
--networking cilium \
--cloud=aws \
--topology private \
--ssh-public-key=$SSH_Public_Key \
--yes
```

<!-- Create Bastion -->
```bash
kops create instancegroup bastions --role Bastion --subnet utility-us-east-1a --name ${KOPS_CLUSTER_NAME}
```

<!-- Update Cluster -->
```bash
kops update cluster --name ${KOPS_CLUSTER_NAME} --yes
```

<!-- Validate Cluster -->
```bash
kops validate cluster --name ${KOPS_CLUSTER_NAME}
```

<!-- Delete Cluster -->
```bash
kops delete cluster --name ${KOPS_CLUSTER_NAME} --yes
```
