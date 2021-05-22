Financial House DevOps Homework

1.Coding

    "python3 listbuckets.py"

I wrote this little script by using Boto3 which is Python library of AWS. When you run the above command on a computer with Python3 installed, it will give you bucket names and creation dates.


2.Configuration Management

I wrote Ansible Playbook by using Ansible modules. I installed nginx with command module because in AWS EC2 Instances not using yum repos for nginx. Also i wrote basic nginx conf and copied to conf.d directory. You can apply playbook with this command;

    "ansible-playbook playbook.yml -i inventory.txt"
