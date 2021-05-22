Financial House DevOps Homework

1.Coding

    "python3 listbuckets.py"

I wrote this little script by using Boto3 which is Python library of AWS. When you run the above command on a computer with Python3 installed, it will give you bucket names and creation dates.



2.Configuration Management


I wrote Ansible Playbook by using Ansible modules. I installed nginx with command module because in AWS EC2 Instances not using yum repos for nginx. Also i wrote basic nginx conf and copied to conf.d directory. You can apply playbook with this command;


    "ansible-playbook playbook.yml -i inventory.yml"
    
    
    
On the Terraform side i created VPC with 10.10.12.0/24 CIDR. After that i create 2 public and 2 private subnet. Each subnet mask is /26 and each subnet has 64 ip addresses. I attached IGW to public subnet and i attached NAT GW to private subnet. I configured route tables. I created S3 Bucket named "emredevops". After that i created folder named "homeworks" and i created file inside this folder which name is "test_object.txt". I encrypted this object with SSE-KMS. I created all the resources in a single Terraform file in one shot.


3. Application Management and Deployment


I build a simple flask web application running on port 5000. The application is running in the "/ home" path. On the Nginx side i configured reverse proxy and ssl certifications. Also i redirected traffic 80 to 443. I created seperate docker network in compose file. When you run compose file you can accessible web app on "https://localhost/home".  It will be writing "Hello. This page created by Emre Oztoprak". I used compose version 3.7
