DevOps Homework

1.Coding

"aws s3 ls --region us-east-1"

    With AWS CLI you can get list of S3 Buckets. This command will give us bucket names and creation dates. If you don't use "us-east-1" as default region creation date can be difference on console screen because S3 global service and sometimes latency can be happen.


2.Configuration Management
    I wrote Ansible Playbook by using Ansible modules. I installed nginx with command module because in AWS EC2 Instances not using yum repos for nginx. Also i wrote basic nginx conf and copied to conf.d directory. You can apply playbook with this command;

    "ansible-playbook playbook.yml -i inventory.txt"