CUDA_VISIBLE_DEVICES=2 python mnist_replica.py \
     --hidden_units=10000\
     --ps_hosts=10.40.199.203:12241,10.40.199.202:12241\
     --worker_hosts=10.40.199.201:12232,10.40.199.200:12232 \
     --job_name=ps --task_index=0 &
     
CUDA_VISIBLE_DEVICES=2 python mnist_replica.py \
     --hidden_units=10000\
     --ps_hosts=10.40.199.203:12241,10.40.199.202:12241\
     --worker_hosts=10.40.199.201:12232,10.40.199.200:12232 \
     --job_name=ps --task_index=1 &

CUDA_VISIBLE_DEVICES=2 python mnist_replica.py \
     --hidden_units=10000\
     --ps_hosts=10.40.199.203:12241,10.40.199.202:12241\
     --worker_hosts=10.40.199.201:12232,10.40.199.200:12232 \
     --job_name=worker --task_index=0 &
     
CUDA_VISIBLE_DEVICES=2 python mnist_replica.py \
     --hidden_units=10000\
     --ps_hosts=10.40.199.203:12241,10.40.199.202:12241\
     --worker_hosts=10.40.199.201:12232,10.40.199.200:12232 \
     --job_name=worker --task_index=1 &
